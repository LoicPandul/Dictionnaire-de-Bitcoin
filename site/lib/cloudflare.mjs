// Fichiers de configuration de Cloudflare Pages, écrits dans dist/ au build :
// _headers (cache et sécurité) et _redirects (anciennes formes d'adresse).
// Doc : https://developers.cloudflare.com/pages/configuration/headers/ et /redirects/

// inlineHash : empreinte SHA-256 du seul script en ligne (thème et classe js), autorisé par la CSP.
export function headers({ inlineHash }) {
  const csp = [
    "default-src 'self'",
    `script-src 'self' 'sha256-${inlineHash}'`,
    "style-src 'self' 'unsafe-inline'",
    "img-src 'self' data:",
    "font-src 'self'",
    "connect-src 'self'",
    "object-src 'none'",
    "base-uri 'self'",
    "form-action 'self'",
    "frame-ancestors 'none'",
  ].join('; ');
  return `/*
  Content-Security-Policy: ${csp}
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  X-Frame-Options: DENY

# Fichiers à empreinte ou qui ne changent pas de nom sans changer de contenu : un an.
/css/*
  Cache-Control: public, max-age=31536000, immutable
/js/*
  Cache-Control: public, max-age=31536000, immutable
/fonts/*
  Cache-Control: public, max-age=31536000, immutable
/katex/*
  Cache-Control: public, max-age=31536000, immutable

# Images et données : une semaine, revalidées ensuite.
/img/*
  Cache-Control: public, max-age=604800, stale-while-revalidate=86400
/video/*
  Cache-Control: public, max-age=604800, stale-while-revalidate=86400
/:slug/assets/*
  Cache-Control: public, max-age=604800, stale-while-revalidate=86400
/recherche.json
  Cache-Control: public, max-age=3600, stale-while-revalidate=86400
/tranche.json
  Cache-Control: public, max-age=3600, stale-while-revalidate=86400

/dictionnaire-de-bitcoin.pdf
  Content-Disposition: inline; filename="dictionnaire-de-bitcoin.pdf"
  Cache-Control: public, max-age=86400
`;
}

// L'ancien préfixe de pandul.fr mène aux bonnes adresses.
export function redirects() {
  return [
    '# Ancien préfixe de pandul.fr, si quelqu’un recopie une adresse à la main',
    '/dictionnaire/ / 301',
    '/dictionnaire/categorie/:cat/ /categorie/:cat/ 301',
    '/dictionnaire/lettre/:l/ /lettre/:l/ 301',
    '/dictionnaire/:slug/ /:slug/ 301',
    '',
  ].join('\n');
}
