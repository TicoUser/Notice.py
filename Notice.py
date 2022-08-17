import requests
from bs4 import BeautifulSoup as bs
url = "https://g1.globo.com/pop-arte/games/"

resposta = request.get(url)
html = bs(resposta.text, "html.parser")
#entrando no G1

noticias = html.find_all('div', {'class':"feed-post-body-resumo"})
#pegando noticia no site

for noticia in noticias>
    print(noticia.text+'\n')
