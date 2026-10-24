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
import { definitionPage, letterPage, categoryPage, homePage, notFoundPage, categoryLabel } from './lib/templates.mjs';
import { homeJsonLd, definitionJsonLd, listJsonLd, sitemap, robots } from './lib/seo.mjs';

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
const copyDir = (from, to) => fs.cpSync(from, path.join(out, to), { recursive: true });

// 1. Données
const data = loadDictionary(repoRoot);
const { definitions, categories, letters } = data;
const notes = loadCategoryNotes(path.join(repoRoot, 'templates', 'categories.yaml'));
for (const w of data.warnings) console.warn(`WARN ${w}`);
if (data.sanitizationHits.length) {
  for (const hit of data.sanitizationHits) console.log(`[assainissement] ${hit.slug} : ${hit.pattern} « ${hit.match} »`);
}

// 2. Sortie propre
fs.rmSync(out, { recursive: true, force: true });
fs.mkdirSync(out, { recursive: true });

// 3. Fichiers statiques, avec une version courte pour casser le cache du CSS et du JS
copyDir(path.join(here, 'static'), '.');
const hash = crypto.createHash('sha1');
for (const f of ['css/site.css', 'js/site.js']) hash.update(fs.readFileSync(path.join(here, 'static', f)));
const assetVersion = hash.digest('hex').slice(0, 8);
fs.mkdirSync(path.join(out, 'katex'), { recursive: true });
fs.copyFileSync(path.join(here, 'node_modules/katex/dist/katex.min.css'), path.join(out, 'katex/katex.min.css'));
fs.mkdirSync(path.join(out, 'katex/fonts'), { recursive: true });
for (const f of fs.readdirSync(path.join(here, 'node_modules/katex/dist/fonts'))) {
  if (f.endsWith('.woff2')) fs.copyFileSync(path.join(here, 'node_modules/katex/dist/fonts', f), path.join(out, 'katex/fonts', f));
}
fs.copyFileSync(path.join(repoRoot, 'dictionnaire-de-bitcoin.pdf'), path.join(out, site.pdf.slice(1)));
write('.nojekyll', '');
// GitHub Pages lit le domaine dans CNAME ; rien tant que l'adresse provisoire est en place.
const host = new URL(url).hostname;
if (!host.endsWith('.example')) write('CNAME', `${host}\n`);

// 4. Définitions
const render = createRenderer();
let mathPages = 0;
let images = 0;
for (const def of definitions) {
  const { html, math } = render(def);
  if (math) mathPages++;
  write(`${def.slug}/index.html`, definitionPage(def, { html, math, assetVersion, jsonLd: definitionJsonLd(def), total: definitions.length }));
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
  write(`lettre/${letter.toLowerCase()}/index.html`, letterPage(letter, defs, letters, { assetVersion, jsonLd: listJsonLd({ path: p, name: `Lettre ${letter}`, defs }) }));
}
for (const cat of categories) {
  const p = `/categorie/${cat.slug}/`;
  write(`categorie/${cat.slug}/index.html`, categoryPage(cat, notes.get(cat.name), { assetVersion, jsonLd: listJsonLd({ path: p, name: categoryLabel(cat.name), defs: cat.defs }) }));
}

// 6. Accueil : terme du jour au moment du build (le script le remplace par celui du jour)
const dayIndex = Math.floor(Date.now() / 86400000) % definitions.length;
const stats = {
  links: definitions.reduce((n, d) => n + d.related.length, 0),
  english: definitions.filter((d) => d.englishTerm).length,
  math: mathPages,
};
const credits = 'Gravures : Encyclopédie de Diderot et d’Alembert, planches de Goussier et Bénard, domaine public, via Wikimedia Commons · Film : Learning to Set Type, 1959, domaine public, via Internet Archive';
write('index.html', homePage({ definitions, categories, letters, featured: definitions[dayIndex], stats }, {
  assetVersion,
  credits,
  jsonLd: homeJsonLd({ total: definitions.length, description: `${definitions.length} définitions du vocabulaire technique de Bitcoin, par Loïc Morel.` }),
}));
write('404.html', notFoundPage({ assetVersion }));

// 7. Index de recherche : une ligne compacte par terme, chargée à la demande
const catIndex = categories.map((c) => [categoryLabel(c.name), c.slug]);
const catPos = new Map(categories.map((c, i) => [c.name, i]));
const index = {
  categories: catIndex,
  terms: definitions.map((d) => [d.title, d.slug, catPos.get(d.category), d.englishTerm || d.frenchTerm || '', d.description || '']),
};
write('recherche.json', JSON.stringify(index));

// 8. Sitemap, robots, llms.txt
const paths = ['/', ...definitions.map((d) => `/${d.slug}/`), ...categories.map((c) => `/categorie/${c.slug}/`),
  ...[...letters].filter(([, d]) => d.length).map(([l]) => `/lettre/${l.toLowerCase()}/`)];
write('sitemap.xml', sitemap(paths));
write('robots.txt', robots());
write('llms.txt', `# ${site.title}\n\n> ${site.subtitle}. ${definitions.length} définitions en français, par ${site.author}, sous licence ${site.license}.\n\n## Catégories\n\n${categories.map((c) => `- [${categoryLabel(c.name)}](${url}/categorie/${c.slug}/) : ${c.defs.length} définitions`).join('\n')}\n\n## Livre\n\n- [PDF complet](${url}${site.pdf})\n- [Sources sur GitHub](${site.github})\n`);

const pages = fs.readdirSync(out, { withFileTypes: true }).filter((e) => e.isDirectory() && fs.existsSync(path.join(out, e.name, 'index.html')));
const defPages = definitions.filter((d) => fs.existsSync(path.join(out, d.slug, 'index.html'))).length;
console.log(`Build terminé en ${((Date.now() - started) / 1000).toFixed(1)} s → ${path.relative(process.cwd(), out) || '.'}`);
console.log(`  définitions source : ${definitions.length}`);
console.log(`  pages de définition : ${defPages}`);
console.log(`  pages de lettre : ${[...letters].filter(([, d]) => d.length).length}, pages de catégorie : ${categories.length}`);
console.log(`  pages avec formules : ${mathPages}, images copiées : ${images}, renvois non résolus : ${data.unresolved}`);
console.log(`  URL de base : ${url} · sitemap : ${paths.length} adresses · ${pages.length} dossiers de premier niveau`);
if (defPages !== definitions.length) {
  console.error('ERREUR : il manque des pages de définition');
  process.exit(1);
}
