import requests
import time
from bs4 import BeautifulSoup
from BeerModel import Beer
import re


def getBeerFromSpecificItem(url, price):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')
    item = soup.find('div', {'class': re.compile("row")})

    # Парсимо назву
    title = item.find('h1', {'class': "h1 headline text-center"}).text.strip()
    for i in range(len(title) - 2):
        if title[i+1].isnumeric() and not title[i].isnumeric():
            title = title[:i+1]
            break


    # Парсимо лінк на фото
    img_url = item.find('img', {'class': 'img-responsive center-block'})['src']
    img_url = "https://www.pravda.beer/" + img_url



    # Парсимо опис
    desciption = item.find('div', {'class': 'thecontent'}).text.strip()

    shopName = "Правда"


    # Парсимо тип пива
    beerType = item.find('h6', {'class': 'h6 underline'}).text.strip()


    # Парсимо об'єм пива
    beerVolume = item.find('div', {'class': 'shop-popup-name'}).text.strip()
    for i in range(len(beerVolume) - 1):
        if beerVolume[i] == "0":
            beerVolume = beerVolume[i:]
            break


    return Beer(title, price, img_url, url, desciption, shopName, beerType, beerVolume)



def getBeerFromPravdaInBottles(array):
    # Завантаження сторінки
    url = 'https://www.pravda.beer/#plyashka'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # print(soup.prettify())

    items = soup.find_all('div', {'class': re.compile(r'(^|\s)item all plyashka(\s|$)')})

    for item in items:
        #Парсимо лінк
        link = item.find('a')['href']
        link = "https://www.pravda.beer/" + link

        #Парсимо ціну
        price_tag = item.find('div', class_='shop-product-inner')
        price = price_tag.find('i', class_='shop-product-price').text.strip()
        for i in range(len(price) - 1):
            if price[i] == "/" or price[i] == "г":
                price = price[: i - 1]
                break


        array.append(getBeerFromSpecificItem(link, price))



def getBeerFromPravdaInCans(array):
    # Завантаження сторінки
    url = 'https://www.pravda.beer/#banka'
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # print(soup.prettify())

    items = soup.find_all('div', {'class': re.compile(r'(^|\s)item all banka(\s|$)')})

    for item in items:
        # Парсимо лінк
        link = item.find('a')['href']
        link = "https://www.pravda.beer/" + link

        # Парсимо ціну
        price_tag = item.find('div', class_='shop-product-inner')
        price = price_tag.find('i', class_='shop-product-price').text.strip()
        for i in range(len(price) - 1):
            if price[i] == "/" or price[i] == "г":
                price = price[: i - 1]
                break


        array.append(getBeerFromSpecificItem(link, price))

