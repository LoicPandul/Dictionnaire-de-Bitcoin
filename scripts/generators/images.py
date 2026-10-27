#!/usr/bin/env python3
"""
Images des définitions dans le livre imprimé en couleur.

Chaque schéma 2027 existe en quatre fichiers (charte, section 6) : `image-N.svg` (source),
`image-N.png` (couleur, 1 280 px), `image-N-nb.pdf` et `image-N-nb.png` (noir et blanc).
L'intérieur étant imprimé en couleur, le livre prend la version couleur, de préférence
vectorielle :
  1. `image-N.pdf`, s'il existe dans le dossier `assets/` ;
  2. `image-N.svg` converti en PDF vectoriel par Chrome sans interface, comme les `-nb.pdf`
     (mêmes polices, `fonts/static/`), dans un cache sous `build/cache/schemas/` ;
  3. `image-N.png`, en couleur (1 280 px, environ 260 ppp à 125 mm) ;
  4. à défaut de couleur, la version noir et blanc (`-nb.pdf`, puis `-nb.png`).
Le livre de poche, imprimé en noir et blanc, prend d'abord les versions « -nb ». Les fichiers
des définitions ne sont jamais modifiés.
"""

import hashlib
import os
import re
import shutil
import subprocess
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Iterable, Optional

from ..config import BUILD_DIR, FONTS_DIR

CACHE_DIR = BUILD_DIR / "cache" / "schemas"

# Polices des schémas : celles que déclare la feuille de style de la charte (charte.css).
_FONT_FACES = [
    ("Archivo Schema", 400, "normal", "ArchivoSchema-Regular.ttf"),
    ("Archivo Schema", 600, "normal", "ArchivoSchema-Bold.ttf"),
    ("Archivo Schema", 400, "italic", "ArchivoSchema-Italic.ttf"),
    ("Atkinson Hyperlegible Mono", 400, "normal", "AtkinsonHyperlegibleMono-Regular.ttf"),
    ("Atkinson Hyperlegible Mono", 700, "normal", "AtkinsonHyperlegibleMono-Bold.ttf"),
]

_chrome: Optional[str] = None
_chrome_searched = False


def find_chrome() -> Optional[str]:
    """Chrome ou Chromium : CHROME_PATH, la commande système, puis le cache de Playwright."""
    global _chrome, _chrome_searched
    if _chrome_searched:
        return _chrome
    _chrome_searched = True
    candidates = [os.environ.get("CHROME_PATH")]
    candidates += [shutil.which(n) for n in ("google-chrome-stable", "google-chrome", "chromium", "chromium-browser")]
    pw = Path.home() / ".cache" / "ms-playwright"
    if pw.is_dir():
        builds = sorted((d for d in pw.iterdir() if re.fullmatch(r"chromium-\d+", d.name)),
                        key=lambda d: int(d.name.split("-")[1]), reverse=True)
        candidates += [str(d / sub / "chrome") for d in builds for sub in ("chrome-linux64", "chrome-linux")]
    _chrome = next((c for c in candidates if c and Path(c).exists()), None)
    return _chrome


def _cached_pdf(svg: Path) -> Path:
    digest = hashlib.sha256(svg.read_bytes()).hexdigest()[:20]
    return CACHE_DIR / f"{digest}.pdf"


def _convert(svg: Path) -> Optional[Path]:
    """SVG → PDF vectoriel couleur, à la taille exacte du schéma. None si la conversion échoue."""
    target = _cached_pdf(svg)
    if target.exists() and target.stat().st_size:
        return target
    chrome = find_chrome()
    if not chrome:
        return None
    source = svg.read_text(encoding="utf-8")
    m = re.search(r'<svg\b[^>]*\bwidth="(\d+)"[^>]*\bheight="(\d+)"', source)
    width, height = (m.group(1), m.group(2)) if m else ("1280", "640")
    faces = "\n".join(
        f'@font-face {{ font-family: "{family}"; font-weight: {weight}; font-style: {style}; '
        f'src: url("{(FONTS_DIR / "static" / name).as_uri()}"); }}'
        for family, weight, style, name in _FONT_FACES)
    page = (f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>\n{faces}\n'
            f"@page {{ size: {width}px {height}px; margin: 0 }} html, body {{ margin: 0 }} svg {{ display: block }}\n"
            f"</style></head><body>{source}</body></html>")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=CACHE_DIR) as tmp:
        html = Path(tmp) / "schema.html"
        html.write_text(page, encoding="utf-8")
        out = Path(tmp) / "schema.pdf"
        cmd = [chrome, "--headless", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files",
               "--force-color-profile=srgb", "--no-pdf-header-footer", f"--user-data-dir={tmp}/profil",
               f"--print-to-pdf={out}", html.as_uri()]
        try:
            subprocess.run(cmd, capture_output=True, timeout=60)
        except (OSError, subprocess.TimeoutExpired):
            return None
        if not out.exists() or not out.stat().st_size:
            return None
        shutil.move(str(out), target)
    return target


def prepare(svgs: Iterable[Path]) -> int:
    """Convertit d'avance, en parallèle, les SVG absents du cache. Retourne le nombre de PDF produits."""
    svgs = [s for s in svgs if not s.with_suffix(".pdf").exists() and not _cached_pdf(s).exists()]
    if not svgs or not find_chrome():
        return 0
    with ThreadPoolExecutor(max_workers=min(8, os.cpu_count() or 2)) as pool:
        return sum(1 for r in pool.map(_convert, svgs) if r)


def for_print(image_path: Path, color: bool = True) -> Path:
    """Fichier à inclure dans le PDF pour l'image `./assets/image-N.png` d'une définition.

    En noir et blanc (livre de poche), les versions « -nb » passent en premier."""
    stem = image_path.with_suffix("")
    if not color:
        for nb in (stem.with_name(stem.name + "-nb.pdf"), stem.with_name(stem.name + "-nb" + image_path.suffix)):
            if nb.exists():
                return nb
        return image_path
    vector = stem.with_suffix(".pdf")
    if vector.exists():
        return vector
    svg = stem.with_suffix(".svg")
    if svg.exists():
        converted = _convert(svg)
        if converted:
            return converted
    if image_path.exists():
        return image_path
    for fallback in (stem.with_name(stem.name + "-nb.pdf"), stem.with_name(stem.name + "-nb" + image_path.suffix)):
        if fallback.exists():
            return fallback
    return image_path
