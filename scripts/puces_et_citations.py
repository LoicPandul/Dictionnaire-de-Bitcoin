import os

def replace_bullet_points(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('- '):
            lines[i] = '*' + line[1:]

    content = '\n'.join(lines)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def add_empty_line_before_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    lines = content.split('\n')
    for i, line in enumerate(lines):
        if line.startswith('>'):
            if i > 0 and lines[i-1] != '':
                lines[i-1] += '\n'

    content = '\n'.join(lines)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'dictionnaire'))
    
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            replace_bullet_points(file_path)
            add_empty_line_before_quotes(file_path)

if __name__ == "__main__":
    main()
