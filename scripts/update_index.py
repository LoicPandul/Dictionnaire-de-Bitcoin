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

def update_index_with_markers(dictionnaire_folder, index_file):
    start_marker = "<!-- AUTO-INDEX START -->"
    end_marker = "<!-- AUTO-INDEX END -->"
    content_before = content_after = ""
    definitions_content = generate_definitions_content(dictionnaire_folder)
    
    with open(index_file, 'r', encoding='utf-8') as file:
        content = file.read()
        start_index = content.find(start_marker)
        end_index = content.find(end_marker)
        
        if start_index != -1 and end_index != -1:
            content_before = content[:start_index + len(start_marker)]
            content_after = content[end_index:]
        else:
            content_before = content
    
    new_content = content_before + "\n" + definitions_content + content_after
    
    with open(index_file, 'w', encoding='utf-8') as file:
        file.write(new_content)

if __name__ == "__main__":
    script_dir = os.path.dirname(__file__) 
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir)) 
    dictionnaire_folder = os.path.join(project_root, 'dictionnaire')  
    index_file = os.path.join(project_root, 'INDEX.md') 
    
    update_index_with_markers(dictionnaire_folder, index_file)
