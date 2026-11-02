// Dictionnaire de Bitcoin : scripts communs à toutes les pages.
// Thème, barre, apparitions, transitions entre pages, recherche, suggestions de la 404.
(() => {
  const d = document;
  const root = d.documentElement;
  const reduit = matchMedia('(prefers-reduced-motion: reduce)');
  root.classList.add('anim');
  // Langue de la page : préfixe des adresses (« » ou « /en ») et textes de l'interface (lib/i18n.mjs, js).
  const B = root.dataset.base || '';
  let T = {};
  try { T = JSON.parse(d.getElementById('i18n')?.textContent || '{}'); } catch {}
  const tx = (k, v = {}) => String(T[k] ?? k).replace(/\{(\w+)\}/g, (_, x) => v[x] ?? '');
  const loc = T.locale || 'fr-FR';
  window.dicoTexte = tx;
  const affiche = (t) => String(t).replace(/\b0X([0-9A-F]+)\b/g, '0x$1').replace(/ - /g, '\u00a0– ').replace(/'/g, '’');
  // Résumé coupé au mot (même règle que lib/templates.mjs, resume).
  // Même règle que lib/templates.mjs : jamais de coupe sur un mot-outil, une élision, un nombre ; une initiale n'est pas une fin de phrase.
  const MOTS_OUTILS = /\s((?:[dljnmstc]|qu|lorsqu|puisqu)['’]\S{0,4}|\S{1,3}|\S*\d\S*|que|qui|dont|dans|pour|avec|sans|sous|leur|leurs|cette|entre|plus|moins|très|comme|selon|grâce|afin|parmi|vers|contre|chaque|plusieurs|jusqu['’]à|puis|donc|mais|ainsi|alors|aussi|autre|autres|aucun|aucune|avant|après|auprès|depuis|chez|lors|lorsque|puisque|quand|tandis|notamment|sont|était|étaient|sera|seront|être|avoir|peut|peuvent|doit|doivent|permet|permettent|permettant|permettre|fait|font|tous|tout|toute|toutes|même|mêmes|bien|encore|the|and|with|from|that|which|into|their|without|through|such|than|each|between|under|where|when|until|about|them|those|this|these|despite|while|whose|also|its|after|before|other|others|another|both|most|more|less|only|same|being|been|have|must|will|would|could|should|lets|allows|allow|over|onto|upon|within|because|since|either|neither|whether|some|many|every|very|just|even|then|once|like|unlike|using|including|whereas|although|though|instead|rather|well)$/i;
  const FIN_PHRASE = /(?<!(?:^|[\s(])[A-Z])(?<!\bInc)[.!?](?=\s|$)/g;
  const resume = (t, n = 84) => {
    t = String(t || '').replace(/'/g, '’').replace(/\s*(\.\.\.|…)$/, '');
    if (t.length <= n) return t === '' ? '' : /[.!?)»]$/.test(t) ? t : `${t}…`;
    // Une phrase entière qui tient, même courte, vaut mieux qu'une coupe : pas de points de suspension.
    const fin = Math.max(...[...t.slice(0, n + 1).matchAll(FIN_PHRASE)].map((m) => m.index));
    if (fin > n * 0.3) return t.slice(0, fin + 1);
    let s = t.slice(0, n + 1);
    s = s.slice(0, Math.max(s.lastIndexOf(' '), 1));
    s = s.replace(/[\s,;:(«–-]+$/, '');
    while (MOTS_OUTILS.test(s) && s.lastIndexOf(' ') > n / 2) s = s.slice(0, s.lastIndexOf(' ')).replace(/[\s,;:(«–-]+$/, '');
    if ((s.match(/\(/g) || []).length > (s.match(/\)/g) || []).length && s.lastIndexOf('(') > n / 2) s = s.slice(0, s.lastIndexOf('('));
    return `${s.replace(/[\s,;:.(«–-]+$/, '')}…`;
  };
  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);
  // Une référence ne se coupe pas (même règle que lib/templates.mjs, insec) ; à appliquer sur du texte déjà échappé.
  const insec = (html) => html.replace(/\b(?:(?:BIP|BOLT|bLIP|SLIP|RFC|NIP|LUD)[- ]\d+|SHA-(?:1|2|3|224|256|384|512))\b/g, '<span class="insec">$&</span>');
  window.dicoInsec = insec;

  // ------------------------------------------------------------ Thème
  // Deux boutons : l'icône de la barre, et une ligne du menu sur les petits téléphones.
  const themeBtns = d.querySelectorAll('[data-theme-toggle]');
  const sombre = () => root.dataset.theme === 'dark' || (!root.dataset.theme && matchMedia('(prefers-color-scheme: dark)').matches);
  const majTheme = () => themeBtns.forEach((b) => {
    const nom = sombre() ? tx('themeClair') : tx('themeSombre');
    if (b.classList.contains('menu-theme')) b.textContent = nom; else b.setAttribute('aria-label', nom);
  });
  majTheme();
  themeBtns.forEach((b) => b.addEventListener('click', () => {
    const t = sombre() ? 'light' : 'dark';
    root.dataset.theme = t;
    try { localStorage.setItem('theme', t); } catch {}
    majTheme();
  }));

  // Safari iOS n'applique :active au toucher que si la page écoute touchstart.
  d.addEventListener('touchstart', () => {}, { passive: true });

  // ------------------------------------------------------------ Barre : se cache en descendant, revient en remontant
  const barre = d.querySelector('[data-barre]');
  let dernierY = scrollY;
  let enAttente = false;
  // Défilement causé par le focus (Tab, Maj+Tab) : la barre garde son état. La page a placé l'élément d'après
  // --haut ; si la barre revenait à ce moment, elle pousserait la pile collante sur lui.
  let gelFocus = 0;
  const majBarre = () => {
    enAttente = false;
    const y = scrollY;
    if (performance.now() < gelFocus) {
      // En haut de page, la barre est toujours là.
      if (y <= 200) barre.classList.remove('est-cachee');
    } else {
      const cacher = y > 200 && y > dernierY + 4 && !d.querySelector('dialog[open]');
      if (cacher) barre.classList.add('est-cachee');
      else if (y < dernierY - 4 || y <= 200) barre.classList.remove('est-cachee');
    }
    root.style.setProperty('--haut', barre.classList.contains('est-cachee') ? '0px' : `${barre.offsetHeight}px`);
    barre.classList.toggle('est-defilee', y > 0);
    dernierY = y;
  };
  if (barre) {
    addEventListener('scroll', () => { if (!enAttente) { enAttente = true; requestAnimationFrame(majBarre); } }, { passive: true });
    // Rotation : la hauteur de la barre change, les éléments collants suivent tout de suite.
    addEventListener('resize', () => requestAnimationFrame(majBarre), { passive: true });
    barre.addEventListener('focusin', () => { barre.classList.remove('est-cachee'); root.style.setProperty('--haut', `${barre.offsetHeight}px`); });
    d.addEventListener('focusin', (e) => { if (!barre.contains(e.target)) gelFocus = performance.now() + 250; });
  }
  // ------------------------------------------------------------ Apparitions, une fois
  const aVoir = d.querySelectorAll('.feuilleter, .categories');
  for (const el of aVoir) {
    const enfants = el.matches('.feuilleter') ? el.querySelectorAll('.blocs li') : el.querySelectorAll('.index-ligne');
    // Décalage plafonné : au-delà de douze lignes, tout arrive ensemble.
    enfants.forEach((c, i) => c.style.setProperty('--k', Math.min(i, 12)));
  }
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) { e.target.classList.add('vu'); io.unobserve(e.target); }
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.05 });
    aVoir.forEach((el) => io.observe(el));
  } else aVoir.forEach((el) => el.classList.add('vu'));
  // La loupe de la barre s'efface tant que le champ de la couverture est à l'écran.
  const champCouv = d.querySelector('.couv-recherche, .cherche-form');
  if (barre && champCouv && 'IntersectionObserver' in window) {
    new IntersectionObserver(([e]) => barre.classList.toggle('champ-visible', e.isIntersecting), { rootMargin: `-${barre.offsetHeight}px 0px 0px 0px` }).observe(champCouv);
  }

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

  // ------------------------------------------------------------ Blocs de code plus larges que la colonne : un filet Figue au bord droit tant qu'il reste à voir
  const larges = d.querySelectorAll('.prose pre, .prose .figure-cadre');
  // Un dépassement qui ne mord que sur la marge intérieure droite ne cache rien : pas de filet.
  const aSuivre = (el) => el.classList.toggle('a-suivre', el.scrollWidth - el.clientWidth - el.scrollLeft > Math.max(2, (parseFloat(getComputedStyle(el).paddingRight) || 0) - 1));
  larges.forEach((el) => { aSuivre(el); el.addEventListener('scroll', () => aSuivre(el), { passive: true }); });
  if (larges.length) {
    addEventListener('resize', () => larges.forEach(aSuivre), { passive: true });
    // La police à chasse fixe arrive après le premier calcul : on recompte une fois chargée.
    d.fonts?.ready.then(() => larges.forEach(aSuivre));
    addEventListener('load', () => larges.forEach(aSuivre));
  }

  // ------------------------------------------------------------ Renvois entrants repliés au-delà de 8
  for (const ul of d.querySelectorAll('[data-repliable]')) {
    const n = ul.children.length;
    const limite = 8;
    if (n <= limite) continue;
    ul.classList.add('replie');
    const b = d.createElement('button');
    b.type = 'button';
    b.className = 'cites-plus';
    b.setAttribute('aria-expanded', 'false');
    b.textContent = tx('voirAutres', { n: n - limite });
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
      if (ok) {
        if (citer.nextElementSibling?.matches('.citer-secours')) citer.nextElementSibling.remove();
        citer.style.minWidth = `${citer.offsetWidth}px`;
        citer.textContent = tx('copiee');
        setTimeout(() => { citer.textContent = tx('citer'); citer.style.minWidth = ''; }, 2400);
        return;
      }
      // Copie refusée : la citation s'affiche sous le bouton, sélectionnée, à copier à la main (le bouton garde sa taille).
      let s = citer.nextElementSibling?.matches('.citer-secours') ? citer.nextElementSibling : null;
      if (!s) { s = d.createElement('span'); s.className = 'citer-secours'; citer.after(s); }
      s.innerHTML = `${esc(tx('copiez'))}<span class="citer-texte">${esc(citer.dataset.citer)}</span>`;
      const r = d.createRange();
      r.selectNodeContents(s.lastChild);
      getSelection().removeAllRanges();
      getSelection().addRange(r);
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
    // L'image elle-même, ou le lien « Agrandir le schéma » sous la figure : la même loupe.
    const a = e.target.closest('.prose .figure-cadre a, .prose .figure-ouvrir');
    const img = a?.closest('.figure')?.querySelector('img');
    if (!a || !img || e.metaKey || e.ctrlKey) return;
    e.preventDefault();
    const loupe = d.createElement('dialog');
    loupe.className = 'loupe';
    loupe.innerHTML = `<div class="loupe-panneau"><div class="loupe-tete"><p class="loupe-legende">${esc(img.alt || tx('schema'))}${a.closest('.figure')?.querySelector('.figure-credit') ? `<span class="figure-credit">${esc(a.closest('.figure').querySelector('.figure-credit').textContent)}</span>` : ''}</p><p class="loupe-boutons"><button class="recherche-fermer" type="button" data-zoom aria-pressed="false">${tx('agrandir')}</button> <button class="recherche-fermer" type="button" data-fermer>${tx('fermer')}</button></p></div><div class="loupe-zone"><img src="${esc(a.getAttribute('href'))}" alt="${esc(img.alt || '')}"></div></div>`;
    d.body.append(loupe);
    loupe.querySelector('[data-fermer]').addEventListener('click', () => loupe.close());
    // Ajusté à la largeur d'abord ; « Agrandir » double la taille (et le pincement reste possible).
    loupe.querySelector('[data-zoom]').addEventListener('click', (ev) => {
      const z = loupe.classList.toggle('loupe--zoom');
      ev.currentTarget.textContent = z ? tx('ajuster') : tx('agrandir');
      ev.currentTarget.setAttribute('aria-pressed', String(z));
    });
    loupe.addEventListener('close', () => { loupe.remove(); a.focus({ preventScroll: true }); });
    loupe.showModal();
  });

  // ------------------------------------------------------------ Changer de catégorie
  d.querySelector('[data-cat-choix]')?.addEventListener('change', (e) => { location.href = e.target.value; });

  // ------------------------------------------------------------ Barre A–Z : la lettre courante visible sur téléphone
  // On centre la lettre courante en faisant défiler la barre elle-même (scrollIntoView déplacerait aussi la page).
  // Centre un élément dans sa rangée qui défile (offsetLeft ne convient pas : les puces ont leur propre repère).
  const centrer = (rangee, el) => { rangee.scrollLeft += el.getBoundingClientRect().left - rangee.getBoundingClientRect().left - rangee.clientWidth / 2 + el.offsetWidth / 2; };
  const courante = d.querySelector('.index-az a[aria-current]');
  if (courante) {
    const ol = courante.closest('ol');
    centrer(ol, courante);
  }
  const motCourant = d.querySelector('[data-mot]');
  // Une liste par langue : un mot lu en français n'a pas la même adresse en anglais.
  const cleDerniers = `derniers-${root.lang || 'fr'}`;
  const lireDerniers = () => { try { return JSON.parse(localStorage.getItem(cleDerniers) || '[]'); } catch { return []; } };
  if (motCourant) {
    try {
      const liste = lireDerniers().filter((m) => m[0] !== motCourant.dataset.mot);
      liste.unshift([motCourant.dataset.mot, motCourant.dataset.titre]);
      localStorage.setItem(cleDerniers, JSON.stringify(liste.slice(0, 8)));
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
        carte.innerHTML = `<p class="carte-nom">${esc(a.dataset.apercuNom || a.querySelector('.reperes-nom')?.textContent || a.textContent)}</p><p class="carte-cat">${esc(a.dataset.apercuCat || '')}</p><p class="carte-desc">${insec(esc(a.dataset.apercu.replace(/'/g, '’').replace(/\.\.\./g, '…')))}</p>`;
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
  // Flèches du clavier : mot précédent ou suivant dans l'ordre du livre ; dans un bloc qui défile en largeur
  // (code, schéma), focus ou dernier clic dedans, elles le font défiler.
  const dansDefileur = (el) => {
    for (; el && el !== d.body && el.nodeType === 1; el = el.parentElement) {
      if (el.scrollWidth > el.clientWidth + 1 && /auto|scroll/.test(getComputedStyle(el).overflowX)) return true;
    }
    return false;
  };
  let dernierAppui = null;
  d.addEventListener('pointerdown', (e) => { dernierAppui = e.target; }, { passive: true });
  d.addEventListener('keydown', (e) => {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    if (e.target.closest('input, textarea, select, [contenteditable], [role="slider"], dialog')) return;
    if ((e.key === 'ArrowLeft' || e.key === 'ArrowRight') && (dansDefileur(e.target) || (e.target === d.body && dansDefileur(dernierAppui)))) return;
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
      fetch(`${B}/recherche.json`).then((r) => r.json()),
      fetch(`${B}/tranche.json`).then((r) => r.json()).catch(() => ({ renvois: [] })),
    ]).then(([j, tranche]) => {
      index = j.terms.map(([title, slug, cat, alt, desc, lang], i) => ({
        i, title, slug, alt, desc, lang,
        cat: j.categories[cat] || ['', ''],
        poids: tranche.renvois?.[i] || 0,
        pt: plat(title), ct: compact(title), pa: plat(alt), noms: alt.split(' · ').map((x) => plat(x).replace(/ +/g, ' ').trim()).filter(Boolean), pd: plat(desc),
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
      // Un autre nom exact : le terme français d'une page anglaise, l'anglais d'une page française.
      else if (t.noms.includes(pq)) rang = 9;
      else if (` ${titre} `.includes(` ${pq} `)) { rang = 8.5; at = t.pt.indexOf(pq); }
      else if (t.pt.startsWith(pq)) { rang = 8; at = 0; }
      else if (cq.length > 1 && t.ct.startsWith(cq)) rang = 7;
      else if (t.noms.some((n) => n.startsWith(pq))) rang = 6;
      else if ((at = t.pt.indexOf(` ${pq}`)) > -1) { rang = 5; at += 1; }
      else if (alt && alt.includes(` ${pq}`)) rang = 4;
      else if (mots.length > 1 && mots.every((m) => t.pt.includes(` ${m}`) || t.pt.startsWith(m))) rang = 4;
      // Trouvé par un autre nom ou en compact (« nip-4 ») : la partie du titre qui correspond passe quand même à l'encre.
      if (rang && at < 0) at = t.pt.indexOf(pq);
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
  <a href="${B}/${t.slug}/" tabindex="-1"><span class="resultat-nom" data-vt-nom>${surligner(t.title, at, len)}</span><span class="resultat-cat">${picto(t.cat[1])}${esc(t.cat[0])}</span>${t.alt ? `<span class="resultat-alt">${insec(esc(affiche(t.alt)))}</span>` : ''}${t.desc ? `<span class="resultat-desc"${t.lang ? ` lang="${t.lang}"` : ''}>${insec(esc(resume(t.desc)))}</span>` : ''}</a></li>`;
  const point = (s) => (/[.!?…]$/.test(s) ? '' : '.');
  const pluriel = (n, [un, plusieurs] = ['', '']) => `${n.toLocaleString(loc)} ${n > 1 ? plusieurs : un}`;
  const jour = () => Math.floor((Date.now() - new Date().getTimezoneOffset() * 60000) / 86400000);

  // ------------------------------------------------------------ Fenêtre de recherche
  const dialog = d.getElementById('recherche');
  const champ = dialog?.querySelector('input');
  const liste = dialog?.querySelector('.resultats');
  const etat = dialog?.querySelector('.recherche-etat');
  let actif = -1;
  let declencheur = null;
  let retour = null;

  function selectionner(i) {
    const items = liste.querySelectorAll('.resultat');
    if (!items.length) { actif = -1; champ.removeAttribute('aria-activedescendant'); return; }
    actif = (i + items.length) % items.length;
    items.forEach((el, k) => el.setAttribute('aria-selected', String(k === actif)));
    champ.setAttribute('aria-activedescendant', items[actif].id);
    items[actif].scrollIntoView({ block: 'nearest' });
  }

  function suggestions(avecCategories) {
    // Le même mot du jour que l'accueil : parmi les entrées écrites dans la langue de la page.
    const ecrits = index ? index.filter((t) => !t.lang) : [];
    const pool = ecrits.length ? ecrits : index || [];
    const n = pool.length ? pool[jour() % pool.length] : null;
    const h = index ? index[Math.floor(Math.random() * index.length)] : null;
    const lettres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('').map((l) => `<a href="${B}/${T.lettre || 'lettre'}/${l.toLowerCase()}/">${l}</a>`).join('');
    const derniers = lireDerniers().filter((m) => !motCourant || m[0] !== motCourant.dataset.mot).slice(0, 5);
    const cats = avecCategories && index?.categories ? `<p>${tx('parCategorie')}</p><div class="cats-mini">${[...index.categories].sort((a, b) => a[0].localeCompare(b[0], d.documentElement.lang)).map(([label, slug, chemin]) => `<a href="${chemin}">${picto(slug)}${esc(label)}</a>`).join('')}</div>` : '';
    return `<li class="suggestions-vides" role="presentation">${derniers.length ? `<p>${tx('derniers')} ${derniers.map((m) => `<a class="lien" href="${B}/${esc(m[0])}/">${esc(m[1])}</a>`).join(', ')}${point(derniers.at(-1)[1])}</p>` : ''}${n ? `<p>${tx('motDuJour')} <a class="lien" href="${B}/${n.slug}/">${esc(affiche(n.title))}</a>${point(n.title)} ${tx('auHasard')} <a class="lien" href="${B}/${h.slug}/">${esc(affiche(h.title))}</a>${point(h.title)}</p>` : ''}<p>${tx('parLettre')}</p><div class="abc">${lettres}</div>${cats}</li>`;
  }

  function vide() {
    etat.textContent = '';
    liste.innerHTML = suggestions(false);
    liste.scrollTop = 0;
    champ.setAttribute('aria-expanded', 'false');
    actif = -1;
  }

  function afficher() {
    const q = champ.value;
    if (!q.trim()) return vide();
    const { res, approx, total } = chercher(q);
    if (!res.length) {
      etat.innerHTML = tx('aucun', { q: esc(q.trim()) });
      liste.innerHTML = suggestions(true);
      liste.scrollTop = 0;
      champ.setAttribute('aria-expanded', 'false');
      return;
    }
    etat.textContent = approx ? tx('aucunExact') : total > res.length ? tx('premiers', { total: pluriel(total, T.resultat), n: res.length }) : pluriel(total, T.resultat);
    liste.innerHTML = res.map((r, i) => ligne(r, i, 'res')).join('');
    champ.setAttribute('aria-expanded', 'true');
    selectionner(0);
  }

  function ouvrir(valeur = '', depuis = null) {
    if (!dialog || dialog.open) return;
    declencheur = depuis;
    retour = d.activeElement !== d.body ? d.activeElement : null;
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
    charger().then(afficher).catch(() => { etat.textContent = tx('indexErreur'); });
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
        if (!champ.value.trim()) { e.preventDefault(); return; }
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
    // À la fermeture, le focus revient là où il était (ou au bouton qui a ouvert), s'il est encore visible.
    dialog.addEventListener('close', () => {
      // Ouverte depuis le champ de la couverture : ce qui a été tapé y revient.
      if (declencheur?.matches?.('[data-hero-search]')) declencheur.querySelector('input').value = champ.value;
      [retour, declencheur].find((el) => el?.isConnected && el.getClientRects().length)?.focus?.({ preventScroll: true });
    });
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
        // Sur la page de recherche, le raccourci mène à son propre champ.
        const champPage = d.querySelector('[data-search-page] input');
        if (champPage && !dialog.open) { champPage.focus(); champPage.select(); }
        else if (dialog.open) champ.select(); else ouvrir('', d.querySelector('[data-search-open]'));
      }
    });
    if (/Mac|iPhone|iPad/.test(navigator.platform)) d.querySelectorAll('[data-kbd]').forEach((k) => (k.textContent = '⌘ K'));
    // Le champ de la couverture s'ouvre en fenêtre (plein écran sur téléphone) avec ce qui est déjà tapé.
    const heros = d.querySelector('[data-hero-search]');
    if (heros) {
      // Ouverture au toucher, au clic ou à la première frappe, jamais au simple focus : à la fermeture,
      // le focus revient dans le champ sans rouvrir la fenêtre.
      const input = heros.querySelector('input');
      const ouvrirDepuis = () => { const v = input.value; input.value = ''; ouvrir(v, heros); };
      input.addEventListener('click', ouvrirDepuis);
      // Champ vidé (deuxième Échap, croix du champ « search », dernier caractère effacé) : rien ne s'ouvre.
      input.addEventListener('input', () => { if (input.value) ouvrirDepuis(); });
      heros.addEventListener('submit', (e) => { e.preventDefault(); ouvrirDepuis(); });
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
    // Le menu n'existe que sous 1 024 px : une tablette tournée en paysage le referme.
    addEventListener('resize', () => { if (menu.open && matchMedia('(min-width: 1024px)').matches) menu.close(); }, { passive: true });
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
    let qFiltres = null;
    let refaireFiltres = false;
    // Les étiquettes de catégorie montrent combien de résultats chacune contient ; seules celles qui en ont restent.
    const etiquettes = (tous) => {
      // Aucun résultat : pas de rangée de filtres (une pastille « Toutes 0 » seule ne dit rien).
      if (!tous.length) { filtres.innerHTML = ''; return; }
      const n = new Map();
      for (const r of tous) n.set(r.t.cat[1], (n.get(r.t.cat[1]) || 0) + 1);
      const liste = index.categories.filter(([, slug]) => n.has(slug) || slug === cat).sort((a, b) => (n.get(b[1]) || 0) - (n.get(a[1]) || 0));
      // Le filtre choisi reste toujours visible, même au-delà des huit premiers.
      const visibles = tout ? liste : liste.slice(0, 8).concat(liste.slice(8).filter(([, slug]) => slug === cat));
      filtres.innerHTML = `<legend class="masque">${tx('filtrer')}</legend>
        <label class="filtre"><input type="radio" name="cat" value=""${cat ? '' : ' checked'}><span>${tx('toutes')} <b>${tous.length}</b></span></label>
        ${visibles.map(([label, slug]) => `<label class="filtre"><input type="radio" name="cat" value="${slug}"${slug === cat ? ' checked' : ''}><span>${picto(slug)}${esc(label)} <b>${n.get(slug) || 0}</b></span></label>`).join('')}
        ${liste.length > visibles.length ? `<button class="filtre-plus" type="button" data-filtres-plus>+ ${liste.length - visibles.length}</button>` : ''}`;
      if (select) select.innerHTML = `<option value="">${tx('toutes')} (${tous.length})</option>${liste.map(([label, slug]) => `<option value="${slug}"${slug === cat ? ' selected' : ''}>${esc(label)} (${n.get(slug) || 0})</option>`).join('')}`;
    };
    const adresse = (q) => {
      const u = new URL(location.href);
      u.searchParams.set('q', q);
      if (cat) u.searchParams.set('cat', cat); else u.searchParams.delete('cat');
      history.replaceState(null, '', u);
    };
    const lancer = () => {
      const q = input.value;
      adresse(q);
      if (!q.trim()) {
        sortie.innerHTML = '';
        filtres.innerHTML = '';
        qFiltres = null;
        statut.textContent = tx('tapez', { n: index.length.toLocaleString(loc) });
        sortie.innerHTML = suggestions(true);
        return;
      }
      // Une seule recherche : les filtres comptent ses résultats et le filtre choisi la découpe, jamais une autre liste.
      const trouve = chercher(q, { limite: 2000 });
      const tousRes = trouve.tous || [];
      // Le filtre choisi n'a plus rien pour la nouvelle requête : retour à « Toutes ».
      if (cat && !tousRes.some((r) => r.t.cat[1] === cat)) { cat = ''; qFiltres = null; adresse(q); }
      // Les filtres ne sont refaits que si la requête change : changer de filtre garde le focus du clavier.
      if (q !== qFiltres || refaireFiltres) {
        const plus = refaireFiltres;
        // Une nouvelle requête repart des huit premiers filtres et de « + N ».
        if (!plus) tout = false;
        etiquettes(tousRes);
        qFiltres = q;
        // Sur téléphone, la rangée défile jusqu'au filtre choisi.
        const choisi = filtres.querySelector('input:checked')?.closest('.filtre');
        if (choisi && filtres.scrollWidth > filtres.clientWidth) centrer(filtres, choisi);
        refaireFiltres = false;
        if (plus) filtres.querySelectorAll('input')[9]?.focus();
      }
      const choisis = cat ? tousRes.filter((r) => r.t.cat[1] === cat) : tousRes;
      const res = choisis.slice(0, 200);
      const { approx } = trouve;
      const total = choisis.length;
      if (!res.length) {
        const p = proches(q, 5);
        statut.innerHTML = tx(p.length ? 'aucunProches' : 'aucunPage', { q: esc(q.trim()) });
        sortie.innerHTML = p.map((r, i) => ligne(r, i, 'page')).join('') + suggestions(true);
      } else {
        statut.textContent = approx ? tx('aucunExact') : pluriel(total, T.resultat);
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
    statut.textContent = tx('chargement');
    charger().then(() => { lancer(); if (!input.value) input.focus(); });
    input.addEventListener('input', () => index && lancer());
    filtres.addEventListener('change', (e) => { cat = e.target.value; index && lancer(); });
    filtres.addEventListener('click', (e) => { if (e.target.closest('[data-filtres-plus]')) { tout = true; refaireFiltres = true; index && lancer(); } });
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
      if (q.trim().length < 2) { sugg.hidden = true; liste404.innerHTML = ''; return; }
      let { res } = chercher(q, { limite: 5 });
      if (res.length < 3) {
        const vus = new Set(res.map((r) => r.t.slug));
        res = res.concat(proches(q, 3 - res.length, vus));
      }
      titre404.textContent = q === q0 ? tx('vouliez') : tx('resultats');
      liste404.innerHTML = res.map(({ t }) => `<li><a href="${B}/${t.slug}/"><span class="perdu-nom">${esc(affiche(t.title))}</span>${t.desc ? `<span class="perdu-desc">${insec(esc(resume(t.desc)))}</span>` : ''}</a></li>`).join('');
      sugg.hidden = !res.length;
    };
    charger().then(montrer404);
    champPerdu.addEventListener('input', () => index && montrer404());
    // « Chercher » mène à la première suggestion affichée ; sans suggestion, à la page de recherche ; champ vide : rien.
    form.addEventListener('submit', (e) => {
      const a = !sugg.hidden && liste404.querySelector('a');
      if (a) { e.preventDefault(); a.click(); }
      else if (!champPerdu.value.trim()) e.preventDefault();
    });
  }

  // ------------------------------------------------------------ Spécifications : filtre par statut
  const filtreStatut = d.querySelector('[data-filtres-statut]');
  if (filtreStatut) {
    filtreStatut.hidden = false;
    const fiches = [...d.querySelectorAll('.spec[data-statut]')];
    filtreStatut.addEventListener('change', (e) => {
      const v = e.target.value;
      for (const f of fiches) f.hidden = !!v && !f.dataset.statut.split(' ').includes(v);
    });
  }

  // La hauteur de la rangée collante (une ou deux lignes selon la largeur) règle les en-têtes collants et les ancres,
  // sur toute page de liste : sous-groupes d'une lettre, alphabet d'une catégorie ou d'une lettre sans sous-groupes.
  const rangeeCollante = d.querySelector('.sous-index') || d.querySelector('.p-lettre .index-az, .p-cat .index-az');
  if (rangeeCollante) {
    const majRangee = () => root.style.setProperty('--rangee', `${getComputedStyle(rangeeCollante).position === 'sticky' ? rangeeCollante.offsetHeight : 0}px`);
    majRangee();
    if ('ResizeObserver' in window) new ResizeObserver(majRangee).observe(rangeeCollante);
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
    const rangee = sousIndex.closest('nav');
    const poser = (puce) => {
      marque?.removeAttribute('aria-current');
      marque = puce;
      puce.setAttribute('aria-current', 'location');
      centrer(sousIndex, puce);
    };
    let figeJusqua = 0;
    // Un clic sur une puce pose le groupe juste sous la rangée : la barre se range pour ne rien masquer.
    sousIndex.addEventListener('click', (e) => {
      const a = e.target.closest('a[href^="#"]');
      const cible = a && d.getElementById(a.hash.slice(1));
      if (!cible || e.metaKey || e.ctrlKey) return;
      e.preventDefault();
      if (barre) { barre.classList.add('est-cachee'); root.style.setProperty('--haut', '0px'); }
      // On mesure le groupe, qui ne colle pas (son en-tête collant peut être poussé en bas du groupe) ;
      // le titre arrive 16 px sous la rangée (8 px de marge haute dans l'en-tête). En bas de page, la position est bornée.
      const groupe = cible.closest('.groupe') || cible;
      const y = Math.min(Math.max(0, groupe.getBoundingClientRect().top + scrollY - rangee.offsetHeight - 8), d.documentElement.scrollHeight - innerHeight);
      dernierY = y;
      scrollTo({ top: y, behavior: 'auto' });
      history.replaceState(null, '', a.hash);
      // La puce touchée reste marquée, même si un groupe court laisse le suivant entrer dans l'écran.
      poser(a);
      figeJusqua = performance.now() + 400;
      if (!cible.hasAttribute('tabindex')) cible.setAttribute('tabindex', '-1');
      cible.focus({ preventScroll: true });
    });
    const marquer = () => {
      const haut = parseFloat(getComputedStyle(d.documentElement).getPropertyValue('--haut')) || 0;
      // Ombre de la rangée seulement quand elle colle.
      const barreCollante = sousIndex.closest('nav');
      barreCollante.classList.toggle('est-collee', barreCollante.getBoundingClientRect().top <= haut + 1 && scrollY > 0 && barreCollante.parentElement.getBoundingClientRect().top < haut);
      if (performance.now() < figeJusqua) return;
      // Le groupe lu est celui dont le haut a passé le bas de l'en-tête de groupe collant.
      const ligne = haut + rangee.offsetHeight + 56;
      let actif = null;
      for (const g of titres) { if (g.getBoundingClientRect().top <= ligne) actif = g; else break; }
      // Une pastille qui mène déjà au groupe lu reste marquée (lettre touchée d'un groupe « D – G »).
      if (marque && actif && marque.hash.slice(1) === actif.getAttribute('aria-labelledby')) return;
      const puce = actif ? puces.get(actif.getAttribute('aria-labelledby')) : null;
      if (puce === marque) return;
      // Revenu au-dessus du premier groupe : la rangée repart de son début.
      if (!puce) { marque?.removeAttribute('aria-current'); marque = null; sousIndex.scrollLeft = 0; return; }
      poser(puce);
    };
    addEventListener('scroll', () => requestAnimationFrame(marquer), { passive: true });
    addEventListener('resize', () => requestAnimationFrame(marquer), { passive: true });
  }
  if (d.querySelector('.liste')) {
    const haut = d.createElement('button');
    haut.type = 'button';
    haut.className = 'haut';
    haut.textContent = '↑';
    haut.setAttribute('aria-label', tx('haut'));
    haut.hidden = true;
    haut.addEventListener('click', () => { scrollTo({ top: 0, behavior: reduit.matches ? 'auto' : 'smooth' }); d.querySelector('h1')?.focus?.(); });
    d.body.append(haut);
    let piedVisible = false;
    const pied = d.querySelector('.dos');
    // Visible en remontant (quand la barre revient), après le premier écran, jamais sur le pied : il ne cache pas la lecture.
    let repos = 0;
    const majHaut = () => {
      haut.hidden = piedVisible || scrollY < innerHeight || !!barre?.classList.contains('est-cachee');
      clearTimeout(repos);
      if (!haut.hidden) repos = setTimeout(() => { if (d.activeElement !== haut) haut.hidden = true; }, 2500);
    };
    if (pied) new IntersectionObserver(([e]) => { piedVisible = e.isIntersecting; majHaut(); }).observe(pied);
    addEventListener('scroll', () => requestAnimationFrame(majHaut), { passive: true });
  }

  // ------------------------------------------------------------ Présentation de catégorie repliée : « Lire la suite »
  // Téléphone : toute la présentation est repliée ; ailleurs, la suite après la première phrase.
  const suite = d.querySelector('[data-repliable-suite]') || (matchMedia('(max-width: 639px)').matches && d.querySelector('.cat-note-premiere'));
  if (suite) {
    const b = d.createElement('button');
    b.type = 'button';
    b.className = 'lire-suite';
    b.textContent = tx('lireSuite');
    b.setAttribute('aria-expanded', 'false');
    // Le bouton déplie et replie.
    b.addEventListener('click', () => {
      const ouvert = suite.closest('.cat-note').classList.toggle('deplie');
      b.textContent = ouvert ? tx('replier') : tx('lireSuite');
      b.setAttribute('aria-expanded', String(ouvert));
    });
    suite.closest('.cat-note').after(b);
  }
})();
