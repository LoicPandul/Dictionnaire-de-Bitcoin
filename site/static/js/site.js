// Dictionnaire de Bitcoin : recherche instantanée, onglets de lettres, terme du jour,
// apparitions au défilement. Sans dépendance ; tout le site reste lisible sans ce script.
(() => {
  const root = document.documentElement;
  const isMac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent);
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ------------------------------------------------------------ Index de recherche
  let indexPromise = null;
  const fold = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();
  const norm = (s) => fold(s).replace(/[^a-z0-9]+/g, ' ').trim();
  const compact = (s) => norm(s).replace(/ /g, '').replace(/([a-z])0+(\d)/g, '$1$2');

  function loadIndex() {
    if (!indexPromise) {
      indexPromise = fetch('/recherche.json')
        .then((r) => (r.ok ? r.json() : Promise.reject(new Error(r.status))))
        .then(({ categories, terms }) =>
          terms.map(([t, s, c, e, d]) => ({
            t, s, e, d,
            cat: categories[c][0],
            catSlug: categories[c][1],
            nt: norm(t),
            ct: compact(t),
            ne: e ? norm(e) : '',
            nd: norm(d),
          })),
        )
        .catch((err) => {
          indexPromise = null;
          throw err;
        });
    }
    return indexPromise;
  }

  function search(entries, query) {
    const q = norm(query);
    if (!q) return [];
    const cq = compact(query);
    const tokens = q.split(' ');
    const out = [];
    for (const x of entries) {
      let score = 0;
      if (x.nt === q || (cq && x.ct === cq)) score = 1000;
      else if (x.nt.startsWith(q)) score = 800;
      else if (cq && x.ct.startsWith(cq)) score = 720;
      else if (x.ne && x.ne === q) score = 700;
      else if (tokens.every((tk) => x.nt.split(' ').some((w) => w.startsWith(tk)))) score = 560;
      else if (x.ne && x.ne.startsWith(q)) score = 480;
      else if (x.nt.includes(q)) score = 420;
      else if (x.ne && x.ne.includes(q)) score = 340;
      else if (tokens.every((tk) => x.nt.includes(tk) || x.ne.includes(tk))) score = 260;
      else if (tokens.every((tk) => x.nd.includes(tk))) score = 100;
      if (score) out.push([score - x.t.length * 0.5, x]);
    }
    out.sort((a, b) => b[0] - a[0]);
    return out.slice(0, 12).map(([, x]) => x);
  }

  const esc = (s) => s.replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]);

  // Souligne le passage trouvé dans le titre, accents compris.
  function highlight(title, query) {
    const q = norm(query);
    if (!q) return esc(title);
    const chars = [...title];
    const flat = chars.map((c) => {
      const f = fold(c)[0] || ' ';
      return /[a-z0-9]/.test(f) ? f : ' ';
    }).join('');
    const at = flat.indexOf(q);
    if (at < 0) return esc(title);
    return `${esc(chars.slice(0, at).join(''))}<mark>${esc(chars.slice(at, at + q.length).join(''))}</mark>${esc(chars.slice(at + q.length).join(''))}`;
  }

  // ------------------------------------------------------------ Combobox
  function combobox(input, list, { status, onClose } = {}) {
    let results = [];
    let active = -1;
    let seq = 0;

    const setActive = (i) => {
      const items = list.querySelectorAll('[role="option"]');
      items.forEach((el, n) => el.setAttribute('aria-selected', String(n === i)));
      active = i;
      if (i >= 0 && items[i]) {
        input.setAttribute('aria-activedescendant', items[i].id);
        items[i].scrollIntoView({ block: 'nearest' });
      } else input.removeAttribute('aria-activedescendant');
    };

    const render = (query) => {
      if (!query.trim()) {
        list.innerHTML = '';
        input.setAttribute('aria-expanded', 'false');
        if (status) status.textContent = 'Tapez un terme, un sigle ou un mot anglais. Entrée ouvre le premier résultat.';
        return;
      }
      const prefix = list.id;
      list.innerHTML = results.length
        ? results
            .map(
              (x, i) => `<li class="result" role="option" id="${prefix}-${i}" aria-selected="false"><a href="/${x.s}/" tabindex="-1">
  <span class="result-title">${highlight(x.t, query)}${x.e ? ` <span class="result-en" lang="en">· ${esc(x.e)}</span>` : ''}</span>
  <span class="result-cat"><span class="picto" style="--picto:url(/img/pictos/${x.catSlug}.webp)" aria-hidden="true"></span>${esc(x.cat)}</span>
  ${x.d ? `<span class="result-note">${esc(x.d)}</span>` : ''}
</a></li>`,
            )
            .join('')
        : `<li class="result-empty" role="presentation">Aucun terme ne correspond à « ${esc(query)} ». Essayez le terme anglais ou un sigle.</li>`;
      input.setAttribute('aria-expanded', 'true');
      if (status) status.textContent = results.length ? `${results.length === 12 ? '12 premiers résultats' : `${results.length} résultat${results.length > 1 ? 's' : ''}`}` : '';
      setActive(results.length ? 0 : -1);
    };

    const run = () => {
      const query = input.value;
      const mine = ++seq;
      loadIndex()
        .then((entries) => {
          if (mine !== seq) return;
          results = search(entries, query);
          render(query);
        })
        .catch(() => {
          list.innerHTML = '<li class="result-empty" role="presentation">La recherche n’a pas pu se charger. Parcourez les lettres en attendant.</li>';
        });
    };

    input.addEventListener('focus', () => loadIndex().catch(() => {}), { once: true });
    input.addEventListener('pointerenter', () => loadIndex().catch(() => {}), { once: true });
    input.addEventListener('input', run);
    input.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowDown' && results.length) {
        e.preventDefault();
        setActive((active + 1) % results.length);
      } else if (e.key === 'ArrowUp' && results.length) {
        e.preventDefault();
        setActive((active - 1 + results.length) % results.length);
      } else if (e.key === 'Enter') {
        e.preventDefault();
        const target = results[active >= 0 ? active : 0];
        if (target) window.location.href = `/${target.s}/`;
      } else if (e.key === 'Escape') {
        if (input.value) {
          input.value = '';
          run();
        } else if (onClose) onClose();
      }
    });
    list.addEventListener('mousemove', (e) => {
      const li = e.target.closest('[role="option"]');
      if (!li) return;
      const i = [...list.children].indexOf(li);
      if (i !== active) setActive(i);
    });
    return { run, clear: () => { input.value = ''; run(); } };
  }

  // ------------------------------------------------------------ Fenêtre de recherche
  const dialog = document.getElementById('recherche');
  let opener = null;
  let dialogBox = null;
  function openSearch(from) {
    if (!dialog) return;
    opener = from || document.activeElement;
    dialog.hidden = false;
    document.body.style.overflow = 'hidden';
    const input = dialog.querySelector('.search-input');
    if (!dialogBox) {
      dialogBox = combobox(input, dialog.querySelector('.search-results'), {
        status: dialog.querySelector('.search-status'),
        onClose: closeSearch,
      });
    }
    dialogBox.run();
    input.focus();
    input.select();
  }
  function closeSearch() {
    if (!dialog || dialog.hidden) return;
    dialog.hidden = true;
    document.body.style.overflow = '';
    if (opener && opener.focus) opener.focus();
  }
  document.addEventListener('click', (e) => {
    const open = e.target.closest('[data-search-open]');
    if (open) {
      e.preventDefault();
      openSearch(open);
    } else if (e.target.closest('[data-search-close]')) closeSearch();
  });
  document.addEventListener('keydown', (e) => {
    const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(document.activeElement?.tagName) || document.activeElement?.isContentEditable;
    if ((e.key === 'k' || e.key === 'K') && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      if (dialog?.hidden) openSearch();
      else closeSearch();
    } else if (e.key === '/' && !typing) {
      e.preventDefault();
      openSearch();
    } else if (e.key === 'Escape' && dialog && !dialog.hidden) closeSearch();
    else if (e.key === 'Tab' && dialog && !dialog.hidden) {
      // La tabulation reste dans la fenêtre.
      const focusables = [...dialog.querySelectorAll('input, button, a[href]')].filter((el) => el.offsetParent && el.tabIndex >= 0);
      const first = focusables[0];
      const last = focusables.at(-1);
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    }
  });
  document.querySelectorAll('[data-kbd]').forEach((el) => { el.textContent = isMac ? '⌘ K' : 'Ctrl K'; });
  // Les moteurs comme Google peuvent pointer vers /?q=terme.
  const q = new URLSearchParams(location.search).get('q');

  // ------------------------------------------------------------ Recherche de l'accueil
  const heroForm = document.querySelector('[data-inline-search]');
  if (heroForm) {
    const input = heroForm.querySelector('input');
    const list = heroForm.querySelector('.search-results');
    const box = combobox(input, list, { onClose: () => input.blur() });
    heroForm.addEventListener('submit', (e) => e.preventDefault());
    document.addEventListener('click', (e) => {
      if (!heroForm.contains(e.target)) { list.innerHTML = ''; input.setAttribute('aria-expanded', 'false'); }
    });
    input.addEventListener('focus', () => { if (input.value) box.run(); });
    if (q) { input.value = q; box.run(); }
  } else if (q) {
    openSearch();
    const input = dialog?.querySelector('.search-input');
    if (input) { input.value = q; dialogBox?.run(); }
  }

  // ------------------------------------------------------------ Onglets de lettres
  const tablist = document.querySelector('.agenda-tabs');
  if (tablist) {
    const tabs = [...tablist.querySelectorAll('[role="tab"]')];
    const select = (tab, focus) => {
      tabs.forEach((t) => {
        const on = t === tab;
        t.setAttribute('aria-selected', String(on));
        t.tabIndex = on ? 0 : -1;
        const panel = document.getElementById(t.getAttribute('aria-controls'));
        if (panel) panel.hidden = !on;
      });
      if (focus) tab.focus();
      const panel = document.getElementById(tab.getAttribute('aria-controls'));
      if (panel && !reduceMotion) { panel.classList.remove('is-swapping'); void panel.offsetWidth; panel.classList.add('is-swapping'); }
    };
    tabs.forEach((t, i) => {
      t.tabIndex = i === 0 ? 0 : -1;
      t.addEventListener('click', (e) => { e.preventDefault(); select(t); });
      t.addEventListener('keydown', (e) => {
        const n = { ArrowRight: 1, ArrowDown: 1, ArrowLeft: -1, ArrowUp: -1 }[e.key];
        if (n) { e.preventDefault(); select(tabs[(i + n + tabs.length) % tabs.length], true); }
        else if (e.key === 'Home') { e.preventDefault(); select(tabs[0], true); }
        else if (e.key === 'End') { e.preventDefault(); select(tabs.at(-1), true); }
      });
    });
  }

  // ------------------------------------------------------------ Terme du jour, au hasard
  const today = document.querySelector('[data-today]');
  const pickRandom = (entries) => entries[Math.floor(Math.random() * entries.length)];
  function showTerm(x) {
    if (!today || !x) return;
    const link = today.querySelector('[data-today-link]');
    link.textContent = x.t;
    link.href = `/${x.s}/`;
    today.querySelector('[data-today-read]').href = `/${x.s}/`;
    today.querySelector('[data-today-cat]').textContent = x.cat;
    today.querySelector('[data-today-desc]').textContent = x.d;
    const p = today.querySelector('[data-today-picto] .picto');
    if (p) p.style.setProperty('--picto', `url(/img/pictos/${x.catSlug}.webp)`);
    if (!reduceMotion) {
      const body = today.querySelector('.today-body');
      body.classList.remove('is-swapping'); void body.offsetWidth; body.classList.add('is-swapping');
    }
  }
  if (today) {
    const modes = today.querySelectorAll('[data-today-mode]');
    const setMode = (mode) => modes.forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.todayMode === mode)));
    const daily = () => loadIndex().then((entries) => showTerm(entries[Math.floor(Date.now() / 86400000) % entries.length]));
    const random = () => loadIndex().then((entries) => showTerm(pickRandom(entries)));
    modes.forEach((b) => b.addEventListener('click', () => {
      setMode(b.dataset.todayMode);
      (b.dataset.todayMode === 'jour' ? daily : random)().catch(() => {});
    }));
    today.querySelector('[data-today-next]').addEventListener('click', () => { setMode('hasard'); random().catch(() => {}); });
    // Le terme affiché au build est celui du jour du build : on le remet à jour sans gêner la lecture.
    const idle = window.requestIdleCallback || ((fn) => setTimeout(fn, 1200));
    new IntersectionObserver((seen, obs) => {
      if (seen.some((s) => s.isIntersecting)) { obs.disconnect(); idle(() => daily().catch(() => {})); }
    }, { rootMargin: '200px' }).observe(today);
  }
  document.addEventListener('click', (e) => {
    const r = e.target.closest('[data-random]');
    if (!r) return;
    e.preventDefault();
    loadIndex().then((entries) => { window.location.href = `/${pickRandom(entries).s}/`; }).catch(() => { window.location.href = r.href; });
  });

  // ------------------------------------------------------------ Apparitions
  const revealTargets = document.querySelectorAll(
    '.today-text, .agenda-head, .agenda-panels, .mosaic, .author-text, .author-facts, .book-band, .entry-links, .pager, .colophon, .index-bands, .index-list .bands, .index-group',
  );
  if ('IntersectionObserver' in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0 });
    revealTargets.forEach((el) => { el.setAttribute('data-reveal', ''); io.observe(el); });
  }
  // ------------------------------------------------------------ Vidéo : lue seulement à l'écran
  document.querySelectorAll('[data-lazy-video]').forEach((video) => {
    if (reduceMotion || !('IntersectionObserver' in window)) return;
    new IntersectionObserver((seen) => {
      seen.forEach((s) => {
        if (s.isIntersecting) video.play().catch(() => {});
        else video.pause();
      });
    }, { threshold: 0.2 }).observe(video);
  });

  root.classList.add('is-ready');
})();
