from getImage import getUrl, download
from applyfilter import applyFilter
from subprocess import run
import os
from colorama import Fore 
from sys import argv

keyword = argv[-1]
url, name = getUrl(keyword)

print(f'{Fore.MAGENTA}Searching {keyword} image..')

download(url, name)

print(f'{Fore.GREEN}Image downloaded.')

print(f'{Fore.MAGENTA}Applying filter..')
applyFilter(name)

run('nitrogen --set-zoom-fill filtered.png', shell=True, capture_output=True)
os.remove(name)

# To run it in background.
keep = input(f'{Fore.YELLOW}keep ? : ')

if keep == 'y' or keep == 'Y':
    os.rename('filtered.png', '/home/mohan/Downloads/walls/filtered.png')
    os.rename('filtered-lock.png', '/home/mohan/Downloads/walls/filtered-lock.png')
    
else :
    run('nitrogen --set-zoom-fill /home/mohan/Downloads/walls/filtered.png', capture_output=True, shell=True)
