from Weapon import fists, Weapon
from HealthBar import HealthBar
class Soldier:

    def __init__(self, name:str, health:int):
        self.name = name
        self.health = health
        self.healthMax = health
        self.weapon = fists
        
    def attack(self,target) -> int:
        target.health = target.health - self.weapon.damage
        target.healthBar.update()
        print(f'{target.name} took {self.weapon.damage} damage!')
        if target.health < 1:
            print(f"{target.name} died! Game Over!")
            return 1
        else: return 0

class Hero(Soldier):
    def __init__(self,name,health):
        super().__init__(name = name,health = health)
        self.healthBar = HealthBar(self,color = 'Green', is_colored = True, length = 20)
    def equip(self,weapon:Weapon):
        self.weapon = weapon
        print(f'{self.name} equipped {self.weapon.name}!')

class Enemy(Soldier):
    def __init__(self,name,health):
        super().__init__(name = name,health =health)
        self.healthBar = HealthBar(self,color = 'Red', is_colored = True, length = 20)

    def equip(self,weapon:Weapon):
        self.weapon = weapon
        print(f'{self.name} equipped {self.weapon}!')