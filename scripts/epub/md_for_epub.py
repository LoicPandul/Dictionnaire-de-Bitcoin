import os
import datetime

def generate_md_for_epub(md_input_path, md_output_path, contributors_path, license_info):
    with open(md_input_path, 'r', encoding='utf-8') as input_file:
        content = input_file.read()

    current_date = datetime.datetime.now().strftime("%d %B %Y")

    license_text = f"""
{license_info}

Version du {current_date}

https://github.com/LoicPandul/Dictionnaire-de-Bitcoin

Cet ouvrage est sous licence CC BY-NC-SA 4.0

https://creativecommons.org/licenses/by-nc-sa/4.0/

Lightning : pandul@sats.rs

Email : loic@pandul.fr

Site web : https://www.pandul.fr/

GitHub : https://github.com/LoicPandul/
"""

    with open(contributors_path, 'r', encoding='utf-8') as contributors_file:
        contributors_content = contributors_file.read()

    contributors_content = contributors_content.replace('*Dictionnaire de Bitcoin*', 'Dictionnaire de Bitcoin')

    def convert_md_lists_to_html(md_content):
        lines = md_content.split('\n')
        html_content = []
        in_list = False

        for line in lines:
            if line.strip().startswith('*'):
                if not in_list:
                    html_content.append('<ul>')
                    in_list = True
                line_content = line.strip().lstrip('*').strip()
                html_content.append(f'<li>{line_content}</li>')
            else:
                if in_list:
                    html_content.append('</ul>')
                    in_list = False
                html_content.append(line)

        if in_list:
            html_content.append('</ul>')

        return '\n'.join(html_content)

    new_content = f"{license_text}\n\n\\newpage\n\n{convert_md_lists_to_html(contributors_content)}\n\n\\newpage\n\n{convert_md_lists_to_html(content)}"

    with open(md_output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(new_content)

    print(f"\nLe fichier Markdown intermédiaire pour ePub a été créé : {md_output_path}\n")

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_input_path = os.path.join(base_dir, "../../autres_formats/dictionnaire_complet/dictionnaire_complet.md")
    md_output_path = os.path.join(base_dir, "dictionnaire_MD_for_ePub.md")
    contributors_path = os.path.join(base_dir, "../../scripts/PDF/contributeurs_paragraphe.md")
    license_info = """
© 2024 Loïc Morel
Dictionnaire de Bitcoin : Tout le vocabulaire technique de Bitcoin
"""

    generate_md_for_epub(md_input_path, md_output_path, contributors_path, license_info)
