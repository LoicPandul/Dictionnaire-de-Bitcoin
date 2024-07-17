import os
import re
import unicodedata
from colorama import init, Fore, Style

init()

def normalize_title(title, is_o_file=False):
    title = re.sub(r'\(.*?\)', '', title)
    title = unicodedata.normalize('NFD', title)
    title = ''.join(c for c in title if unicodedata.category(c) != 'Mn')
    if not is_o_file:
        title = re.sub(r'[^\w]', '', title)
    else:
        title = re.sub(r'[^\w_]', '', title)
    return title.lower()

def verify_alphabetical_order(filepath, is_o_file=False):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    titles = [line.strip() for line in lines if line.startswith('##') and not re.match(r'##\s*(BIP|SIGHASH)', line, re.IGNORECASE)]
    normalized_titles = [normalize_title(title, is_o_file) for title in titles]
    sorted_titles = sorted(normalized_titles)

    misplaced_titles = []
    for i, (title, normalized_title) in enumerate(zip(titles, normalized_titles)):
        if normalized_title != sorted_titles[i]:
            misplaced_titles.append(title)

    return misplaced_titles

def main():
    dict_dir = './dictionnaire'
    md_files = [f for f in os.listdir(dict_dir) if f.endswith('.md')]

    all_misplaced_titles = {}
    for md_file in md_files:
        filepath = os.path.join(dict_dir, md_file)
        is_o_file = (md_file.lower() == 'o.md')
        misplaced_titles = verify_alphabetical_order(filepath, is_o_file)
        if misplaced_titles:
            all_misplaced_titles[md_file] = misplaced_titles

    if all_misplaced_titles:
        for md_file, titles in all_misplaced_titles.items():
            print(Fore.YELLOW + f"File {md_file}:" + Style.RESET_ALL)
            for title in titles:
                print(Fore.YELLOW + f"  - {title}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "Alphabetical order OK!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
