from bs4 import BeautifulSoup
import requests 
import pandas as pd
import numpy as np

url="http://quotes.toscrape.com/page/"
npo_quotes = {}
quotes_no = 0

for i in range (1,10):
    url= "http://quotes.toscrape.com/page/" + str(i)

    response = requests.get(url)
    data = response.content
    soup = BeautifulSoup(data,'html.parser')
    quotes=soup.find_all("div", class_="quote")
    scraped = []
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        scraped.append([text, author])
        print("Text: ", text, "Author: ", author)
        quotes_no +=1
        npo_quotes[quotes_no] = [text, author]
print("Total quotes:", quotes_no)

npo_quotes_df = pd.DataFrame.from_dict(npo_quotes, orient = 'index', columns = ['Text','Author'])

npo_quotes_df.to_csv('Quotes.csv')
