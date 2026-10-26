// Gabarits HTML du site. Chaque fonction rend une page complète.
// Direction : site/design/direction.md (« Le livre ouvert »).
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { url, site, palette } from '../config.mjs';
import { escapeHtml as h } from './markdown.mjs';
import { compareFr } from './content.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const advances = JSON.parse(fs.readFileSync(path.join(here, 'archivo-advances.json'), 'utf8'));
const JAQ = JSON.parse(fs.readFileSync(path.join(here, 'jaquette.json'), 'utf8'));

const nf = new Intl.NumberFormat('fr-FR');
export const num = (n) => nf.format(n);
const plural = (n, one, many) => `${num(n)} ${n > 1 ? many : one}`;
const ordinal = (n) => (n === 1 ? 'premier' : `${num(n)}<sup>e</sup>`);
const NB = ' ';

// Nom de catégorie lisible : « ÉCONOMIE ET RÉGULATION » -> « Économie et régulation ».
const KEEP_UPPER = new Set(['BIP', 'RGB']);
export function categoryLabel(name) {
  if (KEEP_UPPER.has(name)) return name;
  return name
    .toLocaleLowerCase('fr')
    .replace(/^./, (c) => c.toLocaleUpperCase('fr'))
    .replace(/lightning network/i, 'Lightning Network');
}

// ---------------------------------------------------------------- Pictogrammes
// Les symboles utilisés par une page sont intégrés une seule fois en tête du <body>.
const pictoDir = path.join(here, '..', 'static', 'img', 'pictos');
const PICTOS = new Map(
  fs.readdirSync(pictoDir)
    .filter((f) => f.endsWith('.svg'))
    .map((f) => [f.slice(0, -4), fs.readFileSync(path.join(pictoDir, f), 'utf8').match(/ d="([^"]+)"/)[1]]),
);
export const pictoSprite = () =>
  `<svg xmlns="http://www.w3.org/2000/svg">${[...PICTOS].map(([k, d]) => `<symbol id="p-${k}" viewBox="0 0 100 100"><path d="${d}"/></symbol>`).join('')}</svg>`;

function pictoCollector() {
  const used = new Set();
  const use = (slug, cls = 'picto') => {
    if (!PICTOS.has(slug)) return '';
    used.add(slug);
    return `<svg class="${cls}" aria-hidden="true" focusable="false"><use href="#p-${slug}"/></svg>`;
  };
  const defs = () =>
    used.size
      ? `<svg class="defs" aria-hidden="true" focusable="false">${[...used].map((k) => `<symbol id="p-${k}" viewBox="0 0 100 100"><path d="${PICTOS.get(k)}"/></symbol>`).join('')}</svg>`
      : '';
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
function head({ title, description, path: p, jsonLd = '', math = false, assets, themeColor = palette.blanc, type = 'website', preloadImage = '', extraJs = '' }) {
  const canonical = `${url}${p}`;
  return `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<script>${assets.inlineScript}</script>
<title>${h(title)}</title>
<meta name="description" content="${h(description)}">
<link rel="canonical" href="${canonical}">
<meta name="theme-color" content="${themeColor}">
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="${type}">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="${h(site.title)}">
<meta property="og:title" content="${h(title)}">
<meta property="og:description" content="${h(description)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${url}/img/carte-sociale.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Dictionnaire de Bitcoin : le banian de la couverture 2027, ses racines blanches sur fond figue">
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
let NAV = { letters: new Map(), categories: [] };
export function setNavigation(letters, categories) {
  NAV = { letters, categories };
}

// ---------------------------------------------------------------- Barre
const loupe = `<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="10.5" cy="10.5" r="6.25" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15.2 15.2 5.3 5.3" stroke="currentColor" stroke-width="2" stroke-linecap="square"/></svg>`;
const lune = `<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path class="ico-lune" d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5Z" fill="currentColor"/><g class="ico-soleil" fill="currentColor"><circle cx="12" cy="12" r="4.2"/><path d="M11 1.5h2v3h-2zM11 19.5h2v3h-2zM1.5 11h3v2h-3zM19.5 11h3v2h-3zM4.2 5.6l1.4-1.4 2.1 2.1-1.4 1.4zM16.3 17.7l1.4-1.4 2.1 2.1-1.4 1.4zM4.2 18.4l2.1-2.1 1.4 1.4-2.1 2.1zM16.3 6.3l2.1-2.1 1.4 1.4-2.1 2.1z"/></g></svg>`;

function bar({ home = false, current = '' } = {}) {
  const cur = (k) => (current === k ? ' aria-current="page"' : '');
  return `<a class="evitement" href="#contenu">Aller au contenu</a>
<header class="barre${home ? ' barre--jaquette' : ''}" data-barre>
  <a class="marque" href="/"${home ? ' aria-current="page"' : ''}>Dictionnaire de Bitcoin</a>
  <nav class="nav" aria-label="Navigation principale">
    <a href="#lettres">Lettres</a>
    <a href="/#categories"${cur('categories')}>Catégories</a>
    <a href="/#livre">Le livre</a>
  </nav>
  <div class="barre-actions">
    <button class="bouton-recherche" type="button" data-search-open aria-haspopup="dialog" aria-controls="recherche" aria-label="Rechercher un mot">${loupe}<span class="bouton-recherche-mot">Rechercher</span><kbd data-kbd>Ctrl${NB}K</kbd></button>
    <button class="bouton-theme" type="button" data-theme-toggle aria-label="Changer de thème (clair ou sombre)">${lune}</button>
    <button class="bouton-menu" type="button" data-menu-open aria-haspopup="dialog" aria-controls="menu" aria-label="Menu : lettres, catégories, recherche"><span class="bouton-menu-traits" aria-hidden="true"></span><span class="bouton-menu-mot">Menu</span></button>
  </div>
</header>`;
}

// ---------------------------------------------------------------- Menu (téléphone et tablette)
function menuDialog() {
  const lettres = [...NAV.letters.entries()]
    .map(([l, d]) => (d.length ? `<li><a href="/lettre/${l.toLowerCase()}/" aria-label="Lettre ${l}, ${plural(d.length, 'mot', 'mots')}">${l}</a></li>` : `<li><span aria-hidden="true">${l}</span></li>`))
    .join('');
  const cats = NAV.categories
    .map((c) => `<li><a href="/categorie/${c.slug}/"><svg class="picto" aria-hidden="true" focusable="false"><use href="/img/pictos.svg#p-${c.slug}"/></svg><span>${h(categoryLabel(c.name))}</span><span class="menu-n">${num(c.defs.length)}</span></a></li>`)
    .join('');
  return `<dialog class="menu" id="menu" aria-labelledby="menu-titre">
  <div class="menu-panneau">
    <div class="menu-tete">
      <h2 class="menu-titre" id="menu-titre">Parcourir</h2>
      <button class="recherche-fermer" type="button" data-menu-close>Fermer</button>
    </div>
    <button class="menu-cherche" type="button" data-search-open>${loupe}<span>Rechercher un mot</span></button>
    <h3 class="menu-sous">Les lettres</h3>
    <ol class="abc">${lettres}</ol>
    <h3 class="menu-sous">Les catégories</h3>
    <ul class="menu-cats">${cats}</ul>
    <ul class="menu-liens">
      <li><a href="/">Accueil</a></li>
      <li><a href="/#livre">Le livre imprimé</a></li>
      <li><a href="${site.pdf}" download>PDF gratuit</a></li>
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
    <h2 class="masque" id="recherche-titre">Rechercher dans le dictionnaire</h2>
    <form class="recherche-champ" role="search" action="/recherche/" method="get">
      ${loupe}
      <label class="masque" for="recherche-q">Terme à chercher</label>
      <input id="recherche-q" name="q" type="search" autocomplete="off" autocapitalize="off" spellcheck="false" enterkeyhint="search"
        placeholder="UTXO, Taproot…" role="combobox" aria-expanded="false" aria-autocomplete="list" aria-controls="recherche-resultats">
      <button class="recherche-fermer" type="button" data-search-close>Fermer</button>
    </form>
    <p class="recherche-etat" role="status" aria-live="polite"></p>
    <ul class="resultats" id="recherche-resultats" role="listbox" aria-label="Résultats"></ul>
  </div>
</dialog>`;
}

// ---------------------------------------------------------------- Le dos (pied de page)
function footer(letters, total, { home = false } = {}) {
  const year = new Date().getFullYear();
  const items = [...letters.entries()]
    .map(([l, defs], i) =>
      defs.length
        ? `<li><a href="/lettre/${l.toLowerCase()}/" style="--i:${i}" aria-label="Lettre ${l}, ${plural(defs.length, 'mot', 'mots')}"><span class="dos-l" aria-hidden="true">${l}</span><span class="dos-n" aria-hidden="true">${num(defs.length)}</span></a></li>`
        : `<li><span class="dos-vide" aria-hidden="true"><span class="dos-l">${l}</span></span></li>`,
    )
    .join('');
  // L'accueil garde le grand alphabet animé ; ailleurs, une rangée compacte (la barre A–Z ou le menu font le reste).
  const tete = home
    ? `<div class="dos-tete">
    <h2 class="dos-titre">De A à Z</h2>
    <p class="dos-phrase">${num(total)} mots, classés comme dans le livre.</p>
  </div>`
    : `<h2 class="dos-court">Toutes les lettres</h2>`;
  return `<footer class="dos${home ? '' : ' dos--court'}" id="lettres">
  ${tete}
  <nav class="alphabet${home ? '' : ' alphabet--court'}" aria-label="Toutes les lettres"><ol class="abc">${items}</ol></nav>
  <div class="dos-pied">
    <p class="dos-marque">${h(site.title)}, ${h(site.author)}, édition ${site.edition}</p>
    <ul class="dos-liens">
      <li><a href="${site.pdf}" download>PDF gratuit</a></li>
      <li><a href="${site.bitcoinBazar}" rel="noopener">Bitcoin Bazar</a></li>
      <li><a href="${site.amazon}" rel="noopener">Amazon</a></li>
      <li><a href="${site.github}" rel="noopener">GitHub</a></li>
      <li><a href="${site.authorUrl}" rel="author">pandul.fr</a></li>
      <li><a href="${site.authorX}" rel="noopener">X (Twitter)</a></li>
    </ul>
    <p class="dos-legal">© ${year} ${h(site.author)}. Textes sous licence <a href="${site.licenseUrl}" rel="license noopener">${site.license}</a>. Polices Archivo et Atkinson Hyperlegible Mono sous licence OFL.</p>
  </div>
</footer>`;
}

// Page complète : barre, contenu, dos, recherche.
function page({ headOpts, body, bodyClass, picto, letters, total, home = false, current = '' }) {
  return `${head(headOpts)}
<body class="${bodyClass}">
${picto.defs()}
${bar({ home, current })}
<main id="contenu">
${body}
</main>
${footer(letters, total, { home })}
${searchDialog()}
${menuDialog()}
</body>
</html>
`;
}

// ---------------------------------------------------------------- Morceaux de listes
// Données de la carte d'aperçu au survol (nom, catégorie, définition courte).
const apercuAttr = (d) => (d.description ? ` data-apercu="${hd(d.description)}" data-apercu-cat="${h(categoryLabel(d.category))}" data-apercu-nom="${h(affiche(d.title))}"` : '');
// Une entrée de liste : nom, catégorie, une ligne de description.
function entry(def, picto, { showCategory = true } = {}) {
  const bip = /^BIP-\d/.test(def.title);
  const sujet = bip ? def.related.filter((r) => !/^BIP(-\d|$)/.test(r.title)).slice(0, 2).map((r) => breakable(r.title)).join(', ') : '';
  return `<li><a class="entree" href="/${def.slug}/"${apercuAttr(def)}>
  <span class="entree-nom" data-vt-nom>${showCategory && !bip ? picto.use(def.categorySlug) : ''}${breakable(def.title)}</span>${sujet ? `<span class="entree-sujet">${sujet}</span>` : ''}
  ${def.description ? `<span class="entree-desc">${hd(resume(def.description, 120))}</span>` : ''}
</a></li>`;
}

// Groupes d'une liste : par centaine pour les BIP, sinon par lettre (catégories)
// ou par deux premières lettres (grandes lettres), en fusionnant les petits groupes.
const norm = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toUpperCase();
function bipKey(title) {
  const m = title.match(/^BIP-?(\d{4})/);
  if (!m) return null;
  const c = Math.floor(Number(m[1]) / 100) * 100;
  return { key: `BIP-${String(c).padStart(4, '0')}`, label: `BIP-${String(c).padStart(4, '0')} à ${String(c + 99).padStart(4, '0')}` };
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
      // est trié en tête par le classement français : il rejoint le premier groupe de sa lettre.
      const t = norm(d.title);
      key = /[A-Z0-9]/.test(t[1] || '') ? t.slice(0, 2) : `${t[0]}A`;
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
  <div class="groupe-tete"><h2 class="groupe-titre" id="${id}"><span class="masque">${labelPrefix}</span>${h(g.label)}</h2><p class="groupe-n">${plural(g.defs.length, 'mot', 'mots')}</p></div>
  <ul class="entrees">${g.defs.map((d) => entry(d, picto, { showCategory })).join('\n')}</ul>
</section>`;
    })
    .join('\n');
}

// ---------------------------------------------------------------- Définition
export function definitionPage(def, { html, math, assets, jsonLd, total, letters }) {
  const picto = pictoCollector();
  const cat = categoryLabel(def.category);
  const letter = def.letter;
  const letterCount = letters.get(letter)?.length || 0;
  const tags = [
    `<li><a class="etiquette" href="/categorie/${def.categorySlug}/">${picto.use(def.categorySlug)}${h(cat)}</a></li>`,
    def.englishTerm ? `<li class="etiquette etiquette--langue"><span class="etiquette-cle">En anglais</span> <span lang="en">${h(def.englishTerm)}</span></li>` : '',
    def.frenchTerm ? `<li class="etiquette etiquette--langue"><span class="etiquette-cle">En français</span> ${h(def.frenchTerm)}</li>` : '',
  ].join('');

  const renvoi = (r) => `<li><a class="renvoi" href="/${r.slug}/">
  <span class="renvoi-nom" data-vt-nom>${breakable(r.title)}</span>
  <span class="renvoi-cat">${picto.use(r.categorySlug)}${h(categoryLabel(r.category))}</span>
  ${r.description ? `<span class="renvoi-desc">${hd(resume(r.description, 120))}</span>` : ''}
</a></li>`;
  const related = def.related.length
    ? `<aside class="renvois" aria-labelledby="renvois-titre">
  <h2 class="renvois-titre" id="renvois-titre">${def.related.length > 1 ? 'Termes associés' : 'Terme associé'}</h2>
  <ul>${def.related.map(renvoi).join('\n')}</ul>
</aside>`
    : '';
  const cited = def.citedBy.filter((d) => !def.related.includes(d)).sort((a, b) => compareFr(a.title, b.title));
  const citedHtml = cited.length
    ? `<section class="cites" aria-labelledby="cites-titre">
  <h2 class="cites-titre" id="cites-titre">${cited.length > 1 ? `${num(cited.length)} définitions renvoient ici` : 'Une définition renvoie ici'}</h2>
  <ul class="cites-liste"${cited.length > 12 ? ' data-repliable' : ''}>${cited.map((d) => `<li><a href="/${d.slug}/"${apercuAttr(d)}>${breakable(d.title)}</a></li>`).join('')}</ul>
</section>`
    : '';

  const turn = (d, dir) => {
    if (!d) return `<span class="tourner-vide"></span>`;
    const label = dir === 'prev' ? 'Mot précédent' : 'Mot suivant';
    return `<a class="tourner-lien tourner-lien--${dir}" href="/${d.slug}/" rel="${dir}" data-turn="${dir}">
  <span class="tourner-sens">${label}</span>
  <span class="tourner-nom">${breakable(d.title)}</span>
  ${d.description ? `<span class="tourner-desc">${hd(resume(d.description, 120))}</span>` : ''}
</a>`;
  };
  const editUrl = `${site.github}/blob/main/${def.sourcePath}`;
  const body = `<nav class="reperes" aria-label="Mots voisins dans le dictionnaire">
  ${def.alphaPrev ? `<a class="reperes-prec" href="/${def.alphaPrev.slug}/" data-turn="prev"${apercuAttr(def.alphaPrev)}><span class="masque">Mot précédent : </span><span class="reperes-nom">${breakable(def.alphaPrev.title)}</span><span class="reperes-court" aria-hidden="true">Précédent</span></a>` : '<span></span>'}
  <a class="reperes-lettre" href="/lettre/${letter.toLowerCase()}/" aria-label="Lettre ${letter}, ${plural(letterCount, 'mot', 'mots')}">${letter}</a>
  ${def.alphaNext ? `<a class="reperes-suiv" href="/${def.alphaNext.slug}/" data-turn="next"${apercuAttr(def.alphaNext)}><span class="masque">Mot suivant : </span><span class="reperes-nom">${breakable(def.alphaNext.title)}</span><span class="reperes-court" aria-hidden="true">Suivant</span></a>` : '<span></span>'}
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
      <div class="signet-tranche" role="img" aria-label="Place de ce mot dans le livre : entrée ${num(def.n)} sur ${num(total)}"><span class="signet-ruban"></span></div>
      <figcaption class="signet-legende">Entrée ${num(def.n)} sur ${num(total)} du dictionnaire, ${ordinal(def.n - (letters.get(letter)?.[0]?.n || 1) + 1)} mot de la lettre\u00a0${letter}</figcaption>
    </figure>
    ${related}
  </div>
  <div class="mot-corps">
    <div class="prose">${html}</div>
  </div>
  ${citedHtml}
</article>
<nav class="tourner" aria-label="Tourner la page">
  ${turn(def.alphaPrev, 'prev')}
  ${turn(def.alphaNext, 'next')}
</nav>
<p class="colophon"><cite>${h(site.title)}</cite>, édition ${site.edition}. <a href="${editUrl}" rel="noopener">Proposer une correction sur GitHub</a> <button class="citer" type="button" data-citer="${h(`${site.author}, « ${def.title} », ${site.title}, édition ${site.edition}, ${url}/${def.slug}/`)}" hidden>Citer cette définition</button></p>`;

  return page({
    headOpts: {
      title: `${def.title} : définition | Dictionnaire de Bitcoin`,
      description: def.description || `${def.title} : définition du Dictionnaire de Bitcoin, catégorie ${cat}.`,
      path: `/${def.slug}/`,
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
  const max = Math.sqrt(Math.max(...defs.map((d) => d.body.length)));
  const pas = 6;
  const trancheLettre = defs
    .map((d, k) => `<a href="/${d.slug}/" tabindex="-1"><title>${h(affiche(d.title))}</title><rect x="${k * pas}" y="${(100 - Math.max(8, (Math.sqrt(d.body.length) / max) * 100)).toFixed(1)}" width="${pas - 2}" height="${Math.max(8, (Math.sqrt(d.body.length) / max) * 100).toFixed(1)}"/></a>`)
    .join('');
  const groups = defs.length > 40 ? groupEntries(defs, 'deux') : [];
  const vedetteLettre = [...defs].sort((a, b) => b.citedBy.length - a.citedBy.length)[0];
  const sousIndex = groups.length > 1
    ? `<nav class="sous-index" aria-label="Groupes de la lettre ${letter}">
  <ul>${groups.map((g, k) => `<li><a href="#groupe-${k + 1}">${h(g.label)}</a></li>`).join('')}</ul>
</nav>`
    : '';
  const body = `${azIndex({ current: letter, hrefFor: (l) => (letters.get(l)?.length ? `/lettre/${l.toLowerCase()}/` : null), label: 'Toutes les lettres' })}
<header class="lettre-tete">
  <p class="grande-lettre" aria-hidden="true"><span class="gl"><span class="gl-in">${letter}</span></span></p>
  <div class="lettre-info">
    <h1 class="titre lettre-titre">Les mots en ${letter}</h1>
    <p class="enonce">${plural(defs.length, 'mot', 'mots')} du dictionnaire, de ${insecable(defs[0].title)} à ${insecable(defs.at(-1).title)}.</p>
    <nav class="lettres-voisines" aria-label="Lettres voisines">
      ${prev ? `<a href="/lettre/${prev.toLowerCase()}/" rel="prev"><span class="masque">Lettre précédente : </span>${prev}</a>` : ''}
      ${next ? `<a href="/lettre/${next.toLowerCase()}/" rel="next"><span class="masque">Lettre suivante : </span>${next}</a>` : ''}
    </nav>
  </div>
  <div class="lettre-tranche">
    <div class="apercu-lettre" aria-live="polite" data-apercu-lettre>
      <p class="apercu-lettre-nom"><a href="/${vedetteLettre.slug}/">${breakable(vedetteLettre.title)}</a></p>
      <p class="apercu-lettre-cat">${h(categoryLabel(vedetteLettre.category))}</p>
      <p class="apercu-lettre-desc">${hd(resume(vedetteLettre.description))}</p>
    </div>
    <figure class="tranche-lettre">
      <svg viewBox="0 0 ${defs.length * pas} 100" preserveAspectRatio="none" aria-hidden="true" data-tranche-lettre>${trancheLettre}</svg>
      <figcaption class="note" data-tranche-legende>Un trait par mot, dans l’ordre du livre&#8239;; sa hauteur suit la longueur de la définition. <span data-geste>Survolez les traits.</span></figcaption>
    </figure>
  </div>
</header>
<div class="liste-bloc">
${sousIndex}
<div class="liste">
${groupedList(defs, picto, { mode: defs.length > 40 ? 'deux' : 'une', labelPrefix: 'Groupe ' })}
</div>
</div>
${next ? `<p class="lettre-suite"><a class="bouton" href="/lettre/${next.toLowerCase()}/">Lettre suivante : ${next}</a></p>` : ''}`;
  return page({
    headOpts: {
      title: `Lettre ${letter} : ${defs.length} définitions | Dictionnaire de Bitcoin`,
      description: `Les ${defs.length} termes du Dictionnaire de Bitcoin qui commencent par la lettre ${letter}, de ${defs[0]?.title} à ${defs.at(-1)?.title}.`,
      path: `/lettre/${letter.toLowerCase()}/`,
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
export function categoryPage(cat, note, { assets, jsonLd, letters, total, categories }) {
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
  const indexGroupes = `<nav class="index-az" aria-label="Lettres de la catégorie ${h(label)}"><ol>${cases.join('')}</ol></nav>`;
  const rayon = `<nav class="rayon" aria-labelledby="rayon-titre"><h2 class="rayon-titre" id="rayon-titre">Les ${categories.length} catégories</h2><ul>${categories
    .map((c) => `<li><a href="/categorie/${c.slug}/"${c.slug === cat.slug ? ' aria-current="page"' : ''}>${picto.use(c.slug)}<span>${h(categoryLabel(c.name))}</span></a></li>`)
    .join('')}</ul></nav>`;
  // Présentation : la première phrase entière, la suite repliée derrière « Lire la suite ».
  const texte = note ? fr(note.replace(/\.$/, '')) + '.' : '';
  const coupe = texte.search(/[.!?] (?=[A-ZÀ-Ý«])/);
  const [premiere, suite] = coupe > 0 ? [texte.slice(0, coupe + 1), texte.slice(coupe + 2)] : [texte, ''];
  const body = `<header class="cat-tete">
  <p class="cat-picto">${picto.use(cat.slug, 'picto picto--grand')}</p>
  <h1 class="cat-nom">${h(label)}</h1>
  <p class="enonce cat-note">${plural(cat.defs.length, 'définition', 'définitions')} du dictionnaire.${premiere ? `<span class="cat-note-premiere"> ${h(premiere)}</span>` : ''}${suite ? `<span class="cat-note-suite" data-repliable-suite> ${h(suite)}</span>` : ''}</p>
  <section class="cat-debut" aria-labelledby="debut-titre">
    <h2 class="cat-debut-titre" id="debut-titre">Pour commencer</h2>
    <ul>${[...cat.defs].sort((a, b) => b.citedBy.length - a.citedBy.length || compareFr(a.title, b.title)).slice(0, 4).map((d) => `<li><a class="renvoi" href="/${d.slug}/"><span class="renvoi-nom" data-vt-nom>${breakable(d.title)}</span>${d.description ? `<span class="renvoi-desc">${hd(resume(d.description))}</span>` : ''}</a></li>`).join('')}</ul>
  </section>
</header>
<div class="liste-bloc">
${indexGroupes}
<div class="liste">
${groupedList(cat.defs, picto, { mode: 'une', showCategory: false, labelPrefix: cat.slug === 'bip' ? '' : 'Lettre ' })}
</div>
</div>
${rayon}`;
  return page({
    headOpts: {
      title: `${label} : ${cat.defs.length} définitions | Dictionnaire de Bitcoin`,
      description: note
        ? `${cat.defs.length} définitions. ${note}`.slice(0, 155).replace(/\s+\S*$/, '…')
        : `Les ${cat.defs.length} définitions de la catégorie ${label} du Dictionnaire de Bitcoin.`,
      path: `/categorie/${cat.slug}/`,
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

// ---------------------------------------------------------------- Accueil
const CONTRIBUTORS = [
  ['Psyduck07', 'https://github.com/Psyduck07'],
  ['Adrien Lacombe', 'https://github.com/adrienlacombe'],
  ['Ludovic Lars', 'https://github.com/lugaxker'],
  ['Beemo', 'https://github.com/nflatrea'],
  ['quinoah', 'https://github.com/quinoah'],
];

export function homePage(data, { assets, jsonLd }) {
  const { definitions, categories, letters, featured, notes } = data;
  const total = definitions.length;
  const picto = pictoCollector();
  for (const c of categories) picto.use(c.slug);

  // Les trois mots les plus cités de chaque catégorie.
  const topWords = (c) => [...c.defs].sort((a, b) => b.citedBy.length - a.citedBy.length || compareFr(a.title, b.title)).slice(0, 3);
  const catRows = categories
    .map(
      (c) => `<li class="index-ligne">
  <a class="index-nom" href="/categorie/${c.slug}/">${picto.use(c.slug)}<span>${h(categoryLabel(c.name))}</span><span class="index-n">${num(c.defs.length)}</span></a>
  <p class="index-mots">${topWords(c).map((d) => `<a href="/${d.slug}/">${breakable(d.title)}</a>`).join(', ')}</p>
</li>`,
    )
    .join('\n');

  const letterBlocks = [...letters.entries()]
    .filter(([, d]) => d.length)
    .map(([l, d]) => `<li style="--n:${d.length}"><a href="/lettre/${l.toLowerCase()}/" data-lettre="${l}" aria-label="Lettre ${l}, ${plural(d.length, 'mot', 'mots')}"><span class="bloc-l" aria-hidden="true">${l}</span></a></li>`)
    .join('');

  const f = featured;
  // Le vrai dossier d'une définition, tel qu'il est sur GitHub.
  const exemple = definitions.find((d) => d.slug === 'utxo') || definitions[0];
  const source = {
    slug: exemple.slug,
    dir: `definitions/fr/${exemple.slug[0]}/${exemple.slug}/`,
    // Les deux premières phrases du fichier : un extrait, pas tout le texte.
    body: `${exemple.body.trim().split(/(?<=\.)\s+/).slice(0, 3).join(' ')} […]`,
  };
  // Positions du titre sur l'avant : celles de la couverture imprimée (lib/jaquette.json),
  // pour que les racines du banian se posent sur les lettres.
  const t = JAQ.titre;
  const asc = 0.834; // ligne de base sous le haut de ligne, en em (Archivo, interligne 1)
  const vars = [
    `--t-corps:${(t.corps * 100).toFixed(3)}cqw`, `--t-x:${(t.x * 100).toFixed(3)}cqw`,
    `--t-l1:calc(${(t.ligne1 * 100).toFixed(3)}cqh - ${asc} * var(--t-corps))`,
    `--t-l2:calc(${(t.ligne2 * 100).toFixed(3)}cqh - ${asc} * var(--t-corps))`,
    `--s-corps:max(14px, ${(JAQ.sous_titre.corps * 100).toFixed(3)}cqw)`,
    `--s-l:calc(${(JAQ.sous_titre.ligne * 100).toFixed(3)}cqh - ${asc} * var(--s-corps))`,
    `--a-corps:max(13px, ${(JAQ.auteur.corps * 100).toFixed(3)}cqw)`,
    `--a-l:calc(${(JAQ.auteur.ligne * 100).toFixed(3)}cqh - ${asc} * var(--a-corps))`,
    `--a-d:${(JAQ.auteur.droite * 100).toFixed(3)}cqw`,
    `--dos:${JAQ.jaquette.dos}`, `--tranche:${JAQ.jaquette.tranche}`, `--ratio:${(JAQ.jaquette.largeur_pt / JAQ.jaquette.hauteur_pt).toFixed(5)}`,
  ].join(';');
  const plein = '(min-width: 1024px) and (min-aspect-ratio: 4/3)';
  const calque = (nom, alt = '') => `<picture class="jaquette-${nom}">
      <source media="${plein}" type="image/avif" srcset="/img/jaquette-${nom}-1100.avif 1622w, /img/jaquette-${nom}-1600.avif 2359w" sizes="96vw">
      <source media="${plein}" type="image/webp" srcset="/img/jaquette-${nom}-1100.webp 1622w, /img/jaquette-${nom}-1600.webp 2359w" sizes="96vw">
      <source type="image/avif" srcset="/img/avant-${nom}-1100.avif 712w, /img/avant-${nom}-1600.avif 1035w" sizes="100vw">
      <img src="/img/avant-${nom}-1100.webp" srcset="/img/avant-${nom}-1100.webp 712w, /img/avant-${nom}-1600.webp 1035w" sizes="100vw" width="712" height="1100" alt="${alt}"${nom === 'couronne' ? ' fetchpriority="high"' : ''} decoding="async">
    </picture>`;
  const body = `<section class="jaquette" aria-labelledby="titre">
  <div class="jaquette-objet" style="${vars}">
    ${calque('couronne', 'La couverture de l’édition 2027 : la couronne d’un banian, aux feuilles figue sombre, sur fond figue')}
    ${calque('racines')}
    <div class="jaquette-couv">
      <h1 class="couv-titre" id="titre"><span class="ligne ligne-1"><span>Dictionnaire</span></span> <span class="ligne ligne-2"><span>de Bitcoin</span></span></h1>
      <p class="couv-sous">Tout le vocabulaire technique de Bitcoin</p>
      <p class="couv-auteur"><span>${h(site.author)}</span> <span>Édition ${site.edition}</span></p>
      <form class="couv-recherche" role="search" action="/recherche/" method="get" data-hero-search>
        <label class="masque" for="couv-q">Chercher un terme parmi les ${num(total)} définitions</label>
        <input id="couv-q" name="q" type="search" autocomplete="off" spellcheck="false" enterkeyhint="search" placeholder="UTXO, Taproot…">
        <button type="submit">Chercher</button>
      </form>
    </div>
    <div class="jaquette-tranche" aria-hidden="true"><span class="tranche-titre">Dictionnaire de Bitcoin</span><span class="tranche-an">${site.edition}</span></div>
    <section class="jaquette-dos jour" aria-labelledby="jour-titre" data-jour>
      <h2 class="jour-titre" id="jour-titre">Le mot du jour</h2>
      <p class="jour-mot"><a href="/${f.slug}/" data-jour-lien><span data-jour-nom>${breakable(f.title)}</span></a></p>
      <p class="jour-cat"><a href="/categorie/${f.categorySlug}/" data-jour-cat>${picto.use(f.categorySlug)}<span>${h(categoryLabel(f.category))}</span></a></p>
      <p class="jour-desc" data-jour-desc>${hd(f.description || '')}</p>
      <p class="jour-actions"><a class="bouton bouton--clair" href="/${f.slug}/" data-jour-lire>Lire la définition</a> <button class="bouton bouton--trait" type="button" data-jour-autre>Un autre mot</button></p>
      <p class="jour-pied">${num(total)} définitions libres et gratuites, 19 catégories.</p>
    </section>
  </div>
</section>

<section class="feuilleter" aria-labelledby="feuilleter-titre" data-tranche>
  <div class="feuilleter-tete">
    <h2 class="titre" id="feuilleter-titre">Feuilleter les ${num(total)} mots</h2>
    <p class="enonce">Chaque trait est une définition, dans l’ordre du livre&#8239;; sa hauteur suit la longueur du texte. Choisissez une lettre, puis glissez sur les traits.</p>
  </div>
  <nav class="blocs" aria-label="Lettres de la tranche"><ol>${letterBlocks}</ol></nav>
  <div class="bande" data-bande><p class="bande-sans-script">Les traits apparaissent avec JavaScript. En attendant, chaque lettre ci-dessus mène à sa liste.</p></div>
  <div class="apercu" aria-live="polite" data-apercu>
    <p class="apercu-nom"><a href="/${f.slug}/" data-apercu-lien>${breakable(f.title)}</a></p>
    <p class="apercu-cat" data-apercu-cat>${h(categoryLabel(f.category))}</p>
    <p class="apercu-desc" data-apercu-desc>${hd(f.description || '')}</p>
  </div>

</section>

<section class="categories" id="categories" aria-labelledby="categories-titre">
  <div class="categories-tete">
    <h2 class="titre" id="categories-titre">Dix-neuf catégories</h2>
    <p class="enonce">Chaque définition appartient à un domaine, signalé dans le livre par son pictogramme.<span class="sans-mobile"> Les trois mots cités sont les plus renvoyés de leur catégorie.</span></p>
  </div>
  <ul class="index">${catRows}</ul>
</section>

<section class="livre" id="livre" aria-labelledby="livre-titre">
  <div class="livre-haut">
    <figure class="livre-volume"><video muted loop playsinline preload="none" poster="/video/feuilletage.webp" width="640" height="990" aria-label="Les pages du livre imprimé qui défilent, de la lettre A à la lettre Z" data-boucle><source src="/video/feuilletage.mp4" type="video/mp4"></video></figure>
    <div class="livre-texte">
      <h2 class="titre" id="livre-titre">Le livre</h2>
      <p class="enonce">Les définitions existent aussi sur papier&#8239;: l’édition 2026 compte 594 pages, en broché ou en relié. L’édition 2027 est en préparation.</p>
      <p class="livre-actions"><a class="bouton" href="${site.bitcoinBazar}" rel="noopener">Commander chez Bitcoin Bazar</a> <a class="lien" href="${site.amazon}" rel="noopener">ou sur Amazon</a></p>
      <p>Le PDF complet reste gratuit&#8239;: <a class="lien" href="${site.pdf}" download>télécharger le PDF</a> (2,7${NB}Mo).</p>
      <p class="note">ISBN de l’édition 2026&#8239;: ${site.isbnPaperback} (broché), ${site.isbnHardcover} (relié). Je gagne une petite marge sur chaque exemplaire vendu&#8239;: c’est la meilleure façon de soutenir le projet.</p>
    </div>
  </div>
  <div class="pages" aria-label="Six pages intérieures de l’édition 2026">
    ${[[3, 'La page de titre du livre : Dictionnaire de Bitcoin, Tout le vocabulaire technique de Bitcoin, Loïc Morel'], [31, 'Page 5 du livre : les entrées ADDRMAN, ADDRV2 et ADRESSE DE RÉCEPTION'], [36, 'Page 10 du livre : les entrées ALERT SYSTEM, ALGORITHME, ALTCOIN et ALUVM'], [212, 'Page 186 du livre : les entrées CONSIGNMENT et CONSOLIDATION'], [467, 'Page 441 du livre : les entrées RÉCURSIF - COVENANT et REDEEM'], [516, 'Page 490 du livre : les entrées SIMPLIFIED PAYMENT VERIFICATION, SINGLE-SIG et SINGLE-USE SEAL']]
      .map(([n, alt], i) => `<figure class="page-livre" style="--i:${i}"><img src="/img/page-${n}.webp" width="600" height="927" alt="${h(alt)}" loading="lazy" decoding="async"></figure>`)
      .join('\n    ')}
  </div>
</section>

<section class="ouvert" aria-labelledby="ouvert-titre">
  <div class="ouvert-texte">
    <h2 class="titre" id="ouvert-titre">Un projet ouvert</h2>
    <p class="enonce">Chaque définition est un dossier sur GitHub. Une coquille, une imprécision, un terme manquant&#8239;: tout le monde peut proposer une correction, et chaque page du site mène au fichier à modifier.</p>
    <p><a class="bouton" href="${site.github}" rel="noopener">Contribuer sur GitHub</a></p>
    <div class="ouvert-auteur">
      <img src="/img/loic-morel.webp" width="560" height="560" alt="Portrait de Loïc Morel" loading="lazy" decoding="async">
      <p>Écrit par <a class="lien" href="${site.authorUrl}" rel="author">Loïc Morel</a>, relu et complété par les contributeurs du dépôt&#8239;: ${CONTRIBUTORS.map(([n, u]) => `<a class="lien" href="${u}" rel="noopener">${h(n)}</a>`).join(', ')}.</p>
    </div>
    <p class="note">Textes sous licence ${site.license}. Pour soutenir l’auteur en Lightning&#8239;: <span class="lightning">${site.lightning}</span>.</p>
  </div>
  <figure class="fichier" data-ui>
    <figcaption class="fichier-chemin"><code>${h(source.dir)}</code></figcaption>
    <p class="fichier-nom">definition.md, le texte source en Markdown</p>
    <pre class="fichier-texte"><code>${h(source.body).replace(/\*([^*]+)\*/g, '<span class="md">*</span><em>$1</em><span class="md">*</span>').replace(/`([^`]+)`/g, '<span class="md">`</span>$1<span class="md">`</span>')}</code></pre>
    <ul class="fichier-liens"><li><a class="lien" href="${site.github}/blob/main/${source.dir}definition.md" rel="noopener">Ouvrir ce fichier sur GitHub</a></li><li><a class="lien" href="/${source.slug}/">Lire la définition rendue</a></li></ul>
  </figure>
</section>`;

  return page({
    headOpts: {
      title: 'Dictionnaire de Bitcoin : tout le vocabulaire technique de Bitcoin',
      description: `Le Dictionnaire de Bitcoin de Loïc Morel : ${num(total)} définitions libres et gratuites du vocabulaire technique de Bitcoin, aussi disponible en livre imprimé et en PDF.`,
      path: '/',
      jsonLd,
      assets,
      themeColor: palette.figue,
      extraJs: assets.home,
      preloadImage: '',
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
  <h1 class="titre-page">Rechercher</h1>
  <p class="enonce">Dans les ${num(total)} définitions, leur terme anglais et leur description. Les fautes de frappe sont tolérées.</p>
  <form class="cherche-form" role="search" action="/recherche/" method="get" data-search-page>
    <label class="masque" for="cherche-q">Terme à chercher</label>
    ${loupe}
    <input id="cherche-q" name="q" type="search" autocomplete="off" spellcheck="false" enterkeyhint="search" placeholder="UTXO, Taproot…" aria-controls="cherche-resultats">
  </form>
  <fieldset class="filtres" data-filtres>
    <legend class="masque">Filtrer par catégorie</legend>
    <label class="filtre"><input type="radio" name="cat" value="" checked><span>Toutes</span></label>
    ${categories.map((c) => `<label class="filtre"><input type="radio" name="cat" value="${c.slug}"><span>${picto.use(c.slug)}${h(categoryLabel(c.name))}</span></label>`).join('\n    ')}
  </fieldset>
</header>
<p class="cherche-etat" role="status" aria-live="polite" data-search-status>La recherche a besoin de JavaScript. Vous pouvez aussi parcourir les mots <a href="#lettres">par lettre</a>.</p>
<ul class="resultats resultats--page" id="cherche-resultats" data-search-results></ul>`;
  return page({
    headOpts: {
      title: 'Rechercher | Dictionnaire de Bitcoin',
      description: `Recherche instantanée dans les ${total} définitions du Dictionnaire de Bitcoin.`,
      path: '/recherche/',
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
  const body = `<section class="perdu" aria-labelledby="perdu-titre">
  <div class="perdu-arbre" aria-hidden="true">
    <picture><source type="image/avif" srcset="/img/jaquette-couronne-1100.avif"><img src="/img/jaquette-couronne-1100.webp" width="1622" height="1100" alt="" decoding="async"></picture>
    <picture><source type="image/avif" srcset="/img/jaquette-racines-1100.avif"><img src="/img/jaquette-racines-1100.webp" width="1622" height="1100" alt="" decoding="async"></picture>
  </div>
  <div class="perdu-texte">
    <h1 class="perdu-titre" id="perdu-titre">Mot introuvable</h1>
    <p class="enonce">Ce mot n’est pas, ou pas encore, dans le dictionnaire&#8239;: l’adresse demandée ne correspond à aucune page.</p>
    <form class="couv-recherche perdu-recherche" role="search" action="/recherche/" method="get" data-perdu-champ>
      <label class="masque" for="perdu-q">Chercher un terme</label>
      <input id="perdu-q" name="q" type="search" autocomplete="off" spellcheck="false" enterkeyhint="search" placeholder="UTXO, Taproot…" aria-controls="perdu-resultats">
      <button type="submit">Chercher</button>
    </form>
    <div class="perdu-suggestions" data-suggestions hidden>
      <h2 class="perdu-sous" data-suggestions-titre>Vouliez-vous dire</h2>
      <ul class="perdu-liste" id="perdu-resultats" data-suggestions-liste></ul>
    </div>
    <p class="perdu-actions"><a class="lien lien--os" href="/">Retour à l’accueil</a> <a class="lien lien--os" href="#lettres">Parcourir par lettre</a></p>
  </div>
</section>`;
  return page({
    headOpts: { title: 'Page introuvable | Dictionnaire de Bitcoin', description: 'Cette page n’existe pas dans le Dictionnaire de Bitcoin.', path: '/404.html', assets, themeColor: palette.figue },
    body,
    bodyClass: 'p-perdu',
    picto,
    letters,
    total,
  });
}
