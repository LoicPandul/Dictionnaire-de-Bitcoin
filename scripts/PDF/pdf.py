import pypandoc

def convert_md_to_pdf(md_file_path, pdf_output_path):
    extra_args = [
        '--pdf-engine=xelatex',
        '-V', 'geometry:top=1.2in',
        '-V', 'geometry:bottom=1.2in',
        '-V', 'geometry:left=1.2in',
        '-V', 'geometry:right=1.2in',
        '-V', 'mainfont=Arial',  # Applique Arial au contenu principal
        r'-V', r'header-includes=\usepackage{sectsty}',  # Permet de personnaliser les sections, notez le préfixe r
        r'-V', r'header-includes=\sectionfont{\usefont{T1}{qtm}{m}{n}}',  # Utilise TeX Gyre Termes pour les titres de section, notez le préfixe r
    ]

    output = pypandoc.convert_file(
        source_file=md_file_path,
        format='md',
        to='pdf',
        outputfile=pdf_output_path,
        extra_args=extra_args
    )

    print(f"Le fichier PDF a été créé : {pdf_output_path}")

markdown_path = "dictionnaire_MD_for_PDF.md"
pdf_path = "../../Dictionnaire de Bitcoin.pdf"

convert_md_to_pdf(markdown_path, pdf_path)
