import pandas as pd
import requests
from bs4 import BeautifulSoup

pages_to_scrape = 50

pages = []
prices = []
titles = []
authors = []


for i in range(1, pages_to_scrape+1):
	url = ('https://www.waterstones.com/books/bestsellers/sort/bestselling/page/' + str(i))
	pages.append(url)

for item in pages:
	page = requests.get(item)
	soup = BeautifulSoup(page.text, 'html.parser')

	for p in soup.findAll(class_='price'):
		price = p.text.strip()
		price = price.strip('£')
		stop_price = ['']
		prices.append(price)
		for pr in list(prices):
			if pr in stop_price:
				prices.remove(pr)


	for a in soup.findAll(class_='author'):
		author = a.text.strip()
		authors.append(author)

	for t in soup.findAll(class_='title-wrap'):
		title = t.text.strip()
		titles.append(title)


data = {'Price':prices, 'Title': titles, 'Author':authors}

df = pd.DataFrame(data=data)
df.index+=1
df.to_csv('Books.csv')



