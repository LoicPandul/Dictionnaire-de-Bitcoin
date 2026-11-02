// Markdown des définitions vers HTML. Les formules LaTeX sont composées au build par
// KaTeX : le lecteur ne télécharge aucun script pour les voir.
import fs from 'node:fs';
import path from 'node:path';
import { Marked, Renderer } from 'marked';
import katex from 'katex';

export const escapeHtml = (s = '') =>
  String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

// Largeur et hauteur d'un PNG, lues dans son en-tête IHDR.
function pngSize(file) {
  try {
    const buf = fs.readFileSync(file);
    if (buf.toString('ascii', 12, 16) !== 'IHDR') return null;
    return { width: buf.readUInt32BE(16), height: buf.readUInt32BE(20) };
  } catch {
    return null;
  }
}

function renderMath(tex, displayMode) {
  return katex.renderToString(tex.trim(), {
    displayMode,
    throwOnError: false,
    strict: 'ignore',
    output: 'htmlAndMathml',
  });
}

// La ponctuation qui suit une formule entre dans la dernière boîte de KaTeX : elle ne peut plus partir seule
// en début de ligne, et la formule garde ses propres points de coupure. Une copie masquée la garde lisible
// pour les lecteurs d'écran (le rendu visuel de KaTeX leur est caché).
const FIN_KATEX = '</span></span></span>';
function collerPonct(html, ponct) {
  if (!ponct || !html.endsWith(FIN_KATEX)) return html + (ponct || '');
  return `${html.slice(0, -FIN_KATEX.length)}<span class="formule-ponct">${ponct}</span>${FIN_KATEX}<span class="masque">${ponct}</span>`;
}

// Remplace les formules par des jetons inertes, hors des blocs et spans de code.
function protectMath(source) {
  const formulas = [];
  const token = (html) => `⁣M${formulas.push(html) - 1}⁣`;
  const parts = source.split(/(```[\s\S]*?```|`[^`\n]*`)/);
  const out = parts.map((part, i) => {
    if (i % 2 === 1) return part;
    return part
      .replace(/\$\$([\s\S]+?)\$\$/g, (_, tex) => token(renderMath(tex, true)))
      .replace(/(?<![\\$])\$([^$\n]+?)\$([,.;:!?)\]]+)?/g, (_, tex, ponct) => token(collerPonct(renderMath(tex, false), ponct)));
  });
  return { text: out.join(''), formulas };
}

const restoreMath = (html, formulas) =>
  html.replace(/⁣M(\d+)⁣/g, (_, i) => formulas[Number(i)]);

// Apostrophes typographiques dans le texte (« l’UTXO »), jamais dans le code ni les blocs de code.
const apostrophes = (html) =>
  html
    .split(/(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>)/)
    .map((part, i) => (i % 2 ? part : part.replace(/&#39;/g, '’').replace(/(^|>)([^<]*)/g, (m, a, t) => a + t.replace(/'/g, '’'))))
    .join('');

// Espaces et coupures, sur le texte seul (ni balises, ni code) : une référence « BIP-0347 » ne se coupe pas à
// son trait d'union, les groupes de chiffres restent ensemble, et en français la ponctuation haute (; : ! ?)
// et les guillemets prennent l'espace fine insécable : jamais de deux-points en début de ligne.
const typo = (html, francais) =>
  html
    .split(/(<pre[\s\S]*?<\/pre>|<code[\s\S]*?<\/code>)/)
    .map((part, i) => (i % 2 ? part : part.replace(/(^|>)([^<]*)/g, (m, a, t) => {
      let x = t.replace(/(\d) (?=\d{3}(?!\d))/g, '$1\u202f');
      if (francais) x = x.replace(/ ([;:!?])/g, '\u202f$1').replace(/« /g, '«\u202f').replace(/ »/g, '\u202f»');
      return a + x.replace(/\b(BIP|BOLT|bLIP|SLIP|RFC|NIP|LUD)-(\d+)\b/g, '<span class="insec">$1-$2</span>');
    })))
    .join('');

// linker (facultatif) : ajoute les renvois dans le texte, avant que les formules soient remises en place.
// base : préfixe de langue des liens (« » ou « /en »). texts : libellés (agrandir le schéma).
// Les schémas pointent vers /<slug>/assets/ (le seul exemplaire des fichiers, partagé par les langues),
// en SVG quand le dossier en a un (charte 2027, section 5 : format préféré sur le site).
export function createRenderer({ linker = null, label = (x) => x, base = '', agrandir = 'Agrandir le schéma', agrandirImage = 'Agrandir l’image', creditLabel = 'Crédit :' } = {}) {
  let current = null;
  const marked = new Marked({ gfm: true, breaks: false });
  marked.use({
    renderer: {
      image({ href, title, text }) {
        // Le texte alternatif est lu tel quel : sans les accents graves du Markdown (`1011`).
        text = text.replace(/`/g, '');
        // Le fichier est cherché depuis le dossier du texte rendu : ./assets/… en français, et pour
        // une traduction ../../../fr/<lettre>/<slug>/assets/… (le schéma de l'entrée française) ou
        // ./assets/… (un schéma redessiné dans sa langue). Il est servi depuis /<slug>/assets/
        // (/en/<slug>/assets/ pour une autre langue), où le build copie les images.
        const fichier = current && !/^[a-z]+:/.test(href) ? path.resolve(current.mdDir || current.sourceDir, href) : null;
        const rel = fichier && path.relative(path.join(current.sourceDir, '..', '..', '..'), fichier).split(path.sep);
        const dansDepot = rel && rel.length > 3 && rel[0] !== '..';
        const local = dansDepot ? rel.slice(3).join('/') : href.replace(/^\.\//, '');
        const dossier = dansDepot ? (rel[0] === 'fr' ? rel[2] : `${rel[0]}/${rel[2]}`) : current?.slugs?.fr || current?.slug;
        const size = fichier ? pngSize(fichier) : null;
        const dims = size ? ` width="${size.width}" height="${size.height}"` : '';
        // Crédit d'une image de tiers (metadata.yaml, assets[].credit), toujours affiché sous l'image.
        const asset = dossier === current?.slugs?.fr ? current?.assets?.find((a) => a.filename === local.replace(/^assets\//, '')) : null;
        const credit = asset?.credit ? `<span class="figure-credit">${escapeHtml(creditLabel)} <span lang="fr">${escapeHtml(asset.credit)}</span></span>` : '';
        // Une image créditée est un logo ou une image de tiers, pas un schéma : elle suit la largeur de l'écran.
        const ouvrir = credit ? agrandirImage : agrandir;
        const caption = title || credit ? `<figcaption>${title ? `<span class="figure-legende">${escapeHtml(title)}</span>` : ''}${credit}</figcaption>` : '';
        const svg = local.replace(/\.png$/, '.svg');
        const vectoriel = fichier && svg !== local && fs.existsSync(fichier.replace(/\.png$/, '.svg'));
        const src = `/${dossier}/${vectoriel ? svg : local}`;
        return `<figure class="figure${credit ? ' figure--tiers' : ''}"><div class="figure-cadre"${credit ? '' : ' tabindex="0"'}><a href="${escapeHtml(src)}" aria-label="${escapeHtml(ouvrir)}"><img src="${escapeHtml(src)}" alt="${escapeHtml(text)}"${dims} loading="lazy" decoding="async"></a></div>${caption}<a class="figure-ouvrir" href="${escapeHtml(src)}">${escapeHtml(ouvrir)}</a></figure>`;
      },
      link({ href, title, tokens }) {
        const text = this.parser.parseInline(tokens);
        const external = /^https?:/.test(href);
        const t = title ? ` title="${escapeHtml(title)}"` : '';
        return `<a href="${escapeHtml(href)}"${t}${external ? ' rel="noopener"' : ''}>${text}</a>`;
      },
      table(token) {
        // Les tableaux défilent seuls sur un téléphone.
        const html = Renderer.prototype.table.call(this, token);
        return `<div class="table-scroll" tabindex="0">${html}</div>`;
      },
    },
  });

  return function render(def) {
    current = def;
    const { text, formulas } = protectMath(def.body);
    let html = marked.parse(text);
    if (linker) html = linker(html, def, { label, base });
    html = apostrophes(html);
    html = typo(html, (def.lang || 'fr') === 'fr');
    html = restoreMath(html, formulas);
    // Une figure seule dans un paragraphe : on retire le <p> qui l'enveloppe.
    html = html.replace(/<p>\s*(<figure class="figure[^"]*">[\s\S]*?<\/figure>)\s*<\/p>/g, '$1');
    return { html, math: formulas.length > 0 };
  };
}
