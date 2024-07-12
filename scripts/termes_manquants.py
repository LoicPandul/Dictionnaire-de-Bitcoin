import os

def read_terms_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.readlines()

def write_terms_file(filepath, lines):
    with open(filepath, 'w', encoding='utf-8') as file:
        file.writelines(lines)

def extract_terms(lines):
    terms = []
    current_term = []
    for line in lines:
        if line.startswith('## '):
            if current_term:
                terms.append(current_term)
            current_term = [line]
        else:
            if current_term:
                current_term.append(line)
    if current_term:
        terms.append(current_term)
    return terms

def sort_terms(terms):
    terms.sort(key=lambda term: term[0].strip().lower())
    return terms

def format_terms(terms):
    formatted_lines = []
    for term in terms:
        formatted_lines.append(term[0].strip() + '\n')
        if len(term) > 1:
            formatted_lines.append('\n')
            formatted_lines.extend([line.strip() + '\n' for line in term[1:] if line.strip()])
            formatted_lines.append('\n\n')
        else:
            formatted_lines.append('\n\n')
    return formatted_lines

def integrate_terms(intro, terms):
    result = intro + ['\n']
    result.extend(terms)
    return result

def extract_existing_terms(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    terms = set()
    for line in lines:
        if line.startswith('## '):
            term = line.strip()
            terms.add(term)
    return terms

def mark_existing_terms(missing_terms, existing_terms):
    marked_terms = []
    for term in missing_terms:
        term_title = term[0].strip()
        if term_title in existing_terms and 'ATTENTION : TERME DÉJÀ PRÉSENT !\n' not in term:
            term.append('ATTENTION : TERME DÉJÀ PRÉSENT !\n')
        marked_terms.append(term)
    return marked_terms

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    terms_file = os.path.join(repo_root, 'Termes en attente.md')
    dictionary_file = os.path.join(repo_root, 'autres_formats/dictionnaire_complet/dictionnaire_complet.md')

    lines = read_terms_file(terms_file)

    intro_end_index = lines.index('___\n') + 1
    intro = lines[:intro_end_index]
    terms_lines = lines[intro_end_index:]

    terms = extract_terms(terms_lines)
    sorted_terms = sort_terms(terms)

    existing_terms = extract_existing_terms(dictionary_file)
    marked_terms = mark_existing_terms(sorted_terms, existing_terms)

    formatted_terms = format_terms(marked_terms)
    final_lines = integrate_terms(intro, formatted_terms)

    write_terms_file(terms_file, final_lines)

if __name__ == '__main__':
    main()
