// Dictionnaire de Bitcoin : scripts communs à toutes les pages.
// Thème, barre, apparitions, transitions entre pages, recherche, suggestions de la 404.
(() => {
  const d = document;
  const root = d.documentElement;
  const reduit = matchMedia('(prefers-reduced-motion: reduce)');
  root.classList.add('anim');
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
  const aVoir = d.querySelectorAll('.jour, .feuilleter, .categories, .pages, .alphabet, .groupe, .liste > .entrees');
  for (const el of aVoir) {
    const enfants = el.matches('.feuilleter') ? el.querySelectorAll('.blocs li') : el.matches('.categories') ? el.querySelectorAll('.index-ligne') : el.matches('.alphabet') ? el.querySelectorAll('li') : el.matches('.groupe, .entrees') ? el.querySelectorAll('.entrees li') : [];
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
    const fiches = new Map([...d.querySelectorAll('.entree')].map((a) => [a.getAttribute('href'), a.dataset]));
    const boite = d.querySelector('[data-apercu-lettre]');
    const geste = d.querySelector('[data-geste]');
    const tactile = matchMedia('(pointer: coarse)').matches;
    if (geste) geste.textContent = tactile ? 'Glissez le doigt sur les traits, puis touchez le mot.' : 'Survolez les traits.';
    let vise = -1;
    const viser = (k) => {
      k = Math.max(0, Math.min(traits.length - 1, k));
      if (k === vise) return;
      traits[vise]?.classList.remove('est-vise');
      vise = k;
      const a = traits[k];
      a.classList.add('est-vise');
      const f = fiches.get(a.getAttribute('href')) || {};
      const lien = boite.querySelector('a');
      lien.href = a.getAttribute('href');
      lien.textContent = f.apercuNom || a.querySelector('title').textContent;
      boite.querySelector('.apercu-lettre-cat').textContent = f.apercuCat || '';
      boite.querySelector('.apercu-lettre-desc').textContent = f.apercu || '';
      boite.hidden = false;
    };
    const depuis = (e) => {
      const r = tl.getBoundingClientRect();
      viser(Math.floor(((e.clientX - r.left) / r.width) * traits.length));
    };
    tl.addEventListener('pointermove', depuis);
    tl.addEventListener('pointerdown', depuis);
    tl.addEventListener('click', (e) => {
      if (tactile) { e.preventDefault(); return; }
      e.preventDefault();
      if (vise > -1) location.href = traits[vise].getAttribute('href');
    });
  }

  // ------------------------------------------------------------ Jaquette : l'arbre suit doucement le curseur (profondeur)
  const arbre = d.querySelector('.p-accueil .arbre');
  if (arbre && matchMedia('(hover: hover) and (pointer: fine)').matches && !reduit.matches) {
    const couv = arbre.closest('.jaquette');
    let raf = 0;
    couv.addEventListener('pointermove', (e) => {
      cancelAnimationFrame(raf);
      raf = requestAnimationFrame(() => {
        const r = couv.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        arbre.style.translate = `${(-x * 14).toFixed(1)}px ${(-y * 10).toFixed(1)}px`;
      });
    });
    couv.addEventListener('pointerleave', () => (arbre.style.translate = '0 0'));
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
    loupe.innerHTML = `<div class="loupe-panneau"><div class="loupe-tete"><p class="loupe-legende">${esc(img.alt || 'Schéma')}</p><button class="recherche-fermer" type="button">Fermer</button></div><div class="loupe-zone"><img src="${esc(a.getAttribute('href'))}" alt="${esc(img.alt || '')}"></div></div>`;
    d.body.append(loupe);
    loupe.querySelector('button').addEventListener('click', () => loupe.close());
    loupe.addEventListener('close', () => { loupe.remove(); a.focus({ preventScroll: true }); });
    loupe.showModal();
  });

  // ------------------------------------------------------------ Changer de catégorie
  d.querySelector('[data-cat-choix]')?.addEventListener('change', (e) => { location.href = e.target.value; });

  // ------------------------------------------------------------ Barre A–Z : la lettre courante visible sur téléphone
  d.querySelector('.index-az a[aria-current]')?.scrollIntoView({ block: 'nearest', inline: 'center' });
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
  if (d.querySelector('[data-apercu]') && matchMedia('(hover: hover)').matches) {
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
    d.addEventListener('pointerover', (e) => { const a = e.target.closest('[data-apercu]'); if (a) montrer(a); });
    d.addEventListener('pointerout', (e) => { const a = e.target.closest('[data-apercu]'); if (a && !a.contains(e.relatedTarget)) cacher(); });
    d.addEventListener('focusin', (e) => { const a = e.target.closest('[data-apercu]'); if (a) montrer(a); else cacher(); });
    d.addEventListener('keydown', (e) => { if (e.key === 'Escape') cacher(); });
    addEventListener('scroll', cacher, { passive: true });
  }

  // ------------------------------------------------------------ Transitions entre pages
  // Un nom cliqué (liste, renvoi, mot du jour) devient la vedette de la page suivante ;
  // « précédent / suivant » tourne la page. Le type est relu par le script en tête de page.
  d.addEventListener('click', (e) => {
    const a = e.target.closest('a[href^="/"]');
    if (!a || e.defaultPrevented || e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target) return;
    root.classList.remove('vt-tour', 'vt-morph');
    d.querySelectorAll('[style*="view-transition-name"]').forEach((el) => el.style.removeProperty('view-transition-name'));
    if (a.dataset.turn) {
      try { sessionStorage.setItem('vt', a.dataset.turn === 'next' ? 'suivant' : 'precedent'); } catch {}
      root.classList.add('vt-tour');
      return;
    }
    const nom = a.querySelector('[data-vt-nom]');
    if (nom) {
      root.classList.add('vt-morph');
      nom.style.viewTransitionName = 'mot';
    }
  });
  addEventListener('pageshow', () => {
    root.classList.remove('vt-tour', 'vt-morph');
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
  function chercher(q, { cat = '', limite = 60 } = {}) {
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
      else if (alt && alt === pq) rang = 9;
      else if (t.pt.startsWith(pq)) { rang = 8; at = 0; }
      else if (cq.length > 1 && t.ct.startsWith(cq)) rang = 7;
      else if (alt && alt.startsWith(pq)) rang = 6;
      else if ((at = t.pt.indexOf(` ${pq}`)) > -1) { rang = 5; at += 1; }
      else if (alt && alt.includes(` ${pq}`)) rang = 4;
      else if (mots.length > 1 && mots.every((m) => t.pt.includes(` ${m}`) || t.pt.startsWith(m))) rang = 4;
      if (rang) { forts.push({ t, rang, at, len: pq.length }); continue; }
      if ((at = t.pt.indexOf(pq)) > -1) faibles.push({ t, rang: 2, at, len: pq.length });
      else if (pq.length > 2 && (t.pd.startsWith(pq) || t.pd.includes(` ${pq}`))) faibles.push({ t, rang: 1, at: -1 });
    }
    let res = forts.length >= 5 ? forts : forts.concat(faibles);
    let approx = false;
    if (!res.length && cq.length > 2) {
      approx = true;
      const max = cq.length < 6 ? 1 : 2;
      for (const t of index) {
        if (cat && t.cat[1] !== cat) continue;
        const dist = Math.min(lev(cq, t.ct, max), lev(cq, t.ct.slice(0, cq.length), max) + 1);
        if (dist <= max) res.push({ t, rang: -dist, at: -1 });
      }
    }
    res.sort((a, b) => b.rang - a.rang || b.t.poids - a.t.poids || a.t.title.length - b.t.title.length || a.t.i - b.t.i);
    return { res: res.slice(0, limite), approx, total: res.length };
  }
  window.dicoChercher = (q, o) => charger().then(() => chercher(q, o));

  const surligner = (title, at, len) => (at < 0 ? esc(title) : `${esc(title.slice(0, at))}<mark>${esc(title.slice(at, at + len))}</mark>${esc(title.slice(at + len))}`);
  const picto = (slug) => `<svg class="picto" aria-hidden="true" focusable="false"><use href="/img/pictos.svg#p-${slug}"/></svg>`;
  const ligne = ({ t, at, len }, i, prefix) => `<li class="resultat" role="option" id="${prefix}-${i}" aria-selected="false">
  <a href="/${t.slug}/" tabindex="-1"><span class="resultat-nom" data-vt-nom>${surligner(t.title, at, len)}</span><span class="resultat-cat">${picto(t.cat[1])}${esc(t.cat[0])}</span>${t.alt ? `<span class="resultat-alt">${esc(t.alt)}</span>` : ''}${t.desc ? `<span class="resultat-desc">${esc(t.desc)}</span>` : ''}</a></li>`;
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
    return `<li class="suggestions-vides" role="presentation">${derniers.length ? `<p>Vos derniers mots&#8239;: ${derniers.map((m) => `<a class="lien" href="/${esc(m[0])}/">${esc(m[1])}</a>`).join(', ')}.</p>` : ''}${n ? `<p>Le mot du jour&#8239;: <a class="lien" href="/${n.slug}/">${esc(n.title)}</a>. Un mot au hasard&#8239;: <a class="lien" href="/${h.slug}/">${esc(h.title)}</a>.</p>` : ''}<p>Ou par lettre&#8239;:</p><div class="lettres-mini">${lettres}</div>${cats}</li>`;
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

  // ------------------------------------------------------------ Page de recherche
  const pageForm = d.querySelector('[data-search-page]');
  if (pageForm) {
    const input = pageForm.querySelector('input');
    const sortie = d.querySelector('[data-search-results]');
    const statut = d.querySelector('[data-search-status]');
    const filtres = d.querySelector('[data-filtres]');
    const params = new URLSearchParams(location.search);
    input.value = params.get('q') || '';
    const catInit = params.get('cat') || '';
    const radio = filtres.querySelector(`input[value="${CSS.escape(catInit)}"]`);
    if (radio) radio.checked = true;
    const lancer = () => {
      const q = input.value;
      const cat = filtres.querySelector('input:checked')?.value || '';
      const u = new URL(location.href);
      u.searchParams.set('q', q);
      if (cat) u.searchParams.set('cat', cat); else u.searchParams.delete('cat');
      history.replaceState(null, '', u);
      if (!q.trim()) {
        sortie.innerHTML = '';
        statut.textContent = cat ? 'Tapez un terme pour chercher dans cette catégorie.' : `Tapez un terme : la recherche porte sur les ${index.length.toLocaleString('fr-FR')} définitions, leur terme anglais et leur description.`;
        return;
      }
      const { res, approx, total } = chercher(q, { cat, limite: 200 });
      statut.textContent = !res.length ? `Aucun mot ne correspond à « ${q.trim()} ». Essayez le terme anglais, un sigle, ou une autre catégorie.` : approx ? 'Aucun mot exact. Vouliez-vous dire :' : pluriel(total, 'résultat', 'résultats');
      sortie.innerHTML = res.map((r, i) => ligne(r, i, 'page')).join('');
      sortie.querySelectorAll('a').forEach((a) => a.removeAttribute('tabindex'));
    };
    statut.textContent = 'Chargement de l’index…';
    charger().then(() => { lancer(); input.focus(); });
    input.addEventListener('input', () => index && lancer());
    filtres.addEventListener('change', () => index && lancer());
    // Sur téléphone, une liste déroulante remplace les étiquettes ; les deux restent synchronisées.
    const select = d.querySelector('[data-filtre-liste]');
    if (select) {
      select.value = catInit;
      select.addEventListener('change', () => {
        const r = filtres.querySelector(`input[value="${CSS.escape(select.value)}"]`);
        if (r) { r.checked = true; index && lancer(); }
      });
    }
    pageForm.addEventListener('submit', (e) => { e.preventDefault(); index && lancer(); });
  }

  // ------------------------------------------------------------ 404 : « Vouliez-vous dire »
  const sugg = d.querySelector('[data-suggestions]');
  if (sugg) {
    const morceau = decodeURIComponent(location.pathname).replace(/^\/+|\/+$/g, '').split('/').pop() || '';
    const q = morceau.replace(/[-_]+/g, ' ').replace(/\.html?$/, '');
    const champPerdu = d.querySelector('[data-perdu-champ] input');
    if (champPerdu && q.length > 1 && q !== '404') champPerdu.value = q;
    if (q.length > 1) {
      charger().then(() => {
        let { res } = chercher(q, { limite: 3 });
        if (res.length < 3) {
          const cq = compact(q);
          const vus = new Set(res.map((r) => r.t.slug));
          const proches = index
            .filter((t) => !vus.has(t.slug))
            .map((t) => ({ t, s: Math.min(lev(cq, t.ct, 8), lev(cq, t.ct.slice(0, cq.length), 8) + 1) }))
            .filter((r) => r.s <= Math.max(3, Math.floor(cq.length / 2)))
            .sort((a, b) => a.s - b.s || b.t.poids - a.t.poids)
            .slice(0, 3 - res.length);
          res = res.concat(proches);
        }
        if (!res.length) return;
        sugg.querySelector('[data-suggestions-liste]').innerHTML = res.map(({ t }) => `<li><a href="/${t.slug}/">${esc(t.title)}</a></li>`).join('');
        sugg.hidden = false;
      });
    }
  }
})();
