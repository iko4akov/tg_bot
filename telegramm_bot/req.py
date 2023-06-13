import requests
from bs4 import BeautifulSoup




def search_products(keyword, article=None):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
               'Sec-Ch-Ua-Platform': 'Windows',
               'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,tg;q=0.6'}
    url = f'https://www.wildberries.ru/catalog/0/search.aspx?search={keyword}'
    response = requests.get(url, headers=headers).content.decode('utf-8')
    with open('qwer.html', mode='w', encoding='utf-8') as file:
        file.write(str(response))
    # soup = BeautifulSoup(response.text, 'html.parser')

search_products('платье')
