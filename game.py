import random
from fallen_human import Chara
from item import food
from item import weapons
from item import armor
from enemy import Enemies
from enemy import RuinsEnemies
from enemy import SnowdinEnemies
from enemy import WaterfallEnemies
from enemy import HotlandEnemies
from enemy import CoreEnemies
from enemy import NewHomeEnemies
from enemy import YellowBosses
from enemy import RuinsEnemiesList
from enemy import SnowdinEnemiesList
from enemy import WaterfallEnemiesList
from enemy import HotlandEnemiesList
from enemy import CoreEnemiesList
from enemy import NewHomeEnemiesList
from enemy import YellowBossesList

class Actions:
    def __init__(self,name):
        self.equipw=food["stick"]["at"]
        self.equipa=weapons["bandage"]["df"]
        self.items=[""]
        self.damage=0

mysteryman=False
turn=0
ruinsencounter=0
while mysteryman!=True:
    name=(input("Name the fallen human. ")).upper()
    if name=="CHARA":
        print("The TRUE NAME.")
        mysteryman=True
    elif name=="FRISK":
        print("WARNING: This name will not make your life hell. PROCEED")
        mysteryman=True
    elif name=="SANS":
        print("nope.")
        mysteryman=False
    elif name=="":
        print("You must choose a name.")
        mysteryman=False
    elif name=="PAPYRU" or name=="PAPAYA":
        print("I'LL ALLOW IT!!!!")
        mysteryman=True
    elif name=="GASTER":
        mysteryman=False
    else:
       mysteryman=True
human=Chara(name)
while ruinsencounter<21:
    r=random.randint(1,6)
    enemyalive=True
    while enemyalive==True:
        Encounter=Enemies(RuinsEnemies[RuinsEnemiesList[r]]["name"],RuinsEnemies[RuinsEnemiesList[r]]["hp"],RuinsEnemies[RuinsEnemiesList[r]]["at"],RuinsEnemies[RuinsEnemiesList[r]]["df"],RuinsEnemies[RuinsEnemiesList[r]]["xpamt"],RuinsEnemies[RuinsEnemiesList[r]]["g"])
        print(RuinsEnemies[RuinsEnemiesList[r]]["name"])
        action=(input("Fight     Check     Items ")).upper()
        turn=True
        while turn==True:
            if action=="FIGHT":
                dmg=Chara.fight(human,weapons["stick"]["at"],Encounter.df)
                Enemies.hplost(Encounter,dmg)
                print(f"You dealt {dmg} damage. ")
                turn=False
            elif action=="CHECK":
                Enemies.check(Encounter)
                turn=False
            elif action=="ITEMS":
                turn=False
            else:
                turn=True
        if Encounter.hp<=0:
            enemyalive=False
    ruinsencounter+=1

