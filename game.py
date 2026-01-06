import random
from fallen_human import Chara
from item import food
from item import weapons
from item import armor
mysteryman=False
ruinsencounter=0
while mysteryman!=True:
    name=(input("Name the fallen human. ")).upper()
    if name=="CHARA":
        print("The TRUE NAME.")
        mysteryman=True
    if name=="FRISK":
        print("WARNING: This name will not make your life hell. PROCEED")
        mysteryman=True
    if name=="GASTER":
        name=""
    else:
        mysteryman=True
    
human=Chara(name)
x=input("check")