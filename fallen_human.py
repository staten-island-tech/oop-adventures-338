class Chara:
    def __init__(self,name):
        self.name=name
        if self.name=="CHARA":
            print("The true name.")
        self.maxhp=20
        self.xp=0
        self.love=1
        self.at=0
        self.df=0
        self.G=0
    def hplost(self,dmg):
        self.hp-=dmg
        print(f"{self.name} has taken {dmg} damage.")
    def hpgain(self,heal):
        self.hp+=heal
        print(f"{self.name} has recover {heal} health.")
    def xpgain(self,exp):
        self.xp+=exp
    def G(self,gold):
        self.G+=gold
    def levelup(self):
        if self.xp>=10 and self.love==1:
            self.love+=1
            self.xp=0
        elif self.xp>=20 and self.love==2:
            self.love+=1
            self.xp=0
        elif self.xp>=40 and self.love==3:
            self.love+=1
            self.xp=0
        elif self.xp>=50 and self.love==4:
            self.love+=1
            self.xp=0
        elif self.xp>=80 and self.love==5:
            self.love+=1
            self.xp=0
        elif self.xp>=100 and self.love==6:
            self.love+=1
            self.xp=0
        elif self.xp>=200 and self.love==7:
            self.love+=1
            self.xp=0
        elif self.xp>=300 and self.love==8:
            self.love+=1
            self.xp=0
        elif self.xp>=400 and self.love==9:
            self.love+=1
            self.xp=0
        elif self.xp>=500 and self.love==10:
            self.love+=1
            self.xp=0
        elif self.xp>=800 and self.love==11:
            self.love+=1
            self.xp=0
        elif self.xp>=1000 and self.love==12:
            self.love+=1
            self.xp=0
        elif self.xp>=1500 and self.love==13:
            self.love+=1
            self.xp=0
        elif self.xp>=2000 and self.love==14:
            self.love+=1
            self.xp=0
        elif self.xp>=3000 and self.love==15:
            self.love+=1
            self.xp=0
        elif self.xp>=5000 and self.love==16:
            self.love+=1
            self.xp=0
        elif self.xp>=10000 and self.love==17:
            self.love+=1
            self.xp=0
        elif self.xp>=25000 and self.love==18:
            self.love+=1
            self.xp=0
        elif self.xp>=49999 and self.love==19:
            self.love+=1
            self.xp=0
        else:
            return
    def levelstat(self):
        if self.love==20:
            self.maxhp=99
            self.at=99
            self.df=round((self.love-1)/4)
        else:
            self.maxhp=16+(4*self.love)
            self.at=-2+(2*self.love)
            self.df=round((self.love-1)/4)
