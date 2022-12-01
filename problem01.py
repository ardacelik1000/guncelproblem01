import requests
from bs4 import BeautifulSoup
import re

''' 
Stage : Development -01
@author : Arda Çelik, 119202051
@author : Şükrü Anıl Kuzey , 119202031
'''
url = 'https://www.imdb.com/'
responseFromUrl = requests.get(url)
soup = BeautifulSoup(responseFromUrl.text, 'lxml')
titles = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value') for b in soup.select('td.posterColumn span[name=ir]')]
votes = [b.attrs.get('data-value') for b in soup.select('td.ratingColumn strong')]

imdb = []

for i in range(0, len(titles)):
    # Seperate movie into: 'place', 'title', 'year'
    title_string = titles[index].get_text()
    title = (' '.join(movie_string.split()).replace('.', ''))
    title_title = titles[len(str(index))+1:-7]
    date = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index))-(len(movie))]
    info = {"movie_title": title_title,
            "year": date,
            "place": place,
            "rating": ratings[index],
            "vote": votes[index],
            "link": links[index]}
    imdb.append(info)

for item in imdb:
    print(item['place'], '-', item['movie_title'], '('+item['year']+') -', 'Starring:', item['star_cast'])




