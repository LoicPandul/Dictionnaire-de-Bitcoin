import pypandoc
import os

def convert_md_to_pdf(md_file_path, pdf_output_path):
    # Définition du chemin de Pandoc si nécessaire
    # Par exemple : os.environ.setdefault('PYPANDOC_PANDOC', 'C:/Program Files/Pandoc/pandoc.exe')
    
    output = pypandoc.convert_file(
        source_file=md_file_path,
        format='md',
        to='pdf',
        outputfile=pdf_output_path,
        extra_args=['--pdf-engine=xelatex', '-V geometry:margin=1in']  # Ajoute des arguments pour la mise en page
    )

    print(f"Le fichier PDF a été créé : {pdf_output_path}")

# Chemin du fichier Markdown
markdown_path = "../../autres_formats/dictionnaire_complet/dictionnaire_complet.md"
# Chemin de sortie du fichier PDF
pdf_path = "../../dictionnaire_complet.pdf"

# Appeler la fonction de conversion
convert_md_to_pdf(markdown_path, pdf_path)
