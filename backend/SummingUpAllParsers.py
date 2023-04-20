from RukavichkaParser import getBeerFromRukavichka
from PravdaParser import getBeerFromPravdaInBottles
from PravdaParser import getBeerFromPravdaInCans


beerForDB = []

getBeerFromRukavichka(beerForDB)
getBeerFromPravdaInBottles(beerForDB)

getBeerFromPravdaInCans(beerForDB)

for beer in beerForDB:
    print(beer. title, beer.link)

print("================Parse completed=================")
