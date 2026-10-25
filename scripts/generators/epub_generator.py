#!/usr/bin/env python3
"""
Génération de l'EPUB 3 d'une édition (livre numérique, Amazon Kindle compris).

Un fichier XHTML par lettre de chaque partie du dictionnaire, par année de la chronologie
et par tranche de 25 documents de spécification. Les formules LaTeX deviennent du MathML
(latex2mathml), les images des définitions sont copiées dans OEBPS/images/. Le fichier
produit doit passer epubcheck sans erreur (`python3 scripts/main.py build --format epub`).
"""

import html
import re
import shutil
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import markdown as md
from latex2mathml.converter import convert as latex_to_mathml

from ..config import BUILD_DIR, TEMPLATES_DIR
from ..core.book import Book, Section
from .pdf_generator import STATUS_FR, load_legal

NBSP = " "
SPEC_CHUNK = 25
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(\./assets/([^)\s]+)\)")

CSS = """
body { font-family: serif; line-height: 1.45; margin: 0 4%; }
h1 { text-align: center; font-size: 1.8em; margin: 2em 0 1em; }
h1.partie { margin-top: 30%; }
h2 { text-align: center; font-size: 1.5em; margin: 1.5em 0 0.8em; page-break-after: avoid; }
h3.vedette { font-family: sans-serif; font-size: 1em; letter-spacing: 0.08em; margin: 1.6em 0 0.2em;
  page-break-after: avoid; }
p { margin: 0.4em 0; text-align: justify; }
p.meta { font-family: sans-serif; font-size: 0.75em; color: #444; margin: 0 0 0.6em; text-align: left; }
p.titre-doc { font-style: italic; margin-bottom: 0.4em; text-align: left; }
p.renvois { font-family: sans-serif; font-size: 0.75em; text-align: right; margin: 0.4em 0 1em; }
p.date { font-family: sans-serif; font-weight: bold; margin: 1.2em 0 0.2em; text-align: left; }
p.intro { font-style: italic; text-align: center; margin: 1em 8%; }
p.centre { text-align: center; }
code { font-family: monospace; font-size: 0.9em; background: #eff1f3; }
pre { font-family: monospace; font-size: 0.8em; background: #eff1f3; padding: 0.5em; white-space: pre-wrap;
  word-wrap: break-word; }
blockquote { margin: 0.6em 1.5em; font-size: 0.95em; }
img { max-width: 100%; }
span.figure { display: block; text-align: center; margin: 0.8em 0; }
span.legende { display: block; font-size: 0.8em; font-style: italic; margin-top: 0.3em; }
span.math-bloc { display: block; text-align: center; margin: 0.4em 0; }
table { border-collapse: collapse; margin: 0.6em auto; font-size: 0.85em; }
th, td { border: 1px solid #000; padding: 0.2em 0.4em; }
nav ol { list-style: none; }
"""


def _xml(text: str) -> str:
    return html.escape(text, quote=True)


def _french_spaces(text: str) -> str:
    """Espaces insécables de la typographie française (texte hors code)."""
    text = re.sub(r"[   ]+([:;!?»])", NBSP + r"\1", text)
    text = re.sub(r"«[   ]+", "«" + NBSP, text)
    return text


class _Converter:
    """Markdown du dictionnaire → XHTML (code, formules et images protégés)."""

    def __init__(self, images: Dict[str, str]):
        self.images = images          # chemin source → nom dans OEBPS/images
        self.has_math = False

    def __call__(self, content: str, assets_dir: Optional[Path] = None, slug: str = "") -> str:
        store: List[str] = []

        def keep(xhtml: str) -> str:
            store.append(xhtml)
            return f"\u0007{len(store) - 1}\u0007"

        def block_code(m):
            return "\n\n" + keep("<pre><code>" + _xml(m.group(2).rstrip("\n")) + "</code></pre>") + "\n\n"
        content = re.sub(r"```([\w+-]*)[ \t]*\n(.*?)```", block_code, content, flags=re.DOTALL)
        content = re.sub(r"`([^`\n]+)`", lambda m: keep("<code>" + _xml(m.group(1)) + "</code>"), content)

        def math(m, display):
            self.has_math = True
            try:
                mathml = latex_to_mathml(m.group(1).strip(), display="block" if display else "inline")
            except Exception:  # formule que latex2mathml ne sait pas lire : texte brut
                return keep("<code>" + _xml(m.group(1)) + "</code>")
            mathml = re.sub(r"&#x0*([0-9A-Fa-f]+);", lambda e: chr(int(e.group(1), 16)), mathml)
            # <math> est un contenu de phrase : même en bloc, il reste valide dans un <p>.
            return keep(f'<span class="{"math-bloc" if display else "math"}">{mathml}</span>')
        content = re.sub(r"\$\$(.+?)\$\$", lambda m: math(m, True), content, flags=re.DOTALL)
        content = re.sub(r"(?<!\\)\$([^$\n]+?)\$", lambda m: math(m, False), content)

        def image(m):
            if not assets_dir:
                return ""
            src = assets_dir / m.group(2)
            if not src.exists():
                return ""
            name = self.images.setdefault(str(src), f"{slug}-{m.group(2)}".replace("/", "-"))
            caption = f'<span class="legende">{_xml(_french_spaces(m.group(1)))}</span>' if m.group(1).strip() else ""
            return "\n\n" + keep(f'<span class="figure"><img src="../images/{_xml(name)}" alt="{_xml(m.group(1))}"/>{caption}</span>') + "\n\n"
        content = IMAGE_RE.sub(image, content)

        content = _french_spaces(content)
        # Python-Markdown exige une ligne vide avant une liste ; le dictionnaire ne la met pas toujours.
        content = re.sub(r"(?m)^(?![ \t]*(?:[*\-]|\d+\.)[ \t])(\S.*)\n(?=[ \t]*(?:[*\-]|\d+\.)[ \t])", r"\1\n\n", content)
        out = md.markdown(content, extensions=["tables"], output_format="xhtml")
        for _ in range(3):
            out = re.sub(r"\u0007(\d+)\u0007", lambda m: store[int(m.group(1))], out)
        # Un bloc protégé seul dans son paragraphe ne doit pas rester dans un <p>.
        out = re.sub(r"<p>\s*(<(?:div|pre)\b.*?</(?:div|pre)>)\s*</p>", r"\1", out, flags=re.DOTALL)
        return out


class _Doc:
    def __init__(self, file: str, title: str, body: str, nav_title: Optional[str] = None, level: int = 1):
        self.file, self.title, self.body = file, title, body
        self.nav_title, self.level = nav_title, level
        self.math = "<math" in body


def _page(title: str, body: str) -> str:
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n'
            '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" '
            'xml:lang="fr" lang="fr">\n<head>\n<meta charset="UTF-8"/>\n'
            f'<title>{_xml(title)}</title>\n<link rel="stylesheet" type="text/css" href="../styles.css"/>\n'
            f'</head>\n<body>\n{body}\n</body>\n</html>\n')


class EpubBuilder:
    def __init__(self, book: Book):
        self.book = book
        self.images: Dict[str, str] = {}
        self.convert = _Converter(self.images)
        self.anchor_file: Dict[str, str] = {}   # ancre → fichier XHTML
        self.docs: List[_Doc] = []

    # --- plan des fichiers et des ancres ---------------------------------

    def _plan(self) -> List[Tuple[Section, str, list]]:
        """(section, nom de fichier, contenu) pour chaque fichier du corps du livre."""
        plan = []
        for s in self.book.edition.sections:
            if s.kind == "dictionary":
                for letter, defs in s.letters.items():
                    f = f"{s.id}-{letter.lower()}.xhtml"
                    plan.append((s, f, (letter, defs)))
                    for d in defs:
                        self.anchor_file[d.slug] = f
            elif s.kind == "chronology":
                years: Dict[int, list] = {}
                for ev in s.events:
                    years.setdefault(ev.year, []).append(ev)
                for y, evs in years.items():
                    plan.append((s, f"chronologie-{y}.xhtml", (y, evs)))
            elif s.kind == "specs":
                for serie in s.series:
                    for i in range(0, len(serie.entries), SPEC_CHUNK):
                        chunk = serie.entries[i:i + SPEC_CHUNK]
                        f = f"{serie.series}-{i // SPEC_CHUNK + 1:02d}.xhtml"
                        plan.append((s, f, (serie, chunk)))
                        for doc in chunk:
                            self.anchor_file[self.book.spec_anchor(doc)] = f
                            if doc.definition:
                                self.anchor_file.setdefault(doc.definition, f)
        return plan

    def _link(self, slug: str, label: str) -> str:
        return f'<a href="{self.anchor_file[slug]}#{slug}">{_xml(label)}</a>'

    def _see(self, targets, one: str, many: str) -> str:
        targets = [t for t in targets if t.slug in self.anchor_file]
        if not targets:
            return ""
        label = one if len(targets) == 1 else many
        links = ", ".join(self._link(t.slug, t.title) for t in targets)
        return f'<p class="renvois">{label}{NBSP}: {links}</p>'

    # --- rendu ---------------------------------------------------------

    def _entry(self, s: Section, d) -> str:
        parts = [f'<section class="entree" id="{d.slug}">', f'<h3 class="vedette">{_xml(d.title)}</h3>']
        meta = [_xml(d.category)] if d.category else []
        if d.english_term:
            meta.append(f"EN{NBSP}: {_xml(d.english_term)}")
        elif d.french_term:
            meta.append(f"FR{NBSP}: {_xml(d.french_term)}")
        if meta:
            parts.append(f'<p class="meta">{" · ".join(meta)}</p>')
        parts.append(self.convert(self.book.body(d, s), d.path / "assets", d.slug))
        if s.version == "developpee":
            parts.append(self._see(self.book.cross_references(d), "Terme associé", "Termes associés"))
        parts.append("</section>")
        return "\n".join(p for p in parts if p)

    def _status(self, doc) -> str:
        labels = []
        for st in doc.status:
            fr = STATUS_FR.get(st.lower())
            labels.append(fr if fr and fr.lower() == st.lower() else f"{fr} ({st})" if fr else st)
        return ", ".join(labels)

    def _spec_entry(self, s: Section, doc) -> str:
        anchor = self.book.spec_anchor(doc)
        parts = [f'<section class="entree" id="{anchor}">']
        if doc.definition and self.anchor_file.get(doc.definition) == self.anchor_file[anchor]:
            parts.append(f'<span id="{doc.definition}"></span>')
        parts.append(f'<h3 class="vedette">{_xml(doc.id)}</h3>')
        meta = []
        if doc.status:
            meta.append(f"Statut{NBSP}: {_xml(self._status(doc))}")
        if doc.type:
            meta.append(f"Type{NBSP}: {_xml(doc.type)}")
        if doc.created:
            meta.append(f"Créé le{NBSP}: {_xml(doc.created)}")
        if meta:
            parts.append(f'<p class="meta">{" · ".join(meta)}</p>')
        if doc.title:
            parts.append(f'<p class="titre-doc" xml:lang="en" lang="en">{_xml(doc.title)}</p>')
        if doc.summary:
            parts.append(self.convert(doc.summary))
        parts.append(self._see(self.book.related(doc.related), "Voir", "Voir"))
        linked = self.book.definition_for(doc)
        if s.detail and linked:
            parts.append(self.convert(linked.content, linked.path / "assets", linked.slug))
        parts.append("</section>")
        return "\n".join(p for p in parts if p)

    def _event(self, ev) -> str:
        parts = [f'<p class="date">{_xml(ev.date_fr())} · <em>{_xml(_french_spaces(ev.title))}</em></p>',
                 self.convert(ev.text),
                 self._see(self.book.related(ev.related), "Voir", "Voir")]
        return "\n".join(p for p in parts if p)

    def _front(self, legal: dict):
        e = self.book.edition
        now = datetime.now()
        self.docs.append(_Doc("titre.xhtml", e.title,
            f'<section epub:type="titlepage"><h1>{_xml(e.title)}</h1>'
            f'<p class="centre">{_xml(e.subtitle)}</p><p class="centre"><em>{_xml(legal.get("author", ""))}</em></p></section>'))
        lines = [f"© {now.year} {legal.get('author', '')}", f"{e.title} : {e.subtitle}",
                 f"Version du {now.day:02d}/{now.month:02d}/{now.year}",
                 f"Cet ouvrage est sous licence {legal.get('license', '')}"]
        links = [legal.get("github_url", ""), legal.get("license_url", ""), legal.get("website", "")]
        body = "".join(f'<p class="centre">{_xml(_french_spaces(l))}</p>' for l in lines)
        body += "".join(f'<p class="centre"><a href="{_xml(u)}">{_xml(u)}</a></p>' for u in links if u)
        body += f'<p class="centre">Lightning{NBSP}: {_xml(legal.get("lightning_address", ""))}</p>'
        self.docs.append(_Doc("mentions.xhtml", "Mentions légales", f'<section epub:type="copyright-page">{body}</section>'))
        for f, title, template in [("contributeurs.xhtml", "Contributeurs et remerciements", "contributors.md"),
                                   ("note.xhtml", "Note de l'auteur", "introduction.md")]:
            path = TEMPLATES_DIR / template
            text = path.read_text(encoding="utf-8") if path.exists() else ""
            text = re.sub(r"^# ", "## ", text, flags=re.MULTILINE)
            self.docs.append(_Doc(f, title, f"<h1>{_xml(title)}</h1>\n{self.convert(text)}", nav_title=title))

    def build(self) -> List[_Doc]:
        legal = load_legal()
        self._front(legal)
        plan = self._plan()
        opened = set()
        for s, f, payload in plan:
            body = []
            nav_title = None
            if s.id not in opened:
                opened.add(s.id)
                body.append(f'<h1 class="partie" id="partie-{s.id}">{_xml(s.title)}</h1>')
                if s.intro:
                    body.append(f'<p class="intro">{_xml(_french_spaces(" ".join(s.intro.split())))}</p>')
                self.docs.append(_Doc(f"partie-{s.id}.xhtml", s.title, "\n".join(body), nav_title=s.title, level=1))
                body = []
            if s.kind == "dictionary":
                letter, defs = payload
                body.append(f"<h2>{letter}</h2>")
                body += [self._entry(s, d) for d in defs]
                nav_title = letter
            elif s.kind == "chronology":
                year, evs = payload
                body.append(f"<h2>{year}</h2>")
                body += [self._event(ev) for ev in evs]
                nav_title = str(year)
            else:
                serie, chunk = payload
                first, last = chunk[0].id, chunk[-1].id
                body.append(f"<h2>{_xml(first)} à {_xml(last)}</h2>" if len(chunk) > 1 else f"<h2>{_xml(first)}</h2>")
                body += [self._spec_entry(s, doc) for doc in chunk]
                nav_title = f"{first} à {last}" if len(chunk) > 1 else first
            self.docs.append(_Doc(f, f"{s.title} : {nav_title}", "\n".join(body), nav_title=nav_title, level=2))
        return self.docs

    # --- paquet ----------------------------------------------------------

    def _nav(self) -> Tuple[str, str]:
        items, ncx_points, open_level1 = [], [], False
        order = 0
        for d in self.docs:
            if not d.nav_title:
                continue
            order += 1
            link = f'<a href="text/{d.file}">{_xml(d.nav_title)}</a>'
            if d.level == 1:
                if open_level1:
                    items.append("</ol></li>")
                items.append(f"<li>{link}<ol>")
                open_level1 = True
            else:
                items.append(f"<li>{link}</li>")
            ncx_points.append((order, d.level, d.nav_title, d.file))
        if open_level1:
            items.append("</ol></li>")
        nav_list = "\n".join(items).replace("<ol></ol>", "")
        # Une partie sans sous-entrée laisse un <ol> vide, interdit en EPUB 3.
        nav_list = re.sub(r"<ol>\s*</ol>", "", nav_list)
        nav = ('<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE html>\n'
               '<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="fr" lang="fr">\n'
               '<head><meta charset="UTF-8"/><title>Table des matières</title></head>\n<body>\n'
               f'<nav epub:type="toc" id="toc"><h1>Table des matières</h1><ol>\n{nav_list}\n</ol></nav>\n'
               '<nav epub:type="landmarks" hidden="hidden"><ol>'
               f'<li><a epub:type="bodymatter" href="text/{self._first_body()}">Début</a></li>'
               '</ol></nav>\n</body>\n</html>\n')
        # toc.ncx pour les liseuses EPUB 2
        points, depth, stack = [], 1, []
        for order, level, title, f in ncx_points:
            while stack and stack[-1] >= level:
                points.append("</navPoint>")
                stack.pop()
            points.append(f'<navPoint id="np{order}" playOrder="{order}"><navLabel><text>{_xml(title)}</text></navLabel>'
                          f'<content src="text/{f}"/>')
            stack.append(level)
            depth = max(depth, len(stack))
        points += ["</navPoint>"] * len(stack)
        self._ncx_depth = depth
        return nav, "\n".join(points)

    def _first_body(self) -> str:
        return next((d.file for d in self.docs if d.file.startswith("partie-")), self.docs[0].file)

    def write(self, path: Path) -> Path:
        self.build()
        e = self.book.edition
        identifier = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, 'dictionnaire-de-bitcoin/' + e.id)}"
        modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        legal = load_legal()
        nav, ncx_points = self._nav()

        manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                    '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                    '<item id="css" href="styles.css" media-type="text/css"/>']
        spine = []
        for i, d in enumerate(self.docs):
            props = ' properties="mathml"' if d.math else ""
            manifest.append(f'<item id="x{i}" href="text/{d.file}" media-type="application/xhtml+xml"{props}/>')
            spine.append(f'<itemref idref="x{i}"/>')
        for i, name in enumerate(sorted(set(self.images.values()))):
            ext = name.rsplit(".", 1)[-1].lower()
            mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "gif": "image/gif",
                    "svg": "image/svg+xml", "webp": "image/webp"}[ext]
            manifest.append(f'<item id="img{i}" href="images/{_xml(name)}" media-type="{mime}"/>')

        opf = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="fr">\n'
               '<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">\n'
               f'<dc:identifier id="bookid">{identifier}</dc:identifier>\n'
               f'<dc:title>{_xml(e.title)}</dc:title>\n'
               f'<dc:creator>{_xml(legal.get("author", ""))}</dc:creator>\n'
               '<dc:language>fr</dc:language>\n'
               f'<dc:publisher>{_xml(legal.get("publisher", legal.get("author", "")))}</dc:publisher>\n'
               f'<dc:rights>{_xml(legal.get("license", ""))}</dc:rights>\n'
               f'<dc:description>{_xml(e.subtitle)}</dc:description>\n'
               f'<meta property="dcterms:modified">{modified}</meta>\n'
               '</metadata>\n'
               f'<manifest>\n{chr(10).join(manifest)}\n</manifest>\n'
               f'<spine toc="ncx">\n{chr(10).join(spine)}\n</spine>\n</package>\n')
        ncx = ('<?xml version="1.0" encoding="UTF-8"?>\n'
               '<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="fr">\n'
               f'<head><meta name="dtb:uid" content="{identifier}"/><meta name="dtb:depth" content="{self._ncx_depth}"/>'
               '<meta name="dtb:totalPageCount" content="0"/><meta name="dtb:maxPageNumber" content="0"/></head>\n'
               f'<docTitle><text>{_xml(e.title)}</text></docTitle>\n<navMap>\n{ncx_points}\n</navMap>\n</ncx>\n')
        container = ('<?xml version="1.0" encoding="UTF-8"?>\n'
                     '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                     '<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>'
                     '</rootfiles></container>\n')

        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        with zipfile.ZipFile(tmp, "w") as z:
            z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
            z.writestr("META-INF/container.xml", container, compress_type=zipfile.ZIP_DEFLATED)
            z.writestr("OEBPS/content.opf", opf, compress_type=zipfile.ZIP_DEFLATED)
            z.writestr("OEBPS/nav.xhtml", nav, compress_type=zipfile.ZIP_DEFLATED)
            z.writestr("OEBPS/toc.ncx", ncx, compress_type=zipfile.ZIP_DEFLATED)
            z.writestr("OEBPS/styles.css", CSS, compress_type=zipfile.ZIP_DEFLATED)
            for d in self.docs:
                z.writestr(f"OEBPS/text/{d.file}", _page(d.title, d.body), compress_type=zipfile.ZIP_DEFLATED)
            for src, name in self.images.items():
                z.write(src, f"OEBPS/images/{name}", compress_type=zipfile.ZIP_DEFLATED)
        shutil.move(str(tmp), path)
        return path


def generate(book: Book, output_dir: Optional[Path] = None) -> Optional[Path]:
    output_dir = output_dir or BUILD_DIR / book.edition.id
    path = output_dir / f"{book.edition.file}.epub"
    try:
        EpubBuilder(book).write(path)
    except Exception as exc:
        import traceback
        traceback.print_exc()
        print(f"[ERREUR] EPUB : {exc}")
        return None
    print(f"[OK] EPUB : {path}")
    return path
