from bs4 import BeautifulSoup
import requests

url = 'https://goldenconcept.ua/collections/apple-watch-cases'

headers = {'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# req = requests.get(url, headers=headers)
# src = req.text
# print(src)

# with open('Watch.html', 'w', encoding='utf-8') as file:
#     file.write(src)

with open('Watch.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
a = soup.find(id='CollectionProductGrid')

for help in a.find_all('a'):
    help_url = help.get('href')
    print(f'https://goldenconcept.ua/{help_url}')
