from Soldier import Soldier, Hero, Enemy

from Weapon import fists,sword,gun,Weapon
import time
import sys

hero = Hero('Hero',100)
enemy = Enemy('Enemy', 100)

while True:
    stateHero = hero.attack(enemy)
    stateEnemy = enemy.attack(hero)

    hero.healthBar.draw()
    enemy.healthBar.draw()
    if hero.health == 50:
        hero.equip(gun)
    time.sleep(1)
    if stateHero == 1 or stateEnemy == 1:
        sys.exit()
    input()
