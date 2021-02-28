from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        return random.randrange(self.max_damage // 2, self.max_damage)