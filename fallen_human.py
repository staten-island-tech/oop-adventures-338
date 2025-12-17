class Chara:
    def __init__(self,name,hp,xp,love,atk,defs,G,):
        self.name=name
        self.hp=hp
        self.xp=xp
        self.love=love
        self.atk=atk
        self.defs=defs
        self.G=G
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
    def lovedisplay(self):
        if self.xp>=10:
        if self.xp>=30:
        if self.xp>=70:
        if self.xp>=120:
        if self.xp>=200:
        if self.xp>=300:
        if self.xp>=500:
        if self.xp>=800:
        if self.xp>=1200:
        if self.xp>=1700:
        if self.xp>=2500:
        if self.xp>=3500:
        if self.xp>=5000:
        if self.xp>=7000:
        if self.xp>=10000:
        if self.xp>=15000:
        if self.xp>=25000:
        if self.xp>=50000:
        else: