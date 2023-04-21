import requests
from bs4 import BeautifulSoup
from BeerModel import Beer
import re


def getBeerFromRukavichka(array):
    # Завантаження сторінки
    url = 'https://market.rukavychka.ua/pivo/?limit=100'
    response = requests.get(url)

    # Парсинг сторінки
    soup = BeautifulSoup(response.text, 'html.parser')

    # Знаходимо всі товари зі списку
    items = soup.find_all('div', {'product-layout product-grid col-6 col-md-4 col-lg-4'})

    # Проходимося по кожному товару та виводимо його дані на екран
    for item in items:
        price = item.find('div', {'class': 'fm-module-price-bottom'}).text.strip()
        link = item.find('a')['href']
        title = item.find('div', {'class': 'fm-module-title'}).text.strip()
        img_url = item.find('img', {'class': 'img-fluid'})['src']

        # Щось придумати і замінити

        shopName = "Рукавичка"
        beerType = "Звичайне смачне пиво для бидла"

        title = title.replace(",", ".")
        title = re.sub(r'\d+(\.\d+)?%', '', title)

        # Extract numbers with "Л" symbol and remove them from the original string
        volume = re.findall(r'\b(?:\d+|\d+\.\d+|0*\d+(?:\.0+)?)\s*Л\b', title)
        title = re.sub(r'\b(?:\d+|\d+\.\d+|0*\d+(?:\.0+)?)\s*Л\b', '', title)

        # Remove any remaining numbers from the string
        title = re.sub(r'\d+(\.\d+)?', '', title)

        title = re.sub(r'\s+', ' ', title)

        title = title.strip()
        description = f"{title} is the best beer in the world!!!"

        array.append(Beer(title, price, img_url, link, description, shopName, beerType, volume[0]))

    return array

