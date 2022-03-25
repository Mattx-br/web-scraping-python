import requests
from bs4 import BeautifulSoup

url = 'https://www.comandotorrents.ninja/ousama-ranking-1a-temporada-completa-torrent-dublada-e-legendada/'

headers = {
    # para saber o user agent do seu pc, escreva no google:
    # my user agent e copie o resultado
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'
}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

episodes = soup.find_all('tr', class_='tr-ep-list tr-quality-web-dl')
# estou usando underline do lado do class pq class já é uma palavra reservada
# do python, ai o beautiful soup usa o underline para diferenciar

with open('ousama_king_eps.csv', 'a', newline='', encoding='UTF-8') as f:
    for episode in episodes:
        try:
            ep_name = episode.find('td', class_='td-ep-eps').get_text()
            ep_resolution = episode.find('td', 'td-ep-res').get_text()
            ep_size = episode.find('td', 'td-ep-tam').get_text()
            ep_link = episode.find('a', href=True)['href']
            print(ep_link)
        except:
            ep_link = 'Não lançado'

        linha = ep_name + ';' + ep_resolution + ';' + ep_size + ';' + ep_link + '\n'
        print(linha)
        f.write(linha)



# oq eu quero procurar
"""
nome do ep -> td td-ep-eps
qualidade -> td td-ep-res
tamanho -> td td-ep-tam
tipo do arquivo -> td td-ep-for
link magnético para baixar -> td td-ep-dow
"""

