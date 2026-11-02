// Espaces insécables communes au texte des définitions (lib/markdown.mjs), aux résumés (lib/templates.mjs, fr)
// et à l'index de recherche (build.mjs).

// Un nombre ne se sépare pas de son unité, en toutes lettres ou en symbole :
// « 256 bits », « 2 000 vB », « 4 Mo », « 10 sat/vB », « 150 EH/s ».
const UNITE = /(\d) (sats?\/vB|sats?\/vbyte|bits?|octets?|bytes?|vbytes?|kvB|vB|WU|satoshis?|sats?|m?BTC|[kKMGTP]i?[oB]|[kMGTPE]?H\/s|ms|µs|ns)(?![\p{L}\d/])/gu;
export const unites = (t) => t.replace(UNITE, '$1 $2');

// En français, une date ne se coupe pas : « 15 mars 2012 », « 1er janvier ».
const MOIS = 'janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|novembre|décembre';
const JOUR_MOIS = new RegExp(`\\b(\\d{1,2}|1er) (${MOIS})\\b`, 'g');
const MOIS_AN = new RegExp(`\\b(${MOIS}) (\\d{4})\\b`, 'g');
export const dates = (t) => t.replace(JOUR_MOIS, '$1 $2').replace(MOIS_AN, '$1 $2');
