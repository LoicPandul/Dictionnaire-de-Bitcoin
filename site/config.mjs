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
// Charte officielle de l'édition 2027 (charte-officielle.md, palette et mode sombre) : Figue #AA226A, validée par Loïc, banian.
// Paires de texte interdites par la charte : Écorce sur Rose, Figue sur Nuit, tout texte sur Galet.
export const palette = {
  blanc: '#FFFFFF', // fond du site, texte sur Figue
  brume: '#FBF2F6', // surface secondaire (encadrés, code en ligne)
  rose: '#F6D3E2', // fond léger d'un élément mis en avant, sélection de texte, correspondances
  galet: '#D8D0D4', // champs et séparateurs de tableaux (jamais sous du texte)
  encre: '#1E1A1D', // texte
  ecorce: '#6B6368', // texte secondaire (5,82 : 1 sur Blanc)
  figue: '#AA226A', // couleur de l'édition : liens, bouton, jaquette (6,67 : 1 avec Blanc)
  figueSombre: '#691E47', // survol des liens et des boutons (11,19 : 1 avec Blanc)
  canopee: '#4B2034', // feuillage le plus sombre : pied de page (13,50 : 1 avec Blanc)
  figueVive: '#E12789', // figues ; grands textes seulement
  figueClaire: '#F07DB8', // liens et bouton du mode sombre (7,30 : 1 sur Nuit)
  nuit: '#2B0618', // fond du mode sombre
  surfaceSombre: '#3B1026', // surfaces du mode sombre (Brume dessus 14,85 : 1)
  ecorceSombre: '#A8979F', // texte secondaire du mode sombre (6,65 : 1 sur Nuit)
  ombre: '#1E1A1D', // teinte des voiles des fenêtres
};
