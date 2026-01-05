class Chara:
    def __init__(self,name):
        self.name=name
        if self.name=="CHARA":
            print("The true name.")
        elif self.name=="GASTER":
            breakpoint
        self.maxhp=20
        self.hp=20
        self.xp=0
        self.love=1
        self.at=0
        self.df=0
        self.G=0
    def hplost(self,dmg):
        self.hp-=dmg
        print(f"{self.name} has taken {dmg} damage.")
        if self.hp<0:
            self.hp=0
    def hpgain(self,heal):
        self.hp+=heal
        if self.hp>self.maxhp:
            self.hp=self.maxhp
        print(f"{self.name} has recover {heal} health.")
    def xpgain(self,exp):
        self.xp+=exp
    def G(self,gold):
        self.G+=gold
    def levelup(self):
        if self.xp==0:
            self.love=1
        if self.xp>=10:
            self.love=2
        if self.xp>=30:
            self.love=3
        if self.xp>=70:
            self.love=4
        if self.xp>=120:
            self.love=5
        if self.xp>=200:
            self.love=6
        if self.xp>=300:
            self.love=7
        if self.xp>=500:
            self.love=8
        if self.xp>=800:
            self.love=9
        if self.xp>=1200:
            self.love=10
        if self.xp>=1700:
            self.love=11
        if self.xp>=2500:
            self.love=12
        if self.xp>=3500:
            self.love=13
        if self.xp>=5000:
            self.love=14
        if self.xp>=7000:
            self.love=15
        if self.xp>=10000:
            self.love=16
        if self.xp>=15000:
            self.love=17
        if self.xp>=25000:
            self.love=18
        if self.xp>=50000:
            self.love=19
        if self.xp>=99999:
            self.love=20
        if self.love==20:
            self.maxhp=99
            self.at=999
            self.df=round((self.love-1)/4)
        else:
            self.maxhp=16+(4*self.love)
            self.at=-2+(2*self.love)
            self.df=round((self.love-1)/4)
