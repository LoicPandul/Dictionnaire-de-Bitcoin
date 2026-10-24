#!/usr/bin/env bash
# Prépare les images du site (à relancer seulement si les sources changent).
# - l'arbre gravé, découpé dans la couverture du livre (assets/cover-paperback.pdf) ;
# - les planches de l'Encyclopédie (domaine public), téléchargées dans un dossier temporaire,
#   passées en gravure claire sur le bleu nuit de la couverture.
# Sources des planches et du film : champ « image » de tools/image-credits.json, à télécharger
# dans $TMPDIR/dict-images/found (ou passer le dossier en premier argument).
# Dépendances : pdftoppm (poppler), ffmpeg avec libwebp et librsvg.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT=..
OUT=static/img
TMP=${TMPDIR:-/tmp}/dict-images
SRC=${1:-$TMP/found}
mkdir -p "$TMP" "$OUT"

# 1. Arbre de la couverture (face avant, 300 dpi)
pdftoppm -r 300 -png "$ROOT/assets/cover-paperback.pdf" "$TMP/cover"
COVER="$TMP/cover-1.png"
ffmpeg -v error -y -i "$COVER" -vf "crop=1690:560:2090:0" -quality 82 "$OUT/arbre-canopee.webp"
ffmpeg -v error -y -i "$COVER" -vf "crop=1690:980:2090:1080" -quality 82 "$OUT/arbre-tronc.webp"
ffmpeg -v error -y -i "$COVER" -vf "crop=1800:2625:1981:0,scale=900:-1" -quality 84 "$OUT/couverture.webp"
ffmpeg -v error -y -i "$COVER" -vf "crop=1800:945:1981:0,scale=1200:630" -q:v 3 "$OUT/social-card.jpg"

# 2. Planches de l'Encyclopédie : gravure claire (#9db0bd) sur bleu nuit (#193042)
duotone="format=gray,lut=y='clip((235-val)*1.45,0,255)',format=rgb24,lutrgb=r='25+val*132/255':g='48+val*128/255':b='66+val*123/255'"
plate() { # source, crop, sortie, largeur
  ffmpeg -v error -y -i "$SRC/$1" -vf "crop=$2,scale=$4:-1,$duotone" -quality 80 "$OUT/$3"
}
plate encyclopedie-de-d-alembert-et-diderot-premiere.jpg "iw*0.96:ih*0.60:iw*0.02:ih*0.015" encyclopedie-titre.webp 1100
plate monnoyage-balancier-g-37125.jpg "iw*0.74:ih*0.36:iw*0.13:ih*0.12" monnoyage-balancier.webp 1400
plate monnoyage-laminoirs-g-37119.jpg "iw*0.74:ih*0.70:iw*0.13:ih*0.10" monnoyage-laminoirs.webp 1100
ls -la "$OUT"

# 3. Pictogrammes de catégorie du livre (assets/pictograms), en masques alpha 160 px :
#    noir -> opaque, blanc -> transparent, pour les teinter en CSS (mask-image).
mkdir -p "$OUT/pictos"
for svg in "$ROOT"/assets/pictograms/*.svg; do
  name=$(basename "$svg" .svg)
  ffmpeg -v error -y -c:v librsvg -width 160 -height 160 -i "$svg" \
    -filter_complex "color=white:s=160x160[bg];[bg][0:v]overlay=shortest=1,format=gray,negate,format=ya8,geq=lum='0':a='clip((lum(X,Y)-16)*1.1644,0,255)'" \
    -frames:v 1 -c:v libwebp -lossless 1 "$OUT/pictos/$name.webp"
done

# 4. Le livre en volume, découpé dans la bannière du dépôt (assets/images/cover.png)
ffmpeg -v error -y -i "$ROOT/assets/images/cover.png" -vf "crop=1150:1000:0:0" -quality 84 "$OUT/livre-volume.webp"

# 5. Boucle vidéo : « Learning to Set Type » (1959, domaine public, Internet Archive),
#    8 secondes de composition à la main, passées au bleu nuit. Source : $TMP/learning1959.mp4
#    (https://archive.org/download/Learning1959/Learning1959.mp4).
VIDEO_SRC=${VIDEO_SRC:-$TMP/learning1959.mp4}
if [ -f "$VIDEO_SRC" ]; then
  mkdir -p static/video
  tone="format=gray,eq=contrast=1.15,format=rgb24,lutrgb=r='25+val*(234-25)/255':g='48+val*(236-48)/255':b='66+val*(233-66)/255',scale=640:480"
  ffmpeg -v error -y -ss 229 -t 8 -i "$VIDEO_SRC" -an -vf "$tone,fps=24" -c:v libx264 -preset slow -crf 27 -pix_fmt yuv420p -movflags +faststart static/video/composition.mp4
  ffmpeg -v error -y -ss 229 -i "$VIDEO_SRC" -frames:v 1 -vf "$tone" -quality 80 static/video/composition.webp
fi
ffmpeg -v error -y -i "$OUT/couverture.webp" -vf scale=240:-1 -quality 82 "$OUT/couverture-petite.webp"
