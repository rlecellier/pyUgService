from bs4 import BeautifulSoup
import requests
import json

SITE_HOST = "https://www.ultimate-guitar.com"

def build_tab_url(uri):
    return f'https://tabs.ultimate-guitar.com{uri}'

def build_search_url(type, value):
    return  f'{SITE_HOST}/search.php?search_type={type}&value={value}'

def extract_data(html):
    print('extract_data:html', html)
    soup = BeautifulSoup(html, 'html.parser')
    js_store_div = soup.find(class_='js-store')
    json_obj = json.loads(js_store_div['data-content'])
    return json_obj

def serializeResults(results):
    return [{
        'artist_name': row['artist_name'],
        'song_name': row['song_name'],
        'rating': row['rating'],
        'votes': row['votes'],   
        'tab_id': row['id'] if 'id' in row else '--',
        'song_id': row['song_id'] if 'song_id' in row else '--',
        'artist_id': row['artist_id'] if 'artist_id' in row else '--',
        'type': row['type'] if 'type' in row else '--',
        'tab_url': row['tab_url'] if 'tab_url' in row else '--',
        'artist_tab_url': row['tab_url'] if 'tab_url' in row else '--',
    } for row in results if 'id' in row and row['type'].lower() == 'chords']
    #  

def search_songs_by_band(search_band):
    search_response = requests.get(build_search_url('band', search_band))
    data = extract_data(search_response.text)
    search_results = data['store']['page']['data']['results']
    return search_results

def search_songs_by_title(search_title):
    search_response = requests.get(build_search_url('title', search_title))
    data = extract_data(search_response.text)
    search_results = data['store']['page']['data']['results']
    return serializeResults(search_results)

def get_song_tab_raw_data(url):
    response = requests.get(url)
    return extract_data(response.text)
    # print('data', data)
    # tab = data['store']['page']['data']['tab']
    # tab_view = data['store']['page']['data']['tab_view']
    # applicature = tab_view['applicature']
    # tab_view['applicature'] = [] # remove big chord elements for now

    return [
        tab, 
        tab_view, 
        applicature
    ]