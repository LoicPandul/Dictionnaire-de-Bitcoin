from PIL import Image
import os

def add_black_background(image_path, output_path):
    img = Image.open(image_path)
    # Create a new image with black background
    black_bg = Image.new('RGBA', img.size, (0, 0, 0, 255))
    black_bg.paste(img, (0, 0), img)
    black_bg.convert('RGB').save(output_path, 'PNG')

cover_path = "../../scripts/PDF/cover_front.png"
output_cover_path = "../../scripts/PDF/cover_front_with_black_bg.png"
add_black_background(cover_path, output_cover_path)

print(f"\nL'image de couverture avec fond noir a été créée : {output_cover_path}\n")
