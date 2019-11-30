from tqdm import tqdm
from colorama import Fore
import requests
import json
import sys

def getUrl(keyword):
    parameters = {
        'client_id': '34b0c45d8af37bf41eae7f26abbd5323a5757bb4e846349d129b639006bb5642',
        'query': keyword,
        'count': 1
    }
    image_headers = '&fit=crop&w=1920&h=1080&fm=png'

    res = requests.get(
        'https://api.unsplash.com/photos/random', 
        params=parameters,
        )
    json_data = json.loads(res.content.decode())
    
    image_url = json_data[0]['urls']['raw'] + image_headers
    image_name = json_data[0]['alt_description'].replace(' ','-') + '.png'

    return image_url, image_name

def download(url, name):
    res = requests.get(url, stream=True)
    size = int(res.headers['Content-Length'])

    with open(name, 'wb') as f:
        for chunk in tqdm(res.iter_content(
            chunk_size=1024), total=size/1024, 
            unit='KB', bar_format=Fore.GREEN + 'Downloading :{percentage:4.0f}%',
            leave=False):
            f.write(chunk)

if __name__ == "__main__":
    query = input('Enter search query : ')
    url, name = getUrl(query)
    download(url, name)