from RukavichkaParser import getBeerFromRukavichka
from PravdaParser import getBeerFromPravdaInBottles
from PravdaParser import getBeerFromPravdaInCans
from ClearDatabase import database_clear
import sqlite3


database_clear()

beerForDB = []

getBeerFromRukavichka(beerForDB)
getBeerFromPravdaInBottles(beerForDB)
getBeerFromPravdaInCans(beerForDB)

conn = sqlite3.connect('beermeal.db')
c = conn.cursor()

for beer in beerForDB:
    c.execute("INSERT INTO ShopProducts (beername, price, photolink, url, description, shop, beerType, volume) "
              "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
              (beer.title, beer.price, beer.imgURL, beer.link, beer.description,
               beer.shopName, beer.beerType, beer.volume))

conn.commit()
conn.close()
