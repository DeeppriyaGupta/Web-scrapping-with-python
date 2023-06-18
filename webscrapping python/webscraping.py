#scraping club

from bs4 import BeautifulSoup
import requests

url='https://scrapingclub.com/exercise/list_basic/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
items=soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count=1
for i in items:
    itemname=i.find('h4', class_='card-title').text.strip('\n')
    itemprice=i.find('h5').text
    print(f'itemname: {itemname}, itemprice: {itemprice}')
    count+=1