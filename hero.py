import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    #this is the stats of the heroes
    def __init__(self, name, starting_health=100):
        self.abilities = list()
        self.armors = list()
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)
        print(f"{weapon.name} has been added to {self.name}'s weapon stash.")


    def add_armor(self, armor):
        self.armors.append(armor)

    def defend(self, damage_amount):
        total_armor = 0
        for armor in self.armors:
            total_armor += armor.block()
        return damage_amount - total_armor

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    
    def take_damage(self, damage):
        self.current_health -= self.defend(damage)
        print(f"{self.name} took {damage} damage. Their current health sits at {self.current_health}.")

    def is_alive(self):  
        if self.current_health <= 0:
            return False
        else:
            return True

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths


    def fight(self, opponent):  
        while self.is_alive() is True and opponent.is_alive() is True:
            opponent.take_damage(self.attack())
            if opponent.is_alive() is True:
                self.take_damage(opponent.attack())

        if self.is_alive() is False:
            opponent.add_kill(1)
            self.add_death(1)
            print(f"{self.name} has been defeated")
            return self.name

        if opponent.is_alive() is False:
            self.add_kill(1)
            opponent.add_death(1)
            print(f"{opponent.name} has been brought to justice")
            return opponent.name