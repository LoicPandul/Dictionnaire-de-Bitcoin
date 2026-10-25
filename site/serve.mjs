// Aperçu local de site/dist, au plus près de Cloudflare Pages : index.html des dossiers,
// redirection vers la barre finale, 404.html servie avec le code 404, en-têtes de _headers
// (règles simples « /chemin/* »), compression gzip.
//   node serve.mjs [--port 4318] [--host 0.0.0.0] [--dir dist]
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import zlib from 'node:zlib';
import { fileURLToPath } from 'node:url';

const here = path.dirname(fileURLToPath(import.meta.url));
const arg = (name, fallback) => {
  const i = process.argv.indexOf(name);
  return i > -1 ? process.argv[i + 1] : fallback;
};
const port = Number(arg('--port', 4318));
const host = arg('--host', '127.0.0.1');
const root = path.resolve(here, arg('--dir', 'dist'));

const TYPES = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8', '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8', '.svg': 'image/svg+xml', '.webp': 'image/webp', '.avif': 'image/avif',
  '.png': 'image/png', '.jpg': 'image/jpeg', '.woff2': 'font/woff2', '.pdf': 'application/pdf', '.mp4': 'video/mp4',
  '.xml': 'application/xml; charset=utf-8', '.txt': 'text/plain; charset=utf-8', '.webmanifest': 'application/manifest+json',
};
const COMPRESS = /\.(html|css|js|json|svg|xml|txt|webmanifest)$/;

// _headers : blocs « chemin » suivis de lignes « Nom: valeur » indentées.
const rules = [];
try {
  let cur = null;
  for (const line of fs.readFileSync(path.join(root, '_headers'), 'utf8').split('\n')) {
    if (!line.trim() || line.trim().startsWith('#')) continue;
    if (!/^\s/.test(line)) rules.push((cur = { pattern: line.trim(), headers: [] }));
    else if (cur) {
      const i = line.indexOf(':');
      cur.headers.push([line.slice(0, i).trim(), line.slice(i + 1).trim()]);
    }
  }
} catch {}
const matches = (pattern, p) => (pattern.endsWith('*') ? p.startsWith(pattern.slice(0, -1)) : p === pattern);

function send(req, res, file, status = 200) {
  const ext = path.extname(file);
  const headers = { 'Content-Type': TYPES[ext] || 'application/octet-stream' };
  for (const r of rules) if (matches(r.pattern, new URL(req.url, 'http://x').pathname)) for (const [k, v] of r.headers) headers[k] = v;
  let body = fs.readFileSync(file);
  if (COMPRESS.test(file) && /\bgzip\b/.test(req.headers['accept-encoding'] || '')) {
    body = zlib.gzipSync(body);
    headers['Content-Encoding'] = 'gzip';
  }
  headers['Content-Length'] = body.length;
  res.writeHead(status, headers);
  res.end(req.method === 'HEAD' ? undefined : body);
}

http
  .createServer((req, res) => {
    const url = new URL(req.url, 'http://x');
    const p = decodeURIComponent(url.pathname);
    const file = path.join(root, p);
    if (!file.startsWith(root)) return res.writeHead(403).end();
    try {
      const st = fs.statSync(file);
      if (st.isDirectory()) {
        if (!p.endsWith('/')) {
          res.writeHead(308, { Location: `${p}/${url.search}` });
          return res.end();
        }
        if (fs.existsSync(path.join(file, 'index.html'))) return send(req, res, path.join(file, 'index.html'));
      } else return send(req, res, file);
    } catch {}
    return send(req, res, path.join(root, '404.html'), 404);
  })
  .listen(port, host, () => console.log(`Aperçu de ${path.relative(process.cwd(), root) || '.'} sur http://${host}:${port}/`));
