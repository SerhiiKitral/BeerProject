class Beer:
    def __init__(self, title: str, price: str, imgURL: str, link: str, description: str, shopName: str, beerType: str,
                 volume: str):
        self.title = title
        self.price = price
        self.imgURL = imgURL
        self.link = link
        self.description = description
        self.shopName = shopName
        self.beerType = beerType
        self.volume = volume

# for beer in array:
# c.execute("INSERT INTO ShopProducts (beername, price, photolink, url, description, shop, beerType, volume)
# VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
# (beer.title, beer.price, beer.imgURL, beer.link, beer.description, beer.shopName, beer.beerType, beer.volume))

