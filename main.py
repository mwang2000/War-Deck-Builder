import requests
import urllib.request
import time
from selenium import webdriver

winConditions = ('Mortar','RG','ElixirGolem','Hog','Ram','Giant','RoyalHogs','Rocket','3M',
'WallBreakers','Barrel','Balloon','XBow','GobGiant','PEKKA','Golem','Miner','RamRider','Graveyard',
'Sparky','Lava','MegaKnight')

antiAir = ('IceSpirit','SpearGobs','Bats','FireSpirits','Archers','Minions','GobGang','Firecracker',
'SkeletonDragons','Tesla','Horde','Rascals','HealSpirit','IceGolem','MM','DartGob','Musk','Furnace',
'FlyingMachine','Zappies','GobHut','Inferno','Wiz','3M','BabyD','Hunter','Witch','eDragon','Exe',
'GobGiant', 'Princess','IceWiz','MagicArcher','NightWitch','InfernoD','eWiz','RamRider')

damageSpells = ('Zap','Snowball','Arrows','RoyalDelivery','Earthquake','Fireball','Rocket',
'BarbBarrel','Tornado','Poison','Freeze','Lightning','Log')

#collect cards from user input and put in list
cardList = []
print('enter your card collection and type done after you enter your last card')
card = ''
while card != 'done':
    choice = input()
    cardList.append(choice)


#get rating of given deck
def retrieveRating():
    url = 'https://www.deckshop.pro/check/?deck=Skellies-IceSpirit-Gobs-SpearGobs-Zap-Bats-FireSpirits-Arrows'
# deck = ''
# for i in range(0,7):
#     ele = input()
#     deck = deck + ele + '-'
# deck = deck + input('Last card?')
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    driver.get(url)
# driver.get(url+deck)
    rating = driver.find_elements_by_xpath("//table[@class='table table-inverse mb-3']//tr")
    for element in rating:
        print(element.text)

# elements = driver.find_elements_by_class_name('col-sm-4 col-md-3 col-6 mb-4 deck-container')

# takes a list of cards and spits out a list of decks that could be made, taking into account different types of cards
def deckBuilder(cards):
    deckList = []
    for card in deckWinConditions:


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


