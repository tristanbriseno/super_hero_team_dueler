import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def add_hero(self, hero):
        self.heroes.append(hero)

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero)

    def stats(self):
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
        print("{} Kills/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = 100
    

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:

            hero = random.choice(living_heroes)
            opponent = random.choice(living_opponents)

            loser = hero.fight(opponent)

            for hero in living_heroes:
                if loser == hero.name:
                    living_heroes.remove(hero)
                    print(f"{hero.name} has lost the fight")
        
            for opponent in living_opponents:
                 if loser == opponent.name:
                    living_opponents.remove(opponent)
                    print(f"{opponent.name} has lost the fight")