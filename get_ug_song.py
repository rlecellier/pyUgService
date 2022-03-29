from utils.dev import pretty_print
from utils.file import save_search_results, get_search_results, get_song_list, save_tab_raw_data
from services.UgService import search_songs_by_title, get_song_tab_raw_data
import time

def search_and_save(author, title):
    search_string = f'{title} {author}'
    results = get_search_results(search_string)
    if results == None:
        print('...New search for: ', search_string)
        results = search_songs_by_title(search_string)
        save_search_results(search_string, results)
        print('New search results: ')
        pretty_print(search_string, results)
        print('sleep 5 seconds before next search...')
        time.sleep(5)
    else:
        print('Saved results for: ') 
        pretty_print(search_string, results)
        print('----')
    return results

song_list = get_song_list('cahier en')
list_len = len(song_list)
i = 0
found = 0
search_results = []
try:
    for song_str in song_list:
        i += 1
        (title, author) = song_str.split(' -- ')
        print(f'[{i}/{list_len}] Search for: ', f'{title} {author}')
        results = search_and_save(author, title)
        if len(results) > 0:
            found += 1
            # most_voted_song = max(results, key=lambda x:x['votes'])
            # raw_tab_data = get_song_tab_raw_data(most_voted_song['tab_url'])
            # print('sleep 5 seconds before next search...')
            # time.sleep(5)
            # save_tab_raw_data(most_voted_song['tab_id'], author, title, raw_tab_data)
except Exception as e:
    print('ERROR: ', e)

print(f'results found {found} / {list_len}')
print(f'missing results {list_len - found} / {list_len}')

    