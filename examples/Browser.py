import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

f= open('titles.txt', 'r')
lines = f.readlines()

encontrado = False

titles = {}
InvertIndex = {}
for line in lines:
    line = line.split(',')
    titles.update({line[0]: line[1]})

f= open('Output.txt', 'r')
search = input('Ingrese palabras a buscar: ')

lines = f.readlines()

search = search.split(' ')

for word in search:
    for line in lines:
        if word in line:
            line = line.replace(' ','').split('|')
            wordcount = line[1][1:-2].split(',')
            for i in wordcount:
                encontrado = True
                article = i.split(':')
                if article[0] in InvertIndex:
                    count = InvertIndex[article[0]]
                    InvertIndex.update({article[0]: count+1})
                else:
                    InvertIndex.update({article[0]: 1})

if encontrado:
    maxArticle = max(InvertIndex.values())
    article = max(InvertIndex, key=InvertIndex.get)
    article = titles[article[1:-1]]
    page_py = wiki_wiki.page(article[:-1])
    print('El articulo que busca es: ',article[:-1])
    print('URL: ',page_py.fullurl)   
else:
    print('Palabras no encontradas.')
