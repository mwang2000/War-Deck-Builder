import requests
import urllib.request
import time
from selenium import webdriver
from itertools import combinations
from deck import Deck

allCards = ('Skellies','IceSpirit','Gobs','SpearGobs','Zap','Bats','FireSpirits','Snowball','Archers','Arrows','Knight','Minions',
'Bomber','Cannon','SkellyBarrel','GobGang','Firecracker','RoyalDelivery','Mortar','SkeletonDragons','Tesla','Barbs','Horde','Rascals',
'RG','eBarbs','RoyalRecruits','HealSpirit','IceGolem','Tombstone','MM','DartGob','Earthquake','ElixirGolem','Fireball','MP','Musk',
'Hog','Valk','Ram','Furnace','FlyingMachine','BombTower','Zappies','BattleHealer','GoblinCage','Giant','GobHut','Inferno','Wiz',
'RoyalHogs','Rocket','Pump','BarbHut','3M','Mirror','WallBreakers','BarbBarrel','Rage','Skarmy','Barrel','Tornado','Guards','Clone',
'BabyD','Hunter','Poison','DarkPrince','Freeze','Prince','Witch','Balloon','Bowler','CannonCart','eDragon','Exe','GiantSkelly','Lightning',
'XBow','GobGiant','PEKKA','Golem','Log','Miner','Princess','IceWiz','Bandit','Fisherman','Ghost','MagicArcher','NightWitch','InfernoD',
'Lumber','eWiz','RamRider','Graveyard','Sparky','Lava','MegaKnight')

winConditions = ('Mortar','RG','ElixirGolem','Hog','Ram','Giant','RoyalHogs','Rocket','3M',
'WallBreakers','Barrel','Balloon','XBow','GobGiant','PEKKA','Golem','Miner','RamRider','Graveyard',
'Sparky','Lava','MegaKnight') #at least one per deck

antiAir = ('IceSpirit','SpearGobs','Bats','FireSpirits','Archers','Minions','GobGang','Firecracker',
'SkeletonDragons','Tesla','Horde','Rascals','HealSpirit','IceGolem','MM','DartGob','Musk','Furnace',
'FlyingMachine','Zappies','GobHut','Inferno','Wiz','3M','BabyD','Hunter','Witch','eDragon','Exe',
'GobGiant', 'Princess','IceWiz','MagicArcher','NightWitch','InfernoD','eWiz','RamRider') # at least 2 per deck

damageSpells = ('Zap','Snowball','Arrows','RoyalDelivery','Earthquake','Fireball','Rocket',
'BarbBarrel','Tornado','Poison','Freeze','Lightning','Log') # at least 1 per deck

# takes a list of cards and spits out a list of decks that could be made, taking into account different types of cards
# def deckBuilder(cards):
#     deckList = combinations(cardList,8)

#get rating of given deck
# todo: operate on a Deck instead of a list of strings
def retrieveRating(deck):
    #url = 'https://www.deckshop.pro/check/?deck=Skellies-IceSpirit-Gobs-SpearGobs-Zap-Bats-FireSpirits-Arrows'
    url = 'https://www.deckshop.pro/check/?deck='
    urlAppend = '-'.join(deck)
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',options=options)
    driver.get(url+urlAppend)
    rating = driver.find_elements_by_xpath("//table[@class='table table-inverse mb-3']//tr")
    ratings = []
    for element in rating: #each element is one rating
        words = element.text.split()
        ratings.append(words[-1]) 
    dictionary = {'RIP' : 0, 'Bad' : 1, 'Mediocre' : 2, 'Good' : 3, 'Great!' : 4, 'Godly!' : 5}
    ratings = [dictionary[k] for k in ratings]
    return Deck(deck,ratings[0],ratings[1],ratings[2],ratings[3])

#collect cards from user input and put in list
cardList = []
print('Enter your card collection and type "done" after you enter your last card')
choice = ''
while choice != 'done':
    choice = input()
    if (choice != 'done') & (choice in allCards):
        cardList.append(choice)
deckCombinations = combinations(cardList,8)
bestDecks = [Deck([],0,0,0,0)]
for deck in deckCombinations:
    currentDeck = retrieveRating(deck)
    points = 0
    if currentDeck.defense > bestDecks[0].defense:
        points += 1
    elif currentDeck.defense < bestDecks[0].defense:
        points -= 1
    else:
        pass
    if currentDeck.offense > bestDecks[0].offense:
        points += 1
    elif currentDeck.offense < bestDecks[0].offense:
        points -= 1
    else:
        pass
    if currentDeck.versatility > bestDecks[0].versatility:
        points += 1
    elif currentDeck.versatility < bestDecks[0].versatility:
        points -= 1
    else:
        pass
    if currentDeck.synergy > bestDecks[0].synergy:
        points += 1
    elif currentDeck.synergy < bestDecks[0].synergy:
        points -= 1
    else:
        pass
    if points >= 1:
        bestDecks = [currentDeck]
    elif points == 0:
        bestDecks.append(currentDeck)
    else:
        pass
for deck in bestDecks:
    print(deck.cards)
    

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


