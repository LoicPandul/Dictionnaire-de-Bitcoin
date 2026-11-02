// Configuration du site du Dictionnaire de Bitcoin.
//
// `url` est la seule clé à changer le jour où le domaine est acheté : elle sert aux
// adresses canoniques, au sitemap, au JSON-LD et aux cartes sociales. Sans barre finale.
export const url = 'https://dictionnaire-bitcoin.com';

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
  // Millésime affiché (jaquette, colophon, données structurées). Les pages et la vidéo du livre
  // imprimé (static/img/page-*.webp, static/video/) restent celles de l'édition 2026, la seule parue.
  edition: '2027',
};

// Palette du site : la seule source des couleurs. Le build en écrit les jetons CSS (bloc « palette »
// en tête de static/css/site.css), la couleur de la barre des navigateurs et le manifeste.
// Palette de l'édition 2027 (design/charte-2027.md, branche feat/couverture-2027) : Mandarine #FD550A,
// Forêt #015D47 et Crête #E0F354 ; les neutres sont dérivés de ces trois couleurs.
export const palette = {
  blanc: '#FFFFFF', // fond clair, texte sur les aplats sombres
  brume: '#F6F9E4', // surface claire ; texte du mode sombre
  galet: '#D2D9C9', // champs et séparateurs (jamais sous du texte)
  encre: '#0B231D', // texte
  ecorce: '#4F5F58', // texte secondaire
  foret: '#015D47', // couleur de travail : liens, boutons, focus
  foretSombre: '#013D2F', // survol des liens et des boutons
  canopee: '#0B2E25', // aplat le plus sombre : pied de page, sol de la couverture, bouton « Chercher »
  mandarine: '#FD550A', // couleur de l'édition : couverture, pastille choisie, barre des navigateurs
  crete: '#E0F354', // accent clair : survols, sélection, soleil de la couverture ; liens et focus du mode sombre
  nuit: '#031B15', // fond du mode sombre
  surfaceSombre: '#0C3229', // surfaces du mode sombre
  ecorceSombre: '#A2B4AB', // texte secondaire du mode sombre
  ombre: '#0B231D', // teinte des voiles
};
