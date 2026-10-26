// Dictionnaire de Bitcoin : scripts communs à toutes les pages.
// Thème, barre, apparitions, transitions entre pages, recherche, suggestions de la 404.
(() => {
  const d = document;
  const root = d.documentElement;
  const reduit = matchMedia('(prefers-reduced-motion: reduce)');
  root.classList.add('anim');
  const affiche = (t) => String(t).replace(/\b0X([0-9A-F]+)\b/g, '0x$1').replace(/ - /g, '\u00a0– ');
  // Résumé coupé au mot (même règle que lib/templates.mjs, resume).
  const resume = (t, n = 84) => {
    t = String(t || '').replace(/\s*(\.\.\.|…)$/, '');
    if (t.length <= n) return t === '' ? '' : /[.!?)»]$/.test(t) ? t : `${t}…`;
    // Une phrase entière qui tient, même courte, vaut mieux qu'une coupe : pas de points de suspension.
    const fin = Math.max(...[...t.slice(0, n + 1).matchAll(/[.!?](?=\s)/g)].map((m) => m.index));
    if (fin > n * 0.45) return t.slice(0, fin + 1);
    let s = t.slice(0, n + 1);
    s = s.slice(0, Math.max(s.lastIndexOf(' '), 1));
    while (/\s(\S{1,3}|\S*\d\S*|que|qui|dont|dans|pour|avec|sans|sous|leur|leurs|cette|entre|plus|très)$/i.test(s) && s.lastIndexOf(' ') > n / 2) s = s.slice(0, s.lastIndexOf(' '));
    if ((s.match(/\(/g) || []).length > (s.match(/\)/g) || []).length && s.lastIndexOf('(') > n / 2) s = s.slice(0, s.lastIndexOf('('));
    return `${s.replace(/[\s,;:.(«–-]+$/, '')}…`;
  };
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);

  // ------------------------------------------------------------ Thème
  const themeBtn = d.querySelector('[data-theme-toggle]');
  const sombre = () => root.dataset.theme === 'dark' || (!root.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches);
  const majTheme = () => themeBtn?.setAttribute('aria-label', sombre() ? 'Passer en thème clair' : 'Passer en thème sombre');
  majTheme();
  themeBtn?.addEventListener('click', () => {
    const t = sombre() ? 'light' : 'dark';
    root.dataset.theme = t;
    try { localStorage.setItem('theme', t); } catch {}
    majTheme();
  });

  // ------------------------------------------------------------ Barre : se cache en descendant, revient en remontant
  const barre = d.querySelector('[data-barre]');
  let dernierY = scrollY;
  let enAttente = false;
  const majBarre = () => {
    enAttente = false;
    const y = scrollY;
    const cacher = y > 200 && y > dernierY + 4 && !d.querySelector('dialog[open]');
    if (cacher) barre.classList.add('est-cachee');
    else if (y < dernierY - 4 || y <= 200) barre.classList.remove('est-cachee');
    root.style.setProperty('--haut', barre.classList.contains('est-cachee') ? '0px' : `${barre.offsetHeight}px`);
    dernierY = y;
  };
  if (barre) {
    addEventListener('scroll', () => { if (!enAttente) { enAttente = true; requestAnimationFrame(majBarre); } }, { passive: true });
    barre.addEventListener('focusin', () => barre.classList.remove('est-cachee'));
  }
  // Accueil : la barre prend la couleur du papier après la jaquette ; le bouton de recherche
  // n'apparaît qu'une fois le champ de la couverture sorti de l'écran.
  const jaquette = d.querySelector('.jaquette');
  if (jaquette && barre) {
    const champ = jaquette.querySelector('.couv-recherche');
    new IntersectionObserver(([e]) => barre.classList.toggle('est-passee', !e.isIntersecting), { rootMargin: `-${barre.offsetHeight}px 0px 0px 0px` }).observe(jaquette);
    if (champ) new IntersectionObserver(([e]) => barre.classList.toggle('champ-visible', e.isIntersecting)).observe(champ);
  }

  // ------------------------------------------------------------ Apparitions, une fois
  const aVoir = d.querySelectorAll('.feuilleter, .categories, .pages, .alphabet');
  for (const el of aVoir) {
    const enfants = el.matches('.feuilleter') ? el.querySelectorAll('.blocs li') : el.matches('.categories') ? el.querySelectorAll('.index-ligne') : el.matches('.alphabet') ? el.querySelectorAll('li') : [];
    // Décalage plafonné : au-delà de douze lignes, tout arrive ensemble.
    enfants.forEach((c, i) => c.style.setProperty('--k', Math.min(i, 12)));
  }
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) { e.target.classList.add('vu'); io.unobserve(e.target); }
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.05 });
    aVoir.forEach((el) => io.observe(el));
  } else aVoir.forEach((el) => el.classList.add('vu'));

  // ------------------------------------------------------------ Boucles vidéo : lues seulement à l'écran, jamais en mouvement réduit
  const boucles = d.querySelectorAll('video[data-boucle]');
  if (boucles.length && 'IntersectionObserver' in window) {
    const iov = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (e.isIntersecting && !reduit.matches) e.target.play().catch(() => {});
        else e.target.pause();
      }
    }, { threshold: 0.25 });
    boucles.forEach((v) => iov.observe(v));
  }

  // ------------------------------------------------------------ Tranche d'une lettre : le trait visé donne son mot
  // Souris : survol et clic. Doigt : on glisse sur les traits, l'aperçu suit, on touche le mot pour l'ouvrir.
  const tl = d.querySelector('[data-tranche-lettre]');
  if (tl) {
    const traits = [...tl.querySelectorAll('a')];
    const hauteurs = traits.map((a) => Number(a.querySelector('rect').getAttribute('height')));
    const fiches = new Map([...d.querySelectorAll('.entree')].map((a) => [a.getAttribute('href'), a.dataset]));
    const boite = d.querySelector('[data-apercu-lettre]');
    const geste = d.querySelector('[data-geste]');
    const tactile = matchMedia('(pointer: coarse)').matches;
    if (geste) geste.textContent = tactile ? 'Glissez le doigt sur les traits, puis touchez le mot.' : 'Survolez les traits.';
    const NS = 'http://www.w3.org/2000/svg';
    const vb = tl.viewBox.baseVal;
    // Le trait visé : une colonne d'or d'au moins 4 px, quelle que soit la densité de la lettre.
    const marque = d.createElementNS(NS, 'rect');
    marque.setAttribute('class', 'vise-lettre');
    marque.setAttribute('y', '0');
    marque.setAttribute('height', '100');
    tl.prepend(marque);
    // Au doigt : une loupe des 21 traits autour du doigt.
    const loupe = d.createElement('div');
    loupe.className = 'loupe-traits';
    loupe.setAttribute('aria-hidden', 'true');
    loupe.innerHTML = Array.from({ length: 21 }, () => '<span></span>').join('');
    loupe.hidden = true;
    tl.parentElement.style.position = 'relative';
    tl.parentElement.prepend(loupe);
    let vise = -1;
    let cacher = 0;
    const viser = (k) => {
      k = Math.max(0, Math.min(traits.length - 1, k));
      if (k === vise) return;
      vise = k;
      const pas = vb.width / traits.length;
      const min = (4 * vb.width) / Math.max(1, tl.clientWidth);
      const w = Math.max(pas, min);
      marque.setAttribute('x', String(k * pas + pas / 2 - w / 2));
      marque.setAttribute('width', String(w));
      const a = traits[k];
      const f = fiches.get(a.getAttribute('href')) || {};
      const lien = boite.querySelector('a');
      lien.href = a.getAttribute('href');
      lien.textContent = f.apercuNom || a.querySelector('title').textContent;
      boite.querySelector('.apercu-lettre-cat').textContent = f.apercuCat || '';
      boite.querySelector('.apercu-lettre-desc').textContent = resume(f.apercu);
      [...loupe.children].forEach((sp, j) => {
        const i = k - 10 + j;
        sp.style.height = i >= 0 && i < traits.length ? `${Math.max(8, hauteurs[i])}%` : '0';
        sp.classList.toggle('est-vise', j === 10);
      });
    };
    const depuis = (e) => {
      const r = tl.getBoundingClientRect();
      viser(Math.floor(((e.clientX - r.left) / r.width) * traits.length));
      if (e.pointerType === 'touch') {
        clearTimeout(cacher);
        loupe.hidden = false;
        loupe.style.left = `${Math.min(Math.max(0, e.clientX - r.left - 105), r.width - 210)}px`;
      }
    };
    tl.addEventListener('pointermove', depuis);
    tl.addEventListener('pointerdown', depuis);
    const finir = () => { cacher = setTimeout(() => (loupe.hidden = true), 700); };
    tl.addEventListener('pointerup', finir);
    tl.addEventListener('pointercancel', finir);
    tl.addEventListener('click', (e) => {
      e.preventDefault();
      if (!tactile && vise > -1) location.href = traits[vise].getAttribute('href');
    });
  }

  // ------------------------------------------------------------ Jaquette : profondeur au curseur
  // La couronne et les racines glissent de quelques pixels en sens opposés : la canopée flotte devant.
  const objet = d.querySelector('.jaquette-objet');
  if (objet && matchMedia('(hover: hover) and (pointer: fine)').matches && !reduit.matches) {
    const couronne = objet.querySelector('.jaquette-couronne img');
    const racines = objet.querySelector('.jaquette-racines img');
    let raf = 0;
    objet.addEventListener('pointermove', (e) => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        const r = objet.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        couronne.style.translate = `${(x * 8).toFixed(1)}px ${(y * 4).toFixed(1)}px`;
        racines.style.translate = `${(-x * 5).toFixed(1)}px 0`;
      });
    });
    objet.addEventListener('pointerleave', () => { couronne.style.translate = racines.style.translate = '0 0'; });
  }

  // ------------------------------------------------------------ Renvois entrants repliés au-delà de 12 (30 sur grand écran)
  for (const ul of d.querySelectorAll('[data-repliable]')) {
    const n = ul.children.length;
    const limite = innerWidth < 700 ? 12 : 30;
    if (n <= limite) continue;
    ul.classList.add('replie');
    const b = d.createElement('button');
    b.type = 'button';
    b.className = 'cites-plus';
    b.setAttribute('aria-expanded', 'false');
    b.textContent = `Voir les ${n - limite} autres`;
    b.addEventListener('click', () => {
      ul.classList.remove('replie');
      b.remove();
      ul.children[limite]?.querySelector('a')?.focus();
    });
    ul.after(b);
  }

  // ------------------------------------------------------------ Citer, et garder les derniers mots consultés
  const citer = d.querySelector('[data-citer]');
  if (citer) {
    citer.hidden = false;
    const confirmer = (ok) => {
      citer.textContent = ok ? 'Citation copiée' : 'Copiez : ' + citer.dataset.citer;
      setTimeout(() => (citer.textContent = 'Citer cette définition'), ok ? 2400 : 8000);
    };
    const secours = () => {
      const t = d.createElement('textarea');
      t.value = citer.dataset.citer;
      t.setAttribute('readonly', '');
      t.style.position = 'fixed';
      t.style.opacity = '0';
      d.body.append(t);
      t.select();
      let ok = false;
      try { ok = d.execCommand('copy'); } catch {}
      t.remove();
      confirmer(ok);
    };
    citer.addEventListener('click', () => {
      if (navigator.clipboard?.writeText) navigator.clipboard.writeText(citer.dataset.citer).then(() => confirmer(true), secours);
      else secours();
    });
  }

  // ------------------------------------------------------------ Schémas : agrandis en plein écran au clic ou au toucher
  d.addEventListener('click', (e) => {
    const a = e.target.closest('.prose .figure a');
    if (!a || e.metaKey || e.ctrlKey) return;
    e.preventDefault();
    const img = a.querySelector('img');
    const loupe = d.createElement('dialog');
    loupe.className = 'loupe';
    loupe.innerHTML = `<div class="loupe-panneau"><div class="loupe-tete"><p class="loupe-legende">${esc(img.alt || 'Schéma')}</p><p class="loupe-boutons"><button class="recherche-fermer" type="button" data-zoom aria-pressed="false">Agrandir</button> <button class="recherche-fermer" type="button" data-fermer>Fermer</button></p></div><div class="loupe-zone"><img src="${esc(a.getAttribute('href'))}" alt="${esc(img.alt || '')}"></div></div>`;
    d.body.append(loupe);
    loupe.querySelector('[data-fermer]').addEventListener('click', () => loupe.close());
    // Ajusté à la largeur d'abord ; « Agrandir » double la taille (et le pincement reste possible).
    loupe.querySelector('[data-zoom]').addEventListener('click', (ev) => {
      const z = loupe.classList.toggle('loupe--zoom');
      ev.currentTarget.textContent = z ? 'Ajuster' : 'Agrandir';
      ev.currentTarget.setAttribute('aria-pressed', String(z));
    });
    loupe.addEventListener('close', () => { loupe.remove(); a.focus({ preventScroll: true }); });
    loupe.showModal();
  });

  // ------------------------------------------------------------ Changer de catégorie
  d.querySelector('[data-cat-choix]')?.addEventListener('change', (e) => { location.href = e.target.value; });

  // ------------------------------------------------------------ Barre A–Z : la lettre courante visible sur téléphone
  // On centre la lettre courante en faisant défiler la barre elle-même (scrollIntoView déplacerait aussi la page).
  const courante = d.querySelector('.index-az a[aria-current]');
  if (courante) {
    const ol = courante.closest('ol');
    ol.scrollLeft = courante.offsetLeft - ol.clientWidth / 2 + courante.offsetWidth / 2;
  }
  const motCourant = d.querySelector('[data-mot]');
  const lireDerniers = () => { try { return JSON.parse(localStorage.getItem('derniers') || '[]'); } catch { return []; } };
  if (motCourant) {
    try {
      const liste = lireDerniers().filter((m) => m[0] !== motCourant.dataset.mot);
      liste.unshift([motCourant.dataset.mot, motCourant.dataset.titre]);
      localStorage.setItem('derniers', JSON.stringify(liste.slice(0, 8)));
    } catch {}
  }

  // ------------------------------------------------------------ Carte d'aperçu au survol des renvois (souris et clavier)
  if (d.querySelector('a[data-apercu]') && matchMedia('(hover: hover)').matches) {
    const carte = d.createElement('div');
    carte.className = 'carte-apercu';
    carte.setAttribute('role', 'tooltip');
    carte.id = 'carte-apercu';
    carte.hidden = true;
    d.body.append(carte);
    let minuteur = 0;
    let lien = null;
    const montrer = (a) => {
      clearTimeout(minuteur);
      minuteur = setTimeout(() => {
        lien = a;
        carte.innerHTML = `<p class="carte-nom">${esc(a.dataset.apercuNom || a.textContent.replace(/^Mot (précédent|suivant) : /, ''))}</p><p class="carte-cat">${esc(a.dataset.apercuCat || '')}</p><p class="carte-desc">${esc(a.dataset.apercu)}</p>`;
        carte.hidden = false;
        a.setAttribute('aria-describedby', 'carte-apercu');
        const r = a.getBoundingClientRect();
        const w = carte.offsetWidth;
        const x = Math.min(Math.max(12, r.left), innerWidth - w - 12);
        const dessous = r.bottom + carte.offsetHeight + 16 < innerHeight;
        carte.style.left = `${x}px`;
        carte.style.top = `${dessous ? r.bottom + 10 : r.top - carte.offsetHeight - 10}px`;
        carte.classList.toggle('carte-apercu--haut', !dessous);
      }, 280);
    };
    const cacher = () => { clearTimeout(minuteur); carte.hidden = true; lien?.removeAttribute('aria-describedby'); lien = null; };
    d.addEventListener('pointerover', (e) => { const a = e.target.closest('a[data-apercu]'); if (a) montrer(a); });
    d.addEventListener('pointerout', (e) => { const a = e.target.closest('a[data-apercu]'); if (a && !a.contains(e.relatedTarget)) cacher(); });
    d.addEventListener('focusin', (e) => { const a = e.target.closest('a[data-apercu]'); if (a) montrer(a); else cacher(); });
    d.addEventListener('keydown', (e) => { if (e.key === 'Escape') cacher(); });
    addEventListener('scroll', cacher, { passive: true });
  }

  // ------------------------------------------------------------ Transitions entre pages
  // Un nom cliqué (liste, renvoi, mot du jour) devient la vedette de la page suivante ;
  // « précédent / suivant » tourne la page. Le type est relu par le script en tête de page.
  d.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="/"]');
    if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target) return;
    root.classList.remove('vt-tour');
    d.querySelectorAll('[style*="view-transition-name"]').forEach((el) => el.style.removeProperty('view-transition-name'));
    if (a.dataset.turn) {
      try { sessionStorage.setItem('vt', a.dataset.turn === 'next' ? 'suivant' : 'precedent'); } catch {}
      root.classList.add('vt-tour');
      return;
    }
  });
  addEventListener('pageshow', () => {
    root.classList.remove('vt-tour');
    d.querySelectorAll('[style*="view-transition-name"]').forEach((el) => el.style.removeProperty('view-transition-name'));
  });
  // Flèches du clavier : mot précédent ou suivant dans l'ordre du livre.
  d.addEventListener('keydown', (e) => {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    if (e.target.closest('input, textarea, select, [contenteditable], [role="slider"], dialog')) return;
    const sens = e.key === 'ArrowLeft' ? 'prev' : e.key === 'ArrowRight' ? 'next' : null;
    if (!sens) return;
    const a = d.querySelector(`.reperes a[data-turn="${sens}"]`);
    if (a) { e.preventDefault(); a.click(); }
  });

  // ------------------------------------------------------------ Recherche : index et moteur
  const norm = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  // Même longueur que l'original : chaque caractère non alphanumérique devient une espace.
  const plat = (s) => norm(s).replace(/[^a-z0-9]/g, ' ');
  const compact = (s) => plat(s).replace(/ +/g, '');
  let index = null;
  let chargement = null;
  const charger = () => {
    if (index) return Promise.resolve(index);
    chargement ||= Promise.all([
      fetch('/recherche.json').then((r) => r.json()),
      fetch('/tranche.json').then((r) => r.json()).catch(() => ({ renvois: [] })),
    ]).then(([j, tranche]) => {
      index = j.terms.map(([title, slug, cat, alt, desc], i) => ({
        i, title, slug, alt, desc,
        cat: j.categories[cat] || ['', ''],
        poids: tranche.renvois?.[i] || 0,
        pt: plat(title), ct: compact(title), pa: plat(alt), pd: plat(desc),
        // La première partie d'un titre composé (« DLP - DISCRETE LOGARITHM PROBLEM ») compte comme titre exact ;
        // les suivantes sont souvent des qualificatifs (« FEE RATE - LIGHTNING »).
        parts: title.includes(' - ') ? title.split(' - ').map((x) => plat(x).trim()) : [],
      }));
      index.categories = j.categories;
      return index;
    });
    return chargement;
  };
  window.dicoIndex = charger;

  const lev = (a, b, max) => {
    if (Math.abs(a.length - b.length) > max) return max + 1;
    let prev = Array.from({ length: b.length + 1 }, (_, i) => i);
    for (let i = 1; i <= a.length; i++) {
      const cur = [i];
      let best = i;
      for (let j = 1; j <= b.length; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        best = Math.min(best, cur[j]);
      }
      if (best > max) return max + 1;
      prev = cur;
    }
    return prev[b.length];
  };

  // Rang d'un terme, du plus fort au plus faible : terme exact (titre, partie du titre ou terme anglais),
  // début du titre, début du terme anglais, début d'un mot du titre, puis milieu de mot et description,
  // gardés seulement quand les rangs forts donnent peu de résultats. Fautes de frappe en dernier recours.
  // À rang égal, le terme le plus renvoyé par les autres définitions passe devant.
  // Mots anglais et formes courantes vers le vocabulaire du dictionnaire.
  const SYNONYMES = {
    wallet: 'portefeuille', seed: 'graine', key: 'cle', keys: 'cles', clef: 'cle', clefs: 'cles', address: 'adresse', fee: 'frais', fees: 'frais',
    mnemonic: 'phrase de recuperation', 'seed phrase': 'phrase de recuperation', '12 mots': 'phrase de recuperation',
    '24 mots': 'phrase de recuperation', block: 'bloc', mining: 'minage', miner: 'mineur', node: 'noeud', channel: 'canal',
    signature: 'signature', privacy: 'confidentialite', transaction: 'transaction', hash: 'hachage',
  };
  function chercher(q, { cat = '', limite = 60 } = {}) {
    // « bip32 », « BIP 32 », « bip-0032 » : la forme du dictionnaire, BIP-0032.
    const bip = q.trim().match(/^bip\s*-?\s*(\d{1,4})$/i);
    if (bip) q = `BIP-${bip[1].padStart(4, '0')}`;
    const pq = plat(q).replace(/ +/g, ' ').trim();
    if (!pq || !index) return { res: [], approx: false };
    const cq = pq.replace(/ /g, '');
    const mots = pq.split(' ');
    const forts = [];
    const faibles = [];
    for (const t of index) {
      if (cat && t.cat[1] !== cat) continue;
      const titre = t.pt.replace(/ +/g, ' ').trim();
      const alt = t.pa.replace(/ +/g, ' ').trim();
      let rang = 0;
      let at = -1;
      if (titre === pq || t.parts[0] === pq) { rang = 10; at = t.pt.indexOf(pq); }
      else if (t.parts.includes(pq)) { rang = 9.5; at = t.pt.indexOf(pq); }
      else if (alt && alt === pq) rang = 9;
      else if (` ${titre} `.includes(` ${pq} `)) { rang = 8.5; at = t.pt.indexOf(pq); }
      else if (t.pt.startsWith(pq)) { rang = 8; at = 0; }
      else if (cq.length > 1 && t.ct.startsWith(cq)) rang = 7;
      else if (alt && alt.startsWith(pq)) rang = 6;
      else if ((at = t.pt.indexOf(` ${pq}`)) > -1) { rang = 5; at += 1; }
      else if (alt && alt.includes(` ${pq}`)) rang = 4;
      else if (mots.length > 1 && mots.every((m) => t.pt.includes(` ${m}`) || t.pt.startsWith(m))) rang = 4;
      if (rang) { forts.push({ t, rang, at, len: pq.length }); continue; }
      if ((at = t.pt.indexOf(pq)) > -1) faibles.push({ t, rang: 2, at, len: pq.length });
      else if (mots.length > 1 && mots.every((m) => ` ${t.pt} ${t.pa} ${t.pd}`.includes(` ${m}`))) {
        // Plusieurs mots trouvés çà et là : devant, ceux dont un mot cherché est le titre ou un mot du titre (« hd wallet » → HD).
        const dansTitre = mots.filter((m) => t.parts.includes(m) || ` ${t.pt}`.includes(` ${m}`)).length;
        faibles.push({ t, rang: 1.5 + dansTitre * 0.2 + (mots.includes(t.parts[0]) ? 0.3 : 0), at: -1 });
      }
      else if (pq.length > 2 && (t.pd.startsWith(pq) || t.pd.includes(` ${pq}`))) faibles.push({ t, rang: 1, at: -1 });
    }
    // Les correspondances faibles (milieu de mot, description) ne viennent que si les fortes sont rares.
    // Synonymes : une requête anglaise ou courante cherche aussi sa forme du dictionnaire.
    const syn = SYNONYMES[pq] || (mots.length > 1 ? mots.map((m) => SYNONYMES[m] || m).join(' ') : '');
    if (syn && syn !== pq && !arguments[1]?.sansSynonyme) {
      const vus = new Set(forts.concat(faibles).map((r) => r.t.slug));
      for (const r of chercher(syn, { cat, limite: 30, sansSynonyme: true }).res) if (!vus.has(r.t.slug)) faibles.push({ ...r, rang: Math.min(r.rang, 3), at: -1 });
    }
    // « cle » : s'il y a assez de titres où c'est un mot entier (CLÉ PUBLIQUE…), on n'y mêle pas les débuts de mot (CLEMENTINE).
    const entiers = forts.filter((r) => r.rang >= 8.5);
    let res = entiers.length >= 5 ? entiers : forts.length >= 5 ? forts : forts.concat(faibles);
    let approx = false;
    if (!res.length && cq.length > 2) {
      approx = true;
      const max = cq.length < 6 ? 1 : 2;
      for (const t of index) {
        if (cat && t.cat[1] !== cat) continue;
        // Une faute de frappe garde en général la première lettre : on ne propose rien d'autre.
        if (t.ct[0] !== cq[0]) continue;
        const dist = Math.min(lev(cq, t.ct, max), lev(cq, t.ct.slice(0, cq.length), max) + 1);
        if (dist <= max) res.push({ t, rang: -dist, at: -1 });
      }
    }
    res.sort((a, b) => b.rang - a.rang || b.t.poids - a.t.poids || a.t.title.length - b.t.title.length || a.t.i - b.t.i);
    return { res: res.slice(0, limite), approx, total: res.length, tous: res };
  }
  window.dicoChercher = (q, o) => charger().then(() => chercher(q, o));

  const surligner = (title, at, len) => { title = affiche(title); return at < 0 ? esc(title) : `${esc(title.slice(0, at))}<mark>${esc(title.slice(at, at + len))}</mark>${esc(title.slice(at + len))}`; };
  const picto = (slug) => `<svg class="picto" aria-hidden="true" focusable="false"><use href="/img/pictos.svg#p-${slug}"/></svg>`;
  const ligne = ({ t, at, len }, i, prefix) => `<li class="resultat" role="option" id="${prefix}-${i}" aria-selected="false">
  <a href="/${t.slug}/" tabindex="-1"><span class="resultat-nom" data-vt-nom>${surligner(t.title, at, len)}</span><span class="resultat-cat">${picto(t.cat[1])}${esc(t.cat[0])}</span>${t.alt ? `<span class="resultat-alt">${esc(t.alt)}</span>` : ''}${t.desc ? `<span class="resultat-desc">${esc(resume(t.desc))}</span>` : ''}</a></li>`;
  const pluriel = (n, un, plusieurs) => `${n.toLocaleString('fr-FR')} ${n > 1 ? plusieurs : un}`;
  const jour = () => Math.floor((Date.now() - new Date().getTimezoneOffset() * 60000) / 86400000);

  // ------------------------------------------------------------ Fenêtre de recherche
  const dialog = d.getElementById('recherche');
  const champ = dialog?.querySelector('input');
  const liste = dialog?.querySelector('.resultats');
  const etat = dialog?.querySelector('.recherche-etat');
  let actif = -1;
  let declencheur = null;

  function selectionner(i) {
    const items = liste.querySelectorAll('.resultat');
    if (!items.length) { actif = -1; champ.removeAttribute('aria-activedescendant'); return; }
    actif = (i + items.length) % items.length;
    items.forEach((el, k) => el.setAttribute('aria-selected', String(k === actif)));
    champ.setAttribute('aria-activedescendant', items[actif].id);
    items[actif].scrollIntoView({ block: 'nearest' });
  }

  function suggestions(avecCategories) {
    const n = index ? index[jour() % index.length] : null;
    const h = index ? index[Math.floor(Math.random() * index.length)] : null;
    const lettres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').map((l) => `<a href="/lettre/${l.toLowerCase()}/">${l}</a>`).join('');
    const derniers = lireDerniers().filter((m) => !motCourant || m[0] !== motCourant.dataset.mot).slice(0, 5);
    const cats = avecCategories && index?.categories ? `<p>Ou par catégorie&#8239;:</p><div class="cats-mini">${index.categories.map(([label, slug]) => `<a href="/categorie/${slug}/">${picto(slug)}${esc(label)}</a>`).join('')}</div>` : '';
    return `<li class="suggestions-vides" role="presentation">${derniers.length ? `<p>Vos derniers mots&#8239;: ${derniers.map((m) => `<a class="lien" href="/${esc(m[0])}/">${esc(m[1])}</a>`).join(', ')}.</p>` : ''}${n ? `<p>Le mot du jour&#8239;: <a class="lien" href="/${n.slug}/">${esc(affiche(n.title))}</a>. Un mot au hasard&#8239;: <a class="lien" href="/${h.slug}/">${esc(affiche(h.title))}</a>.</p>` : ''}<p>Ou par lettre&#8239;:</p><div class="abc">${lettres}</div>${cats}</li>`;
  }

  function vide() {
    etat.textContent = '';
    liste.innerHTML = suggestions(false);
    champ.setAttribute('aria-expanded', 'false');
    actif = -1;
  }

  function afficher() {
    const q = champ.value;
    if (!q.trim()) return vide();
    const { res, approx, total } = chercher(q);
    if (!res.length) {
      etat.innerHTML = `Aucun mot ne correspond à «&#8239;${esc(q.trim())}&#8239;». Essayez le terme anglais ou un sigle, ou repartez d’ici&#8239;:`;
      liste.innerHTML = suggestions(true);
      champ.setAttribute('aria-expanded', 'false');
      return;
    }
    etat.textContent = approx ? `Aucun mot exact. Vouliez-vous dire :` : total > res.length ? `${pluriel(total, 'résultat', 'résultats')}, les ${res.length} premiers` : pluriel(total, 'résultat', 'résultats');
    liste.innerHTML = res.map((r, i) => ligne(r, i, 'res')).join('');
    champ.setAttribute('aria-expanded', 'true');
    selectionner(0);
  }

  function ouvrir(valeur = '', depuis = null) {
    if (!dialog || dialog.open) return;
    declencheur = depuis;
    champ.value = valeur;
    dialog.showModal();
    champ.focus();
    if (valeur) champ.setSelectionRange(valeur.length, valeur.length);
    // La fenêtre s'ouvre depuis le bouton ou le champ qui l'a appelée.
    if (depuis && !reduit.matches && dialog.animate) {
      const a = depuis.getBoundingClientRect();
      const b = dialog.getBoundingClientRect();
      if (b.width && a.width) {
        dialog.animate([
          { transform: `translate(${a.left - b.left}px, ${a.top - b.top}px) scale(${a.width / b.width}, ${Math.max(a.height / b.height, 0.08)})`, opacity: 0.4 },
          { transform: 'none', opacity: 1 },
        ], { duration: 300, easing: 'cubic-bezier(0.22, 1, 0.36, 1)' });
        dialog.style.transformOrigin = '0 0';
      }
    }
    charger().then(afficher).catch(() => { etat.textContent = 'L’index de recherche n’a pas pu être chargé. Vérifiez la connexion, ou parcourez par lettre.'; });
  }
  window.dicoOuvrirRecherche = ouvrir;

  if (dialog) {
    champ.addEventListener('input', () => (index ? afficher() : charger().then(afficher)));
    champ.addEventListener('keydown', (e) => {
      // Échap ferme la fenêtre d'un coup (un champ « search » se contenterait d'effacer son texte).
      if (e.key === 'Escape') { e.preventDefault(); dialog.close(); return; }
      if (e.key === 'ArrowDown') { e.preventDefault(); selectionner(actif + 1); }
      else if (e.key === 'ArrowUp') { e.preventDefault(); selectionner(actif - 1); }
      else if (e.key === 'Enter') {
        const a = liste.querySelectorAll('.resultat a')[Math.max(actif, 0)];
        if (a) { e.preventDefault(); a.click(); }
      }
    });
    liste.addEventListener('mousemove', (e) => {
      const li = e.target.closest('.resultat');
      if (!li) return;
      const i = [...liste.querySelectorAll('.resultat')].indexOf(li);
      if (i !== actif) selectionner(i);
    });
    dialog.addEventListener('click', (e) => {
      if (e.target === dialog || e.target.closest('[data-search-close]')) dialog.close();
    });
    dialog.addEventListener('close', () => { declencheur?.focus?.({ preventScroll: true }); });
    d.addEventListener('click', (e) => {
      const b = e.target.closest('[data-search-open]');
      if (!b) return;
      e.preventDefault();
      const m = d.getElementById('menu');
      if (m?.open) { m.close(); ouvrir('', d.querySelector('.barre [data-search-open]')); }
      else ouvrir('', b);
    });
    d.addEventListener('keydown', (e) => {
      const k = e.key.toLowerCase();
      if ((k === 'k' && (e.ctrlKey || e.metaKey)) || (k === '/' && !e.target.closest('input, textarea, [contenteditable]'))) {
        e.preventDefault();
        if (dialog.open) champ.select(); else ouvrir('', d.querySelector('[data-search-open]'));
      }
    });
    if (/Mac|iPhone|iPad/.test(navigator.platform)) d.querySelectorAll('[data-kbd]').forEach((k) => (k.textContent = '⌘ K'));
    // Le champ de la couverture s'ouvre en fenêtre (plein écran sur téléphone) avec ce qui est déjà tapé.
    const heros = d.querySelector('[data-hero-search]');
    if (heros) {
      const input = heros.querySelector('input');
      input.addEventListener('focus', () => { ouvrir(input.value, heros); input.value = ''; });
      heros.addEventListener('submit', (e) => { e.preventDefault(); ouvrir(input.value, heros); });
    }
    // Préchargement discret de l'index quand on survole un bouton de recherche.
    d.addEventListener('pointerover', (e) => { if (e.target.closest('[data-search-open], [data-hero-search]')) charger(); }, { passive: true });
  }

  // ------------------------------------------------------------ Menu (téléphone et tablette)
  const menu = d.getElementById('menu');
  if (menu) {
    d.addEventListener('click', (e) => {
      if (e.target.closest('[data-menu-open]')) { e.preventDefault(); menu.showModal(); }
      else if (e.target === menu || e.target.closest('[data-menu-close]')) menu.close();
    });
    menu.addEventListener('close', () => d.querySelector('[data-menu-open]')?.focus({ preventScroll: true }));
  }

  // Mots les plus proches à l'orthographe, quand rien ne correspond (404, recherche sans résultat).
  const proches = (q, n, exclus = new Set()) => {
    const cq = compact(q);
    if (cq.length < 2) return [];
    return index
      .filter((t) => !exclus.has(t.slug))
      .map((t) => ({ t, s: Math.min(lev(cq, t.ct, 8), lev(cq, t.ct.slice(0, cq.length), 8) + 1), at: -1 }))
      .filter((r) => r.s <= Math.max(3, Math.floor(cq.length / 2)))
      .sort((a, b) => a.s - b.s || b.t.poids - a.t.poids)
      .slice(0, n);
  };

  // ------------------------------------------------------------ Page de recherche
  const pageForm = d.querySelector('[data-search-page]');
  if (pageForm) {
    const input = pageForm.querySelector('input');
    const sortie = d.querySelector('[data-search-results]');
    const statut = d.querySelector('[data-search-status]');
    const filtres = d.querySelector('[data-filtres]');
    const select = null;
    const params = new URLSearchParams(location.search);
    input.value = params.get('q') || '';
    let cat = params.get('cat') || '';
    let tout = false;
    // Les étiquettes de catégorie montrent combien de résultats chacune contient ; seules celles qui en ont restent.
    const etiquettes = (tous) => {
      const n = new Map();
      for (const r of tous) n.set(r.t.cat[1], (n.get(r.t.cat[1]) || 0) + 1);
      const liste = index.categories.filter(([, slug]) => n.has(slug) || slug === cat).sort((a, b) => (n.get(b[1]) || 0) - (n.get(a[1]) || 0));
      const visibles = tout ? liste : liste.slice(0, 8);
      filtres.innerHTML = `<legend class="masque">Filtrer par catégorie</legend>
        <label class="filtre"><input type="radio" name="cat" value=""${cat ? '' : ' checked'}><span>Toutes <b>${tous.length}</b></span></label>
        ${visibles.map(([label, slug]) => `<label class="filtre"><input type="radio" name="cat" value="${slug}"${slug === cat ? ' checked' : ''}><span>${picto(slug)}${esc(label)} <b>${n.get(slug) || 0}</b></span></label>`).join('')}
        ${liste.length > visibles.length ? `<button class="filtre-plus" type="button" data-filtres-plus>+ ${liste.length - visibles.length}</button>` : ''}`;
      if (select) select.innerHTML = `<option value="">Toutes les catégories (${tous.length})</option>${liste.map(([label, slug]) => `<option value="${slug}"${slug === cat ? ' selected' : ''}>${esc(label)} (${n.get(slug) || 0})</option>`).join('')}`;
    };
    const lancer = () => {
      const q = input.value;
      const u = new URL(location.href);
      u.searchParams.set('q', q);
      if (cat) u.searchParams.set('cat', cat); else u.searchParams.delete('cat');
      history.replaceState(null, '', u);
      if (!q.trim()) {
        sortie.innerHTML = '';
        filtres.innerHTML = '';
        statut.textContent = `Tapez un terme : la recherche porte sur les ${index.length.toLocaleString('fr-FR')} définitions, leur terme anglais et leur description.`;
        sortie.innerHTML = suggestions(true);
        return;
      }
      const tous = chercher(q, { limite: 2000 });
      etiquettes(tous.tous || []);
      const { res, approx, total } = chercher(q, { cat, limite: 200 });
      if (!res.length) {
        const p = proches(q, 5);
        statut.innerHTML = `Aucun mot ne correspond à «&#8239;${esc(q.trim())}&#8239;». ${p.length ? 'Les mots les plus proches&#8239;:' : 'Essayez le terme anglais ou un sigle, ou repartez des lettres et des catégories&#8239;:'}`;
        sortie.innerHTML = p.map((r, i) => ligne(r, i, 'page')).join('') + suggestions(true);
      } else {
        statut.textContent = approx ? 'Aucun mot exact. Vouliez-vous dire :' : pluriel(total, 'résultat', 'résultats');
        sortie.innerHTML = res.map((r, i) => ligne(r, i, 'page')).join('');
        // Premier affichage : les rangées arrivent l'une après l'autre (une fois, pas à chaque frappe).
        if (!sortie.dataset.vu) {
          sortie.dataset.vu = '1';
          sortie.querySelectorAll('.resultat').forEach((li, k) => li.style.setProperty('--k', Math.min(k, 12)));
          sortie.classList.add('arrivee');
          setTimeout(() => sortie.classList.remove('arrivee'), 1200);
        }
      }
      sortie.querySelectorAll('a').forEach((a) => a.removeAttribute('tabindex'));
    };
    statut.textContent = 'Chargement de l’index…';
    charger().then(() => { lancer(); if (!input.value) input.focus(); });
    input.addEventListener('input', () => index && lancer());
    filtres.addEventListener('change', (e) => { cat = e.target.value; index && lancer(); });
    filtres.addEventListener('click', (e) => { if (e.target.closest('[data-filtres-plus]')) { tout = true; index && lancer(); } });
    select?.addEventListener('change', () => { cat = select.value; index && lancer(); });
    pageForm.addEventListener('submit', (e) => { e.preventDefault(); index && lancer(); });
  }

  // ------------------------------------------------------------ 404 : recherche directe sous le champ, prérempli avec l'adresse
  const sugg = d.querySelector('[data-suggestions]');
  if (sugg) {
    const morceau = decodeURIComponent(location.pathname).replace(/^\/+|\/+$/g, '').split('/').pop() || '';
    const q0 = morceau.replace(/[-_]+/g, ' ').replace(/\.html?$/, '');
    const form = d.querySelector('[data-perdu-champ]');
    const champPerdu = form.querySelector('input');
    const liste404 = sugg.querySelector('[data-suggestions-liste]');
    const titre404 = sugg.querySelector('[data-suggestions-titre]');
    if (q0.length > 1 && q0 !== '404') champPerdu.value = q0;
    const montrer404 = () => {
      const q = champPerdu.value;
      if (q.trim().length < 2) { sugg.hidden = true; return; }
      let { res } = chercher(q, { limite: 5 });
      if (res.length < 3) {
        const vus = new Set(res.map((r) => r.t.slug));
        res = res.concat(proches(q, 3 - res.length, vus));
      }
      titre404.textContent = q === q0 ? 'Vouliez-vous dire' : 'Résultats';
      liste404.innerHTML = res.map(({ t }) => `<li><a href="/${t.slug}/"><span class="perdu-nom">${esc(affiche(t.title))}</span>${t.desc ? `<span class="perdu-desc">${esc(resume(t.desc))}</span>` : ''}</a></li>`).join('');
      sugg.hidden = !res.length;
    };
    charger().then(montrer404);
    champPerdu.addEventListener('input', () => index && montrer404());
    form.addEventListener('submit', (e) => {
      const a = liste404.querySelector('a');
      if (a) { e.preventDefault(); a.click(); }
    });
  }

  // ------------------------------------------------------------ Rangée collante d'une liste (sous-groupes d'une lettre, alphabet d'une catégorie) :
  // le groupe lu est marqué, et la rangée le garde en vue.
  const sousIndex = d.querySelector('.liste-bloc .sous-index ul, .liste-bloc .index-az ol');
  if (sousIndex) {
    // Plusieurs lettres peuvent mener au même groupe (« J – L ») : on garde la première.
    const puces = new Map();
    for (const a of sousIndex.querySelectorAll('a')) if (!puces.has(a.hash.slice(1))) puces.set(a.hash.slice(1), a);
    const titres = [...puces.keys()].map((id) => d.getElementById(id)?.closest('.groupe')).filter(Boolean);
    let marque = null;
    const marquer = () => {
      const ligne = (parseFloat(getComputedStyle(d.documentElement).getPropertyValue('--haut')) || 0) + 120;
      let actif = null;
      for (const g of titres) { if (g.getBoundingClientRect().top <= ligne) actif = g; else break; }
      const puce = actif ? puces.get(actif.getAttribute('aria-labelledby')) : null;
      if (puce === marque) return;
      marque?.removeAttribute('aria-current');
      marque = puce;
      if (!puce) return;
      puce.setAttribute('aria-current', 'location');
      sousIndex.scrollLeft = puce.offsetLeft - sousIndex.clientWidth / 2 + puce.offsetWidth / 2;
    };
    addEventListener('scroll', () => requestAnimationFrame(marquer), { passive: true });
  }
  if (d.querySelector('.liste')) {
    const haut = d.createElement('button');
    haut.type = 'button';
    haut.className = 'haut';
    haut.textContent = '↑';
    haut.setAttribute('aria-label', 'Revenir en haut de la page');
    haut.hidden = true;
    haut.addEventListener('click', () => { scrollTo({ top: 0, behavior: reduit.matches ? 'auto' : 'smooth' }); d.querySelector('h1')?.focus?.(); });
    d.body.append(haut);
    let piedVisible = false;
    const pied = d.querySelector('.dos');
    // Visible en remontant (quand la barre revient), après le premier écran, jamais sur le pied : il ne cache pas la lecture.
    const majHaut = () => { haut.hidden = piedVisible || scrollY < innerHeight || !!barre?.classList.contains('est-cachee'); };
    if (pied) new IntersectionObserver(([e]) => { piedVisible = e.isIntersecting; majHaut(); }).observe(pied);
    addEventListener('scroll', () => requestAnimationFrame(majHaut), { passive: true });
  }

  // ------------------------------------------------------------ Présentation de catégorie repliée : « Lire la suite »
  const suite = d.querySelector('[data-repliable-suite]');
  if (suite) {
    const b = d.createElement('button');
    b.type = 'button';
    b.className = 'lire-suite';
    b.textContent = 'Lire la suite';
    b.setAttribute('aria-expanded', 'false');
    b.addEventListener('click', () => { suite.closest('.cat-note').classList.add('deplie'); b.remove(); });
    suite.closest('.cat-note').after(b);
  }
})();
