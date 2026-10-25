// Rend les calques de la jaquette 2027 (couronne.svg, racines.svg, produits par tools/jaquette-2027.py) en PNG.
//   node tools/raster-jaquette.mjs <dossier> 1100 1600   (Playwright installé à côté, sans écran)
// Rend couronne.svg (opaque) et racines.svg (transparent) en PNG à plusieurs hauteurs.
import { chromium } from 'playwright';
import fs from 'node:fs';
const [dir, ...hs] = process.argv.slice(2);
const b = await chromium.launch();
for (const name of ['couronne', 'racines']) {
  const svg = fs.readFileSync(`${dir}/${name}.svg`, 'utf8');
  const [, w, h] = svg.match(/viewBox="0 0 ([\d.]+) ([\d.]+)"/).map(Number);
  for (const H of hs.map(Number)) {
    const W = Math.round((H * w) / h);
    const p = await b.newPage({ viewport: { width: W, height: H } });
    await p.setContent(`<html><body style="margin:0;background:transparent">${svg.replace(/width="[\d.]+" height="[\d.]+"/, `width="${W}" height="${H}"`)}</body></html>`);
    await p.waitForTimeout(300);
    await p.screenshot({ path: `${dir}/${name}-${H}.png`, omitBackground: name === 'racines', clip: { x: 0, y: 0, width: W, height: H } });
    await p.close();
  }
}
await b.close();
console.log('ok');
