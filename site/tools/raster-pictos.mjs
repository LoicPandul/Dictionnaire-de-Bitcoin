// Rend les 19 pictogrammes du livre (assets/pictograms/*.svg) en PNG 1024 px, noir sur blanc,
// pour que prepare-assets.py les retrace en SVG d'un seul tracé. Certains SVG d'origine
// contiennent une image intégrée : seul un navigateur les lit tous correctement.
//   node tools/raster-pictos.mjs /tmp/pictos   (Playwright installé à côté, sans écran)
import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const src = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '../../assets/pictograms');
const out = process.argv[2] || '/tmp/pictos';
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1024, height: 1024 } });
for (const f of fs.readdirSync(src).filter((n) => n.endsWith('.svg'))) {
  const svg = fs.readFileSync(path.join(src, f), 'utf8').replace(/width="2000"/, 'width="1024"').replace(/height="2000"/, 'height="1024"');
  await page.setContent(`<body style="margin:0;background:#fff"><div style="width:1024px;height:1024px">${svg}</div></body>`);
  await page.waitForTimeout(150);
  await page.screenshot({ path: path.join(out, f.replace(/\.svg$/, '.png')), clip: { x: 0, y: 0, width: 1024, height: 1024 } });
}
await browser.close();
console.log(`pictogrammes rendus dans ${out}`);
