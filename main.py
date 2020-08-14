import requests
import urllib.request
import time
from selenium import webdriver
from itertools import combinations

winConditions = ('Mortar','RG','ElixirGolem','Hog','Ram','Giant','RoyalHogs','Rocket','3M',
'WallBreakers','Barrel','Balloon','XBow','GobGiant','PEKKA','Golem','Miner','RamRider','Graveyard',
'Sparky','Lava','MegaKnight')

antiAir = ('IceSpirit','SpearGobs','Bats','FireSpirits','Archers','Minions','GobGang','Firecracker',
'SkeletonDragons','Tesla','Horde','Rascals','HealSpirit','IceGolem','MM','DartGob','Musk','Furnace',
'FlyingMachine','Zappies','GobHut','Inferno','Wiz','3M','BabyD','Hunter','Witch','eDragon','Exe',
'GobGiant', 'Princess','IceWiz','MagicArcher','NightWitch','InfernoD','eWiz','RamRider')

damageSpells = ('Zap','Snowball','Arrows','RoyalDelivery','Earthquake','Fireball','Rocket',
'BarbBarrel','Tornado','Poison','Freeze','Lightning','Log')

# takes a list of cards and spits out a list of decks that could be made, taking into account different types of cards
# def deckBuilder(cards):
#     deckList = combinations(cardList,8)

#get rating of given deck
def retrieveRating(deck):
    #url = 'https://www.deckshop.pro/check/?deck=Skellies-IceSpirit-Gobs-SpearGobs-Zap-Bats-FireSpirits-Arrows'
    url = 'https://www.deckshop.pro/check/?deck='
    urlAppend = '-'.join(deck)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options=options)
    driver.get(url+urlAppend)
    rating = driver.find_elements_by_xpath("//table[@class='table table-inverse mb-3']//tr")
    for element in rating:
        print(element.text)

#collect cards from user input and put in list
cardList = []
print('enter your card collection and type done after you enter your last card')
choice = ''
while choice != 'done':
    choice = input()
    if choice != 'done':
        cardList.append(choice)
deckList = combinations(cardList,8)
for deck in deckList:
    retrieveRating(deck)


# labels certain cards as 
def deckLabeler(cards):
    deckWinConditions = []
    deckAntiAir = []
    deckDamageSpells = []
    for card in cards:
        if card in winConditions:
            deckWinConditions.append(card)
        if card in antiAir:
            deckAntiAir.append(card)
        if card in damageSpells:
            deckDamageSpells.append(card)


