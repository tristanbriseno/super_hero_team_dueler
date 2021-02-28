from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:
    def __init__(self, team_one, team_two):
        self.team_one = team_one
        self.team_two = team_two

    def create_ability(self):
        name = input("What is the name of the ability?")
        max_damage = int(input("What is the maximum damage of the ability?  "))

        return Ability(name, max_damage)

    def create_weapon(self):
        weapon_name = input("What is the name of the weapon? ")
        weapon_max_dmg = int(input("What is the maximum damage of the weapon? "))

        return Weapon(weapon_name, weapon_max_dmg)

    def create_armor(self):
        armor_name = input("What kind of armor does the character have? ")
        armor_health = int(input("How much protection does the armor provide? "))

        return Armor(armor_name, armor_health)

    def create_hero(self):
        hero_name = input("What is the character's name?: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               ability_input = self.create_ability()
               hero.add_ability(ability_input)
           elif add_item == "2":
               weapon_input = self.create_weapon()
               hero.add_weapon(weapon_input)
           elif add_item == "3":
               armor_input = self.create_armor()
               hero.add_armor(armor_input)
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(input("How many heroes are in team one\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = int(input("How many villians are in team two?\n"))
        for i in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def team_one_stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.team_one.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_one.name + " Your K.D.R is: " + str(team_kills/team_deaths))
        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("Has survived an attack from " + self.team_one.name + ": " + hero.name)


    def team_two_stats(self):
        team_kills = 0
        team_deaths = 0
        for hero in self.team_two.heroes:
            team_kills += hero.kills
            team_deaths += hero.deaths
        if team_deaths == 0:
            team_deaths = 1
        print(self.team_two.name + " Your K.D.R is: " + str(team_kills/team_deaths))
        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print(" has survived" + self.team_two.name + ": " + hero.name)


    def show_stats(self):
        print("HEROES SCOREBOARD")
        self.team_one_stats()
        print("VILLIANS SCOREBOARD")
        self.team_two_stats()


if __name__ == "__main__":
    game_running = True
    arena = Arena(Team("Heroes"), Team("Villians"))

    # team building
    arena.build_team_one()
    arena.build_team_two()

    while game_running:
        arena.team_battle()
        arena.show_stats()
        play_again = input("Will you continue to play? yes or no: ")

        if play_again.lower() == "no":
            game_running = False

        else:
           
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()