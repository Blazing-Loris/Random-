import requests
from bs4 import BeautifulSoup

source = requests.get('https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1').text

soup = BeautifulSoup(source, 'lxml')

info = soup.find('div', class_='lister-item mode-advanced')

name = info.h3.a.text
print(name)

year = info.h3.find('span', class_='lister-item-year text-muted unbold').text
print(year)

rating = info.strong.text
print(rating)

metascore = info.find('span', class_='metascore favorable')
metascore = int(metascore.text)
print(metascore)

votes = info.find('span', attrs = {'name':'nv'})
print(votes['data-value'])                                                                     