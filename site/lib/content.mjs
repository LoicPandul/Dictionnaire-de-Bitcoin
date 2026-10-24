// Lecture des définitions depuis definitions/fr et calcul de tout ce que les pages
// en dérivent : renvois croisés résolus, descriptions, catégories, lettres, voisins.
// Repris du pipeline de pandul.fr (_scripts/sync-dictionnaire.js) pour que les slugs,
// les catégories et les descriptions restent identiques.
import fs from 'node:fs';
import path from 'node:path';

const collator = new Intl.Collator('fr', { sensitivity: 'base', numeric: true });
export const compareFr = (a, b) => collator.compare(a, b);

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

export function loadDictionary(repoRoot) {
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

      const def = {
        uuid: meta.uuid,
        title: meta.title,
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
      };
      if (!def.description) warnings.push(`description omise : ${def.slug}`);
      definitions.push(def);
      if (def.uuid) byUuid.set(def.uuid, def);
    }
  }

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
  definitions.sort((a, b) => compareFr(a.title, b.title));

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
    letters: lettersMap,
    warnings,
    unresolved,
    sanitizationHits,
  };
}
