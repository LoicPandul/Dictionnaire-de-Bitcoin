// Accueil : le mot du jour et la tranche (« Feuilleter les mots »).
(() => {
  const d = document;
  const reduit = matchMedia('(prefers-reduced-motion: reduce)');
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  const affiche = (t) => String(t).replace(/\b0X([0-9A-F]+)\b/g, '0x$1').replace(/ - /g, '\u00a0– ').replace(/'/g, '’');
  const coupe = (s) => esc(affiche(s)).replace(/_/g, '_<wbr>');
  const picto = (slug) => `<svg class="picto" aria-hidden="true" focusable="false"><use href="/img/pictos.svg#p-${slug}"/></svg>`;
  const B = d.documentElement.dataset.base || '';
  const tx = window.dicoTexte || ((k) => k);
  const jour = () => Math.floor((Date.now() - new Date().getTimezoneOffset() * 60000) / 86400000);

  const sectionJour = d.querySelector('[data-jour]');
  const sectionTranche = d.querySelector('[data-tranche]');
  if (!sectionJour && !sectionTranche) return;

  let termes = null;
  let longueurs = null;
  let lettresMots = '';
  const charger = () =>
    Promise.all([window.dicoIndex(), fetch(`${B}/tranche.json`).then((r) => r.json())]).then(([idx, tranche]) => {
      termes = idx;
      longueurs = tranche.longueurs;
      lettresMots = tranche.lettres || '';
    });

  // ------------------------------------------------------------ Le mot du jour
  // Parmi les entrées écrites dans la langue de la page (en anglais, les traduites seulement).
  const ecrits = () => { const e = termes.filter((t) => !t.lang); return e.length ? e : termes; };
  const nomJour = sectionJour?.querySelector('[data-jour-nom]');
  function poserMot(t, anime) {
    if (!sectionJour) return;
    const lien = sectionJour.querySelector('[data-jour-lien]');
    const lire = sectionJour.querySelector('[data-jour-lire]');
    const cat = sectionJour.querySelector('[data-jour-cat]');
    lien.href = lire.href = `${B}/${t.slug}/`;
    cat.href = t.cat[2] || cat.href;
    cat.innerHTML = `${picto(t.cat[1])}<span>${esc(t.cat[0])}</span>`;
    const desc = sectionJour.querySelector('[data-jour-desc]');
    desc.textContent = t.desc.replace(/'/g, '’');
    if (t.lang) desc.lang = t.lang; else desc.removeAttribute('lang');
    if (!anime || reduit.matches) { nomJour.innerHTML = coupe(t.title); return; }
    // Les lettres du nouveau mot roulent en place, l'une après l'autre.
    nomJour.innerHTML = [...affiche(t.title)].map((c, i) => (c === ' ' ? ' ' : `<span class="roule" style="--r:${i}">${esc(c)}</span>`)).join('');
    const jeton = ++tirage;
    const anims = [...nomJour.querySelectorAll('.roule')].map((s, i) =>
      s.animate([{ transform: 'translateY(0.9em)', opacity: 0 }, { transform: 'none', opacity: 1 }], { duration: 420, delay: Math.min(i * 22, 400), easing: 'cubic-bezier(0.16, 1, 0.3, 1)', fill: 'backwards' }));
    // L'animation finie, le mot redevient du texte : le soulignement du lien court de nouveau sous tout le mot.
    Promise.all(anims.map((a) => a.finished)).then(() => { if (jeton === tirage) nomJour.innerHTML = coupe(t.title); }, () => {});
  }
  let tirage = 0;
  sectionJour?.querySelector('[data-jour-autre]')?.addEventListener('click', () => {
    (termes ? Promise.resolve() : charger()).then(() => {
      const choix = ecrits();
      poserMot(choix[Math.floor(Math.random() * choix.length)], true);
    });
  });

  // ------------------------------------------------------------ La tranche
  const bande = sectionTranche?.querySelector('[data-bande]');
  const blocs = sectionTranche ? [...sectionTranche.querySelectorAll('.blocs a')] : [];
  const apercu = {
    lien: sectionTranche?.querySelector('[data-apercu-lien]'),
    cat: sectionTranche?.querySelector('[data-apercu-cat]'),
    desc: sectionTranche?.querySelector('[data-apercu-desc]'),
  };
  const NS = 'http://www.w3.org/2000/svg';
  let lettres = [];
  let courant = 0;
  let mode = null;

  function montrer(i) {
    const t = termes[i];
    if (!t) return;
    courant = i;
    apercu.lien.innerHTML = coupe(t.title);
    apercu.lien.href = `${B}/${t.slug}/`;
    apercu.cat.textContent = t.cat[0];
    apercu.desc.textContent = t.desc.replace(/'/g, '’').replace(/\s*\.\.\.$/, '…');
    const l = lettreDe(i);
    blocs.forEach((b) => b.setAttribute('aria-current', String(b.dataset.lettre === l.l)));
    bande.setAttribute('aria-valuenow', String(i + 1));
    bande.setAttribute('aria-valuetext', `${t.title}, ${t.cat[0]}`);
  }
  // Chaque lettre réunit ses mots (ids, dans l'ordre du livre), comme sa page de lettre ; debut est le premier mot
  // de sa plus longue série consécutive, là où l'aiguille se pose quand on choisit la lettre.
  let lettreDuMot = [];
  const lettreDe = (i) => lettreDuMot[i] || lettres[0];
  const hauteur = (i, H) => Math.max(6, Math.round((Math.sqrt(longueurs[i]) / Math.sqrt(maxLen)) * H));
  let maxLen = 1;

  // Bureau : la bande montre les traits d'une seule lettre, espacés pour être visés.
  let lettreActive = null;
  let svg = null;
  let vise = null;
  function dessinerLettre(l) {
    lettreActive = l;
    const W = bande.clientWidth;
    const H = bande.clientHeight;
    const n = l.ids.length;
    const pas = Math.min(28, W / n);
    const larg = Math.max(1.5, Math.min(pas * 0.5, 6));
    const x0 = (W - pas * n) / 2;
    svg = d.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
    svg.setAttribute('aria-hidden', 'true');
    vise = d.createElementNS(NS, 'rect');
    vise.setAttribute('class', 'vise');
    vise.setAttribute('y', '0');
    vise.setAttribute('height', String(H));
    svg.append(vise);
    const frag = d.createDocumentFragment();
    for (let k = 0; k < n; k++) {
      const i = l.ids[k];
      const h = hauteur(i, H - 8);
      const r = d.createElementNS(NS, 'rect');
      r.setAttribute('class', 'trait');
      r.setAttribute('x', (x0 + k * pas + (pas - larg) / 2).toFixed(2));
      r.setAttribute('y', String(H - h));
      r.setAttribute('width', larg.toFixed(2));
      r.setAttribute('height', String(h));
      if (!reduit.matches) {
        r.style.transformOrigin = `0 ${H}px`;
        r.animate([{ transform: 'scaleY(0)' }, { transform: 'none' }], { duration: 520, delay: Math.min(k * 3, 420), easing: 'cubic-bezier(0.16, 1, 0.3, 1)', fill: 'backwards' });
      }
      frag.append(r);
    }
    svg.append(frag);
    svg.dataset.x0 = x0;
    svg.dataset.pas = pas;
    bande.replaceChildren(svg);
  }
  function viser(i) {
    if (!lettreActive || lettreDe(i) !== lettreActive) {
      dessinerLettre(lettreDe(i));
    }
    const pas = Number(svg.dataset.pas);
    const x0 = Number(svg.dataset.x0);
    const k = lettreActive.ids.indexOf(i);
    vise.setAttribute('x', (x0 + k * pas).toFixed(2));
    vise.setAttribute('width', pas.toFixed(2));
    montrer(i);
  }
  function brancherBureau() {
    mode = 'bureau';
    bande.classList.remove('bande-defile');
    viser(courant);
    blocs.forEach((b) => {
      const l = lettres.find((x) => x.l === b.dataset.lettre);
      const choisir = () => { if (lettreActive !== l) { dessinerLettre(l); viser(l.debut); } };
      b.addEventListener('mouseenter', choisir);
      b.addEventListener('focus', choisir);
    });
    bande.addEventListener('pointermove', (e) => {
      if (mode !== 'bureau' || !svg) return;
      const rect = bande.getBoundingClientRect();
      const k = Math.floor((e.clientX - rect.left - Number(svg.dataset.x0)) / Number(svg.dataset.pas));
      const i = lettreActive.ids[Math.min(lettreActive.ids.length - 1, Math.max(0, k))];
      if (i !== courant) viser(i);
    });
    bande.addEventListener('click', () => { if (mode === 'bureau') location.href = `${B}/${termes[courant].slug}/`; });
    bande.style.cursor = 'pointer';
  }

  // Téléphone : toute la tranche défile sous une aiguille fixe (défilement natif, inertie).
  const PAS = 4;
  let aiguille = null;
  // Dessine la tranche entière et place l'aiguille ; refait à chaque changement de largeur (rotation de la tablette).
  function dessinerDoigt() {
    const H = bande.clientHeight;
    const W = bande.clientWidth;
    const n = termes.length;
    const largeur = n * PAS + W;
    const s = d.createElementNS(NS, 'svg');
    s.setAttribute('width', String(largeur));
    s.setAttribute('height', String(H));
    s.setAttribute('viewBox', `0 0 ${largeur} ${H}`);
    s.setAttribute('aria-hidden', 'true');
    s.style.width = `${largeur}px`;
    s.style.maxWidth = 'none';
    let path = '';
    for (let i = 0; i < n; i++) {
      const h = hauteur(i, H - 10);
      path += `M${W / 2 + i * PAS + 0.5} ${H}v-${h}h2v${h}z`;
    }
    const p = d.createElementNS(NS, 'path');
    p.setAttribute('class', 'trait');
    p.setAttribute('d', path);
    s.append(p);
    const piste = d.createElement('div');
    piste.className = 'bande-piste';
    piste.append(s);
    bande.replaceChildren(piste);
    aiguille.style.top = `${bande.offsetTop - 8}px`;
    aiguille.style.bottom = 'auto';
    aiguille.style.height = `${H + 16}px`;
    bande.scrollLeft = courant * PAS;
  }
  function brancherDoigt() {
    mode = 'doigt';
    const n = termes.length;
    bande.classList.add('bande-defile');
    aiguille = d.createElement('span');
    aiguille.className = 'aiguille';
    bande.parentElement.style.position = 'relative';
    bande.after(aiguille);
    dessinerDoigt();
    let attente = false;
    bande.addEventListener('scroll', () => {
      if (attente) return;
      attente = true;
      requestAnimationFrame(() => {
        attente = false;
        const i = Math.min(n - 1, Math.max(0, Math.round(bande.scrollLeft / PAS)));
        if (i !== courant) montrer(i);
      });
    }, { passive: true });
    montrer(courant);
    blocs.forEach((b) => {
      b.addEventListener('click', (e) => {
        e.preventDefault();
        const l = lettres.find((x) => x.l === b.dataset.lettre);
        bande.scrollTo({ left: l.debut * PAS, behavior: reduit.matches ? 'auto' : 'smooth' });
      });
    });
  }

  function brancherTranche() {
    // Les lettres de la tranche : début et fin de chaque lettre dans l'index alphabétique.
    const parLettre = new Map();
    let prec = 'A';
    termes.forEach((t, i) => {
      // La lettre des pages de lettre ; à défaut (ancien tranche.json, chiffre), l'initiale du titre ou la précédente.
      let l = (lettresMots[i] || t.title.normalize('NFD').replace(/[^A-Za-z]/g, '')[0] || '').toUpperCase();
      if (!/^[A-Z]$/.test(l)) l = prec;
      prec = l;
      if (!parLettre.has(l)) parLettre.set(l, []);
      parLettre.get(l).push(i);
    });
    lettres = [...parLettre.keys()].sort().map((l) => {
      const ids = parLettre.get(l);
      let debut = ids[0];
      let meilleure = 0;
      for (let k = 0, depart = 0; k < ids.length; k++) {
        if (k > 0 && ids[k] !== ids[k - 1] + 1) depart = k;
        if (k - depart + 1 > meilleure) { meilleure = k - depart + 1; debut = ids[depart]; }
      }
      return { l, ids, debut };
    });
    lettreDuMot = [];
    for (const l of lettres) for (const i of l.ids) lettreDuMot[i] = l;
    maxLen = Math.max(...longueurs);
    // Départ sur un mot au hasard, différent du mot du jour affiché juste au-dessus.
    const duJour = jour() % termes.length;
    do { courant = Math.floor(Math.random() * termes.length); } while (courant === duJour && termes.length > 1);
    bande.setAttribute('role', 'slider');
    bande.setAttribute('tabindex', '0');
    bande.setAttribute('aria-label', tx('trancheAria'));
    bande.setAttribute('aria-valuemin', '1');
    bande.setAttribute('aria-valuemax', String(termes.length));
    // Souris ou pavé sur grand écran : la bande d'une lettre ; écran tactile ou étroit : la tranche entière sous l'aiguille.
    const doigt = matchMedia('(pointer: coarse), (max-width: 899px)');
    (doigt.matches ? brancherDoigt : brancherBureau)();
    bande.addEventListener('keydown', (e) => {
      let i = courant;
      const l = lettreDe(i);
      const k = lettres.indexOf(l);
      // Bureau : les flèches parcourent les mots de la lettre affichée, puis passent à la lettre voisine.
      const pos = l.ids.indexOf(i);
      const avant = e.key === 'ArrowRight' || e.key === 'ArrowUp';
      const arriere = e.key === 'ArrowLeft' || e.key === 'ArrowDown';
      if (mode === 'bureau' && avant) i = l.ids[pos + 1] ?? (lettres[k + 1] || l).ids[0];
      else if (mode === 'bureau' && arriere) i = l.ids[pos - 1] ?? (lettres[k - 1] || l).ids.at(-1);
      else if (avant) i++;
      else if (arriere) i--;
      else if (e.key === 'PageDown') i = (lettres[k + 1] || l).debut;
      else if (e.key === 'PageUp') i = (lettres[k - 1] || l).debut;
      else if (e.key === 'Home') i = 0;
      else if (e.key === 'End') i = termes.length - 1;
      else if (e.key === 'Enter') { location.href = `${B}/${termes[courant].slug}/`; return; }
      else return;
      e.preventDefault();
      i = Math.max(0, Math.min(termes.length - 1, i));
      if (mode === 'bureau') viser(i);
      else { bande.scrollLeft = i * PAS; montrer(i); }
    });
    let largeurPrec = innerWidth;
    addEventListener('resize', () => {
      if (Math.abs(innerWidth - largeurPrec) < 40) return;
      largeurPrec = innerWidth;
      if (mode === 'bureau' && lettreActive) { dessinerLettre(lettreActive); viser(courant); }
      else if (mode === 'doigt') { const i = courant; dessinerDoigt(); montrer(i); }
    });
  }

  // ------------------------------------------------------------ Démarrage
  // Le mot du jour du lecteur (le HTML porte celui du jour du build).
  const demarrer = () => charger().then(() => {
    const choix = ecrits();
    const t = choix[jour() % choix.length];
    const lien = sectionJour?.querySelector('[data-jour-lien]');
    if (t && lien && lien.getAttribute('href') !== `${B}/${t.slug}/`) {
      poserMot(t, false);
    }
    if (bande) brancherTranche();
  });
  if ('IntersectionObserver' in window && sectionJour) {
    const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { io.disconnect(); demarrer(); } }, { rootMargin: '600px 0px' });
    io.observe(sectionJour);
  } else demarrer();
})();
