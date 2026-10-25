// Données structurées (JSON-LD), sitemap et robots. Mêmes types que sur pandul.fr :
// DefinedTermSet pour le dictionnaire, DefinedTerm par définition, BreadcrumbList partout.
import { url, site } from '../config.mjs';

export const SET_ID = `${url}/#dictionnaire`;
export const PERSON_ID = 'https://pandul.fr/#person-loic';

const person = {
  '@type': 'Person',
  '@id': PERSON_ID,
  name: site.author,
  alternateName: 'Pandul',
  url: 'https://pandul.fr/a-propos/',
  sameAs: [site.authorX, 'https://github.com/LoicPandul', 'https://www.amazon.fr/stores/Loïc-Morel/author/B0GX5ZYL9F'],
};

const graph = (nodes) =>
  `<script type="application/ld+json">${JSON.stringify({ '@context': 'https://schema.org', '@graph': nodes }).replace(/</g, '\\u003c')}</script>`;

const crumbs = (pageUrl, items) => ({
  '@type': 'BreadcrumbList',
  '@id': `${pageUrl}#fil`,
  itemListElement: items.map(([name, path], i) => ({
    '@type': 'ListItem',
    position: i + 1,
    name,
    ...(path ? { item: `${url}${path}` } : {}),
  })),
});

export function homeJsonLd({ total, description }) {
  return graph([
    {
      '@type': 'WebSite',
      '@id': `${url}/#site`,
      url: `${url}/`,
      name: site.title,
      inLanguage: 'fr',
      author: { '@id': PERSON_ID },
    },
    {
      '@type': 'DefinedTermSet',
      '@id': SET_ID,
      name: site.title,
      description,
      url: `${url}/`,
      inLanguage: 'fr',
      author: { '@id': PERSON_ID },
      license: site.licenseUrl,
    },
    {
      '@type': 'Book',
      '@id': `${url}/#livre`,
      name: site.title,
      alternativeHeadline: site.subtitle,
      author: { '@id': PERSON_ID },
      inLanguage: 'fr',
      bookEdition: `Édition ${site.edition}`,
      workExample: [
        { '@type': 'Book', bookFormat: 'https://schema.org/Paperback', isbn: site.isbnPaperback },
        { '@type': 'Book', bookFormat: 'https://schema.org/Hardcover', isbn: site.isbnHardcover },
        { '@type': 'Book', bookFormat: 'https://schema.org/EBook', url: `${url}${site.pdf}`, isAccessibleForFree: true },
      ],
      abstract: `${total} définitions du vocabulaire technique de Bitcoin.`,
    },
    person,
  ]);
}

export function definitionJsonLd(def) {
  const pageUrl = `${url}/${def.slug}/`;
  const alt = [def.englishTerm, def.frenchTerm].filter(Boolean);
  return graph([
    {
      '@type': 'DefinedTerm',
      '@id': `${pageUrl}#terme`,
      name: def.title,
      ...(alt.length === 1 ? { alternateName: alt[0] } : alt.length ? { alternateName: alt } : {}),
      ...(def.description ? { description: def.description } : {}),
      url: pageUrl,
      termCode: def.slug,
      inDefinedTermSet: { '@id': SET_ID },
    },
    crumbs(pageUrl, [
      ['Dictionnaire', '/'],
      [def.category, `/categorie/${def.categorySlug}/`],
      [def.title, null],
    ]),
  ]);
}

export function listJsonLd({ path, name, defs }) {
  const pageUrl = `${url}${path}`;
  return graph([
    {
      '@type': 'CollectionPage',
      '@id': pageUrl,
      name,
      url: pageUrl,
      inLanguage: 'fr',
      isPartOf: { '@id': SET_ID },
      mainEntity: {
        '@type': 'ItemList',
        numberOfItems: defs.length,
        itemListElement: defs.map((d, i) => ({ '@type': 'ListItem', position: i + 1, url: `${url}/${d.slug}/`, name: d.title })),
      },
    },
    crumbs(pageUrl, [
      ['Dictionnaire', '/'],
      [name, null],
    ]),
  ]);
}

export function sitemap(paths) {
  const today = new Date().toISOString().slice(0, 10);
  const rows = paths
    .map((p) => `<url><loc>${url}${p}</loc><lastmod>${today}</lastmod></url>`)
    .join('\n');
  return `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${rows}\n</urlset>\n`;
}

export const robots = () => `User-agent: *\nAllow: /\n\nSitemap: ${url}/sitemap.xml\n`;
