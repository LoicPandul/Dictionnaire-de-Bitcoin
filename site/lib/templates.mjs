// Gabarits HTML du site. Chaque fonction rend une page complète.
import { url, site } from '../config.mjs';
import { escapeHtml as h } from './markdown.mjs';

const nf = new Intl.NumberFormat('fr-FR');
export const num = (n) => nf.format(n).replace(/ /g, ' ');
const plural = (n, one, many) => `${num(n)} ${n > 1 ? many : one}`;

// Les titres du dépôt sont en capitales, comme dans le livre. Pour les phrases courantes
// (titres de page, attributs), on garde la casse d'origine.
const pictoNames = new Set([
  'attaque', 'bip', 'communaute', 'confidentialite', 'couche-superieure', 'cryptographie',
  'economie-et-regulation', 'histoire', 'informatique', 'lightning-network', 'minage',
  'organisation', 'outil', 'portefeuille', 'protocole', 'reseau', 'rgb', 'script', 'sidechain',
]);
export const picto = (slug, cls = '') =>
  pictoNames.has(slug)
    ? `<span class="picto ${cls}" style="--picto:url(/img/pictos/${slug}.webp)" aria-hidden="true"></span>`
    : '';

// Nom de catégorie lisible : « ÉCONOMIE ET RÉGULATION » -> « Économie et régulation ».
const KEEP_UPPER = new Set(['BIP', 'RGB']);
export function categoryLabel(name) {
  if (KEEP_UPPER.has(name)) return name;
  const lower = name.toLocaleLowerCase('fr');
  return lower
    .replace(/^./, (c) => c.toLocaleUpperCase('fr'))
    .replace(/lightning network/i, 'Lightning Network');
}

// Taille du mot-vedette selon sa longueur, pour qu'il tienne en deux lignes.
export function headwordSize(title) {
  const n = title.length;
  if (n <= 10) return 'hw-xl';
  if (n <= 18) return 'hw-l';
  if (n <= 26) return 'hw-m';
  return 'hw-s';
}

function head({ title, description, path, jsonLd = '', math = false, image = '/img/social-card.jpg', type = 'website', assetVersion }) {
  const canonical = `${url}${path}`;
  const v = assetVersion ? `?v=${assetVersion}` : '';
  return `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<script>document.documentElement.classList.add('js')</script>
<title>${h(title)}</title>
<meta name="description" content="${h(description)}">
<link rel="canonical" href="${canonical}">
<meta name="theme-color" content="#193042">
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="${type}">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="${h(site.title)}">
<meta property="og:title" content="${h(title)}">
<meta property="og:description" content="${h(description)}">
<meta property="og:url" content="${canonical}">
<meta property="og:image" content="${url}${image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Couverture du Dictionnaire de Bitcoin : un arbre gravé sur fond bleu nuit">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@Loic_Pandul">
<meta name="author" content="${h(site.author)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.png" type="image/png" sizes="64x64">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preload" href="/fonts/cmu-serif-500-roman.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/css/site.css${v}">
${math ? `<link rel="stylesheet" href="/katex/katex.min.css">\n` : ''}<script src="/js/site.js${v}" defer></script>
${jsonLd}
</head>`;
}

function bar({ home = false } = {}) {
  return `<a class="skip" href="#contenu">Aller au contenu</a>
<header class="bar${home ? ' bar--home' : ''}">
  <a class="wordmark" href="/"${home ? ' aria-current="page"' : ''}>Dictionnaire de Bitcoin</a>
  <nav class="bar-nav" aria-label="Navigation principale">
    <a href="/#lettres">Lettres</a>
    <a href="/#categories">Catégories</a>
    <a href="/#livre">Le livre</a>
    <a href="${site.pdf}" download>PDF</a>
  </nav>
  <button class="search-open" type="button" data-search-open aria-haspopup="dialog" aria-controls="recherche">
    <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15.5 15.5 5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
    <span>Rechercher</span><kbd class="kbd" data-kbd>Ctrl K</kbd>
  </button>
</header>`;
}

// Fenêtre de recherche, partagée par toutes les pages.
function searchDialog() {
  return `<div class="search" id="recherche" role="dialog" aria-modal="true" aria-label="Rechercher une définition" hidden>
  <div class="search-scrim" data-search-close></div>
  <div class="search-panel">
    <div class="search-field">
      <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="m15.5 15.5 5 5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>
      <input type="search" class="search-input" placeholder="Un terme, un sigle, un mot anglais…" autocomplete="off" spellcheck="false"
        role="combobox" aria-expanded="false" aria-autocomplete="list" aria-controls="recherche-resultats" aria-label="Rechercher une définition">
      <button type="button" class="search-close" data-search-close>Fermer</button>
    </div>
    <ul class="search-results" id="recherche-resultats" role="listbox" aria-label="Résultats"></ul>
    <p class="search-status" role="status" aria-live="polite"></p>
  </div>
</div>`;
}

function footer({ full = false, credits = '' } = {}) {
  const year = new Date().getFullYear();
  return `<footer class="foot${full ? ' foot--full' : ''}">
  <div class="foot-cols">
    <div>
      <p class="foot-head">Parcourir</p>
      <ul>
        <li><a href="/#lettres">Les lettres de A à Z</a></li>
        <li><a href="/#categories">Les 19 catégories</a></li>
        <li><a href="/lettre/a/" data-random>Un terme au hasard</a></li>
      </ul>
    </div>
    <div>
      <p class="foot-head">Le livre</p>
      <ul>
        <li><a href="${site.bitcoinBazar}" rel="noopener">Bitcoin Bazar</a></li>
        <li><a href="${site.amazon}" rel="noopener">Amazon</a></li>
        <li><a href="${site.pdf}" download>PDF gratuit</a></li>
      </ul>
    </div>
    <div>
      <p class="foot-head">Contribuer</p>
      <ul>
        <li><a href="${site.github}" rel="noopener">Le dépôt GitHub</a></li>
        <li><a href="${site.licenseUrl}" rel="noopener license">Licence ${site.license}</a></li>
        <li>Lightning : ${site.lightning}</li>
      </ul>
    </div>
    <div>
      <p class="foot-head">L’auteur</p>
      <ul>
        <li>${site.author}</li>
        <li><a href="${site.authorUrl}" rel="author">pandul.fr</a></li>
        <li><a href="${site.authorX}" rel="noopener">@Loic_Pandul</a></li>
      </ul>
    </div>
  </div>
  <div class="foot-mark">
    <svg class="foot-word" viewBox="0 0 1000 66" role="img" aria-label="Dictionnaire de Bitcoin"><text x="0" y="56" textLength="1000" lengthAdjust="spacingAndGlyphs">DICTIONNAIRE DE BITCOIN</text></svg>
    <p class="foot-legal">© ${year} ${site.author} · Textes sous licence ${site.license} · Police Computer Modern (OFL)${credits ? ` · ${credits}` : ''}</p>
  </div>
</footer>`;
}

function page({ headOpts, body, home = false, footerOpts = {} }) {
  return `${head(headOpts)}
<body class="${home ? 'is-home' : 'is-inner'}">
${bar({ home })}
<main id="contenu">
${body}
</main>
${footer({ full: home, ...footerOpts })}
${searchDialog()}
</body>
</html>
`;
}

// Une ligne de liste : titre, extrait, catégorie.
function band(def, { showCategory = true, tag = 'li' } = {}) {
  return `<${tag} class="band"><a href="/${def.slug}/">
  <span class="band-title">${h(def.title)}</span>
  ${def.description ? `<span class="band-note">${h(def.description)}</span>` : ''}
  ${showCategory ? `<span class="band-cat">${picto(def.categorySlug)}${h(categoryLabel(def.category))}</span>` : ''}
</a></${tag}>`;
}

function azStrip(letters, current = null, { label = 'Lettres', hrefFor = (l) => `/lettre/${l.toLowerCase()}/` } = {}) {
  return `<nav class="az" aria-label="${h(label)}"><ul>
${[...letters.entries()]
  .map(([l, defs]) => {
    if (!defs.length) return `<li><span class="az-off" aria-disabled="true">${l}</span></li>`;
    const cur = l === current ? ' aria-current="page"' : '';
    return `<li><a href="${hrefFor(l)}"${cur}>${l}</a></li>`;
  })
  .join('\n')}
</ul></nav>`;
}

// ---------------------------------------------------------------- Définition

export function definitionPage(def, { html, math, assetVersion, jsonLd, total }) {
  const cat = categoryLabel(def.category);
  const side = `<dl class="entry-facts">
    <div><dt>Catégorie</dt><dd><a href="/categorie/${def.categorySlug}/">${picto(def.categorySlug)}${h(cat)}</a></dd></div>
    ${def.englishTerm ? `<div><dt>En anglais</dt><dd lang="en">${h(def.englishTerm)}</dd></div>` : ''}
    ${def.frenchTerm ? `<div><dt>En français</dt><dd>${h(def.frenchTerm)}</dd></div>` : ''}
    <div><dt>Lettre</dt><dd><a href="/lettre/${def.letter.toLowerCase()}/">${def.letter}</a></dd></div>
  </dl>`;

  const related = def.related.length
    ? `<section class="entry-related" aria-labelledby="associes">
  <h2 id="associes" class="side-head">${def.related.length > 1 ? 'Termes associés' : 'Terme associé'}</h2>
  <ul class="bands">${def.related.map((r) => band(r)).join('\n')}</ul>
</section>`
    : '';

  const cited = def.citedBy.filter((d) => !def.related.includes(d)).slice(0, 6);
  const citedHtml = cited.length
    ? `<section class="entry-cited" aria-labelledby="cite">
  <h2 id="cite" class="side-head">Renvoient ici</h2>
  <ul class="chips">${cited.map((d) => `<li><a href="/${d.slug}/">${h(d.title)}</a></li>`).join('')}</ul>
</section>`
    : '';

  const pager = `<nav class="pager" aria-label="Dans la catégorie ${h(cat)}">
  ${def.prev ? `<a class="pager-prev" href="/${def.prev.slug}/" rel="prev"><span class="pager-label">Précédent dans ${h(cat)}</span><span class="pager-title">${h(def.prev.title)}</span></a>` : `<a class="pager-prev" href="/categorie/${def.categorySlug}/"><span class="pager-label">Début de la catégorie</span><span class="pager-title">${h(cat)}</span></a>`}
  ${def.next ? `<a class="pager-next" href="/${def.next.slug}/" rel="next"><span class="pager-label">Suivant dans ${h(cat)}</span><span class="pager-title">${h(def.next.title)}</span></a>` : `<a class="pager-next" href="/categorie/${def.categorySlug}/"><span class="pager-label">Fin de la catégorie</span><span class="pager-title">${h(cat)}</span></a>`}
</nav>`;

  const editUrl = `${site.github}/blob/main/${def.sourcePath}`;
  const body = `<article class="entry">
  <nav class="crumbs" aria-label="Fil d’Ariane"><ol>
    <li><a href="/">Dictionnaire</a></li>
    <li><a href="/categorie/${def.categorySlug}/">${h(cat)}</a></li>
    <li aria-current="page">${h(def.title)}</li>
  </ol></nav>
  <header class="entry-head">
    <h1 class="headword ${headwordSize(def.title)}" style="--lw:${Math.max(...def.title.split(/\s+/).map((w) => w.length))};--len:${def.title.length}">${h(def.title)}</h1>
  </header>
  <aside class="entry-side" aria-label="Fiche">${side}</aside>
  <div class="entry-body prose">${html}</div>
  <div class="entry-links">${related}${citedHtml}</div>
</article>
${pager}
<aside class="colophon" aria-labelledby="colophon-titre">
  <h2 id="colophon-titre" class="colophon-head">Tiré du Dictionnaire de Bitcoin</h2>
  <p>Cette définition fait partie des ${plural(total, 'entrée', 'entrées')} du livre de ${site.author}, libre et gratuit, aussi vendu imprimé chez <a href="${site.bitcoinBazar}" rel="noopener">Bitcoin Bazar</a> et sur <a href="${site.amazon}" rel="noopener">Amazon</a>.</p>
  <p>Une erreur, un ajout ? <a href="${editUrl}" rel="noopener">Proposer une correction sur GitHub</a>.</p>
  <img class="colophon-cover" src="/img/couverture-petite.webp" width="240" height="350" alt="Couverture du Dictionnaire de Bitcoin, édition 2026" loading="lazy" decoding="async">
</aside>`;

  return page({
    headOpts: {
      title: `${def.title} : définition | Dictionnaire de Bitcoin`,
      description: def.description || `${def.title} : définition du Dictionnaire de Bitcoin, catégorie ${cat}.`,
      path: `/${def.slug}/`,
      jsonLd,
      math,
      type: 'article',
      assetVersion,
    },
    body,
  });
}

// ---------------------------------------------------------------- Lettre

export function letterPage(letter, defs, letters, { assetVersion, jsonLd }) {
  const body = `<section class="letter-page">
  <nav class="crumbs" aria-label="Fil d’Ariane"><ol><li><a href="/">Dictionnaire</a></li><li aria-current="page">Lettre ${letter}</li></ol></nav>
  <div class="letter-side"><h1 class="index-glyph"><span class="sr-only">Lettre </span>${letter}</h1></div>
  <div class="letter-main">
    <div class="index-title">
      <p class="index-count">${plural(defs.length, 'définition', 'définitions')}, de ${h(defs[0]?.title || '')} à ${h(defs.at(-1)?.title || '')}.</p>
      ${azStrip(letters, letter)}
    </div>
    <ul class="bands index-bands" aria-label="Définitions en ${letter}">${defs.map((d) => band(d)).join('\n')}</ul>
  </div>
</section>`;
  return page({
    headOpts: {
      title: `Lettre ${letter} : ${defs.length} définitions | Dictionnaire de Bitcoin`,
      description: `Les ${defs.length} termes du Dictionnaire de Bitcoin qui commencent par la lettre ${letter}, de ${defs[0]?.title} à ${defs.at(-1)?.title}.`,
      path: `/lettre/${letter.toLowerCase()}/`,
      jsonLd,
      assetVersion,
    },
    body,
  });
}

// ---------------------------------------------------------------- Catégorie

export function categoryPage(cat, note, { assetVersion, jsonLd }) {
  const label = categoryLabel(cat.name);
  const groups = new Map();
  for (const d of cat.defs) {
    const first = d.title.normalize('NFD')[0].toUpperCase();
    const key = /[A-Z]/.test(first) ? first : '#';
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(d);
  }
  const letters = new Map('ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').map((l) => [l, groups.get(l) || []]));
  const body = `<section class="index-head index-head--cat">
  <nav class="crumbs" aria-label="Fil d’Ariane"><ol><li><a href="/">Dictionnaire</a></li><li aria-current="page">${h(label)}</li></ol></nav>
  <div class="index-glyph">${picto(cat.slug, 'picto--xl')}</div>
  <div class="index-title">
    <h1>${h(label)}</h1>
    <p class="index-count">${plural(cat.defs.length, 'définition', 'définitions')} dans cette catégorie.</p>
    ${note ? `<p class="index-note">${h(note)}</p>` : ''}
    ${azStrip(letters, null, { label: `Lettres de la catégorie ${label}`, hrefFor: (l) => `#lettre-${l.toLowerCase()}` })}
  </div>
</section>
<section class="index-list" aria-label="Définitions de la catégorie ${h(label)}">
${[...groups.entries()]
  .map(
    ([l, defs]) => `<div class="index-group" id="lettre-${l.toLowerCase()}">
  <h2 class="index-letter">${l}</h2>
  <ul class="bands">${defs.map((d) => band(d, { showCategory: false })).join('\n')}</ul>
</div>`,
  )
  .join('\n')}
</section>`;
  return page({
    headOpts: {
      title: `${label} : ${cat.defs.length} définitions | Dictionnaire de Bitcoin`,
      description: note
        ? `${cat.defs.length} définitions. ${note}`.slice(0, 155).replace(/\s+\S*$/, '…')
        : `Les ${cat.defs.length} définitions de la catégorie ${label} du Dictionnaire de Bitcoin.`,
      path: `/categorie/${cat.slug}/`,
      jsonLd,
      assetVersion,
    },
    body,
  });
}

// ---------------------------------------------------------------- Accueil

export function homePage(data, { assetVersion, jsonLd, credits }) {
  const { definitions, categories, letters, featured, stats } = data;
  const total = definitions.length;

  const letterPanels = [...letters.entries()]
    .filter(([, defs]) => defs.length)
    .map(([l, defs], i) => {
      const shown = defs.slice(0, 7);
      return `<div class="agenda-panel" id="panneau-${l.toLowerCase()}" role="tabpanel" aria-labelledby="onglet-${l.toLowerCase()}"${i === 0 ? '' : ' hidden'}>
  <ul class="bands bands--agenda">${shown.map((d) => band(d)).join('\n')}</ul>
  <a class="agenda-more" href="/lettre/${l.toLowerCase()}/">Les ${plural(defs.length, 'terme', 'termes')} en ${l}</a>
</div>`;
    })
    .join('\n');

  const letterTabs = [...letters.entries()]
    .map(([l, defs], i) =>
      defs.length
        ? `<a class="agenda-tab" href="/lettre/${l.toLowerCase()}/" id="onglet-${l.toLowerCase()}" data-tab="${l.toLowerCase()}" role="tab" aria-controls="panneau-${l.toLowerCase()}" aria-selected="${i === 0}"><span class="agenda-l">${l}</span><span class="agenda-n">${defs.length}</span></a>`
        : `<span class="agenda-tab agenda-tab--off" aria-hidden="true"><span class="agenda-l">${l}</span><span class="agenda-n">0</span></span>`,
    )
    .join('');

  const catList = categories
    .map(
      (c) =>
        `<li><a href="/categorie/${c.slug}/">${picto(c.slug)}<span class="cat-name">${h(categoryLabel(c.name))}</span><span class="cat-n">${c.defs.length}</span></a></li>`,
    )
    .join('\n');

  const biggest = [...categories].sort((a, b) => b.defs.length - a.defs.length)[0];

  const body = `<section class="hero" aria-labelledby="titre">
  <h1 id="titre" class="hero-title"><span class="line"><span>Dictionnaire</span></span> <span class="line"><span>de Bitcoin</span></span></h1>
  <div class="hero-talk">
    <p class="hero-lede">Tout le vocabulaire technique de Bitcoin en ${num(total)} définitions libres.</p>
    <form class="hero-search" role="search" data-inline-search>
      <label class="sr-only" for="hero-q">Rechercher une définition</label>
      <input id="hero-q" class="hero-input" type="search" name="q" placeholder="Chercher un terme : UTXO, Taproot…" autocomplete="off" spellcheck="false"
        role="combobox" aria-expanded="false" aria-autocomplete="list" aria-controls="hero-resultats">
      <ul class="search-results search-results--inline" id="hero-resultats" role="listbox" aria-label="Résultats"></ul>
    </form>
  </div>
  <figure class="hero-plate">
    <img src="/img/arbre-canopee.webp" width="1800" height="560" alt="Le feuillage de l’arbre gravé qui orne la couverture du livre, en traits clairs sur fond bleu nuit" fetchpriority="high">
    <figcaption class="hero-figure"><span class="hero-figure-n">${num(total)}</span><span>définitions en ${categories.length} catégories, aussi imprimées dans l’édition 2026</span></figcaption>
  </figure>
</section>

<section class="today" aria-labelledby="jour-titre" data-today>
  <div class="today-plate">
    <img src="/img/monnoyage-laminoirs.webp" width="1100" height="1311" alt="Planche de l’Encyclopédie : les laminoirs qui aplatissaient le métal des pièces de monnaie" loading="lazy" decoding="async">
    <span class="today-picto" data-today-picto>${picto(featured.categorySlug, 'picto--plate')}</span>
  </div>
  <div class="today-text">
    <div class="today-tabs" role="group" aria-label="Choisir un terme">
      <button type="button" class="today-tab" aria-pressed="true" data-today-mode="jour">Aujourd’hui</button>
      <button type="button" class="today-tab" aria-pressed="false" data-today-mode="hasard">Au hasard</button>
    </div>
    <div class="today-body">
      <h2 id="jour-titre" class="section-title">Le terme du jour</h2>
      <p class="today-term"><a href="/${featured.slug}/" data-today-link>${h(featured.title)}</a></p>
      <p class="today-cat" data-today-cat>${h(categoryLabel(featured.category))}</p>
      <p class="today-desc" data-today-desc>${h(featured.description || '')}</p>
    </div>
    <div class="today-actions">
      <a class="cell cell--ink" href="/${featured.slug}/" data-today-read>Lire la définition</a>
      <button type="button" class="cell cell--tone" data-today-next>Un autre terme</button>
    </div>
  </div>
</section>

<section class="agenda" id="lettres" aria-labelledby="lettres-titre">
  <div class="agenda-head">
    <h2 id="lettres-titre" class="section-title">Parcourir de A à Z</h2>
    <p class="agenda-lede">${num(total)} entrées classées comme dans le livre. Choisissez une lettre&nbsp;: B en compte ${letters.get('B').length}, Q seulement ${letters.get('Q').length}.</p>
  </div>
  <div class="agenda-tabs" role="tablist" aria-label="Lettres">${letterTabs}</div>
  <div class="agenda-panels">${letterPanels}</div>
</section>

<section class="mosaic-page" id="categories" aria-labelledby="categories-titre">
  <div class="mosaic">
    <div class="tile tile--head t-head">
      <h2 id="categories-titre" class="section-title">Dix-neuf domaines</h2>
      <p>Chaque définition appartient à une catégorie, de la cryptographie à l’histoire, avec le pictogramme qui la signale dans le livre.</p>
    </div>
    <ul class="tile tile--list cat-list t-list">${catList}</ul>
    <figure class="tile tile--photo t-photo">
      <img src="/img/monnoyage-balancier.webp" width="1400" height="883" alt="Planche de l’Encyclopédie : des ouvriers actionnent le balancier qui frappe les pièces de monnaie" loading="lazy" decoding="async">
    </figure>
    <div class="tile tile--figure t-fig1">
      <p class="tile-n">${biggest.defs.length}</p>
      <p>définitions dans la catégorie <a href="/categorie/${biggest.slug}/">${h(categoryLabel(biggest.name))}</a>, la plus fournie.</p>
    </div>
    <div class="tile tile--figure tile--tone t-fig2">
      <p class="tile-n">${num(stats.links)}</p>
      <p>renvois relient les définitions entre elles.</p>
    </div>
    <div class="tile tile--sentence t-sent1">
      <p>${num(stats.english)} entrées donnent aussi le terme anglais, pour lire la documentation d’origine.</p>
    </div>
    <div class="tile tile--sentence tile--accent t-sent2">
      <p>${num(stats.math)} définitions composent leurs formules comme le livre, en Computer Modern.</p>
    </div>
  </div>
</section>

<section class="author" aria-labelledby="auteur-titre">
  <ul class="author-facts">
    <li>Édition 2026</li>
    <li>Licence ${site.license}</li>
    <li><a href="${site.authorUrl}" rel="author">pandul.fr</a></li>
  </ul>
  <div class="author-text">
    <h2 id="auteur-titre" class="section-title">Écrit par Loïc Morel</h2>
    <p class="author-statement"><img class="author-portrait" src="/img/loic-morel.webp" width="560" height="560" alt="Portrait de Loïc Morel" loading="lazy" decoding="async"><strong>Loïc Morel</strong> est rédacteur spécialisé sur Bitcoin, auteur de plus de 200 articles, formations et tutoriels en français, tous gratuits et sous licence libre.</p>
    <p class="author-more">Le dictionnaire est un projet ouvert. Chacun peut proposer une correction, une précision ou un terme manquant sur <a href="${site.github}" rel="noopener">le dépôt GitHub</a>&nbsp;; chaque page de définition mène directement au fichier à modifier.</p>
  </div>
</section>

<section class="book" id="livre" aria-labelledby="livre-titre">
  <div class="book-strip">
    <img src="/img/livre-volume.webp" width="1150" height="1000" alt="Le Dictionnaire de Bitcoin imprimé, édition 2026, vu de trois quarts avec sa tranche" loading="lazy" decoding="async">
    <video class="book-video" muted loop playsinline preload="none" poster="/video/composition.webp" width="640" height="480" aria-label="Film de 1959 : deux mains prennent les caractères de plomb dans une casse pour composer un texte" data-lazy-video>
      <source src="/video/composition.mp4" type="video/mp4">
    </video>
    <img src="/img/encyclopedie-titre.webp" width="1100" height="1105" alt="Page de titre de l’Encyclopédie, ou Dictionnaire raisonné des sciences, des arts et des métiers, 1751" loading="lazy" decoding="async">
  </div>
  <div class="book-band">
    <h2 id="livre-titre" class="section-title">Le livre</h2>
    <p class="book-statement">Les ${num(total)} définitions existent aussi sur papier, en broché et en relié. <a href="${site.bitcoinBazar}" rel="noopener">Commander sur Bitcoin Bazar</a></p>
    <p class="book-small">Également sur <a href="${site.amazon}" rel="noopener">Amazon</a>. Le PDF complet reste gratuit&nbsp;: <a href="${site.pdf}" download>télécharger le PDF</a> (2,7&nbsp;Mo).</p>
    <p class="book-small">ISBN ${site.isbnPaperback} (broché) · ${site.isbnHardcover} (relié)</p>
    <img class="book-cover" src="/img/couverture.webp" width="900" height="1313" alt="Couverture du livre : le titre en capitales sur un arbre gravé, fond bleu nuit" loading="lazy" decoding="async">
  </div>
</section>`;

  return page({
    home: true,
    headOpts: {
      title: 'Dictionnaire de Bitcoin : tout le vocabulaire technique de Bitcoin',
      description: `Le Dictionnaire de Bitcoin de Loïc Morel : ${num(total)} définitions libres et gratuites du vocabulaire technique de Bitcoin, aussi disponible en livre imprimé et en PDF.`,
      path: '/',
      jsonLd,
      assetVersion,
    },
    body,
    footerOpts: { credits },
  });
}

// ---------------------------------------------------------------- 404

export function notFoundPage({ assetVersion }) {
  const body = `<section class="lost">
  <p class="lost-glyph" aria-hidden="true">?</p>
  <div>
    <h1>Ce terme n’est pas dans le dictionnaire</h1>
    <p>L’adresse ne correspond à aucune page. Cherchez le terme ou repartez d’une lettre.</p>
    <p><button type="button" class="cell cell--ink" data-search-open>Rechercher un terme</button> <a class="cell cell--tone" href="/">Retour à l’accueil</a></p>
  </div>
</section>
<figure class="lost-tree"><img src="/img/arbre-tronc.webp" width="1690" height="980" alt="Le tronc et les branches de l’arbre gravé de la couverture du livre" loading="lazy" decoding="async"></figure>`;
  return page({
    headOpts: { title: 'Page introuvable | Dictionnaire de Bitcoin', description: 'Cette page n’existe pas.', path: '/404.html', assetVersion },
    body,
  });
}
