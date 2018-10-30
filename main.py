from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import jsonlines

# NOTE Contador de filmes por gênero
quantityPerGenre = {}

# NOTE Insere o filme no seu respectivo arquivo
def insert_movie(title, genre, rating):
    try:
        if (quantityPerGenre[genre] <= 500):
            quantityPerGenre[genre] = quantityPerGenre[genre] + 1
            movie = {}
            movie['title'] = title
            movie['genre'] = genre
            movie['rating'] = rating

            with jsonlines.open(genre + '.jsonl', mode='a') as writer:
                writer.write(movie)
    except:
        quantityPerGenre[genre] = 1

# NOTE Obtem os dados de uma determinada página
def getData(start):
    print('Starting at:' + str(start))
    try:
        html = urlopen('https://www.imdb.com/search/title?title_type=feature&year=2018-01-01,2018-12-31&sort=user_rating,desc&start=' + str(start) + '&ref_=adv_nxt')

    except HTTPError as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), features="lxml")
        title = bsObj.findAll("div", {"class":"lister-item mode-advanced"})
        for t in title:
            title = t.find('a').find('img').attrs['alt']
            rating = t.find('strong').text

            try:
                # NOTE Executar uma inserção no JSON para cada gênero que o filme possuir
                genres = t.find('span', {'class':'genre'}).get_text()
                for genre in genres.split(','):
                    genre = genre.strip()
                    insert_movie(title, genre, rating)

            except AttributeError as e:
                genre = 'undefined'
                insert_movie(title, genre, rating)

        getData(start + 50)
    except AttributeError as e:
        print('END')

getData(1)
