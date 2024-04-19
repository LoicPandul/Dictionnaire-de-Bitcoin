import pypandoc

def convert_md_to_pdf(md_file_path, pdf_output_path):

    output = pypandoc.convert_file(
        source_file=md_file_path,
        format='md',
        to='pdf',
        outputfile=pdf_output_path,
        extra_args=['--pdf-engine=xelatex', '-V geometry:margin=1in']
    )

    print(f"Le fichier PDF a été créé : {pdf_output_path}")

markdown_path = "../../autres_formats/dictionnaire_complet/dictionnaire_complet.md"
pdf_path = "../../dictionnaire_complet.pdf"

convert_md_to_pdf(markdown_path, pdf_path)
