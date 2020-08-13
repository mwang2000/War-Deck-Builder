import requests
import urllib.request
import time
from selenium import webdriver
import tkinter

url = 'https://www.deckshop.pro/check/?deck=Skellies-IceSpirit-Gobs-SpearGobs-Zap-Bats-FireSpirits-Arrows'
# deckList = ''
# for i in range(0,7):
#     ele = input()
#     deckList = deckList + ele + '-'
# deckList = deckList + input('Last card?')
driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
driver.get(url)
# driver.get(url+deckList)
rating = driver.find_elements_by_xpath("//table[@class='table table-inverse mb-3']//tr")
for element in rating:
    print(element.text)

# elements = driver.find_elements_by_class_name('col-sm-4 col-md-3 col-6 mb-4 deck-container')


#Skellies
#IceSpirit
#Gobs
#SpearGobs
#Zap
#Bats
#FireSpirits
#Snowball
#Archers
#Arrows
#Knight
#Minions
#Bomber
#Cannon
#SkellyBarrel
#GobGang
#Firecracker
#RoyalDelivery
#Mortar
#SkeletonDragons
#Tesla
#Barbs
#Horde
#Rascals
#RG
#eBarbs
#RoyalRecruits
#HealSpirit
#IceGolem
#Tombstone
#MM
#DartGob
#Earthquake
#ElixirGolem
#Fireball
#MP
#Musk
#Hog
#Valk
#Ram
#Furnace
#FlyingMachine
#BombTower
#Zappies
#BattleHealer
#GoblinCage
#Giant
#GobHut
#Inferno
#Wiz
#RoyalHogs
#Rocket
#Pump
#BarbHut
#3M
#Mirror
#WallBreakers
#BarbBarrel
#Rage
#Skarmy
#Barrel
#Tornado
#Guards
#Clone
#BabyD
#Hunter
#Poison
#DarkPrince
#Freeze
#Prince
#Witch
#Balloon
#Bowler
#CannonCart
#eDragon
#Exe
#GiantSkelly
#Lightning
#XBow
#GobGiant
#PEKKA
#Golem
#Log
#Miner
#Princess
#IceWiz
#Bandit
#Fisherman
#Ghost
#MagicArcher
#NightWitch
#InfernoD
#Lumber
#eWiz
#RamRider
#Graveyard
#Sparky
#Lava
#MegaKnight
