// Espaces insécables communes au texte des définitions (lib/markdown.mjs), aux résumés (lib/templates.mjs, fr),
// aux cartes d'aperçu (lib/liens.mjs) et à l'index de recherche (build.mjs).

// Un nombre ne se sépare pas de son unité, en toutes lettres ou en symbole :
// « 256 bits », « 2 000 vB », « 4 Mo », « 10 sat/vB », « 150 EH/s », « 400 000 unités de poids ».
const NOMS = String.raw`sats?\/vB|sats?\/vbyte|bits?|octets?|bytes?|vbytes?|virtual bytes?|kvB|vB|WU|weight units?|unités?|satoshis?|sats?|m?BTC|[kKMGTP]i?[oB]|[kMGTPE]?H\/s|ms|µs|ns`;
const FIN = String.raw`(?![\p{L}\d/])`;
const UNITE = new RegExp(String.raw`(\d) (${NOMS})${FIN}`, 'gu');
export const unites = (t) => t.replace(UNITE, '$1 $2');
// Même règle quand l'unité est un lien (« 100 000 <a>octets virtuels</a> »), dans du HTML déjà rendu.
const UNITE_LIEN = new RegExp(String.raw`(\d) (<a\b[^>]*>)(?=(?:${NOMS})${FIN})`, 'gu');
export const unitesHtml = (html) => html.replace(UNITE_LIEN, '$1 $2');

// En français, une date ne se coupe pas : « 15 mars 2012 », « 1er janvier ».
const MOIS = 'janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre';
const JOUR_MOIS = new RegExp(`\\b(\\d{1,2}|1er) (${MOIS})\\b`, 'g');
const MOIS_AN = new RegExp(`\\b(${MOIS}) (\\d{4})\\b`, 'g');
export const dates = (t) => t.replace(JOUR_MOIS, '$1 $2').replace(MOIS_AN, '$1 $2');
