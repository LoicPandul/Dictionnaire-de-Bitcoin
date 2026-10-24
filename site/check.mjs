// Vérifie le site construit (site/dist) :
//   - une page par définition de definitions/fr ;
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
  (pandulSlugs.length === built.length ? ok : ko)(`${pandulSlugs.length} définitions sur pandul.fr, ${built.length} ici`);
  const missing = pandulSlugs.filter((s) => !fs.existsSync(path.join(dist, s, 'index.html')));
  (missing.length === 0 ? ok : ko)(`slugs de pandul.fr absents ici : ${missing.length}${missing.length ? ` (${missing.slice(0, 5).join(', ')}…)` : ''}`);
  const step = Math.floor(pandulSlugs.length / 10);
  samples.definitions = Array.from({ length: 10 }, (_, i) => pandulSlugs[i * step + 3]);
  const cats = fs.readdirSync(path.join(pandulDir, '_categorie')).map((f) => f.replace(/\.md$/, ''));
  const catMissing = cats.filter((c) => !fs.existsSync(path.join(dist, 'categorie', c, 'index.html')));
  (catMissing.length === 0 ? ok : ko)(`${cats.length} catégories de pandul.fr, absentes ici : ${catMissing.length}`);
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
(locs === sourceSlugs.length + 1 + fs.readdirSync(path.join(dist, 'categorie')).length + fs.readdirSync(path.join(dist, 'lettre')).length ? ok : ko)(`sitemap : ${locs} adresses`);
const sample = fs.readFileSync(path.join(dist, samples.definitions[0], 'index.html'), 'utf8');
(/"@type":"DefinedTerm"/.test(sample) && /"inDefinedTermSet"/.test(sample) ? ok : ko)('JSON-LD DefinedTerm sur les définitions');
(/"@type":"DefinedTermSet"/.test(fs.readFileSync(path.join(dist, 'index.html'), 'utf8')) ? ok : ko)('JSON-LD DefinedTermSet sur l’accueil');
(fs.existsSync(path.join(dist, 'dictionnaire-de-bitcoin.pdf')) ? ok : ko)('PDF téléchargeable');

console.log(failures ? `\n${failures} échec(s).` : '\nTout est conforme.');
process.exit(failures ? 1 : 0);
