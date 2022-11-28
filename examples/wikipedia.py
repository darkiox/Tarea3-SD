import requests
import wikipediaapi
import os
import shutil

shutil.rmtree('Carpeta1',ignore_errors=True)
shutil.rmtree('Carpeta2',ignore_errors=True)

S = requests.Session()

wiki_wiki = wikipediaapi.Wikipedia('en')

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "10",
    "rnfilterredir": "nonredirects",
    "rnnamespace" : 0
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

RANDOMS = DATA["query"]["random"]
i = 1

directory = "Carpeta1"
os.makedirs(directory,exist_ok = True)

directory = "Carpeta2"
os.makedirs(directory,exist_ok = True)

carpeta = 'Carpeta1/'
for r in RANDOMS:

    Titulo = r["title"].replace(' ', '_')
    page_py = wiki_wiki.page(Titulo)
    file = carpeta+str(i)+'.txt'

    with open("titles.txt", 'a') as f:
        f.write(str(i))
        f.write(",")
        f.write(Titulo)
        f.write('\n')

    with open(file, 'w') as f:
        f.write(str(i))
        f.write(",")
        f.write(Titulo)
        f.write('\n')
        f.write(page_py.text)

    if i == 5:
        carpeta = 'Carpeta2/'

    i+=1

