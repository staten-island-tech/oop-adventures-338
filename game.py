import random
from fallen_human import Chara
from item import food
from item import weapons
from item import armor
from enemy import RuinsEnemies
from enemy import SnowdinEnemies
from enemy import WaterfallEnemies
from enemy import HotlandEnemies
from enemy import CoreEnemies
from enemy import NewHomeEnemy
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
    random.randint(0,5)
    enemyalive=True
    while enemyalive==True:
        print("")
        if hp<=0:
            enemyalive=False
    ruinsencounter+=1

