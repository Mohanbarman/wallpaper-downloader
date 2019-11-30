from getImage import getUrl, download
from applyfilter import applyFilter
from subprocess import run
import os
from colorama import Fore 
from sys import argv

if len(argv) <= 1:
    print(f'{Fore.RED}Please pass the search query.')
    quit()

# Last number of the files in history
files = os.listdir('history/')
last_num = 1 if len(files) == 0 else max(map(lambda f: int(f.split('-')[0]), files), 1)

keyword = argv[-1]
url, name = getUrl(keyword)
print(f'{Fore.MAGENTA}Searching {keyword} image..')

download(url, name)
print(f'{Fore.GREEN}Image downloaded.')

print(f'{Fore.MAGENTA}Applying filter..')
applyFilter(name, last_num)

run('nitrogen --set-zoom-fill filtered.png', shell=True, capture_output=True)
os.remove(name)

keep = input(f'{Fore.YELLOW}keep ? : ')

history_files = os.listdir('history/') # To save images in history

if keep == 'y' or keep == 'Y':
    print(f'Put "nitrogen --set-zoom-fill {os.getcwd()}/filtered.png" to your startup file.')
else :
    run('nitrogen --set-zoom-fill /home/mohan/Downloads/walls/filtered.png', capture_output=True, shell=True)