// Gabarits HTML du site. Chaque fonction rend une page complète.
// Direction : site/design/direction.md (« Le livre ouvert »).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { url, site, palette } from '../config.mjs';
import { escapeHtml as h } from './markdown.mjs';
import { t, lien, chemins, LANGUES, categoryLabel, partieTitre, partieIntro, nomsSeries } from './i18n.mjs';

export { categoryLabel };
const here = path.dirname(fileURLToPath(import.meta.url));
const advances = JSON.parse(fs.readFileSync(path.join(here, 'archivo-advances.json'), 'utf8'));
const ALLEE = JSON.parse(fs.readFileSync(path.join(here, 'allee.json'), 'utf8'));

export const num = (n) => new Intl.NumberFormat(t.locale).format(n);
// plural(n, ['mot', 'mots']) -> « 3 mots ».
const plural = (n, [one, many]) => `${num(n)}\u00a0${n > 1 ? many : one}`;
const ordinal = (n) => (n === 1 ? t.premier : t.ordinal(num(n)));
const NB = '\u00a0';
const FR_PATHS = chemins(LANGUES.fr);
const EN_PATHS = chemins(LANGUES.en);
const autres = () => (t.code === 'fr' ? EN_PATHS : FR_PATHS);
// Comparaison des titres dans la langue de la page.
const compareTitres = (a, b) => a.localeCompare(b, t.code, { sensitivity: 'base', numeric: true });

// ---------------------------------------------------------------- Pictogrammes
// Les pictogrammes 2027 du livre (assets/pictograms, traits de 2 px sur une grille de 24),
// un par catégorie d'après templates/parts.yaml. setPictos() les reçoit du build.
// Les symboles utilisés par une page sont intégrés une seule fois en tête du <body>.
let PICTOS = new Map();
export function setPictos(map) {
  PICTOS = map;
}
const symbole = (k) => `<symbol id="p-${k}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square" stroke-linejoin="miter">${PICTOS.get(k)}</symbol>`;
export const pictoSprite = () => `<svg xmlns="http://www.w3.org/2000/svg">${[...PICTOS.keys()].map(symbole).join('')}</svg>`;

function pictoCollector() {
  const used = new Set();
  const use = (slug, cls = 'picto') => {
    if (!PICTOS.has(slug)) return '';
    used.add(slug);
    return `<svg class="${cls}" aria-hidden="true" focusable="false"><use href="#p-${slug}"/></svg>`;
  };
  const defs = () => (used.size ? `<svg class="defs" aria-hidden="true" focusable="false">${[...used].map(symbole).join('')}</svg>` : '');
  return { use, defs };
}

// ---------------------------------------------------------------- Vedettes
// Largeur en em du titre composé en Archivo Titre (approche −0,02 em), pour la taille en unités de conteneur :
// la plus petite largeur qui tient en deux lignes au plus (les coupures possibles : espace, « _ », « - »).
const emWidth = (s) => [...s].reduce((w, ch) => w + (advances[ch] ?? 0.55) - 0.02, 0);
// Les opcodes (« OP_RETURN – 0x6A ») : le nom fait la vedette, le code passe dessous en petit, comme une étiquette.
const codeVedette = (title) => affiche(title).match(/^(.+)\u00a0– (0x[0-9A-Fa-f]+)$/);
export function headwordEm(raw) {
  // Un opcode tient sur une ligne (« OP_ » ne reste pas seul) : sa largeur entière fixe la taille.
  const code = codeVedette(raw);
  if (code) return Math.round(emWidth(code[1]) * 1000) / 1000;
  const title = affiche(raw);
  const pieces = title.match(/[^ _-]+[_-]*\s*|[_-]+\s*|\s+/g) || [title];
  let best = emWidth(title.trim());
  for (let i = 1; i < pieces.length; i++) {
    const a = pieces.slice(0, i).join('').trimEnd();
    const b = pieces.slice(i).join('').trim();
    if (!a || !b) continue;
    best = Math.min(best, Math.max(emWidth(a), emWidth(b)));
  }
  return Math.round(best * 1000) / 1000;
}
// Points de coupure après « _ » (le navigateur coupe déjà après « - » et les espaces).
// Titres affichés : les codes hexadécimaux en « 0x » minuscule (« OP_RETURN - 0x6A »), comme on les écrit.
export const affiche = (title) => String(title).replace(/\b0X([0-9A-F]+)\b/g, '0x$1').replace(/ - /g, '\u00a0– ').replace(/'/g, '’');
const breakable = (title) => h(affiche(title)).replace(/_/g, '_<wbr>');
// Espaces fines insécables de la typographie française dans les textes affichés (descriptions).
export const fr = (t = '') => String(t).replace(/'/g, '’').replace(/\.\.\./g, '…').replace(/« /g, '«\u202f').replace(/ »/g, '\u202f»').replace(/ ([;:!?])/g, '\u202f$1');
const hd = (t) => h(fr(t));
// Résumé coupé au mot, jamais sur un mot-outil, un nombre entamé ni une lettre seule (« que… », « 500 00… », « et M… »).
// La longueur est choisie pour tenir dans les lignes que la mise en page lui laisse : la coupe CSS ne sert que de filet.
export const resume = (t, n = 84) => {
  t = String(t || '').replace(/\s*(\.\.\.|…)$/, '');
  if (t.length <= n) return t === '' ? '' : /[.!?)»]$/.test(t) ? t : `${t}…`;
  // Une phrase entière qui tient, même courte, vaut mieux qu'une coupe : pas de points de suspension.
  const fin = Math.max(...[...t.slice(0, n + 1).matchAll(/[.!?](?=\s)/g)].map((m) => m.index));
  if (fin > n * 0.3) return t.slice(0, fin + 1);
  let s = t.slice(0, n + 1);
  s = s.slice(0, Math.max(s.lastIndexOf(' '), 1));
  while (/\s(\S{1,3}|\S*\d\S*|que|qui|dont|dans|pour|avec|sans|sous|leur|leurs|cette|entre|plus|très)$/i.test(s) && s.lastIndexOf(' ') > n / 2) s = s.slice(0, s.lastIndexOf(' '));
  // Une parenthèse ouverte et pas refermée : on coupe avant elle.
  if ((s.match(/\(/g) || []).length > (s.match(/\)/g) || []).length && s.lastIndexOf('(') > n / 2) s = s.slice(0, s.lastIndexOf('('));
  return `${s.replace(/[\s,;:.(«–-]+$/, '')}…`;
};
// Dans une phrase, un titre ne se coupe pas à son trait d'union (« B-MONEY ») : trait d'union insécable.
const insecable = (t) => h(affiche(t)).replace(/-/g, '\u2011').replace(/– /g, '–\u00a0');

// Les mots d'une vedette, chacun dans son masque, pour qu'ils se posent l'un après l'autre.
// On coupe sur les espaces ordinaires du titre affiché : « OP_RETURN – 0x6A » garde son tiret avec le mot qui précède.
const headwordWords = (title) => {
  const code = codeVedette(title);
  const mots = (code ? code[1] : affiche(title))
    .split(' ')
    .map((w, i) => `<span class="vw" style="--i:${i}">${breakable(w)}</span>`)
    .join(' ');
  return code ? `${mots}<span class="vedette-code"><span class="masque">\u00a0– </span>${code[2]}</span>` : mots;
};

// ---------------------------------------------------------------- Tête de page
// alt : le chemin de la même page dans l'autre langue (null : pas d'équivalent).
// canonique : un autre chemin canonique (une page anglaise pas encore traduite renvoie au français).
function head({ title, description, path: p, jsonLd = '', math = false, assets, themeColor = palette.blanc, type = 'website', preloadImage = '', extraJs = '', alt = null, canonique = null, robots = '' }) {
  const canonical = `${url}${canonique || p}`;
  const [fr, en] = t.code === 'fr' ? [p, alt] : [alt, p];
  const alternates = alt && !canonique
    ? `<link rel="alternate" hreflang="fr" href="${url}${fr}">
<link rel="alternate" hreflang="en" href="${url}${en}">
<link rel="alternate" hreflang="x-default" href="${url}${fr}">
`
    : '';
  return `<!doctype html>
<html lang="${t.code}" data-base="${t.base}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<script>${assets.inlineScript}</script>
<title>${h(title)}</title>
<meta name="description" content="${h(description)}">
<link rel="canonical" href="${canonical}">
${alternates}${robots ? `<meta name="robots" content="${robots}">\n` : ''}
<meta name="theme-color" content="${themeColor}">
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="${type}">
<meta property="og:locale" content="${t.og}">
<meta property="og:site_name" content="${h(t.marque)}">
<meta property="og:title" content="${h(title)}">
<meta property="og:description" content="${h(description)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${url}/img/carte-sociale.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="${h(t.ogAlt)}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@Loic_Pandul">
<meta name="author" content="${h(site.author)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preload" href="/fonts/archivo.woff2" as="font" type="font/woff2" crossorigin>
${preloadImage}<link rel="stylesheet" href="${assets.css}">
${math ? '<link rel="stylesheet" href="/katex/katex.min.css">\n' : ''}<script src="${assets.js}" defer></script>
${extraJs ? `<script src="${extraJs}" defer></script>\n` : ''}${jsonLd}
</head>`;
}

// ---------------------------------------------------------------- Navigation commune
// Lettres et catégories, données une fois par le build, pour le menu de toutes les pages.
let NAV = { letters: new Map(), categories: [], parts: [] };
export function setNavigation(letters, categories, parts) {
  NAV = { letters, categories, parts };
}

// ---------------------------------------------------------------- Barre
const loupe = `<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="10.5" cy="10.5" r="6.25" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15.2 15.2 5.3 5.3" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg>`;
const lune = `<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path class="ico-lune" d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z" fill="currentColor"/><g class="ico-soleil" fill="currentColor"><circle cx="12" cy="12" r="4.2"/><path d="M11 1.5h2v3h-2zM11 19.5h2v3h-2zM1.5 11h3v2h-3zM19.5 11h3v2h-3zM4.2 5.6l1.4-1.4 2.1 2.1-1.4 1.4zM16.3 17.7l1.4-1.4 2.1 2.1-1.4 1.4zM4.2 18.4l2.1-2.1 1.4 1.4-2.1 2.1zM16.3 6.3l2.1-2.1 1.4 1.4-2.1 2.1z"/></g></svg>`;

// Le bouton de langue : la même page dans l'autre langue (l'accueil si elle n'a pas d'équivalent).
function langue(alt) {
  const autre = t.code === 'fr' ? LANGUES.en : LANGUES.fr;
  const href = alt || autres().accueil();
  return `<a class="bouton-langue" href="${href}" hreflang="${autre.code}" lang="${autre.code}" data-langue="${autre.code}"><span class="masque">${h(t.autreLangue)}</span><span aria-hidden="true">${autre.court}</span></a>`;
}

function bar({ home = false, current = '', alt = null } = {}) {
  const cur = (k) => (current === k ? ' aria-current="page"' : '');
  return `<a class="evitement" href="#contenu">${t.allerContenu}</a>
<header class="barre${home ? ' barre--jaquette' : ''}" data-barre>
  <a class="marque" href="${lien.accueil()}"${home ? ' aria-current="page"' : ''}>${h(t.marque)}</a>
  <nav class="nav" aria-label="${t.navPrincipale}">
    <a href="${lien.accueil()}#categories"${cur('categories')}>${t.categories}</a>
    <a href="${lien.chronologie()}"${cur('chronologie')}>${t.chronologie}</a>
    <a href="${lien.specs()}"${cur('specs')}>${t.specifications}</a>
    <a href="${lien.accueil()}#livre">${t.livre}</a>
  </nav>
  <div class="barre-actions">
    <button class="bouton-recherche" type="button" data-search-open aria-haspopup="dialog" aria-controls="recherche" aria-label="${t.rechercherMot}">${loupe}<span class="bouton-recherche-mot">${t.rechercher}</span><kbd data-kbd>Ctrl${NB}K</kbd></button>
    ${langue(alt)}
    <button class="bouton-theme" type="button" data-theme-toggle aria-label="${t.theme}">${lune}</button>
    <button class="bouton-menu" type="button" data-menu-open aria-haspopup="dialog" aria-controls="menu" aria-label="${t.menuAria}"><span class="bouton-menu-traits" aria-hidden="true"></span><span class="bouton-menu-mot">${t.menu}</span></button>
  </div>
</header>`;
}

// ---------------------------------------------------------------- Menu (téléphone et tablette)
// Le menu se remplit à l'ouverture (static/js/site.js) depuis ce modèle : les pages ne portent
// pas chacune la liste des catégories.
function menuDialog(alt) {
  const lettres = [...NAV.letters.entries()]
    .map(([l, d]) => (d.length ? `<li><a href="${lien.lettre(l)}" aria-label="${t.lettreAria(l, plural(d.length, t.mot))}">${l}</a></li>` : `<li><span aria-hidden="true">${l}</span></li>`))
    .join('');
  const parties = NAV.parts
    .filter((p) => p.cats.length)
    .map((p) => `<h3 class="menu-sous">${h(partieTitre(p))}</h3>
    <ul class="menu-cats">${p.cats
      .map((c) => `<li><a href="${lien.categorie(c)}"><svg class="picto" aria-hidden="true" focusable="false"><use href="/img/pictos.svg#p-${c.slug}"/></svg><span>${h(categoryLabel(c.name))}</span><span class="menu-n">${num(c.defs.length)}</span></a></li>`)
      .join('')}</ul>`)
    .join('\n    ');
  return `<dialog class="menu" id="menu" aria-labelledby="menu-titre">
  <div class="menu-panneau">
    <div class="menu-tete">
      <h2 class="menu-titre" id="menu-titre">${t.parcourir}</h2>
      <button class="recherche-fermer" type="button" data-menu-close>${t.fermer}</button>
    </div>
    <button class="menu-cherche" type="button" data-search-open>${loupe}<span>${t.rechercherMot}</span></button>
    <ul class="menu-liens menu-liens--haut">
      <li><a href="${lien.chronologie()}">${t.chronologie}</a></li>
      <li><a href="${lien.specs()}">${t.specifications}</a></li>
      <li><a href="${alt || autres().accueil()}" hreflang="${t.code === 'fr' ? 'en' : 'fr'}">${t.autreLangue}</a></li>
      <li><button class="menu-theme" type="button" data-theme-toggle>${t.theme}</button></li>
    </ul>
    <h3 class="menu-sous">${t.lesLettres}</h3>
    <ol class="abc">${lettres}</ol>
    ${parties}
    <ul class="menu-liens">
      <li><a href="${lien.accueil()}">${t.accueil}</a></li>
      <li><a href="${lien.accueil()}#livre">${t.livreImprime}</a></li>
      <li><a href="${site.pdf}" download>${t.pdfGratuit}</a></li>
      <li><a href="${site.github}" rel="noopener">GitHub</a></li>
    </ul>
  </div>
</dialog>`;
}

// Barre A–Z collante des pages de lettre et de catégorie. hrefFor(l) renvoie le lien, ou null si la lettre est absente.
function azIndex({ current = null, hrefFor, label }) {
  const items = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    .split('')
    .map((l) => {
      const href = hrefFor(l);
      if (!href) return '';
      return `<li><a href="${href}"${l === current ? ' aria-current="page"' : ''}>${l}</a></li>`;
    })
    .join('');
  return `<nav class="index-az" aria-label="${h(label)}"><ol>${items}</ol></nav>`;
}

// ---------------------------------------------------------------- Recherche (fenêtre partagée)
function searchDialog() {
  return `<dialog class="recherche" id="recherche" aria-labelledby="recherche-titre">
  <div class="recherche-panneau">
    <h2 class="masque" id="recherche-titre">${t.rechercheTitre}</h2>
    <form class="recherche-champ" role="search" action="${lien.recherche()}" method="get">
      ${loupe}
      <label class="masque" for="recherche-q">${t.termeAChercher}</label>
      <input id="recherche-q" name="q" type="search" autocomplete="off" autocapitalize="off" spellcheck="false" enterkeyhint="search"
        placeholder="${t.exemple}" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-controls="recherche-resultats">
      <button class="recherche-fermer" type="button" data-search-close>${t.fermer}</button>
    </form>
    <p class="recherche-etat" role="status" aria-live="polite"></p>
    <ul class="resultats" id="recherche-resultats" role="listbox" aria-label="${t.resultats}"></ul>
  </div>
</dialog>`;
}

// ---------------------------------------------------------------- Le dos (pied de page)
function footer(letters, total) {
  const year = new Date().getFullYear();
  const items = [...letters.entries()]
    .map(([l, defs], i) =>
      defs.length
        ? `<li><a href="${lien.lettre(l)}" style="--i:${i}" aria-label="${t.lettreAria(l, plural(defs.length, t.mot))}"><span class="dos-l" aria-hidden="true">${l}</span><span class="dos-n" aria-hidden="true">${num(defs.length)}</span></a></li>`
        : `<li><span class="dos-vide" aria-hidden="true"><span class="dos-l">${l}</span></span></li>`,
    )
    .join('');
  return `<footer class="dos dos--court" id="lettres">
  <h2 class="dos-court">${t.toutesLettres}</h2>
  <nav class="alphabet alphabet--court" aria-label="${t.toutesLettres}"><ol class="abc">${items}</ol></nav>
  <div class="dos-pied">
    <p class="dos-marque">${h(t.marque)}, ${h(site.author)}, ${t.edition(site.edition)}</p>
    <ul class="dos-liens">
      <li><a href="${lien.chronologie()}">${t.chronologie}</a></li>
      <li><a href="${lien.specs()}">${t.specifications}</a></li>
      <li><a href="${site.pdf}" download>${t.pdfGratuit}</a></li>
      <li><a href="${site.bitcoinBazar}" rel="noopener">Bitcoin Bazar</a></li>
      <li><a href="${site.amazon}" rel="noopener">Amazon</a></li>
      <li><a href="${site.github}" rel="noopener">GitHub</a></li>
      <li><a href="${site.authorUrl}" rel="author">pandul.fr</a></li>
      <li><a href="${site.authorX}" rel="noopener">X (Twitter)</a></li>
    </ul>
    <p class="dos-legal">${t.legal(year, h(site.author), `<a href="${site.licenseUrl}" rel="license noopener">${site.license}</a>`)}</p>
  </div>
</footer>`;
}

// Page complète : barre, contenu, dos, recherche.
function page({ headOpts, body, bodyClass, picto, letters, total, home = false, current = '' }) {
  const alt = headOpts.alt || null;
  return `${head(headOpts)}
<body class="${bodyClass}">
${picto.defs()}
${bar({ home, current, alt })}
<main id="contenu">
${body}
</main>
${footer(letters, total)}
${searchDialog()}
${menuDialog(alt)}
<script type="application/json" id="i18n">${JSON.stringify(t.js).replace(/</g, '\\u003c')}</script>
</body>
</html>
`;
}

// La page d'une partie ; la partie « Spécifications » mène aux résumés des spécifications.
const lienPartie = (p) => (p.id === 'specifications' ? lien.specs() : lien.partie(p.id));

// ---------------------------------------------------------------- Morceaux de listes
// Le texte d'une définition pas encore traduite reste en français : on le signale par lang="fr".
const langAttr = (d) => (d.lang && d.lang !== t.code ? ` lang="${d.lang}"` : '');
const resumeDe = (d) => d.resume || d.description || '';
// Données de la carte d'aperçu au survol (nom, catégorie, définition courte).
const apercuAttr = (d) => (resumeDe(d) ? ` data-apercu="${hd(resume(resumeDe(d), 220))}" data-apercu-cat="${h(categoryLabel(d.category))}" data-apercu-nom="${h(affiche(d.title))}"` : '');
// Une entrée de liste : nom, catégorie, une ligne de description.
function entry(def, picto, { showCategory = true } = {}) {
  const bip = /^BIP-\d/.test(def.titleFr || def.title);
  const sujet = bip ? def.related.filter((r) => !/^BIP(-\d|$)/.test(r.titleFr || r.title)).slice(0, 2).map((r) => breakable(r.title)).join(', ') : '';
  return `<li><a class="entree" href="${lien.def(def.slug)}"${apercuAttr(def)}>
  <span class="entree-nom" data-vt-nom>${showCategory && !bip ? picto.use(def.categorySlug) : ''}${breakable(def.title)}</span>${sujet ? `<span class="entree-sujet">${sujet}</span>` : ''}
  ${resumeDe(def) ? `<span class="entree-desc"${langAttr(def)}>${hd(resume(resumeDe(def), 120))}</span>` : ''}
</a></li>`;
}

// Groupes d'une liste : par centaine pour les BIP, sinon par lettre (catégories)
// ou par deux premières lettres (grandes lettres), en fusionnant les petits groupes.
const norm = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toUpperCase();
function bipKey(title) {
  const m = title.match(/^BIP-?(\d{4})/);
  if (!m) return null;
  const c = Math.floor(Number(m[1]) / 100) * 100;
  const a = String(c).padStart(4, '0');
  const b = String(c + 99).padStart(4, '0');
  return { key: `BIP-${a}`, label: t.code === 'fr' ? `BIP-${a} à ${b}` : `BIP-${a} to ${b}` };
}
function groupEntries(defs, mode) {
  const raw = [];
  for (const d of defs) {
    const b = bipKey(d.title);
    let key;
    let label;
    if (b) ({ key, label } = b);
    else if (mode === 'deux') {
      // Les deux premières lettres ; un titre dont le second signe n'est pas une lettre (B-MONEY)
      // est trié en tête par le classement : il rejoint le premier groupe de sa lettre.
      const tt = norm(d.title);
      key = /[A-Z0-9]/.test(tt[1] || '') ? tt.slice(0, 2) : `${tt[0]}A`;
      label = key;
    } else {
      const f = norm(d.title)[0];
      key = /[A-Z]/.test(f) ? f : '#';
      label = key;
    }
    const last = raw.at(-1);
    if (last && last.key === key) last.defs.push(d);
    else raw.push({ key, label, defs: [d] });
  }
  // Fusion des petits groupes avec leurs voisins (hors BIP) : « BA – BE » (deux lettres, moins de 5 mots)
  // ou « J – L » (une lettre, moins de 4 mots dans une catégorie).
  const seuil = mode === 'deux' ? 5 : 4;
  const out = [];
  for (const g of raw) {
    const prev = out.at(-1);
    const isBip = g.key.startsWith('BIP-');
    if (prev && !isBip && !prev.bip && (prev.defs.length < seuil || g.defs.length < seuil) && prev.defs.length + g.defs.length <= (mode === 'deux' ? 999 : 12)) {
      prev.defs.push(...g.defs);
      prev.last = g.label;
    } else out.push({ ...g, bip: isBip, first: g.label, last: g.label, keys: [] });
    out.at(-1).keys.push(g.key);
  }
  for (const g of out) if (!g.bip) g.label = g.first === g.last ? g.first : `${g.first} – ${g.last}`;
  // Un libellé en double (« BI » avant et après les BIP) prend les trois premières lettres de ses mots.
  const trois = (d) => norm(d.title).replace(/[^A-Z0-9]/g, '').slice(0, 3);
  const compte = new Map();
  for (const g of out) compte.set(g.label, (compte.get(g.label) || 0) + 1);
  for (const g of out) {
    if (g.bip || compte.get(g.label) < 2) continue;
    const a = trois(g.defs[0]);
    const b = trois(g.defs.at(-1));
    g.label = a === b ? a : `${a} – ${b}`;
  }
  return out;
}

function groupedList(defs, picto, { mode, showCategory = true, labelPrefix = '' }) {
  const groups = groupEntries(defs, mode);
  if (groups.length === 1 && mode === 'deux') {
    return `<ul class="entrees">${defs.map((d) => entry(d, picto, { showCategory })).join('\n')}</ul>`;
  }
  return groups
    .map((g, i) => {
      const id = `groupe-${i + 1}`;
      return `<section class="groupe" aria-labelledby="${id}">
  <div class="groupe-tete"><h2 class="groupe-titre" id="${id}"><span class="masque">${labelPrefix}</span>${h(g.label)}</h2><p class="groupe-n">${plural(g.defs.length, t.mot)}</p></div>
  <ul class="entrees">${g.defs.map((d) => entry(d, picto, { showCategory })).join('\n')}</ul>
</section>`;
    })
    .join('\n');
}

// Texte court en Markdown d'une ligne (chronologie, résumés de spécifications) : italique, code, liens.
const enLigne = (s) =>
  h(fr(s))
    .replace(/`([^`]+)`/g, '<code>$1</code>')
    .replace(/\*([^*\n]+)\*/g, '<em>$1</em>');

// Date de la chronologie : « 2015-01-04 » -> « 4 janvier 2015 », « 1978-02 » -> « février 1978 ».
export function dateLisible(d) {
  const [a, m, j] = d.split('-');
  if (j) return t.dateLongue(Number(j), t.mois[Number(m) - 1], a);
  if (m) return `${t.mois[Number(m) - 1]} ${a}`;
  return a;
}
export const ancreEvenement = (e, i) => `d-${e.date}-${i}`;

// ---------------------------------------------------------------- Définition
// liens : { chrono: [événements liés], spec: entrée de spécification consacrée au mot }.
export function definitionPage(def, { html, math, assets, jsonLd, total, letters, liens = {} }) {
  const picto = pictoCollector();
  const cat = categoryLabel(def.category);
  const letter = def.letter;
  const letterCount = letters.get(letter)?.length || 0;
  const nonTraduite = def.lang !== t.code;
  const tags = [
    `<li><a class="etiquette" href="${lien.categorie({ name: def.category, slug: def.categorySlug })}">${picto.use(def.categorySlug)}${h(cat)}</a></li>`,
    def.englishTerm && t.code === 'fr' ? `<li class="etiquette etiquette--langue"><span class="etiquette-cle">${t.enAnglais}</span> <span lang="en">${h(def.englishTerm)}</span></li>` : '',
    def.frenchTerm ? `<li class="etiquette etiquette--langue"><span class="etiquette-cle">${t.enFrancais}</span> <span lang="fr">${h(def.frenchTerm)}</span></li>` : '',
    t.code === 'en' && def.titleFr !== def.title && !def.frenchTerm ? `<li class="etiquette etiquette--langue"><span class="etiquette-cle">${t.enFrancais}</span> <span lang="fr">${h(affiche(def.titleFr))}</span></li>` : '',
  ].join('');

  const renvoi = (r) => `<li><a class="renvoi" href="${lien.def(r.slug)}">
  <span class="renvoi-nom" data-vt-nom>${breakable(r.title)}</span>
  <span class="renvoi-cat">${picto.use(r.categorySlug)}${h(categoryLabel(r.category))}</span>
  ${resumeDe(r) ? `<span class="renvoi-desc"${langAttr(r)}>${hd(resume(resumeDe(r), 120))}</span>` : ''}
</a></li>`;
  const related = def.related.length
    ? `<aside class="renvois" aria-labelledby="renvois-titre">
  <h2 class="renvois-titre" id="renvois-titre">${t.termesAssocies[def.related.length > 1 ? 1 : 0]}</h2>
  <ul>${def.related.map(renvoi).join('\n')}</ul>
</aside>`
    : '';
  const cited = def.citedBy.filter((d) => !def.related.includes(d)).sort((a, b) => compareTitres(a.title, b.title));
  const citedHtml = cited.length
    ? `<section class="cites" aria-labelledby="cites-titre">
  <h2 class="cites-titre" id="cites-titre">${t.renvoientIci(num(cited.length))}</h2>
  <ul class="cites-liste"${cited.length > 12 ? ' data-repliable' : ''}>${cited.map((d) => `<li><a href="${lien.def(d.slug)}"${apercuAttr(d)}>${breakable(d.title)}</a></li>`).join('')}</ul>
</section>`
    : '';

  // Les dates de la chronologie qui parlent de ce mot, et sa fiche de spécification.
  const chrono = liens.chrono?.length
    ? `<section class="mot-chrono" aria-labelledby="mot-chrono-titre">
  <h2 class="cites-titre" id="mot-chrono-titre">${t.dansChronologie}</h2>
  <ol>${liens.chrono.map(({ e, ancre }) => `<li><a href="${lien.chronologie()}#${ancre}"><time datetime="${h(e.date)}">${h(dateLisible(e.date))}</time><span${e.lang !== t.code ? ` lang="${e.lang}"` : ''}>${h(fr(e.title))}</span></a></li>`).join('')}</ol>
</section>`
    : '';
  const spec = liens.spec
    ? (() => {
        const sp = liens.spec;
        const lignes = [
          sp.status.length ? `<div><dt>${t.statut}</dt><dd>${sp.status.map(h).join(', ')}</dd></div>` : '',
          sp.type ? `<div><dt>${t.type}</dt><dd>${h(sp.type)}${sp.layer ? ` · ${h(sp.layer)}` : ''}</dd></div>` : '',
          sp.authors.length ? `<div><dt>${t.auteurs[sp.authors.length > 1 ? 1 : 0]}</dt><dd>${sp.authors.map(h).join(', ')}</dd></div>` : '',
          sp.created ? `<div><dt>${t.cree}</dt><dd><time datetime="${h(sp.created)}">${h(dateLisible(sp.created))}</time></dd></div>` : '',
        ].join('');
        return `<aside class="mot-spec" aria-labelledby="mot-spec-titre">
  <h2 class="cites-titre" id="mot-spec-titre"><span lang="en">${h(sp.id)}</span> · <span lang="en">${h(sp.title)}</span></h2>
  <dl>${lignes}</dl>
  <p class="mot-spec-liens">${sp.url ? `<a href="${h(sp.url)}" rel="noopener">${t.lireDocument}</a>` : ''} <a href="${lien.specs(sp.groupe)}#${sp.id.toLowerCase()}">${t.voirResume}</a></p>
</aside>`;
      })()
    : '';

  const turn = (d, dir) => {
    if (!d) return `<span class="tourner-vide"></span>`;
    const label = dir === 'prev' ? t.motPrecedent : t.motSuivant;
    return `<a class="tourner-lien tourner-lien--${dir}" href="${lien.def(d.slug)}" rel="${dir}" data-turn="${dir}">
  <span class="tourner-sens">${label}</span>
  <span class="tourner-nom">${breakable(d.title)}</span>
  ${resumeDe(d) ? `<span class="tourner-desc"${langAttr(d)}>${hd(resume(resumeDe(d), 120))}</span>` : ''}
</a>`;
  };
  const editUrl = `${site.github}/blob/main/${def.sourcePath}`;
  const avis = nonTraduite ? `<p class="avis-langue" role="note"><span class="avis-langue-cle">${t.nonTraduitCourt}</span> ${t.nonTraduit}</p>` : '';
  const body = `<nav class="reperes" aria-label="${t.motsVoisins}">
  ${def.alphaPrev ? `<a class="reperes-prec" href="${lien.def(def.alphaPrev.slug)}" data-turn="prev"${apercuAttr(def.alphaPrev)}><span class="masque">${t.motPrecedent} : </span><span class="reperes-nom">${breakable(def.alphaPrev.title)}</span><span class="reperes-court" aria-hidden="true">${t.precedent}</span></a>` : '<span></span>'}
  <a class="reperes-lettre" href="${lien.lettre(letter)}" aria-label="${t.lettreAria(letter, plural(letterCount, t.mot))}">${letter}</a>
  ${def.alphaNext ? `<a class="reperes-suiv" href="${lien.def(def.alphaNext.slug)}" data-turn="next"${apercuAttr(def.alphaNext)}><span class="masque">${t.motSuivant} : </span><span class="reperes-nom">${breakable(def.alphaNext.title)}</span><span class="reperes-court" aria-hidden="true">${t.suivant}</span></a>` : '<span></span>'}
</nav>
<article class="mot${related ? '' : ' mot--seul'}" data-mot="${h(def.slug)}" data-titre="${h(affiche(def.title))}">
  <header class="mot-tete">
    <div class="mot-titre">
      <h1 class="vedette${def.title.includes('_') ? ' vedette--bas' : ''}" style="--em:${headwordEm(def.title)}">${headwordWords(def.title)}</h1>
      <ul class="etiquettes">${tags}</ul>
    </div>
  </header>
  <div class="mot-marge">
    <figure class="signet" style="--pos:${((def.n - 0.5) / total * 100).toFixed(3)}%">
      <div class="signet-tranche" role="img" aria-label="${t.placeLivre(num(def.n), num(total))}"><span class="signet-ruban"></span></div>
      <figcaption class="signet-legende">${t.signetLegende(num(def.n), num(total), ordinal(def.n - (letters.get(letter)?.[0]?.n || 1) + 1), letter)}</figcaption>
    </figure>
    ${spec}
    ${related}
  </div>
  <div class="mot-corps">
    ${avis}
    <div class="prose"${langAttr(def)}>${html}</div>
  </div>
  ${chrono}
  ${citedHtml}
</article>
<nav class="tourner" aria-label="${t.tournerPage}">
  ${turn(def.alphaPrev, 'prev')}
  ${turn(def.alphaNext, 'next')}
</nav>
<p class="colophon"><cite>${h(t.marque)}</cite>, ${t.edition(site.edition)}. <a href="${editUrl}" rel="noopener">${t.corriger}</a> <button class="citer" type="button" data-citer="${h(t.citation(site.author, affiche(def.title), t.marque, site.edition, `${url}${lien.def(def.slug)}`))}" hidden>${t.citer}</button></p>`;

  const autre = autres();
  return page({
    headOpts: {
      title: t.titreDef(affiche(def.title)),
      description: def.description || t.descDef(def.title, cat),
      path: lien.def(def.slug),
      // La même entrée dans l'autre langue, sous son slug dans cette langue (null : exclue de la traduction).
      alt: def.slugs[autre.code] ? autre.def(def.slugs[autre.code]) : null,
      // Une page anglaise encore en français : l'adresse canonique est la page française.
      canonique: t.code !== 'fr' && nonTraduite ? FR_PATHS.def(def.slugs.fr) : null,
      jsonLd,
      math,
      type: 'article',
      assets,
    },
    body,
    bodyClass: 'p-mot',
    picto,
    letters,
    total,
  });
}

// ---------------------------------------------------------------- Lettre
export function letterPage(letter, defs, letters, { assets, jsonLd, total }) {
  const picto = pictoCollector();
  const keys = [...letters.keys()].filter((l) => letters.get(l).length);
  const i = keys.indexOf(letter);
  const prev = keys[i - 1];
  const next = keys[i + 1];
  const groups = defs.length > 40 ? groupEntries(defs, 'deux') : [];
  const sousIndex = groups.length > 1
    ? `<nav class="sous-index" aria-label="${t.groupesLettre(letter)}">
  <ul>${groups.map((g, k) => `<li><a href="#groupe-${k + 1}">${h(g.label)}</a></li>`).join('')}</ul>
</nav>`
    : '';
  const body = `${azIndex({ current: letter, hrefFor: (l) => (letters.get(l)?.length ? lien.lettre(l) : null), label: t.toutesLettres })}
<header class="lettre-tete">
  <p class="grande-lettre" aria-hidden="true"><span class="gl"><span class="gl-in">${letter}</span></span></p>
  <div class="lettre-info">
    <h1 class="titre lettre-titre">${t.motsEn(letter)}</h1>
    <p class="enonce">${t.motsDuDico(plural(defs.length, t.mot), insecable(defs[0].title), insecable(defs.at(-1).title))}</p>
    <nav class="lettres-voisines" aria-label="${t.lettresVoisines}">
      ${prev ? `<a href="${lien.lettre(prev)}" rel="prev"><span class="masque">${t.lettrePrecedente}</span>${prev}</a>` : ''}
      ${next ? `<a href="${lien.lettre(next)}" rel="next"><span class="masque">${t.lettreSuivante}</span>${next}</a>` : ''}
    </nav>
  </div>
</header>
<div class="liste-bloc">
${sousIndex}
<div class="liste">
${groupedList(defs, picto, { mode: defs.length > 40 ? 'deux' : 'une', labelPrefix: t.groupe })}
</div>
</div>
${next ? `<p class="lettre-suite"><a class="bouton" href="${lien.lettre(next)}">${t.lettreSuivante}${next}</a></p>` : ''}`;
  return page({
    headOpts: {
      title: t.titreLettre(letter, defs.length),
      description: t.descLettre(defs.length, letter, affiche(defs[0]?.title), affiche(defs.at(-1)?.title)),
      path: lien.lettre(letter),
      alt: autres().lettre(letter),
      jsonLd,
      assets,
    },
    body,
    bodyClass: 'p-lettre',
    picto,
    letters,
    total,
  });
}

// ---------------------------------------------------------------- Catégorie
export function categoryPage(cat, note, { assets, jsonLd, letters, total, categories, part }) {
  const picto = pictoCollector();
  const label = categoryLabel(cat.name);
  const groups = groupEntries(cat.defs, 'une');
  // Barre d'index collante : une entrée par groupe (lettres, et centaines pour les BIP).
  // Toutes les lettres restent à leur place (les absentes, désactivées) ; les BIP ajoutent leurs centaines.
  const ancres = new Map();
  groups.forEach((g, i) => (g.keys || [g.key]).forEach((k) => ancres.set(k, `#groupe-${i + 1}`)));
  const cases = [];
  for (const l of 'ABCDEFGHIJKLMNOPQRSTUVWXYZ') {
    cases.push(ancres.has(l) ? `<li><a href="${ancres.get(l)}">${l}</a></li>` : `<li><span class="absente" aria-hidden="true">${l}</span></li>`);
    if (l === 'B') for (const g of groups) if (g.key.startsWith('BIP-')) cases.push(`<li><a href="${ancres.get(g.key)}" aria-label="${h(g.label)}">${g.key.slice(4)}</a></li>`);
  }
  const indexGroupes = `<nav class="index-az" aria-label="${h(t.lettresCategorie(label))}"><ol>${cases.join('')}</ol></nav>`;
  // Le rayon : les catégories de la même partie du livre.
  const voisines = part ? part.cats : categories;
  const rayon = `<nav class="rayon" aria-labelledby="rayon-titre"><h2 class="rayon-titre" id="rayon-titre">${part ? h(partieTitre(part)) : t.lesNCategories(categories.length)}</h2><ul>${voisines
    .map((c) => `<li><a href="${lien.categorie(c)}"${c.slug === cat.slug ? ' aria-current="page"' : ''}>${picto.use(c.slug)}<span>${h(categoryLabel(c.name))}</span></a></li>`)
    .join('')}</ul></nav>`;
  // Présentation : la première phrase entière, la suite repliée derrière « Lire la suite ».
  // Les notes de categories.yaml sont en français : en anglais, on ne les montre pas.
  const texte = note && t.code === 'fr' ? fr(note.replace(/\.$/, '')) + '.' : '';
  const coupe = texte.search(/[.!?] (?=[A-ZÀ-Ý«])/);
  // Une suite courte (moins de 160 signes) s'affiche avec le reste : un « Lire la suite » pour une ligne ne sert à rien.
  const [premiere, suite] = coupe > 0 && texte.length - coupe > 160 ? [texte.slice(0, coupe + 1), texte.slice(coupe + 2)] : [texte, ''];
  const body = `<header class="cat-tete">
  <p class="cat-picto">${picto.use(cat.slug, 'picto picto--grand')}</p>
  ${part ? `<p class="cat-partie"><a href="${lienPartie(part)}">${h(partieTitre(part))}</a></p>` : ''}
  <h1 class="cat-nom">${h(label)}</h1>
  <p class="enonce cat-note">${t.defsDuDico(plural(cat.defs.length, t.definition))}${premiere ? `<span class="cat-note-premiere"> ${h(premiere)}</span>` : ''}${suite ? `<span class="cat-note-suite" data-repliable-suite> ${h(suite)}</span>` : ''}</p>
  <section class="cat-debut" aria-labelledby="debut-titre">
    <h2 class="cat-debut-titre" id="debut-titre">${t.pourCommencer}</h2>
    <ul>${[...cat.defs].sort((a, b) => b.citedBy.length - a.citedBy.length || compareTitres(a.title, b.title)).slice(0, 4).map((d) => `<li><a class="renvoi" href="${lien.def(d.slug)}"><span class="renvoi-nom" data-vt-nom>${breakable(d.title)}</span>${resumeDe(d) ? `<span class="renvoi-desc"${langAttr(d)}>${hd(resume(resumeDe(d)))}</span>` : ''}</a></li>`).join('')}</ul>
  </section>
</header>
<div class="liste-bloc">
${indexGroupes}
<div class="liste">
${groupedList(cat.defs, picto, { mode: 'une', showCategory: false, labelPrefix: cat.slug === 'bip' ? '' : t.lettre })}
</div>
</div>
${rayon}`;
  return page({
    headOpts: {
      title: t.titreCat(label, cat.defs.length),
      description: note && t.code === 'fr'
        ? `${cat.defs.length} définitions. ${note}`.slice(0, 155).replace(/\s+\S*$/, '…')
        : t.descCat(cat.defs.length, label),
      path: lien.categorie(cat),
      alt: autres().categorie(cat),
      jsonLd,
      assets,
    },
    body,
    bodyClass: 'p-cat',
    picto,
    letters,
    total,
    current: 'categories',
  });
}

// ---------------------------------------------------------------- Partie du livre
// Une partie (technique, écosystème, personnes) : ses catégories, chacune avec toutes ses entrées.
export function partPage(part, { assets, letters, total, jsonLd }) {
  const picto = pictoCollector();
  const n = part.cats.reduce((s, c) => s + c.defs.length, 0);
  const body = `<header class="partie-tete">
  <h1 class="titre-page">${h(partieTitre(part))}</h1>
  <p class="enonce">${h(fr(partieIntro(part)))}</p>
  <nav class="partie-cats" aria-label="${t.categories}"><ul>${part.cats.map((c) => `<li><a href="#c-${c.slug}">${picto.use(c.slug)}<span>${h(categoryLabel(c.name))}</span><span class="menu-n">${num(c.defs.length)}</span></a></li>`).join('')}</ul></nav>
</header>
<div class="partie-liste">
${part.cats.map((c) => `<section class="groupe" id="c-${c.slug}" aria-labelledby="t-${c.slug}">
  <div class="groupe-tete"><h2 class="groupe-titre groupe-titre--cat" id="t-${c.slug}">${picto.use(c.slug)}<a href="${lien.categorie(c)}">${h(categoryLabel(c.name))}</a></h2><p class="groupe-n">${plural(c.defs.length, t.definition)}</p></div>
  <ul class="entrees">${c.defs.map((d) => entry(d, picto, { showCategory: false })).join('\n')}</ul>
</section>`).join('\n')}
</div>`;
  return page({
    headOpts: {
      title: t.titrePartie(partieTitre(part), n),
      description: fr(partieIntro(part)).slice(0, 155),
      path: lien.partie(part.id),
      alt: autres().partie(part.id),
      jsonLd,
      assets,
    },
    body,
    bodyClass: 'p-partie',
    picto,
    letters,
    total,
    current: 'categories',
  });
}

// ---------------------------------------------------------------- Accueil
const CONTRIBUTORS = [
  ['Psyduck07', 'https://github.com/Psyduck07'],
  ['Adrien Lacombe', 'https://github.com/adrienlacombe'],
  ['Ludovic Lars', 'https://github.com/lugaxker'],
  ['Beemo', 'https://github.com/nflatrea'],
  ['quinoah', 'https://github.com/quinoah'],
];

// L'Allée des baobabs de la couverture (lib/allee.json, tiré de design/couverture/baobab.py) :
// un calque par arbre, pour qu'ils poussent l'un après l'autre et suivent le pointeur.
export function allee(cls = 'allee') {
  const [x, y, w, hh] = ALLEE.viewBox;
  const arbre = (a, k) => `<g class="allee-arbre allee-${a.nom}" style="--k:${k}">${a.fond ? `<path class="a-fond" d="${a.fond}"/>` : ''}<path class="a-arbre" d="${a.arbre}"/><path class="a-clair" d="${a.clair}"/></g>`;
  return `<svg class="${cls}" viewBox="${x} ${y} ${w} ${hh}" aria-hidden="true" focusable="false" preserveAspectRatio="xMidYMax meet">
  <g class="allee-astre"><path class="a-soleil" d="${ALLEE.soleil}"/></g>
  ${ALLEE.fond.map((a, k) => arbre(a, k)).join('\n  ')}
  ${arbre(ALLEE.grand, 3)}
  <path class="a-sol" d="${ALLEE.sol}"/>
</svg>`;
}

export function homePage(data, { assets, jsonLd }) {
  const { definitions, categories, letters, featured, parts, chrono, specs } = data;
  const total = definitions.length;
  const picto = pictoCollector();
  for (const c of categories) picto.use(c.slug);

  const catRow = (c) => `<li class="index-ligne">
  <a class="index-nom" href="${lien.categorie(c)}">${picto.use(c.slug)}<span>${h(categoryLabel(c.name))}</span><span class="index-n">${num(c.defs.length)}</span></a>
</li>`;
  // Les parties du livre (hors spécifications, qui ont leur propre section) ; à défaut, toutes les catégories.
  const partsDico = parts.filter((p) => p.id !== 'specifications' && p.cats.length);
  const blocsParties = partsDico.length
    ? partsDico.map((p, k) => `<section class="partie" aria-labelledby="partie-${p.id}" style="--k:${k}">
  <div class="partie-entete">
    <h3 class="partie-titre" id="partie-${p.id}"><a href="${lienPartie(p)}">${h(partieTitre(p))}</a></h3>
    <p class="partie-n">${plural(p.cats.reduce((s, c) => s + c.defs.length, 0), t.definition)}</p>
  </div>
  <ul class="index">${p.cats.map(catRow).join('\n')}</ul>
</section>`).join('\n')
    : `<ul class="index">${categories.map(catRow).join('\n')}</ul>`;

  const letterBlocks = [...letters.entries()]
    .filter(([, d]) => d.length)
    .map(([l, d]) => `<li style="--n:${d.length}"><a href="${lien.lettre(l)}" data-lettre="${l}" aria-label="${t.lettreAria(l, plural(d.length, t.mot))}"><span class="bloc-l" aria-hidden="true">${l}</span></a></li>`)
    .join('');

  // Nouveautés de l'édition : les chiffres viennent des fichiers présents.
  const nEvenements = chrono.reduce((s, a) => s + a.events.length, 0);
  const premiere = chrono[0]?.events[0]?.date.slice(0, 4);
  const derniere = chrono.at(-1)?.events.at(-1)?.date.slice(0, 4);
  const nSpecs = specs.reduce((s, g) => s + g.series.reduce((x, se) => x + se.entries.length, 0), 0);
  const partie = (id) => parts.find((p) => p.id === id);
  const nPartie = (id) => partie(id)?.cats.reduce((s, c) => s + c.defs.length, 0) || 0;
  // Un schéma, pas un logo : les images de tiers portent un crédit.
  const avecSchema = definitions.filter((d) => d.assets.some((x) => !x.credit));
  const schema = avecSchema.find((d) => d.slugs.fr === 'double-depense') || avecSchema[0];
  const cartes = [
    nEvenements ? { href: lien.chronologie(), titre: t.chronologie, texte: t.chronoCarte(num(nEvenements), premiere, derniere) } : null,
    nSpecs ? { href: lien.specs(), titre: t.specifications, texte: t.specsCarte(num(nSpecs), nomsSeries(specs.flatMap((g) => g.series.map((se) => se.id)))) } : null,
    nPartie('personnes') ? { href: lien.partie('personnes'), titre: partieTitre(partie('personnes')), texte: t.personnesCarte(num(nPartie('personnes'))) } : null,
    nPartie('ecosysteme') ? { href: lien.partie('ecosysteme'), titre: partieTitre(partie('ecosysteme')), texte: t.ecoCarte(num(nPartie('ecosysteme'))) } : null,
    schema ? { href: lien.def(schema.slug), titre: t.schemas, texte: t.schemasCarte(num(avecSchema.length)) } : null,
  ].filter(Boolean);
  // Le sommaire des nouveautés : une ligne par contenu, son nom puis ce qu'il contient.
  const nouveautes = cartes.length
    ? `<section class="nouveautes" aria-labelledby="nouveautes-titre">
  <div class="nouveautes-tete">
    <h2 class="titre" id="nouveautes-titre">${t.nouveautes}</h2>
    <p class="enonce">${t.nouveautesEnonce}</p>
  </div>
  <ul class="sommaire">${cartes.map((c, k) => `<li style="--k:${k}"><a href="${c.href}"><span class="sommaire-nom">${h(c.titre)}</span><span class="sommaire-texte">${c.texte}</span></a></li>`).join('')}</ul>
</section>`
    : '';

  const f = featured;
  // Le vrai dossier d'une définition, tel qu'il est sur GitHub.
  const exemple = definitions.find((d) => d.slugs.fr === 'utxo') || definitions[0];
  const source = {
    slug: exemple.slug,
    dir: path.dirname(exemple.sourcePath) + '/',
    body: `${exemple.body.trim().split(/(?<=\.)\s+/).slice(0, 3).join(' ')} […]`,
  };
  const [l1, l2] = t.couvTitre;
  const body = `<section class="couverture" aria-labelledby="titre">
  <div class="couverture-texte">
    <h1 class="couv-titre" id="titre"><span class="ligne"><span>${h(l1)}</span></span> <span class="ligne"><span>${h(l2)}</span></span></h1>
    <p class="couv-sous">${h(t.sousTitre)}</p>
    <form class="couv-recherche" role="search" action="${lien.recherche()}" method="get" data-hero-search>
      <label class="masque" for="couv-q">${t.chercherParmi(num(total))}</label>
      <input id="couv-q" name="q" type="search" autocomplete="off" spellcheck="false" enterkeyhint="search" placeholder="${t.exemple}">
      <button type="submit">${t.chercher}</button>
    </form>
    <p class="couv-meta">${t.couvMeta(num(total), h(site.author), site.edition)}</p>
  </div>
  <div class="couverture-image" aria-hidden="true">${allee()}</div>
</section>

<section class="jour" aria-labelledby="jour-titre" data-jour>
  <h2 class="titre jour-titre" id="jour-titre">${t.motDuJour}</h2>
  <div class="jour-corps">
    <p class="jour-mot"><a href="${lien.def(f.slug)}" data-jour-lien><span data-jour-nom>${breakable(f.title)}</span></a></p>
    <p class="jour-cat"><a class="etiquette" href="${lien.categorie({ name: f.category, slug: f.categorySlug })}" data-jour-cat>${picto.use(f.categorySlug)}<span>${h(categoryLabel(f.category))}</span></a></p>
    <p class="jour-desc" data-jour-desc${langAttr(f)}>${hd(resumeDe(f))}</p>
    <p class="jour-actions"><a class="bouton" href="${lien.def(f.slug)}" data-jour-lire>${t.lireDef}</a> <button class="bouton bouton--doux" type="button" data-jour-autre>${t.autreMot}</button></p>
  </div>
</section>

${nouveautes}

<section class="feuilleter" aria-labelledby="feuilleter-titre" data-tranche>
  <div class="feuilleter-tete">
    <h2 class="titre" id="feuilleter-titre">${t.feuilleter(num(total))}</h2>
    <p class="enonce">${t.feuilleterEnonce}</p>
  </div>
  <nav class="blocs" aria-label="${t.lettresTranche}"><ol>${letterBlocks}</ol></nav>
  <div class="bande" data-bande><p class="bande-sans-script">${t.sansScript}</p></div>
  <div class="apercu" aria-live="polite" data-apercu>
    <p class="apercu-nom"><a href="${lien.def(f.slug)}" data-apercu-lien>${breakable(f.title)}</a></p>
    <p class="apercu-cat" data-apercu-cat>${h(categoryLabel(f.category))}</p>
    <p class="apercu-desc" data-apercu-desc>${hd(resumeDe(f))}</p>
  </div>
</section>

<section class="categories" id="categories" aria-labelledby="categories-titre">
  <div class="categories-tete">
    <h2 class="titre" id="categories-titre">${partsDico.length ? t.partiesTitre : t.categories}</h2>
    <p class="enonce">${t.partiesEnonce}</p>
  </div>
  <div class="parties">${blocsParties}</div>
</section>

<section class="livre" id="livre" aria-labelledby="livre-titre">
  <div class="livre-haut">
    <figure class="livre-volume"><video muted loop playsinline preload="none" poster="/video/feuilletage.webp" width="640" height="990" aria-label="${t.video}" data-boucle><source src="/video/feuilletage.mp4" type="video/mp4"></video></figure>
    <div class="livre-texte">
      <h2 class="titre" id="livre-titre">${t.livreTitre}</h2>
      <p class="enonce">${t.livreEnonce}</p>
      <p class="livre-actions"><a class="bouton" href="${site.bitcoinBazar}" rel="noopener">${t.commander}</a> <a class="lien" href="${site.amazon}" rel="noopener">${t.ouAmazon}</a></p>
      <p>${t.pdfReste}<a class="lien" href="${site.pdf}" download>${t.telechargerPdf}</a> (2,7${NB}Mo).</p>
      <p class="note">${t.isbn(site.isbnPaperback, site.isbnHardcover)}</p>
    </div>
  </div>
</section>

<section class="ouvert" aria-labelledby="ouvert-titre">
  <div class="ouvert-texte">
    <h2 class="titre" id="ouvert-titre">${t.ouvertTitre}</h2>
    <p class="enonce">${t.ouvertEnonce}</p>
    <p><a class="bouton" href="${site.github}" rel="noopener">${t.contribuer}</a></p>
    <div class="ouvert-auteur">
      <img src="/img/loic-morel.webp" width="560" height="560" alt="${t.portrait}" loading="lazy" decoding="async">
      <p>${t.ecritPar} <a class="lien" href="${site.authorUrl}" rel="author">Loïc Morel</a>, ${t.reluPar}${CONTRIBUTORS.map(([n, u]) => `<a class="lien" href="${u}" rel="noopener">${h(n)}</a>`).join(', ')}.</p>
    </div>
    <p class="note">${t.licenceNote(site.license, `<span class="lightning">${site.lightning}</span>`)}</p>
  </div>
  <figure class="fichier" data-ui>
    <figcaption class="fichier-chemin"><code>${h(source.dir)}</code></figcaption>
    <p class="fichier-nom">${t.fichierNom}</p>
    <pre class="fichier-texte"${langAttr(exemple)}><code>${h(source.body).replace(/\*([^*]+)\*/g, '<span class="md">*</span><em>$1</em><span class="md">*</span>').replace(/`([^`]+)`/g, '<span class="md">`</span>$1<span class="md">`</span>')}</code></pre>
    <ul class="fichier-liens"><li><a class="lien" href="${site.github}/blob/main/${exemple.sourcePath}" rel="noopener">${t.ouvrirFichier}</a></li><li><a class="lien" href="${lien.def(source.slug)}">${t.lireRendue}</a></li></ul>
  </figure>
</section>`;

  return page({
    headOpts: {
      title: t.titreAccueil,
      description: t.descAccueil(num(total)),
      path: lien.accueil(),
      alt: autres().accueil(),
      jsonLd,
      assets,
      themeColor: palette.figue,
      extraJs: assets.home,
    },
    body,
    bodyClass: 'p-accueil',
    picto,
    letters,
    total,
    home: true,
  });
}

// ---------------------------------------------------------------- Recherche (page)
export function searchPage({ assets, letters, total, categories }) {
  const picto = pictoCollector();
  const body = `<header class="cherche-tete">
  <h1 class="titre-page">${t.rechercher}</h1>
  <p class="enonce">${t.rechercheEnonce(num(total))}</p>
  <form class="cherche-form" role="search" action="${lien.recherche()}" method="get" data-search-page>
    <label class="masque" for="cherche-q">${t.termeAChercher}</label>
    ${loupe}
    <input id="cherche-q" name="q" type="search" autocomplete="off" spellcheck="false" enterkeyhint="search" placeholder="${t.exemple}" aria-controls="cherche-resultats">
  </form>
  <fieldset class="filtres" data-filtres>
    <legend class="masque">${t.filtrer}</legend>
    <label class="filtre"><input type="radio" name="cat" value="" checked><span>${t.toutes}</span></label>
    ${categories.map((c) => `<label class="filtre"><input type="radio" name="cat" value="${c.slug}"><span>${picto.use(c.slug)}${h(categoryLabel(c.name))}</span></label>`).join('\n    ')}
  </fieldset>
</header>
<p class="cherche-etat" role="status" aria-live="polite" data-search-status>${t.rechercheSansJs}</p>
<ul class="resultats resultats--page" id="cherche-resultats" data-search-results></ul>`;
  return page({
    headOpts: {
      title: t.titreRecherche,
      description: t.descRecherche(total),
      path: lien.recherche(),
      alt: autres().recherche(),
      robots: 'noindex, follow',
      assets,
    },
    body,
    bodyClass: 'p-cherche',
    picto,
    letters,
    total,
  });
}

// ---------------------------------------------------------------- 404
export function notFoundPage({ assets, letters, total }) {
  const picto = pictoCollector();
  const body = `<section class="couverture perdu" aria-labelledby="perdu-titre">
  <div class="couverture-texte perdu-texte">
    <h1 class="perdu-titre" id="perdu-titre">${t.introuvable}</h1>
    <p class="couv-sous">${t.introuvableEnonce}</p>
    <form class="couv-recherche" role="search" action="${lien.recherche()}" method="get" data-perdu-champ>
      <label class="masque" for="perdu-q">${t.chercherTerme}</label>
      <input id="perdu-q" name="q" type="search" autocomplete="off" spellcheck="false" enterkeyhint="search" placeholder="${t.exemple}" aria-controls="perdu-resultats">
      <button type="submit">${t.chercher}</button>
    </form>
    <div class="perdu-suggestions" data-suggestions hidden>
      <h2 class="perdu-sous" data-suggestions-titre>${t.vouliezVous}</h2>
      <ul class="perdu-liste" id="perdu-resultats" data-suggestions-liste></ul>
    </div>
    <p class="perdu-actions"><a href="${lien.accueil()}">${t.retourAccueil}</a> <a href="#lettres">${t.parLettre}</a></p>
  </div>
  <div class="couverture-image" aria-hidden="true">${allee()}</div>
</section>`;
  return page({
    headOpts: { title: t.titre404, description: t.desc404, path: `${t.base}/404.html`, robots: 'noindex', assets, themeColor: palette.figue },
    body,
    bodyClass: 'p-perdu',
    picto,
    letters,
    total,
  });
}

// ---------------------------------------------------------------- Chronologie
// Une seule page, une section par année, une barre des années collante. bySlug : les définitions
// de la langue, pour les liens « Voir aussi » (un mot retiré du dictionnaire n'est simplement pas lié).
export function chronologyPage(annees, { assets, letters, total, bySlug, jsonLd }) {
  const picto = pictoCollector();
  const n = annees.reduce((s, a) => s + a.events.length, 0);
  const a0 = annees[0]?.events[0]?.date.slice(0, 4);
  const a1 = annees.at(-1)?.events.at(-1)?.date.slice(0, 4);
  const nomAnnee = (a) => (a.avant ? t.avant2009 : a.id);
  const enFr = t.code !== 'fr' && annees.some((a) => a.lang !== t.code);
  const max = Math.max(...annees.map((a) => a.events.length));
  const hote = (u) => {
    try {
      return new URL(u).hostname.replace(/^www\./, '');
    } catch {
      return u;
    }
  };
  const evenement = (e, i) => {
    const liens = e.related.map((s) => bySlug.get(s)).filter(Boolean);
    return `<li class="evt" id="${ancreEvenement(e, i)}">
  <time class="evt-date" datetime="${h(e.date)}">${h(dateLisible(e.date))}</time>
  <div class="evt-corps"${e.lang !== t.code ? ` lang="${e.lang}"` : ''}>
    <h3 class="evt-titre">${enLigne(e.title)}</h3>
    <p class="evt-texte">${enLigne(e.text)}</p>
    ${liens.length ? `<p class="evt-liens" lang="${t.code}"><span class="evt-cle">${t.voirAussi}</span> ${liens.map((d) => `<a href="${lien.def(d.slug)}"${apercuAttr(d)}>${breakable(d.title)}</a>`).join(' ')}</p>` : ''}
    ${e.sources.length ? `<p class="evt-sources" lang="${t.code}"><span class="evt-cle">${t.sources[e.sources.length > 1 ? 1 : 0]}</span> ${e.sources.map((u) => `<a href="${h(u)}" rel="noopener nofollow">${h(hote(u))}</a>`).join(' ')}</p>` : ''}
  </div>
</li>`;
  };
  let k = 0;
  const body = `<header class="chrono-tete">
  <h1 class="titre-page">${t.chronoTitre}</h1>
  <p class="enonce">${t.chronoEnonce}</p>
  ${enFr ? `<p class="avis-langue" role="note"><span class="avis-langue-cle">${t.nonTraduitCourt}</span> ${t.chronoFr}</p>` : ''}
  <figure class="chrono-frise" aria-hidden="true"><ol>${annees.map((a) => `<li style="--h:${(a.events.length / max).toFixed(3)}"><a href="#a-${a.id}" tabindex="-1"><span class="frise-barre"></span><span class="frise-an">${a.avant ? '<2009' : `’${a.id.slice(2)}`}</span></a></li>`).join('')}</ol></figure>
</header>
<div class="liste-bloc">
<nav class="index-az index-annees" aria-label="${t.annees}"><ol>${annees.map((a) => `<li><a href="#a-${a.id}">${h(nomAnnee(a))}</a></li>`).join('')}</ol></nav>
<div class="chrono">
${annees.map((a) => `<section class="annee" id="a-${a.id}" aria-labelledby="t-${a.id}">
  <div class="annee-tete"><h2 class="annee-titre" id="t-${a.id}">${h(nomAnnee(a))}</h2><p class="groupe-n">${plural(a.events.length, t.date)}</p></div>
  <ol class="evts">${a.events.map((e) => evenement(e, k++)).join('\n')}</ol>
</section>`).join('\n')}
</div>
</div>`;
  return page({
    headOpts: {
      title: t.titreChrono(n),
      description: t.descChrono(num(n), a0, a1),
      path: lien.chronologie(),
      alt: autres().chronologie(),
      jsonLd,
      assets,
    },
    body,
    bodyClass: 'p-chrono',
    picto,
    letters,
    total,
    current: 'chronologie',
  });
}

// ---------------------------------------------------------------- Spécifications
const statutClasse = (s) => {
  const k = String(s).toLowerCase();
  if (/^(final|active|actif|deployed|complete|mandatory)$/.test(k)) return 'statut--actif';
  if (/^(draft|proposed|optional|relay)$/.test(k)) return 'statut--projet';
  return 'statut--clos';
};
export function specsHubPage(groupes, { assets, letters, total, jsonLd }) {
  const picto = pictoCollector();
  const body = `<header class="specs-tete">
  <h1 class="titre-page">${t.specsTitre}</h1>
  <p class="enonce">${t.specsEnonce}</p>
</header>
<ul class="specs-series">${groupes.map((g) => {
    const s = t.series[g.id] || { titre: g.title, long: '', intro: '' };
    const n = g.series.reduce((x, se) => x + se.entries.length, 0);
    return `<li><a class="serie" href="${lien.specs(g.id)}">${picto.use(g.series[0].id)}<span class="serie-titre">${h(s.titre)}</span><span class="serie-long" lang="en">${h(s.long)}</span><span class="serie-n">${plural(n, t.document)}</span><span class="serie-intro">${h(fr(s.intro))}</span></a></li>`;
  }).join('')}</ul>`;
  return page({
    headOpts: { title: t.titreSpecs(nomsSeries(groupes.flatMap((g) => g.series.map((se) => se.id)))), description: t.specsEnonce, path: lien.specs(), alt: autres().specs(), jsonLd, assets },
    body,
    bodyClass: 'p-specs',
    picto,
    letters,
    total,
    current: 'specs',
  });
}

export function specsPage(groupe, { assets, letters, total, bySlug, jsonLd }) {
  const picto = pictoCollector();
  const s = t.series[groupe.id] || { titre: groupe.title, long: '', intro: '' };
  const entries = groupe.series.flatMap((se) => se.entries);
  const enFr = t.code !== 'fr' && entries.some((e) => !e.summaryEn);
  const maj = groupe.series.map((se) => se.updated).filter(Boolean).sort().at(-1);
  const ancre = (e) => e.id.toLowerCase();
  const fiche = (e) => {
    const def = e.definition ? bySlug.get(e.definition) : null;
    const lies = e.related.map((x) => bySlug.get(x)).filter(Boolean);
    const resumeTxt = t.code === 'en' && e.summaryEn ? e.summaryEn : e.summary;
    const resumeLang = t.code === 'en' && e.summaryEn ? 'en' : 'fr';
    const ref = (n) => {
      const cible = entries.find((x) => x.number === n && x.serie === e.serie);
      return cible ? `<a href="#${ancre(cible)}">${h(cible.id)}</a>` : h(String(n));
    };
    const meta = [
      e.type ? `<div><dt>${t.type}</dt><dd>${h(e.type)}${e.layer ? ` · ${h(e.layer)}` : ''}</dd></div>` : '',
      e.authors.length ? `<div><dt>${t.auteurs[e.authors.length > 1 ? 1 : 0]}</dt><dd>${e.authors.map(h).join(', ')}</dd></div>` : '',
      e.created ? `<div><dt>${t.cree}</dt><dd><time datetime="${h(e.created)}">${h(dateLisible(e.created))}</time></dd></div>` : '',
      e.kinds.length ? `<div><dt>${t.kinds}</dt><dd>${e.kinds.map((k) => `<code>${h(k)}</code>`).join(' ')}</dd></div>` : '',
      e.replaces.length ? `<div><dt>${t.remplace}</dt><dd>${e.replaces.map(ref).join(', ')}</dd></div>` : '',
      e.supersededBy.length ? `<div><dt>${t.remplacePar}</dt><dd>${e.supersededBy.map(ref).join(', ')}</dd></div>` : '',
    ].join('');
    return `<li class="spec" id="${ancre(e)}" data-statut="${h(e.status.map((x) => String(x).toLowerCase()).join(' '))}">
  <div class="spec-tete">
    <p class="spec-id">${h(e.id)}</p>
    <h3 class="spec-titre" lang="en">${h(e.title)}</h3>
    <ul class="spec-statuts">${e.status.map((x) => `<li class="statut ${statutClasse(x)}" lang="en">${h(x)}</li>`).join('')}</ul>
  </div>
  <p class="spec-resume"${resumeLang !== t.code ? ` lang="${resumeLang}"` : ''}>${enLigne(resumeTxt)}</p>
  ${meta ? `<dl class="spec-meta">${meta}</dl>` : ''}
  <p class="spec-liens">${def ? `<a class="spec-def" href="${lien.def(def.slug)}"${apercuAttr(def)}><span class="evt-cle">${t.definitionLiee}</span> ${breakable(def.title)}</a>` : ''}${lies.map((d) => `<a href="${lien.def(d.slug)}"${apercuAttr(d)}>${breakable(d.title)}</a>`).join(' ')}${e.url ? `<a class="spec-source" href="${h(e.url)}" rel="noopener">${t.lireDocument}</a>` : ''}</p>
</li>`;
  };
  const statuts = [...new Set(entries.flatMap((e) => e.status.map((x) => String(x))))];
  const body = `<header class="specs-tete">
  <p class="cat-partie"><a href="${lien.specs()}">${t.specsTitre}</a></p>
  <h1 class="titre-page">${h(s.titre)}</h1>
  <p class="enonce">${h(fr(s.intro))}</p>
  <p class="note">${plural(entries.length, t.document)}.${maj ? ` ${t.majLe(dateLisible(maj))}` : ''}${groupe.series.map((se) => (se.source ? ` <a class="lien" href="${h(se.source)}" rel="noopener">${h(new URL(se.source).pathname.slice(1))}</a>` : '')).join('')}</p>
  ${enFr ? `<p class="avis-langue" role="note"><span class="avis-langue-cle">${t.nonTraduitCourt}</span> ${t.resumesFr}</p>` : ''}
  <fieldset class="filtres filtres--statut" data-filtres-statut hidden>
    <legend class="masque">${t.filtrerStatut}</legend>
    <label class="filtre"><input type="radio" name="statut" value="" checked><span>${t.tous}</span></label>
    ${statuts.map((x) => `<label class="filtre"><input type="radio" name="statut" value="${h(x.toLowerCase())}"><span lang="en">${h(x)}</span></label>`).join('\n    ')}
  </fieldset>
</header>
<div class="liste-bloc">
<nav class="sous-index sous-index--specs" aria-label="${t.sommaireSerie}"><ul>${entries.map((e) => `<li><a href="#${ancre(e)}">${h(e.id.replace(/^(BIP|BOLT|bLIP|BLIP|NIP)-/i, ''))}</a></li>`).join('')}</ul></nav>
<div class="specs">
${groupe.series.map((se) => `<section class="serie-bloc" aria-labelledby="s-${se.id}">
  ${groupe.series.length > 1 ? `<h2 class="annee-titre" id="s-${se.id}">${h(se.id === 'blip' ? 'bLIP' : se.id.toUpperCase())}</h2>` : `<h2 class="masque" id="s-${se.id}">${h(s.titre)}</h2>`}
  <ol class="specs-liste">${se.entries.map(fiche).join('\n')}</ol>
</section>`).join('\n')}
</div>
</div>`;
  return page({
    headOpts: {
      title: t.titreSerie(s.titre, entries.length),
      description: t.descSerie(s.titre, entries.length),
      path: lien.specs(groupe.id),
      alt: autres().specs(groupe.id),
      jsonLd,
      assets,
    },
    body,
    bodyClass: 'p-specs',
    picto,
    letters,
    total,
    current: 'specs',
  });
}
