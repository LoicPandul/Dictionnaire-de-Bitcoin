import subprocess
import os

def generate_epub(md_file_path, epub_output_path, metadata_file, css_file):
    command = [
        "pandoc",
        md_file_path,
        "--output", epub_output_path,
        "--metadata-file", metadata_file,
        "--css", css_file,
        "--toc",
        "--epub-cover-image=../../scripts/PDF/cover_front_with_black_bg.png",
        "--epub-metadata", metadata_file,
        "--from=markdown",
        "--to=epub"
    ]
    
    subprocess.run(command, check=True)
    print(f"\nLe fichier ePub a été créé : {epub_output_path}\n")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_file_path = os.path.join(base_dir, "dictionnaire_MD_for_ePub.md")
    epub_output_path = os.path.join(base_dir, "../../Dictionnaire_de_Bitcoin.epub")
    metadata_file = os.path.join(base_dir, "metadata.yaml")
    css_file = os.path.join(base_dir, "style.css")
    
    generate_epub(md_file_path, epub_output_path, metadata_file, css_file)
