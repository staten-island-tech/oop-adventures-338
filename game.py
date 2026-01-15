import random
from fallen_human import *
from item import *
from enemy import *

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
    elif name=="PAPYRUS":
        print("THATS MY NAME HUMAN!")
    elif name=="GASTER":
        mysteryman=False
    else:
       mysteryman=True
human=Chara(name)
Chara.levelup(human)
while ruinsencounter<21:
    r=random.randint(1,6)
    enemyalive=True
    Encounter=Enemies(RuinsEnemies[RuinsEnemiesList[r]]["name"],RuinsEnemies[RuinsEnemiesList[r]]["hp"],RuinsEnemies[RuinsEnemiesList[r]]["at"],RuinsEnemies[RuinsEnemiesList[r]]["df"],RuinsEnemies[RuinsEnemiesList[r]]["xpamt"],RuinsEnemies[RuinsEnemiesList[r]]["g"])
    while enemyalive==True and human.hp>0:
        print(f"{RuinsEnemies[RuinsEnemiesList[r]]["name"]} ({Encounter.hp})")
        print(f"{human.name} ({human.hp}/{human.maxhp})")
        turn=True
        while turn==True:
            action=(input("Fight     Check     Items ")).upper()
            if action=="FIGHT":
                Chara.fight(human,weapons["stick"]["at"],Encounter.df)
                Enemies.hplost(Encounter,human.damage)
                turn=False
            elif action=="CHECK":
                Enemies.check(Encounter)
                turn=False
            elif action=="ITEMS":
                turn=False
                print("not implemented yet")
            else:
                turn=True
        if Encounter.hp<=0:
            enemyalive=False
            Chara.xpgain(human,Encounter.xpamt)
            Chara.levelup(human)
        else:
            enemyalive=True
            Enemies.fight(Encounter,human.df)
            Chara.hplost(human,Encounter.damage)
    ruinsencounter+=1

