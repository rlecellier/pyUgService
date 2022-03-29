import re
import os
import json
from utils.dev import pretty_print
from os.path import exists

# file_exists = exists(path_to_file)
SAVE_BASE_DIR = '/home/rlecellier/work/perso/pyUgService'

def get_song_list(list_name):
    file_path = f'{SAVE_BASE_DIR}/song_list/{string_to_file_name(list_name)}.json'
    if exists(file_path):
        f = open(file_path)
        data = json.load(f)
        f.close()
        if data['list']:
            return data['list']
    return None

def string_to_file_name(str):
    file_name = re.sub(f"[ ,'\-:]", '_', str.lower())
    return re.sub(f"_+", '_', file_name)

def get_search_results_file_path(search_string):
    file_name = string_to_file_name(search_string)
    return f'{SAVE_BASE_DIR}/search_results/{file_name}.json'

def get_search_results(search_string):
    file_path = get_search_results_file_path(search_string)
    if exists(file_path):
        f = open(file_path)
        data = json.load(f)
        f.close()
        return data
    return None

def save_search_results(search_string, data):
    file_path = get_search_results_file_path(search_string)
    fp = open(file_path, 'w+', encoding="utf-8")
    fp.write(json.dumps(data, indent=2))
    fp.write('\n')
    fp.close()

def get_tab_raw_data_file_path(tab_id, author, title):
    file_name = string_to_file_name(f'{author} {title} {tab_id}')
    author_dir = string_to_file_name(author if author else 'unknown')
    return f'{SAVE_BASE_DIR}/tab_raw_data/{author_dir}/{file_name}.json'

def save_tab_raw_data(tab_id, author, title, data):
    file_path = get_tab_raw_data_file_path(tab_id, author, title)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    fp = open(file_path, 'w+', encoding="utf-8")
    fp.write(json.dumps(data, indent=2))
    fp.write('\n')
    fp.close()