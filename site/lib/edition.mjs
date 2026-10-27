// Contenus de l'édition 2027 hors définitions : parties du livre (templates/parts.yaml),
// chronologie (chronologie/<langue>/*.yaml) et spécifications (specifications/<langue>/*.yaml).
//
// Tout est lu dans les fichiers présents : une année, une série ou une catégorie ajoutée
// ou retirée apparaît ou disparaît du site sans toucher au code.
import fs from 'node:fs';
import path from 'node:path';
import YAML from 'yaml';

const lire = (f) => YAML.parse(fs.readFileSync(f, 'utf8'));

// Parties du livre : chaque catégorie y est rangée une fois, avec son pictogramme.
export function loadParts(repoRoot) {
  const f = path.join(repoRoot, 'templates', 'parts.yaml');
  if (!fs.existsSync(f)) return [];
  return (lire(f).parts || []).map((p) => ({
    id: p.id,
    title: p.title,
    intro: (p.intro || '').trim(),
    categories: (p.categories || []).map((c) => ({ name: c.name, display: c.display || null, pictogram: c.pictogram || null })),
  }));
}

// Chronologie : un fichier par année (« avant-2009 » en tête). La langue demandée si elle
// existe, sinon le français ; chaque événement dit dans quelle langue il est écrit.
export function loadChronology(repoRoot, lang = 'fr') {
  const dir = (l) => path.join(repoRoot, 'chronologie', l);
  const fichiers = (l) => (fs.existsSync(dir(l)) ? fs.readdirSync(dir(l)).filter((f) => f.endsWith('.yaml')) : []);
  const fr = fichiers('fr');
  const traduits = new Set(lang === 'fr' ? [] : fichiers(lang));
  const annees = [];
  for (const f of new Set([...fr, ...traduits])) {
    const l = traduits.has(f) ? lang : 'fr';
    const data = lire(path.join(dir(l), f)) || {};
    const id = f.replace(/\.yaml$/, '');
    const events = (data.events || []).map((e) => ({
      date: String(e.date),
      title: e.title || '',
      text: e.text || '',
      related: e.related || [],
      sources: e.sources || [],
    }));
    if (!events.length) continue;
    events.sort((a, b) => a.date.localeCompare(b.date));
    annees.push({ id, avant: !/^\d{4}$/.test(id), lang: l, events });
  }
  // « avant-2009 » d'abord, puis les années dans l'ordre.
  annees.sort((a, b) => (a.avant !== b.avant ? (a.avant ? -1 : 1) : a.id.localeCompare(b.id)));
  return annees;
}

// Spécifications : une série par fichier. Les séries sont regroupées comme dans le livre
// (templates/editions.yaml : BOLT et bLIP ensemble) ; une série inconnue forme son propre groupe.
// Les séries viennent de specifications/fr/ (docs/structure.md) ; specifications/en/, s'il existe,
// donne le résumé anglais de chaque document (même fichier, même id), sinon le champ summary_en.
export function loadSpecifications(repoRoot) {
  const racine = path.join(repoRoot, 'specifications');
  const dir = fs.existsSync(path.join(racine, 'fr')) ? path.join(racine, 'fr') : racine;
  if (!fs.existsSync(dir)) return [];
  const series = new Map();
  for (const f of fs.readdirSync(dir).filter((x) => x.endsWith('.yaml')).sort()) {
    const data = lire(path.join(dir, f)) || {};
    const id = f.replace(/\.yaml$/, '');
    const fEn = path.join(racine, 'en', f);
    const en = new Map(fs.existsSync(fEn) ? (lire(fEn)?.entries || []).filter((e) => e.summary).map((e) => [e.id, e.summary]) : []);
    const entries = (data.entries || []).map((e) => ({
      serie: id,
      id: e.id,
      number: e.number ?? e.sort_key ?? null,
      title: e.title || '',
      status: Array.isArray(e.status) ? e.status : e.status ? [e.status] : [],
      type: e.type || null,
      layer: e.layer || null,
      authors: e.authors || [],
      created: e.created ? String(e.created) : null,
      replaces: e.replaces || [],
      supersededBy: e.superseded_by || [],
      kinds: e.kinds || [],
      summary: e.summary || '',
      summaryEn: en.get(e.id) || e.summary_en || null,
      definition: e.definition || null,
      related: e.related || [],
      url: e.url || null,
    }));
    entries.sort((a, b) => (a.number ?? 0) - (b.number ?? 0));
    series.set(id, { id, source: data.source || null, updated: data.updated ? String(data.updated) : null, entries });
  }
  // Groupes du livre : lus dans editions.yaml (sections « specs » de l'édition complète).
  const groupes = [];
  const ed = path.join(repoRoot, 'templates', 'editions.yaml');
  const vus = new Set();
  if (fs.existsSync(ed)) {
    const complete = lire(ed)?.editions?.complete;
    for (const s of complete?.sections || []) {
      if (s.type !== 'specs') continue;
      const membres = (s.series || []).filter((x) => series.has(x));
      if (!membres.length) continue;
      membres.forEach((m) => vus.add(m));
      groupes.push({ id: s.id || membres[0], title: s.title || membres[0].toUpperCase(), series: membres.map((m) => series.get(m)) });
    }
  }
  for (const [id, s] of series) if (!vus.has(id)) groupes.push({ id, title: id.toUpperCase(), series: [s] });
  return groupes;
}
