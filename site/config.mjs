// Configuration du site du Dictionnaire de Bitcoin.
//
// `url` est la seule clé à changer le jour où le domaine est acheté : elle sert aux
// adresses canoniques, au sitemap, au JSON-LD et aux cartes sociales. Sans barre finale.
export const url = 'https://dictionnaire-bitcoin.example';

export const site = {
  title: 'Dictionnaire de Bitcoin',
  subtitle: 'Tout le vocabulaire technique de Bitcoin',
  author: 'Loïc Morel',
  authorUrl: 'https://pandul.fr/',
  authorX: 'https://x.com/Loic_Pandul',
  github: 'https://github.com/LoicPandul/Dictionnaire-de-Bitcoin',
  license: 'CC BY-NC-SA 4.0',
  licenseUrl: 'https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr',
  bitcoinBazar: 'https://bitcoinbazar.fr/products/le-dictionnaire-de-bitcoin',
  amazon: 'https://amzn.to/4cxaOA8',
  pdf: '/dictionnaire-de-bitcoin.pdf',
  isbnPaperback: '9798250570664',
  isbnHardcover: '9798251996579',
  lightning: 'sats@pandul.fr',
  // Millésime affiché (couverture, colophon, données structurées). Les images du livre imprimé
  // (static/img/livre.webp, couverture.webp, pages, vidéo) sont celles de l'édition 2026.
  edition: '2026',
};

// Palette du site : la seule source des couleurs. Le build en écrit les jetons CSS (bloc « palette »
// en tête de static/css/site.css), la couleur de la barre des navigateurs et le manifeste.
// Valeurs provisoires tirées de l'édition 2026 (couverture bleu nuit). À remplacer par la charte
// de l'édition 2027 (design/charte-2027.md, branche feat/couverture-2027) dès qu'elle est arrêtée :
// changer ces valeurs, relancer le build, rien d'autre à toucher.
export const palette = {
  papier: '#F4F3F0', // fond des pages
  sable: '#E3DFD6', // pas de ton entre surfaces
  encre: '#193042', // texte, boutons, cartouches
  ardoise: '#4F5F6E', // notes secondaires sur papier
  couverture: '#193040', // couleur dominante : jaquette, dos, 404 (l'arbre s'y fond)
  os: '#EBEAE6', // texte sur la couleur de couverture
  gravure: '#A9BAC8', // traits et notes sur la couleur de couverture
  lavis: '#22405A', // surfaces sur la couleur de couverture
  accent: '#E9C46A', // seul accent : survol, sélection, correspondances
  flottant: '#FBFAF8', // cartes et fenêtres qui flottent
  ombre: '#09121A', // teinte des ombres portées et des voiles
  sombreFond: '#0E1A24', // mode sombre : fond
  sombreSurface: '#1F3548', // mode sombre : surfaces
  sombreFlottant: '#1F3548', // mode sombre : cartes flottantes
};
