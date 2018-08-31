# SCRAPING COREY-S WEBSITE
import requests
from bs4 import BeautifulSoup

source = requests.get('http://coreyms.com/').text

soup = BeautifulSoup(source, 'lxml')

#print(soup.prettify())
for title in soup.find_all('article'):

	headline = title.h2.a.text
	print(headline)
	summary = title.div.p.text
	print(summary)

	link = title.find('iframe', class_='youtube-player')['src']
	ytlink = link.split('/')[4]
	ytlink = ytlink.split('?')[0]
	ytlink = f"youtube.com/watch?v={ytlink}"
	print(ytlink)
	print()