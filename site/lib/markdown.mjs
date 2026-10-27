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

// Remplace les formules par des jetons inertes, hors des blocs et spans de code.
function protectMath(source) {
  const formulas = [];
  const token = (html) => `⁣M${formulas.push(html) - 1}⁣`;
  const parts = source.split(/(```[\s\S]*?```|`[^`\n]*`)/);
  const out = parts.map((part, i) => {
    if (i % 2 === 1) return part;
    return part
      .replace(/\$\$([\s\S]+?)\$\$/g, (_, tex) => token(renderMath(tex, true)))
      .replace(/(?<![\\$])\$([^$\n]+?)\$/g, (_, tex) => token(renderMath(tex, false)));
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

// linker (facultatif) : ajoute les renvois dans le texte, avant que les formules soient remises en place.
// base : préfixe de langue des liens (« » ou « /en »). texts : libellés (agrandir le schéma).
// Les schémas pointent vers /<slug>/assets/ (le seul exemplaire des fichiers, partagé par les langues),
// en SVG quand le dossier en a un (charte 2027, section 5 : format préféré sur le site).
export function createRenderer({ linker = null, label = (x) => x, base = '', agrandir = 'Agrandir le schéma' } = {}) {
  let current = null;
  const marked = new Marked({ gfm: true, breaks: false });
  marked.use({
    renderer: {
      image({ href, title, text }) {
        const local = href.replace(/^\.\//, '');
        const size = current ? pngSize(path.join(current.sourceDir, local)) : null;
        const dims = size ? ` width="${size.width}" height="${size.height}"` : '';
        const caption = title ? `<figcaption>${escapeHtml(title)}</figcaption>` : '';
        const svg = local.replace(/\.png$/, '.svg');
        const vectoriel = current && svg !== local && fs.existsSync(path.join(current.sourceDir, svg));
        const src = `/${current?.slug}/${vectoriel ? svg : local}`;
        return `<figure class="figure"><div class="figure-cadre" tabindex="0"><a href="${escapeHtml(src)}" aria-label="${escapeHtml(agrandir)}"><img src="${escapeHtml(src)}" alt="${escapeHtml(text)}"${dims} loading="lazy" decoding="async"></a></div>${caption}<a class="figure-ouvrir" href="${escapeHtml(src)}">${escapeHtml(agrandir)}</a></figure>`;
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
    html = restoreMath(html, formulas);
    // Une figure seule dans un paragraphe : on retire le <p> qui l'enveloppe.
    html = html.replace(/<p>\s*(<figure class="figure">[\s\S]*?<\/figure>)\s*<\/p>/g, '$1');
    return { html, math: formulas.length > 0 };
  };
}
