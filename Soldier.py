from Weapon import fists,sword,gun,Weapon
class Soldier:
    def __init__(self, name:str, health:int):
        self.name = name
        self.health = health
        self.healthMax = health
        self.weapon = fists
