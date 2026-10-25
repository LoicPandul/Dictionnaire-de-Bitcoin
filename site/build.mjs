// Construit le site statique dans site/dist depuis definitions/fr.
//   node build.mjs            construit tout
//   node build.mjs --out DIR  autre dossier de sortie
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { url, site } from './config.mjs';
import { loadDictionary, loadCategoryNotes } from './lib/content.mjs';
import { createRenderer } from './lib/markdown.mjs';
import { createLinker } from './lib/liens.mjs';
import { definitionPage, letterPage, categoryPage, homePage, searchPage, notFoundPage, categoryLabel, pictoSprite, setNavigation } from './lib/templates.mjs';
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

// 1. Données
const data = loadDictionary(repoRoot);
const { definitions, categories, letters } = data;
const notes = loadCategoryNotes(path.join(repoRoot, 'templates', 'categories.yaml'));
for (const w of data.warnings) console.warn(`WARN ${w}`);
for (const hit of data.sanitizationHits) console.log(`[assainissement] ${hit.slug} : ${hit.pattern} « ${hit.match} »`);
const total = definitions.length;
setNavigation(letters, categories);

// 2. Sortie propre
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

// 3. Fichiers statiques. Le CSS et les scripts reçoivent une empreinte dans leur nom :
//    ils peuvent alors être mis en cache un an (voir _headers).
fs.cpSync(path.join(here, 'static'), out, {
  recursive: true,
  filter: (src) => !/[/\\](css|js)[/\\][^/\\]+$/.test(src),
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
const hashed = {};
for (const f of ['css/site.css', 'js/site.js', 'js/accueil.js']) {
  let buf = fs.readFileSync(path.join(here, 'static', f));
  if (f.endsWith('.css')) buf = Buffer.from(minCss(buf.toString()));
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
  background_color: '#F5F3EE',
  theme_color: '#193042',
  icons: [
    { src: '/apple-touch-icon.png', sizes: '180x180', type: 'image/png' },
    { src: '/icon-512.png', sizes: '512x512', type: 'image/png' },
  ],
}));

// 4. Définitions
const render = createRenderer({ linker: createLinker(definitions), label: categoryLabel });
let mathPages = 0;
let images = 0;
for (const def of definitions) {
  const { html, math } = render(def);
  if (math) mathPages++;
  write(`${def.slug}/index.html`, definitionPage(def, { html, math, assets, jsonLd: definitionJsonLd(def), total, letters }));
  for (const asset of def.assets) {
    const src = path.join(def.sourceDir, 'assets', asset.filename);
    if (fs.existsSync(src)) {
      fs.mkdirSync(path.join(out, def.slug, 'assets'), { recursive: true });
      fs.copyFileSync(src, path.join(out, def.slug, 'assets', asset.filename));
      images++;
    } else console.warn(`WARN image manquante ${src}`);
  }
}

// 5. Lettres et catégories
for (const [letter, defs] of letters) {
  if (!defs.length) continue;
  const p = `/lettre/${letter.toLowerCase()}/`;
  write(`lettre/${letter.toLowerCase()}/index.html`, letterPage(letter, defs, letters, { assets, total, jsonLd: listJsonLd({ path: p, name: `Lettre ${letter}`, defs }) }));
}
for (const cat of categories) {
  const p = `/categorie/${cat.slug}/`;
  write(`categorie/${cat.slug}/index.html`, categoryPage(cat, notes.get(cat.name), { assets, letters, total, categories, jsonLd: listJsonLd({ path: p, name: categoryLabel(cat.name), defs: cat.defs }) }));
}

// 6. Accueil (le mot du jour du build ; le script le remplace par celui du jour du lecteur),
//    recherche et 404.
const dayIndex = Math.floor(Date.now() / 86400000) % total;
write('index.html', homePage({ definitions, categories, letters, featured: definitions[dayIndex], notes }, {
  assets,
  jsonLd: homeJsonLd({ total, description: `${total} définitions du vocabulaire technique de Bitcoin, par Loïc Morel.` }),
}));
write('recherche/index.html', searchPage({ assets, letters, total, categories }));
write('404.html', notFoundPage({ assets, letters, total }));

// 7. Index de recherche : une ligne compacte par terme, chargée à la demande.
const catIndex = categories.map((c) => [categoryLabel(c.name), c.slug]);
const catPos = new Map(categories.map((c, i) => [c.name, i]));
write('recherche.json', JSON.stringify({
  categories: catIndex,
  terms: definitions.map((d) => [d.title, d.slug, catPos.get(d.category), d.englishTerm || d.frenchTerm || '', d.description || '']),
}));
// La tranche : longueur de chaque définition, dans le même ordre que l'index.
// Avec le nombre de renvois reçus, qui départage les résultats de recherche de même rang.
write('tranche.json', JSON.stringify({ longueurs: definitions.map((d) => d.body.length), renvois: definitions.map((d) => d.citedBy.length) }));
// Et la même tranche dessinée, en masque teintable pour le signet des pages de définition :
// un trait par mot, hauteur en racine carrée de la longueur, étirée à la largeur du bloc.
{
  const max = Math.sqrt(Math.max(...definitions.map((d) => d.body.length)));
  const dPath = definitions.map((d, i) => `M${i} 100V${(100 - Math.max(6, (Math.sqrt(d.body.length) / max) * 100)).toFixed(1)}h.62V100z`).join('');
  write('img/tranche.svg', `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${definitions.length} 100" preserveAspectRatio="none"><path d="${dPath}"/></svg>`);
}

// 8. Sitemap, robots, llms.txt, en-têtes et redirections Cloudflare Pages
const paths = ['/', ...definitions.map((d) => `/${d.slug}/`), ...categories.map((c) => `/categorie/${c.slug}/`),
  ...[...letters].filter(([, d]) => d.length).map(([l]) => `/lettre/${l.toLowerCase()}/`)];
write('sitemap.xml', sitemap(paths));
write('robots.txt', robots());
write('llms.txt', `# ${site.title}\n\n> ${site.subtitle}. ${total} définitions en français, par ${site.author}, sous licence ${site.license}.\n\n## Catégories\n\n${categories.map((c) => `- [${categoryLabel(c.name)}](${url}/categorie/${c.slug}/) : ${c.defs.length} définitions`).join('\n')}\n\n## Livre\n\n- [PDF complet](${url}${site.pdf})\n- [Sources sur GitHub](${site.github})\n`);
write('_headers', headers({ inlineHash }));
write('_redirects', redirects());

const defPages = definitions.filter((d) => fs.existsSync(path.join(out, d.slug, 'index.html'))).length;
let files = 0;
const count = (dir) => { for (const e of fs.readdirSync(dir, { withFileTypes: true })) e.isDirectory() ? count(path.join(dir, e.name)) : files++; };
count(out);
console.log(`Build terminé en ${((Date.now() - started) / 1000).toFixed(1)} s → ${path.relative(process.cwd(), out) || '.'}`);
console.log(`  définitions source : ${total}`);
console.log(`  pages de définition : ${defPages}`);
console.log(`  pages de lettre : ${[...letters].filter(([, d]) => d.length).length}, pages de catégorie : ${categories.length}`);
console.log(`  pages avec formules : ${mathPages}, images copiées : ${images}, renvois non résolus : ${data.unresolved}`);
console.log(`  URL de base : ${url} · sitemap : ${paths.length} adresses · ${files} fichiers`);
if (defPages !== total) {
  console.error('ERREUR : il manque des pages de définition');
  process.exit(1);
}
