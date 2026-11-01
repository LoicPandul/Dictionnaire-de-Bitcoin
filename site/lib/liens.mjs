// Renvois dans le texte : la première occurrence d'un terme du dictionnaire devient un lien
// vers sa définition, avec les données de la carte d'aperçu.
//
// Règles, pour éviter les faux amis :
// - les termes associés de la définition (renvois choisis par l'auteur) sont toujours liés ;
// - les autres termes ne le sont que s'ils sont assez distinctifs : plusieurs mots, un code
//   (chiffre, « _ » ou « - » collé : BIP-0032, OP_RETURN, P2WPKH), un sigle écrit en capitales
//   dans le texte (UTXO, PSBT), ou un mot seul rare dans l'ensemble du dictionnaire ;
// - jamais dans un lien, un code, une formule ou une figure, jamais vers la page elle-même ;
// - un lien par terme, huit liens au plus par définition.
import { escapeHtml as h } from './markdown.mjs';

// Le nom tel que les listes l'affichent (capitales des données, tiret demi-cadratin).
const nom = (t) => String(t).replace(/\b0X([0-9A-F]+)\b/g, '0x$1').replace(/ - /g, '\u00a0– ').replace(/'/g, '’');

const LETTRE = '\\p{L}\\p{N}_';
const MOTS_LIENS = new Set(['de', 'du', 'des', 'la', 'le', 'les', 'en', 'et', 'à', 'au', 'aux', 'd', 'l', 'of', 'the', 'a', 'an', 'to']);
const MAX_LIENS = 8;

const decode = (s) => s.replace(/&#39;/g, "'").replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
const escapeRe = (s) => s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
// Clé de comparaison : minuscules, apostrophes droites, pluriels simples retirés.
const cle = (s) =>
  s.toLocaleLowerCase('fr').replace(/['’`]/g, ' ').trim().split(/\s+/).map((w) => (w.length > 3 && !MOTS_LIENS.has(w) ? w.replace(/[sx]$/, '') : w)).join(' ');
const MOT = /[\p{L}\p{N}]+(?:[_-][\p{L}\p{N}]+)*/gu;

// Formes d'un terme : le titre, chaque partie autour de « - », les termes anglais et français.
function formes(def) {
  const out = new Set();
  const add = (s) => {
    const t = (s || '').trim().replace(/[’`]/g, "'");
    if (t.length < 3 || /^0X[0-9A-F]+$/i.test(t)) return;
    out.add(t);
  };
  add(def.title);
  if (def.title.includes(' - ')) def.title.split(' - ').forEach(add);
  add(def.englishTerm);
  add(def.frenchTerm);
  return [...out];
}

export function createLinker(definitions) {
  // Fréquence de chaque mot seul dans l'ensemble des textes : un mot présent partout
  // (« bitcoin », « transaction ») n'est lié que s'il fait partie des termes associés.
  const corps = definitions.map((d) => d.body.toLocaleLowerCase('fr'));
  const frequence = (mot) => {
    const re = new RegExp(`(?<![${LETTRE}])${escapeRe(mot)}[sx]?(?![${LETTRE}])`, 'u');
    let n = 0;
    for (const c of corps) if (re.test(c)) n++;
    return n / corps.length;
  };

  const parCle = new Map(); // clé -> { def, sigle, distinctif }
  for (const def of definitions) {
    for (const f of formes(def)) {
      const mots = f.split(/\s+/);
      const code = mots.length === 1 && /[\d_]|\p{L}-\p{L}/u.test(f) && f.length >= 4;
      const sigle = mots.length === 1 && /^[A-Z0-9]{3,}$/.test(f) && !code;
      const plusieurs = mots.length >= 2 && f.length >= 8;
      let distinctif = plusieurs || code;
      if (!distinctif && !sigle && mots.length === 1 && f.length >= 5) distinctif = frequence(f.toLocaleLowerCase('fr')) < 0.04;
      const k = cle(f);
      const prev = parCle.get(k);
      if (!prev || def.citedBy.length > prev.def.citedBy.length) parCle.set(k, { def, sigle, distinctif, forme: f });
    }
  }
  // Nombre de mots de la plus longue forme : les n-grammes du texte sont essayés du plus long au plus court.
  const maxMots = Math.max(...[...parCle.keys()].map((k) => k.split(' ').length));

  return function lier(html, page, { label, base = '' }) {
    const associes = new Set(page.related.map((d) => d.slug));
    const deja = new Set([page.slug]);
    let n = 0;
    // On découpe le HTML en balises et en texte ; on ne touche qu'au texte hors <a>, <code>, <pre>, <figure>.
    let interdit = 0;
    html = html.replace(/(?<!<pre>)<code>([^<]{3,60})<\/code>/g, (m, code) => {
      if (n >= MAX_LIENS) return m;
      const trouve = parCle.get(cle(decode(code)));
      if (!trouve || deja.has(trouve.def.slug)) return m;
      deja.add(trouve.def.slug);
      n++;
      const def = trouve.def;
      return `<a class="renvoi-texte renvoi-code" href="${base}/${def.slug}/" data-apercu="${h(def.resume || def.description || '')}" data-apercu-cat="${h(label(def.category))}" data-apercu-nom="${h(nom(def.title))}"><code>${code}</code></a>`;
    });
    return html.replace(/(<[^>]+>)|([^<]+)/g, (m, tag, text) => {
      if (tag) {
        const t = tag.match(/^<(\/?)(a|code|pre|figure|figcaption|h[1-6])\b/i);
        if (t) interdit += t[1] ? -1 : 1;
        return tag;
      }
      if (interdit > 0 || n >= MAX_LIENS) return text;
      const brut = decode(text);
      const mots = [...brut.matchAll(MOT)];
      let out = '';
      let pos = 0;
      for (let i = 0; i < mots.length && n < MAX_LIENS; i++) {
        for (let k = Math.min(maxMots, mots.length - i); k >= 1; k--) {
          const debut = mots[i].index;
          const dernier = mots[i + k - 1];
          const fin = dernier.index + dernier[0].length;
          const extrait = brut.slice(debut, fin);
          // Les mots d'une forme ne sont séparés que par des blancs ou une apostrophe.
          if (k > 1 && /[^\s'’]/u.test(extrait.replace(MOT, ''))) continue;
          const trouve = parCle.get(cle(extrait));
          if (!trouve) continue;
          const { def } = trouve;
          // Déjà lié plus haut : on saute tout le groupe de mots, sans lier un morceau.
          if (deja.has(def.slug)) { i += k - 1; break; }
          const associe = associes.has(def.slug);
          // Un sigle n'est lié que s'il est écrit en capitales dans le texte.
          if (!associe && trouve.sigle && extrait !== extrait.toUpperCase()) continue;
          if (!associe && !trouve.sigle && !trouve.distinctif) continue;
          deja.add(def.slug);
          n++;
          out += h(brut.slice(pos, debut));
          out += `<a class="renvoi-texte" href="${base}/${def.slug}/" data-apercu="${h(def.resume || def.description || '')}" data-apercu-cat="${h(label(def.category))}" data-apercu-nom="${h(nom(def.title))}">${h(extrait)}</a>`;
          pos = fin;
          i += k - 1;
          break;
        }
      }
      return pos ? out + h(brut.slice(pos)) : text;
    });
  };
}
