import os
import re

def get_definitions_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    titles = re.findall(r'^## (.+)$', content, re.MULTILINE)
    return titles

def generate_definitions_content(dictionnaire_folder):
    definitions_content = ""
    definitions = {}
    
    for filename in os.listdir(dictionnaire_folder):
        if filename.endswith(".md"):
            letter = filename.split('.')[0] 
            filepath = os.path.join(dictionnaire_folder, filename)
            definitions[letter] = get_definitions_from_file(filepath)
    
    for letter, titles in sorted(definitions.items()):
        definitions_content += f"### {letter.upper()}\n\n"
        for title in titles:
            anchor = title.lower().replace(' ', '-')
            definitions_content += f"- [{title}](./dictionnaire/{letter}.md#{anchor})\n"
        definitions_content += "\n"
    return definitions_content

def update_index(dictionnaire_folder, index_file):
    definitions_content = generate_definitions_content(dictionnaire_folder)
    
    with open(index_file, 'w', encoding='utf-8') as file:
        file.write(definitions_content)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__) 
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir)) 
    dictionnaire_folder = os.path.join(project_root, 'dictionnaire')  
    index_file = os.path.join(project_root, 'INDEX.md') 
    
    update_index(dictionnaire_folder, index_file)
