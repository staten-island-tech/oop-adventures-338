import random
from fallen_human import Chara
from item import food
from item import weapons
from item import armor
ruinsencounter=0
name=(input("Name the fallen human. ")).upper
human=Chara(name)
while ruinsencounter<20:
    rand=random.randint(1,5)
    enemy=enemies(ruinsenemies[rand])