// Vérifie le site construit (site/dist) :
//   - une page par définition de definitions/fr, en français et sous /en/ ;
//   - aucun lien interne cassé (fichier ou ancre) dans toutes les pages ;
//   - le contrat d'URL attendu par les redirections de pandul.fr :
//       /<slug>/, /categorie/<slug>/, /lettre/<lettre>/ ;
//   - si le dépôt pandul.fr est présent, mêmes slugs que ses collections Jekyll.
//
//   node check.mjs [--pandul ~/Documents/GitHub/pandul.fr] [--base http://hôte:port]
// Avec --base, chaque adresse vérifiée est aussi demandée au serveur (code 200 attendu).
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { url } from './config.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const dist = path.join(here, 'dist');
const arg = (name, fallback) => {
  const i = process.argv.indexOf(name);
  return i > -1 ? process.argv[i + 1] : fallback;
};
const pandulDir = arg('--pandul', path.join(os.homedir(), 'Documents/GitHub/pandul.fr')).replace(/^~/, os.homedir());
const base = arg('--base', null);

let failures = 0;
const ok = (msg) => console.log(`  ok   ${msg}`);
const ko = (msg) => {
  failures++;
  console.log(`  ÉCHEC ${msg}`);
};

if (!fs.existsSync(path.join(dist, 'index.html'))) {
  console.error('dist/ est vide : lancez d’abord « node build.mjs ».');
  process.exit(1);
}

// 1. Une page par définition
const sourceDir = path.join(here, '..', 'definitions', 'fr');
const sourceSlugs = [];
for (const letter of fs.readdirSync(sourceDir).filter((d) => /^[a-z]$/.test(d))) {
  for (const entry of fs.readdirSync(path.join(sourceDir, letter))) {
    const meta = path.join(sourceDir, letter, entry, 'metadata.yaml');
    if (fs.existsSync(meta)) sourceSlugs.push(fs.readFileSync(meta, 'utf8').match(/^slug:\s*"?([^"\n]+)"?/m)[1]);
  }
}
const built = sourceSlugs.filter((s) => fs.existsSync(path.join(dist, s, 'index.html')));
console.log('Pages de définition');
(built.length === sourceSlugs.length ? ok : ko)(`${built.length} pages pour ${sourceSlugs.length} définitions dans definitions/fr`);

// 2. Comparaison avec pandul.fr
const samples = { definitions: [], categories: [], letters: [] };
if (fs.existsSync(path.join(pandulDir, '_dictionnaire'))) {
  console.log(`Comparaison avec ${pandulDir}`);
  const pandulSlugs = fs.readdirSync(path.join(pandulDir, '_dictionnaire')).filter((f) => f.endsWith('.md')).map((f) => f.replace(/\.md$/, '')).sort();
  (built.length >= pandulSlugs.length ? ok : ko)(`${pandulSlugs.length} définitions sur pandul.fr, ${built.length} ici`);
  const missing = pandulSlugs.filter((s) => !fs.existsSync(path.join(dist, s, 'index.html')));
  (missing.length === 0 ? ok : ko)(`slugs de pandul.fr absents ici : ${missing.length}${missing.length ? ` (${missing.slice(0, 5).join(', ')}…)` : ''}`);
  const step = Math.floor(pandulSlugs.length / 10);
  samples.definitions = Array.from({ length: 10 }, (_, i) => pandulSlugs[i * step + 3]);
  const cats = fs.readdirSync(path.join(pandulDir, '_categorie')).map((f) => f.replace(/\.md$/, ''));
  // Une catégorie renommée en 2027 compte si _redirects la mène à sa remplaçante.
  const redirs = fs.readFileSync(path.join(dist, '_redirects'), 'utf8');
  const catMissing = cats.filter((c) => !fs.existsSync(path.join(dist, 'categorie', c, 'index.html')));
  const catRedirigees = catMissing.filter((c) => new RegExp(`^/categorie/${c}/ /categorie/[a-z0-9-]+/ 301$`, 'm').test(redirs));
  (catMissing.length === catRedirigees.length ? ok : ko)(`${cats.length} catégories de pandul.fr : ${cats.length - catMissing.length} présentes, ${catRedirigees.length} redirigées (${catRedirigees.join(', ') || 'aucune'}), ${catMissing.length - catRedirigees.length} perdues`);
  const lets = fs.readdirSync(path.join(pandulDir, '_lettre')).map((f) => f.replace(/\.md$/, ''));
  const letMissing = lets.filter((l) => !fs.existsSync(path.join(dist, 'lettre', l, 'index.html')));
  (letMissing.length === 0 ? ok : ko)(`${lets.length} lettres de pandul.fr, absentes ici : ${letMissing.length}`);
  samples.categories = [cats.sort()[0], 'lightning-network'];
  samples.letters = ['a', 'q'];
} else {
  console.log(`(pandul.fr introuvable dans ${pandulDir} : comparaison sautée)`);
  samples.definitions = sourceSlugs.slice(0, 10);
  samples.categories = ['bip'];
  samples.letters = ['a'];
}

// 3. Contrat d'URL sur un échantillon : fichier présent et adresse canonique exacte
console.log('Contrat d’URL (échantillon)');
const paths = [
  '/',
  ...samples.definitions.map((s) => `/${s}/`),
  ...samples.categories.map((c) => `/categorie/${c}/`),
  ...samples.letters.map((l) => `/lettre/${l}/`),
];
for (const p of paths) {
  const file = path.join(dist, p, 'index.html');
  if (!fs.existsSync(file)) {
    ko(`${p} : fichier absent`);
    continue;
  }
  const canonical = fs.readFileSync(file, 'utf8').match(/<link rel="canonical" href="([^"]+)">/)?.[1];
  if (canonical !== `${url}${p}`) {
    ko(`${p} : canonique ${canonical}`);
    continue;
  }
  if (base) {
    const res = await fetch(new URL(p, base));
    if (res.status !== 200) {
      ko(`${p} : HTTP ${res.status}`);
      continue;
    }
    ok(`${p} → ${canonical} · HTTP 200`);
  } else ok(`${p} → ${canonical}`);
}

// 4. Sitemap et données structurées
const sitemap = fs.readFileSync(path.join(dist, 'sitemap.xml'), 'utf8');
const locs = (sitemap.match(/<loc>/g) || []).length;
const absentsSitemap = sourceSlugs.filter((s) => !sitemap.includes(`<loc>${url}/${s}/</loc>`));
(absentsSitemap.length === 0 ? ok : ko)(`sitemap : ${locs} adresses, toutes les définitions françaises comprises`);
const sample = fs.readFileSync(path.join(dist, samples.definitions[0], 'index.html'), 'utf8');
(/"@type":"DefinedTerm"/.test(sample) && /"inDefinedTermSet"/.test(sample) ? ok : ko)('JSON-LD DefinedTerm sur les définitions');
(/"@type":"DefinedTermSet"/.test(fs.readFileSync(path.join(dist, 'index.html'), 'utf8')) ? ok : ko)('JSON-LD DefinedTermSet sur l’accueil');
(fs.existsSync(path.join(dist, 'dictionnaire-de-bitcoin.pdf')) ? ok : ko)('PDF téléchargeable');

// 5. Anglais, chronologie, spécifications
console.log('Édition 2027 et anglais');
const enBuilt = sourceSlugs.filter((s) => fs.existsSync(path.join(dist, 'en', s, 'index.html')));
(enBuilt.length === sourceSlugs.length ? ok : ko)(`${enBuilt.length} pages sous /en/ pour ${sourceSlugs.length} définitions`);
for (const p of ['/en/', '/chronologie/', '/en/timeline/', '/specifications/', '/en/specifications/', '/partie/personnes/', '/en/part/people/', '/en/404.html']) {
  const f = p.endsWith('.html') ? path.join(dist, p) : path.join(dist, p, 'index.html');
  (fs.existsSync(f) ? ok : ko)(`${p}`);
}
const enHome = fs.readFileSync(path.join(dist, 'en', 'index.html'), 'utf8');
(/<html lang="en"/.test(enHome) && /hreflang="fr"/.test(enHome) ? ok : ko)('accueil anglais : lang="en" et liens hreflang');

// Crédits des images de tiers (assets[].credit dans metadata.yaml) : affichés sous l'image, en français et en anglais.
const esc = (x) => x.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
const credits = [];
for (const letter of fs.readdirSync(sourceDir).filter((d) => /^[a-z]$/.test(d))) {
  for (const entry of fs.readdirSync(path.join(sourceDir, letter))) {
    const meta = path.join(sourceDir, letter, entry, 'metadata.yaml');
    if (!fs.existsSync(meta)) continue;
    const txt = fs.readFileSync(meta, 'utf8');
    const slug = txt.match(/^slug:\s*"?([^"\n]+)"?/m)[1];
    for (const m of txt.matchAll(/^\s{4}credit:\s*"(.*)"\s*$/gm)) credits.push([slug, m[1].replace(/\\"/g, '"')]);
  }
}
// Le site compose les apostrophes typographiques (’) : on compare apostrophes confondues.
const apos = (x) => x.replace(/['’]/g, '’');
const sansCredit = credits.filter(([slug, c]) => ['', 'en'].some((l) => {
  const html = apos(fs.readFileSync(path.join(dist, l, slug, 'index.html'), 'utf8'));
  return !html.includes(apos(`class="figure-credit">`)) || !html.includes(apos(`<span lang="fr">${esc(c)}</span>`));
}));
(sansCredit.length === 0 ? ok : ko)(`${credits.length} image(s) créditée(s), crédit affiché sous l'image en français et en anglais${sansCredit.length ? ` ; manquant : ${sansCredit.map(([s]) => s).join(', ')}` : ''}`);

// 6. Liens internes : chaque href ou src qui commence par « / » mène à un fichier, et son ancre existe.
console.log('Liens internes');
const pages = [];
const walk = (dir) => { for (const e of fs.readdirSync(dir, { withFileTypes: true })) { const f = path.join(dir, e.name); if (e.isDirectory()) walk(f); else if (e.name.endsWith('.html')) pages.push(f); } };
walk(dist);
const idsCache = new Map();
const idsDe = (file) => {
  if (!idsCache.has(file)) idsCache.set(file, new Set([...fs.readFileSync(file, 'utf8').matchAll(/\sid="([^"]+)"/g)].map((m) => m[1])));
  return idsCache.get(file);
};
const cible = (p) => {
  const f = path.join(dist, decodeURIComponent(p));
  if (p.endsWith('/')) return fs.existsSync(path.join(f, 'index.html')) ? path.join(f, 'index.html') : null;
  return fs.existsSync(f) && fs.statSync(f).isFile() ? f : null;
};
const casses = new Map();
let nLiens = 0;
for (const page of pages) {
  const html = fs.readFileSync(page, 'utf8');
  for (const m of html.matchAll(/\s(?:href|src)="([^"]+)"/g)) {
    const v = m[1].replace(/&amp;/g, '&');
    if (v.startsWith('//') || !(v.startsWith('/') || v.startsWith('#'))) continue;
    nLiens++;
    const [chemin, ancre] = v.split('#');
    const fichier = chemin ? cible(chemin.split('?')[0]) : page;
    let erreur = null;
    if (!fichier) erreur = 'cible absente';
    else if (ancre && /\.(html|svg)$/.test(fichier) && !idsDe(fichier).has(decodeURIComponent(ancre))) erreur = 'ancre absente';
    if (erreur) {
      const k = `${v} (${erreur})`;
      if (!casses.has(k)) casses.set(k, path.relative(dist, page));
    }
  }
}
(casses.size === 0 ? ok : ko)(`${nLiens} liens internes dans ${pages.length} pages, ${casses.size} cassé(s)`);
for (const [k, p] of [...casses].slice(0, 15)) console.log(`       ${k} dans ${p}`);

console.log(failures ? `\n${failures} échec(s).` : '\nTout est conforme.');
process.exit(failures ? 1 : 0);
