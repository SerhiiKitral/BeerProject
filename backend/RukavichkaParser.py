import requests
from bs4 import BeautifulSoup
from BeerModel import Beer

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
        description = f"{title} is the best beer in the world!!!"
        shopName = "Рукавичка"
        beerType = "звичайне смачне пиво для бидла"


        #Змінити
        volume = 0

        array.append(Beer(title, price, img_url, link, description, shopName, beerType, volume))
