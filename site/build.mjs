// Construit le site statique dans site/dist depuis definitions/fr.
//   node build.mjs            construit tout
//   node build.mjs --out DIR  autre dossier de sortie
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { url, site, palette } from './config.mjs';
import { loadDictionary, loadCategoryNotes, slugify } from './lib/content.mjs';
import { loadParts, loadChronology, loadSpecifications } from './lib/edition.mjs';
import { createRenderer } from './lib/markdown.mjs';
import { createLinker } from './lib/liens.mjs';
import { definitionPage, letterPage, categoryPage, partPage, homePage, searchPage, notFoundPage, chronologyPage, specsHubPage, specsPage, ancreEvenement, categoryLabel, pictoSprite, setNavigation, setPictos } from './lib/templates.mjs';
import { LANGUES, setLangue, chemins, setAffichage } from './lib/i18n.mjs';
import { homeJsonLd, definitionJsonLd, listJsonLd, sitemap, robots } from './lib/seo.mjs';
import { headers, redirects } from './lib/cloudflare.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(here, '..');
const outArg = process.argv.indexOf('--out');
const out = path.resolve(outArg > -1 ? process.argv[outArg + 1] : path.join(here, 'dist'));
const started = Date.now();

const write = (rel, content) => {
  const file = path.join(out, rel);
  fs.mkdirSync(path.dirname(file), { recursive: true });
  fs.writeFileSync(file, content);
};
const sha = (buf, n = 10) => crypto.createHash('sha256').update(buf).digest('hex').slice(0, n);

// 1. Données communes aux deux langues : parties du livre, pictogrammes, chronologie, spécifications.
const notes = loadCategoryNotes(path.join(repoRoot, 'templates', 'categories.yaml'));
const parts = loadParts(repoRoot);
const specs = loadSpecifications(repoRoot);
// Pictogrammes 2027 (assets/pictograms) : un par catégorie d'après parts.yaml ; un par série de spécifications.
const pictoDir = path.join(repoRoot, 'assets', 'pictograms');
const pictoDe = (nom) => {
  const f = path.join(pictoDir, `${nom}.svg`);
  return fs.existsSync(f) ? fs.readFileSync(f, 'utf8').replace(/^[\s\S]*?<svg[^>]*>|<\/svg>\s*$/g, '').trim() : null;
};
const pictos = new Map();
for (const p of parts) for (const c of p.categories) {
  const corps = c.pictogram && pictoDe(c.pictogram);
  if (corps) pictos.set(slugify(c.name), corps);
}
for (const g of specs) for (const se of g.series) if (!pictos.has(se.id) && pictoDe(se.id)) pictos.set(se.id, pictoDe(se.id));
setPictos(pictos);
setAffichage(parts.flatMap((p) => p.categories.map((c) => [c.name, c.display])));

// 2. Sortie propre
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

// 3. Fichiers statiques. Le CSS et les scripts reçoivent une empreinte dans leur nom :
//    ils peuvent alors être mis en cache un an (voir _headers).
fs.cpSync(path.join(here, 'static'), out, {
  recursive: true,
  filter: (src) => !/[/\\](css|js)[/\\][^/\\]+$/.test(src) && !/[/\\]img[/\\]pictos/.test(src),
});
// Minification prudente du CSS : commentaires et blancs superflus. Jamais d'espace retirée avant « : »
// (« .dos :focus-visible » n'est pas « .dos:focus-visible »).
const minCss = (css) => css
  .replace(/\/\*[\s\S]*?\*\//g, '')
  .replace(/\s+/g, ' ')
  .replace(/\s*([{};,])\s*/g, '$1')
  .replace(/:\s+/g, ':')
  .replace(/;}/g, '}')
  .trim();
// Le bloc « palette » du CSS est réécrit depuis config.mjs : c'est le seul endroit où vivent les couleurs.
const JETONS = {
  blanc: 'blanc', brume: 'brume', rose: 'rose', galet: 'galet', encre: 'encre', ecorce: 'ecorce', figue: 'figue',
  figueSombre: 'figue-sombre', canopee: 'canopee', figueVive: 'figue-vive', figueClaire: 'figue-claire', nuit: 'nuit',
  surfaceSombre: 'surface-sombre', ecorceSombre: 'ecorce-sombre', ombre: 'ombre',
};
function appliquerPalette(css) {
  const lignes = Object.entries(JETONS).map(([cle, nom]) => {
    if (!palette[cle]) throw new Error(`palette.${cle} manque dans config.mjs`);
    return `--${nom}: ${palette[cle]};`;
  });
  const bloc = /(\/\* palette:début[^*]*\*\/)[\s\S]*?(\/\* palette:fin \*\/)/;
  if (!bloc.test(css)) throw new Error('bloc « palette » introuvable dans site.css');
  return css.replace(bloc, `$1\n  ${lignes.join('\n  ')}\n  $2`);
}
const hashed = {};
for (const f of ['css/site.css', 'js/site.js', 'js/accueil.js']) {
  let buf = fs.readFileSync(path.join(here, 'static', f));
  if (f.endsWith('.css')) buf = Buffer.from(minCss(appliquerPalette(buf.toString())));
  const name = f.replace(/\.(css|js)$/, `.${sha(buf)}.$1`);
  write(name, buf);
  hashed[f] = `/${name}`;
}
// Script en ligne de la tête (thème et classe js) : son empreinte va dans la politique de sécurité.
// Il lit aussi le type de transition (page tournée) à l'arrivée sur une page : ce doit être fait
// avant le premier rendu, donc ici et pas dans le script différé.
const inlineScript = "(function(d){d.classList.add('js');try{var t=localStorage.getItem('theme');if(t)d.dataset.theme=t}catch(e){}addEventListener('pagereveal',function(e){if(!e.viewTransition)return;d.classList.add('vt-arrivee');try{var v=sessionStorage.getItem('vt');sessionStorage.removeItem('vt');if(v){e.viewTransition.types.add(v);d.classList.add('vt-tour')}}catch(x){}})})(document.documentElement)";
const inlineHash = crypto.createHash('sha256').update(inlineScript).digest('base64');
const assets = { css: hashed['css/site.css'], js: hashed['js/site.js'], home: hashed['js/accueil.js'], inlineScript };

fs.mkdirSync(path.join(out, 'katex/fonts'), { recursive: true });
fs.copyFileSync(path.join(here, 'node_modules/katex/dist/katex.min.css'), path.join(out, 'katex/katex.min.css'));
for (const f of fs.readdirSync(path.join(here, 'node_modules/katex/dist/fonts'))) {
  if (f.endsWith('.woff2')) fs.copyFileSync(path.join(here, 'node_modules/katex/dist/fonts', f), path.join(out, 'katex/fonts', f));
}
fs.copyFileSync(path.join(repoRoot, 'dictionnaire-de-bitcoin.pdf'), path.join(out, site.pdf.slice(1)));
write('img/pictos.svg', pictoSprite());
write('site.webmanifest', JSON.stringify({
  name: site.title,
  short_name: 'Dictionnaire',
  lang: 'fr',
  start_url: '/',
  display: 'standalone',
  background_color: palette.blanc,
  theme_color: palette.figue,
  icons: [
    { src: '/apple-touch-icon.png', sizes: '180x180', type: 'image/png' },
    { src: '/icon-512.png', sizes: '512x512', type: 'image/png' },
  ],
}));

// 4. Une passe par langue : le français à la racine, l'anglais sous /en/.
const sitemapPaths = [];
const bilan = {};
const nIndex = (L) => (L.code === 'fr' ? '' : L.base);
for (const code of Object.keys(LANGUES)) {
  const L = setLangue(code);
  const P = chemins(L);
  // Adresses déjà prises au premier niveau : les pages de l'interface, et à la racine les dossiers statiques et les langues.
  const reserves = [...Object.values(L.seg), ...(code === 'fr' ? ['css', 'js', 'img', 'fonts', 'katex', ...Object.keys(LANGUES).filter((c) => c !== 'fr')] : [])];
  const data = loadDictionary(repoRoot, { lang: code, reserves });
  if (data.collisions.length) {
    for (const c of data.collisions) console.error(`ERREUR ${c}`);
    process.exit(1);
  }
  const { definitions, categories, letters } = data;
  if (code === 'fr') {
    for (const w of data.warnings) console.warn(`WARN ${w}`);
    for (const hit of data.sanitizationHits) console.log(`[assainissement] ${hit.slug} : ${hit.pattern} « ${hit.match} »`);
  }
  const total = definitions.length;
  // Par slug français : la chronologie et les spécifications citent les entrées sous ce nom.
  const bySlug = new Map(definitions.map((d) => [d.slugs.fr, d]));
  // Parties : les catégories présentes, dans l'ordre du livre ; une catégorie absente de parts.yaml
  // rejoint la partie technique (ou une partie « Autres » s'il n'y en a pas).
  const catByName = new Map(categories.map((c) => [c.name, c]));
  const partsL = parts.map((p) => ({ ...p, cats: p.categories.map((c) => catByName.get(c.name)).filter(Boolean) }));
  const rangees = new Set(partsL.flatMap((p) => p.cats.map((c) => c.name)));
  const orphelines = categories.filter((c) => !rangees.has(c.name));
  if (orphelines.length) (partsL.find((p) => p.id === 'technique') || (partsL.push({ id: 'autres', title: 'Autres', intro: '', cats: [] }), partsL.at(-1))).cats.push(...orphelines);
  const partOf = new Map(partsL.flatMap((p) => p.cats.map((c) => [c.name, p])));
  const ordreCats = partsL.flatMap((p) => p.cats);
  setNavigation(letters, ordreCats, partsL);

  // Chronologie et spécifications, avec les liens retour vers les définitions.
  const chrono = loadChronology(repoRoot, code);
  const chronoDe = new Map();
  let k = 0;
  for (const a of chrono) for (const e of a.events) {
    e.lang = a.lang;
    const ancre = ancreEvenement(e, k++);
    for (const s of e.related) (chronoDe.get(s) || chronoDe.set(s, []).get(s)).push({ e, ancre });
  }
  const specDe = new Map();
  for (const g of specs) for (const se of g.series) for (const e of se.entries) if (e.definition) specDe.set(e.definition, { ...e, groupe: g.id });

  // Définitions
  const render = createRenderer({ linker: createLinker(definitions), label: (n) => categoryLabel(n), base: L.base, agrandir: L.agrandir, agrandirImage: L.agrandirImage, creditLabel: L.creditImage });
  let mathPages = 0;
  let images = 0;
  for (const def of definitions) {
    const { html, math } = render(def);
    if (math) mathPages++;
    write(`${P.def(def.slug).slice(1)}index.html`, definitionPage(def, { html, math, assets, jsonLd: definitionJsonLd(def), total, letters, liens: { chrono: chronoDe.get(def.slugs.fr), spec: specDe.get(def.slugs.fr) } }));
    if (code !== 'fr') {
      // Un schéma redessiné dans la langue de la traduction : dans son propre dossier assets/.
      const propres = path.join(def.mdDir, 'assets');
      if (def.mdDir !== def.sourceDir && fs.existsSync(propres)) {
        fs.mkdirSync(path.join(out, code, def.slug, 'assets'), { recursive: true });
        for (const f of fs.readdirSync(propres)) if (/\.(png|svg|jpe?g|webp)$/.test(f)) { fs.copyFileSync(path.join(propres, f), path.join(out, code, def.slug, 'assets', f)); images++; }
      }
      continue;
    }
    // Les images, une seule fois (sous l'adresse française), avec leur SVG quand il existe.
    const fichiers = new Set(def.assets.map((a) => a.filename));
    for (const f of [...fichiers]) { const svg = f.replace(/\.png$/, '.svg'); if (svg !== f && fs.existsSync(path.join(def.sourceDir, 'assets', svg))) fichiers.add(svg); }
    for (const f of fichiers) {
      const src = path.join(def.sourceDir, 'assets', f);
      if (fs.existsSync(src)) {
        fs.mkdirSync(path.join(out, def.slug, 'assets'), { recursive: true });
        fs.copyFileSync(src, path.join(out, def.slug, 'assets', f));
        images++;
      } else console.warn(`WARN image manquante ${src}`);
    }
  }
  const indexable = (d) => code === 'fr' || d.lang === code;

  // Lettres, catégories, parties
  const lettresPleines = [...letters].filter(([, d]) => d.length);
  for (const [letter, defs] of lettresPleines) {
    write(`${P.lettre(letter).slice(1)}index.html`, letterPage(letter, defs, letters, { assets, total, jsonLd: listJsonLd({ path: P.lettre(letter), name: L.nomLettre(letter), defs, L }) }));
  }
  for (const cat of categories) {
    const p = P.categorie(cat);
    write(`${p.slice(1)}index.html`, categoryPage(cat, notes.get(cat.name), { assets, letters, total, categories: ordreCats, part: partOf.get(cat.name), jsonLd: listJsonLd({ path: p, name: categoryLabel(cat.name), defs: cat.defs, L }) }));
  }
  for (const part of partsL.filter((x) => x.cats.length && x.id !== 'specifications')) {
    const p = P.partie(part.id);
    write(`${p.slice(1)}index.html`, partPage(part, { assets, letters, total, jsonLd: listJsonLd({ path: p, name: part.title, defs: part.cats.flatMap((c) => c.defs), L }) }));
  }

  // Chronologie et spécifications
  if (chrono.length) write(`${P.chronologie().slice(1)}index.html`, chronologyPage(chrono, { assets, letters, total, bySlug, jsonLd: '' }));
  if (specs.length) {
    write(`${P.specs().slice(1)}index.html`, specsHubPage(specs, { assets, letters, total, jsonLd: '' }));
    for (const g of specs) write(`${P.specs(g.id).slice(1)}index.html`, specsPage(g, { assets, letters, total, bySlug, jsonLd: '' }));
  }

  // Accueil (le mot du jour du build ; le script le remplace par celui du jour du lecteur), recherche et 404.
  // Le mot du jour est pris parmi les entrées écrites dans la langue de la page (les traduites, en anglais).
  const duJour = definitions.filter((d) => d.lang === code);
  const featured = (duJour.length ? duJour : definitions)[Math.floor(Date.now() / 86400000) % (duJour.length || total)];
  write(`${P.accueil().slice(1)}index.html`, homePage({ definitions, categories: ordreCats, letters, featured, notes, parts: partsL, chrono, specs }, {
    assets,
    jsonLd: homeJsonLd({ total, description: L.descAccueil(total), L }),
  }));
  write(`${P.recherche().slice(1)}index.html`, searchPage({ assets, letters, total, categories: ordreCats }));
  write(`${nIndex(L).slice(1)}${code === 'fr' ? '' : '/'}404.html`, notFoundPage({ assets, letters, total }));

  // Index de recherche : une ligne compacte par terme, chargée à la demande.
  // [titre, slug, catégorie, autres noms, résumé, langue du résumé si ce n'est pas celle de la page]
  const catIndex = categories.map((c) => [categoryLabel(c.name), c.slug, P.categorie(c)]);
  const catPos = new Map(categories.map((c, i) => [c.name, i]));
  const autresNoms = (d) => [d.englishTerm, d.frenchTerm, d.titleFr !== d.title ? d.titleFr : ''].filter((x, i, a) => x && a.indexOf(x) === i).join(' · ');
  write(`${nIndex(L).slice(1)}${code === 'fr' ? '' : '/'}recherche.json`, JSON.stringify({
    categories: catIndex,
    terms: definitions.map((d) => {
      const ligne = [d.title, d.slug, catPos.get(d.category), autresNoms(d), d.resume || ''];
      if (d.lang !== code) ligne.push(d.lang);
      return ligne;
    }),
  }));
  // La tranche : longueur de chaque définition, dans le même ordre que l'index.
  // Avec le nombre de renvois reçus, qui départage les résultats de recherche de même rang.
  write(`${nIndex(L).slice(1)}${code === 'fr' ? '' : '/'}tranche.json`, JSON.stringify({ longueurs: definitions.map((d) => d.body.length), renvois: definitions.map((d) => d.citedBy.length) }));
  if (code === 'fr') {
    // La tranche dessinée, en masque teintable pour le signet des pages de définition :
    // un trait par mot, hauteur en racine carrée de la longueur, étirée à la largeur du bloc.
    const max = Math.sqrt(Math.max(...definitions.map((d) => d.body.length)));
    const dPath = definitions.map((d, i) => `M${i} 100V${(100 - Math.max(6, (Math.sqrt(d.body.length) / max) * 100)).toFixed(1)}h.62V100z`).join('');
    write('img/tranche.svg', `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${definitions.length} 100" preserveAspectRatio="none"><path d="${dPath}"/></svg>`);
  }

  // Adresses du sitemap : les pages anglaises encore en français n'y sont pas (leur canonique est la page française).
  sitemapPaths.push(P.accueil(), ...definitions.filter(indexable).map((d) => P.def(d.slug)), ...categories.map((c) => P.categorie(c)),
    ...lettresPleines.map(([l]) => P.lettre(l)), ...partsL.filter((x) => x.cats.length && x.id !== 'specifications').map((x) => P.partie(x.id)));
  if (chrono.length) sitemapPaths.push(P.chronologie());
  if (specs.length) sitemapPaths.push(P.specs(), ...specs.map((g) => P.specs(g.id)));
  bilan[code] = { total, traduites: data.translated, lettres: lettresPleines.length, categories: categories.length, parties: partsL.filter((x) => x.cats.length).length, evenements: chrono.reduce((s, a) => s + a.events.length, 0), mathPages, images, unresolved: data.unresolved, definitions, categoriesL: categories };
}
setLangue('fr');
const { definitions, categoriesL: categories } = bilan.fr;
const total = definitions.length;

// 8. Sitemap, robots, llms.txt, en-têtes et redirections Cloudflare Pages
const paths = sitemapPaths;
write('sitemap.xml', sitemap(paths));
write('robots.txt', robots());
write('llms.txt', `# ${site.title}\n\n> ${site.subtitle}. ${total} définitions en français, par ${site.author}, sous licence ${site.license}. English version: ${url}/en/ (${bilan.en?.traduites || 0} definitions translated so far).\n\n## Catégories\n\n${categories.map((c) => `- [${categoryLabel(c.name)}](${url}/categorie/${c.slug}/) : ${c.defs.length} définitions`).join('\n')}\n\n## Annexes\n\n- [Chronologie](${url}/chronologie/)\n- [Spécifications](${url}/specifications/)\n\n## Livre\n\n- [PDF complet](${url}${site.pdf})\n- [Sources sur GitHub](${site.github})\n`);
write('_headers', headers({ inlineHash }));
// Catégories renommées : docs/edition-2027/reclassement.tsv (slug, ancienne catégorie, nouvelle) quand il existe ;
// une ancienne catégorie qui n'existe plus mène à la nouvelle catégorie de la plupart de ses entrées.
const anciennes = [];
{
  const f = [path.join(repoRoot, 'docs', 'edition-2027', 'reclassement.tsv'), path.join(repoRoot, 'edition-2027', 'reclassement.tsv')].find((x) => fs.existsSync(x));
  if (f) {
    const actuelles = new Set(categories.map((c) => c.slug));
    const votes = new Map();
    for (const ligne of fs.readFileSync(f, 'utf8').split('\n').slice(1)) {
      const [, avant, apres] = ligne.split('\t');
      if (!avant || !apres) continue;
      const a = slugify(avant);
      const b = slugify(apres);
      if (actuelles.has(a) || !actuelles.has(b)) continue;
      const v = votes.get(a) || new Map();
      v.set(b, (v.get(b) || 0) + 1);
      votes.set(a, v);
    }
    for (const [a, v] of votes) anciennes.push([a, [...v].sort((x, y) => y[1] - x[1])[0][0]]);
  }
}
// Slugs anglais : /en/<slug français>/ redirige vers la page traduite, sauf si une autre page anglaise porte ce slug.
const traductions = Object.entries(bilan).filter(([c]) => c !== 'fr').flatMap(([c, b]) => {
  const pris = new Set(b.definitions.map((d) => d.slug));
  return b.definitions.filter((d) => d.lang === c && d.slug !== d.slugs.fr && !pris.has(d.slugs.fr)).map((d) => [d.slugs.fr, d.slug]);
});
write('_redirects', redirects({ anciennes, traductions }));

const defPages = definitions.filter((d) => fs.existsSync(path.join(out, d.slug, 'index.html'))).length;
let files = 0;
const count = (dir) => { for (const e of fs.readdirSync(dir, { withFileTypes: true })) e.isDirectory() ? count(path.join(dir, e.name)) : files++; };
count(out);
console.log(`Build terminé en ${((Date.now() - started) / 1000).toFixed(1)} s → ${path.relative(process.cwd(), out) || '.'}`);
console.log(`  définitions source : ${total}`);
console.log(`  pages de définition : ${defPages} (fr), ${bilan.en ? `${bilan.en.total} (en, dont ${bilan.en.traduites} traduites)` : ''}`);
console.log(`  pages de lettre : ${bilan.fr.lettres}, pages de catégorie : ${categories.length}, parties : ${bilan.fr.parties}, dates de la chronologie : ${bilan.fr.evenements}, séries de spécifications : ${specs.length}`);
console.log(`  pages avec formules : ${bilan.fr.mathPages}, images copiées : ${bilan.fr.images}, renvois non résolus : ${bilan.fr.unresolved}`);
console.log(`  URL de base : ${url} · sitemap : ${paths.length} adresses · ${files} fichiers`);
if (defPages !== total) {
  console.error('ERREUR : il manque des pages de définition');
  process.exit(1);
}
