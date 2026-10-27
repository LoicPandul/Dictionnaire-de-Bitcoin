// Lecture des définitions depuis definitions/fr et calcul de tout ce que les pages
// en dérivent : renvois croisés résolus, descriptions, catégories, lettres, voisins.
// Repris du pipeline de pandul.fr (_scripts/sync-dictionnaire.js) pour que les slugs,
// les catégories et les descriptions restent identiques.
import fs from 'node:fs';
import path from 'node:path';
import YAML from 'yaml';

const collator = new Intl.Collator('fr', { sensitivity: 'base', numeric: true });
export const compareFr = (a, b) => collator.compare(a, b);
const collatorEn = new Intl.Collator('en', { sensitivity: 'base', numeric: true });

// Traductions (definitions/<langue>/, docs/structure.md) : un dossier par entrée, nommé d'après
// son slug dans la langue (definitions/en/b/block/), avec definition.md, courte.md et un
// metadata.yaml qui porte l'uuid de l'entrée française, le titre et le slug traduits.
// L'entrée est retrouvée par son uuid, sinon par son source_slug ou le nom du dossier.
// Rien n'est écrit en dur : les entrées sans dossier traduit restent en français.
export function loadTranslations(repoRoot, lang) {
  const root = path.join(repoRoot, 'definitions', lang);
  const found = new Map();
  if (!fs.existsSync(root)) return found;
  const walk = (dir, depth) => {
    for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
      if (!e.isDirectory()) continue;
      const d = path.join(dir, e.name);
      const md = path.join(d, 'definition.md');
      if (fs.existsSync(md)) {
        const metaPath = path.join(d, 'metadata.yaml');
        const meta = fs.existsSync(metaPath) ? parseMetadata(fs.readFileSync(metaPath, 'utf8')) : {};
        const courtePath = path.join(d, 'courte.md');
        const tr = {
          dir: d,
          slug: meta.slug || e.name,
          sourcePath: path.relative(repoRoot, md),
          body: fs.readFileSync(md, 'utf8').replace(/\r\n/g, '\n'),
          courte: fs.existsSync(courtePath) ? fs.readFileSync(courtePath, 'utf8').trim() : '',
          meta,
        };
        if (!tr.body.trim()) continue;
        for (const k of [meta.uuid, meta.source_slug, e.name]) if (k && !found.has(k)) found.set(k, tr);
      } else if (depth < 2) walk(d, depth + 1);
    }
  };
  walk(root, 0);
  return found;
}

// Langues traduites : les dossiers de definitions/ autres que le français. Pour chacune, les
// entrées françaises exclues (templates/languages.yaml, translations.<langue>.exclude) : sans
// objet dans cette langue, elles n'y ont pas de page.
function loadLanguages(repoRoot) {
  const root = path.join(repoRoot, 'definitions');
  const codes = fs.readdirSync(root, { withFileTypes: true }).filter((e) => e.isDirectory() && e.name !== 'fr').map((e) => e.name);
  const f = path.join(repoRoot, 'templates', 'languages.yaml');
  const conf = fs.existsSync(f) ? YAML.parse(fs.readFileSync(f, 'utf8'))?.translations || {} : {};
  return codes.map((code) => ({ code, traductions: loadTranslations(repoRoot, code), exclues: new Set(conf[code]?.exclude || []) }));
}

export function slugify(str) {
  return str
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-|-$/g, '');
}

// YAML minimaliste du dépôt : clés simples, listes de chaînes, liste d'assets {filename}.
export function parseMetadata(content) {
  const result = {};
  let currentKey = null;
  let currentList = null;
  for (const line of content.replace(/\r\n/g, '\n').split('\n')) {
    const keyMatch = line.match(/^([a-z_]+):\s*(.*)$/);
    if (keyMatch) {
      const [, key, raw] = keyMatch;
      const value = raw.trim();
      if (value === '') {
        currentKey = key;
        currentList = [];
        result[key] = currentList;
      } else {
        result[key] = value.replace(/^"(.*)"$/, '$1');
        currentKey = null;
        currentList = null;
      }
      continue;
    }
    if (currentKey && currentList) {
      // Champ supplémentaire d'un asset, sous son « - filename: » (credit: "…").
      const champ = currentKey === 'assets' && line.match(/^\s{4}([a-z_]+):\s*(.*)$/);
      if (champ && currentList.length) {
        currentList.at(-1)[champ[1]] = champ[2].trim().replace(/^"(.*)"$/, '$1').replace(/\\"/g, '"');
        continue;
      }
      const item = line.match(/^\s{2}-\s+(.*)$/);
      if (!item) continue;
      const value = item[1].trim();
      if (currentKey === 'assets') {
        const file = value.match(/^filename:\s*"?([^"]+)"?$/);
        if (file) currentList.push({ filename: file[1] });
      } else {
        currentList.push(value.replace(/^"(.*)"$/, '$1'));
      }
    }
  }
  return result;
}

// Passe 10 de pandul.fr : retire du corps les motifs d'injection de prompt.
const SANITIZATION_PATTERNS = [
  { name: 'html_comment', regex: /<!--[\s\S]*?-->/g },
  { name: 'ignore_instructions', regex: /\b(ignore|disregard|forget)\s+(previous|the\s+above|all)\s+(instructions|prompts)\b/gi },
  { name: 'role_marker', regex: /(^|\n)\s*(system|assistant|user)\s*:/gi },
  { name: 'identity_affirmation', regex: /\b(you\s+are\s+(now|a|an|\w+)|act\s+as\s+\w+|pretend\s+to\s+be|roleplay\s+as)\b/gi },
];

export function sanitizeBody(body) {
  const hits = [];
  let sanitized = body;
  for (const { name, regex } of SANITIZATION_PATTERNS) {
    sanitized = sanitized.replace(regex, (match) => {
      hits.push({ pattern: name, match: match.slice(0, 60) });
      return '';
    });
  }
  return { sanitized, hits };
}

// Descriptions écrites à la main par Loïc pour les définitions trop courtes (pandul.fr).
const STUB_DESCRIPTIONS = {
  'cln-c-lightning': '« CLN » désigne aujourd\'hui Core-Lightning. « C-Lightning » est l\'ancien nom de cette implémentation Lightning Network.',
  'crypter': '« Crypter » est un anglicisme qui n\'existe pas en français. Le terme correct pour parler du chiffrement de données est « chiffrer ».',
  'op-1add-0x8b': 'OP_1ADD (0x8b) est un opcode Bitcoin Script qui ajoute 1 à la valeur entière située en haut de la pile d\'exécution.',
  'op-1sub-0x8c': 'OP_1SUB (0x8c) est un opcode Bitcoin Script qui soustrait 1 à la valeur entière située en haut de la pile d\'exécution.',
  'op-false-0x00': 'OP_FALSE (0x00) est un opcode Bitcoin Script identique à OP_0 — il empile une valeur nulle (interprétée comme « faux ») sur la pile.',
  'taro': 'Taro est l\'ancien nom du protocole Taproot Assets Protocol, qui permet d\'émettre des actifs natifs sur Bitcoin via Taproot.',
  'zprv': 'ZPRV est le préfixe d\'une clé privée étendue utilisée pour dériver les comptes SegWit V0 (P2WPKH natif) sur Bitcoin.',
};

export function stripMarkdown(content) {
  return content
    .replace(/\$\$[\s\S]*?\$\$/g, '')
    .replace(/\$[^$\n]+?\$/g, '')
    .replace(/```[\s\S]*?```/g, '')
    .replace(/!\[[^\]]*\]\([^)]+\)/g, '')
    .replace(/\[([^\]]+)\]\([^)]+\)/g, '$1')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*\n]+)\*/g, '$1')
    .replace(/`([^`\n]+)`/g, '$1')
    .replace(/^>\s*/gm, '')
    .replace(/^\|.*\|$/gm, '')
    .replace(/^[\s]*[-*]\s+/gm, '')
    .replace(/\s+/g, ' ')
    .trim();
}

// Description de 70 à 155 caractères tirée du corps (algorithme D-02 de pandul.fr).
export function computeMetaDescription(content) {
  const stripped = stripMarkdown(content);
  if (stripped.length < 20) return null;
  const sentences = stripped.split(/(?<=[.!?])[\s ]+(?=[A-ZÀ-Ý])/);
  let result = sentences[0].trim();
  if (result.length >= 70 && result.length <= 155) return result;
  let i = 1;
  while (result.length < 70 && i < sentences.length) {
    result = `${result} ${sentences[i].trim()}`.trim();
    i++;
  }
  if (result.length > 155) {
    const cut = result.lastIndexOf(' ', 152);
    if (cut < 50) return null;
    result = `${result.slice(0, cut).replace(/[.,;:!?]+$/, '')}…`;
  }
  return result.length < 70 ? null : result;
}

// Les commentaires de templates/categories.yaml décrivent chaque catégorie.
export function loadCategoryNotes(file) {
  const notes = new Map();
  let buffer = [];
  for (const line of fs.readFileSync(file, 'utf8').split('\n')) {
    const comment = line.match(/^\s+#\s?(.*)$/);
    const item = line.match(/^\s+-\s+(.+)$/);
    if (comment) buffer.push(comment[1].trim());
    else if (item) {
      notes.set(item[1].trim(), buffer.join(' ').replace(/\s+/g, ' ').trim());
      buffer = [];
    } else if (!line.trim()) buffer = [];
  }
  return notes;
}

// reserves : premiers segments d'adresse déjà pris dans la langue (category, letter…).
export function loadDictionary(repoRoot, { lang = 'fr', reserves = [] } = {}) {
  const langues = loadLanguages(repoRoot);
  const ici = langues.find((x) => x.code === lang);
  const compare = lang === 'fr' ? compareFr : (a, b) => collatorEn.compare(a, b);
  const sourceDir = path.join(repoRoot, 'definitions', 'fr');
  const warnings = [];
  const sanitizationHits = [];
  const definitions = [];
  const byUuid = new Map();

  const letters = fs.readdirSync(sourceDir).filter((e) => /^[a-z]$/.test(e)).sort();
  for (const letterDir of letters) {
    const dir = path.join(sourceDir, letterDir);
    for (const entry of fs.readdirSync(dir).sort()) {
      const defDir = path.join(dir, entry);
      if (!fs.statSync(defDir).isDirectory()) continue;
      const metaPath = path.join(defDir, 'metadata.yaml');
      if (!fs.existsSync(metaPath)) {
        warnings.push(`metadata.yaml manquant : ${letterDir}/${entry}`);
        continue;
      }
      const meta = parseMetadata(fs.readFileSync(metaPath, 'utf8'));
      const mdPath = path.join(defDir, 'definition.md');
      const raw = fs.existsSync(mdPath) ? fs.readFileSync(mdPath, 'utf8').replace(/\r\n/g, '\n') : '';
      if (!raw) warnings.push(`definition.md manquant ou vide : ${meta.slug}`);
      const { sanitized, hits } = sanitizeBody(raw);
      for (const hit of hits) sanitizationHits.push({ slug: meta.slug, ...hit });

      const courtePath = path.join(defDir, 'courte.md');
      const courte = fs.existsSync(courtePath) ? fs.readFileSync(courtePath, 'utf8').trim() : '';
      const def = {
        uuid: meta.uuid,
        title: meta.title,
        titleFr: meta.title,
        slug: meta.slug,
        category: meta.category || 'SANS CATÉGORIE',
        categorySlug: slugify(meta.category || 'sans categorie'),
        englishTerm: meta.english_term || null,
        frenchTerm: meta.french_term || null,
        letter: meta.slug[0].toUpperCase(),
        assets: Array.isArray(meta.assets) ? meta.assets : [],
        crossRefUuids: Array.isArray(meta.cross_references) ? meta.cross_references : [],
        sourceDir: defDir,
        sourcePath: path.relative(repoRoot, mdPath),
        body: sanitized,
        description: computeMetaDescription(raw) || STUB_DESCRIPTIONS[meta.slug] || null,
        // La version courte du livre (courte.md) : le résumé des listes, des cartes d'aperçu et de la recherche.
        courte: courte ? stripMarkdown(courte) : null,
        lang: 'fr',
      };
      // L'adresse de l'entrée dans chaque langue : son slug traduit, le slug français tant
      // qu'elle n'est pas traduite (la page montre alors le français), null si elle est exclue.
      def.slugs = { fr: meta.slug };
      for (const x of langues) {
        const t = x.traductions.get(meta.uuid) || x.traductions.get(meta.slug) || x.traductions.get(entry);
        def.slugs[x.code] = x.exclues.has(meta.slug) ? null : t ? t.slug : meta.slug;
      }
      def.mdDir = defDir;
      if (lang !== 'fr' && !def.slugs[lang]) continue;
      const tr = ici && (ici.traductions.get(meta.uuid) || ici.traductions.get(meta.slug) || ici.traductions.get(entry));
      if (tr) {
        def.slug = def.slugs[lang];
        def.mdDir = tr.dir;
        def.lang = lang;
        def.title = tr.meta.title || def.title;
        def.englishTerm = tr.meta.english_term || def.englishTerm;
        def.frenchTerm = tr.meta.french_term || (def.title !== def.titleFr ? def.titleFr : def.frenchTerm);
        def.sourcePath = tr.sourcePath;
        def.body = sanitizeBody(tr.body).sanitized;
        def.description = computeMetaDescription(tr.body) || def.description;
        def.courte = tr.courte ? stripMarkdown(tr.courte) : null;
        const initiale = def.title.normalize('NFD').replace(/[^A-Za-z]/g, '')[0];
        if (initiale) def.letter = initiale.toUpperCase();
      }
      def.resume = def.courte || def.description;
      if (!def.description) warnings.push(`description omise : ${def.slug}`);
      definitions.push(def);
      if (def.uuid) byUuid.set(def.uuid, def);
    }
  }

  // Deux entrées ne partagent jamais une adresse : un slug traduit qui tombe sur le slug d'une
  // autre entrée, ou sur un segment réservé de la langue, est signalé (le build échoue).
  const prises = new Map(reserves.map((r) => [r, null]));
  for (const def of definitions) {
    if (prises.has(def.slug)) warnings.push(`slug en double (${lang}) : ${def.slug} (${def.slugs.fr} et ${prises.get(def.slug)?.slugs.fr || 'adresse réservée'})`);
    else prises.set(def.slug, def);
  }
  const collisions = warnings.filter((w) => w.startsWith('slug en double'));

  let unresolved = 0;
  for (const def of definitions) {
    def.related = [];
    for (const uuid of def.crossRefUuids) {
      const target = byUuid.get(uuid);
      if (target) def.related.push(target);
      else {
        unresolved++;
        warnings.push(`renvoi non résolu ${uuid} dans ${def.slug}`);
      }
    }
  }

  // Ordre de lecture : alphabétique français sur le titre, comme pandul.fr.
  definitions.sort((a, b) => compare(a.title, b.title));
  // Rang dans le livre et voisins alphabétiques : les mots-repères des pages de définition.
  definitions.forEach((def, i) => {
    def.n = i + 1;
    def.alphaPrev = definitions[i - 1] || null;
    def.alphaNext = definitions[i + 1] || null;
  });

  const categories = new Map();
  for (const def of definitions) {
    if (!categories.has(def.category)) {
      categories.set(def.category, { name: def.category, slug: def.categorySlug, defs: [] });
    }
    categories.get(def.category).defs.push(def);
  }
  for (const cat of categories.values()) {
    cat.defs.forEach((def, i) => {
      def.prev = cat.defs[i - 1] || null;
      def.next = cat.defs[i + 1] || null;
    });
  }

  const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  const lettersMap = new Map(alphabet.map((l) => [l, []]));
  for (const def of definitions) lettersMap.get(def.letter)?.push(def);

  // Qui renvoie vers moi : utile pour « cité dans ».
  for (const def of definitions) def.citedBy = [];
  for (const def of definitions) for (const target of def.related) target.citedBy.push(def);

  return {
    definitions,
    categories: [...categories.values()].sort((a, b) => compareFr(a.name, b.name)),
    translated: definitions.filter((d) => d.lang !== 'fr').length,
    collisions,
    letters: lettersMap,
    warnings,
    unresolved,
    sanitizationHits,
  };
}
