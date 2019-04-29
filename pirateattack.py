import random
import time



class PirateEncounter(object):
    def __init__(self, game):
        self.game = game
        self.pirate_risk = 0
        self.pirate_strength = 10
        self.change_for_escape = 15
        self.check_for_pirates()

    def check_for_pirates(self):
        result = random.randint(0,100)
        if result <= self.pirate_risk:
            self.pirate_attack()

    def pirate_attack(self):
        print("PIRATES HAVE ATTACKED YOUR VESSELS!")
        self.number_of_pirates = random.randint(1, self.pirate_strength)
        fighting_pirates = True
        while fighting_pirates:
            print("----------------------------")
            print("There are %s pirates remaining." % self.number_of_pirates)
            print("You have %s cannons and %s health remaining\n" % (self.game.cannons, self.game.ship_health))
            attack_input = input("What will you choose to do? [R]un or [F]ight?")
            if attack_input.upper() == "R":
                if self.try_to_run():           # TRUE IF YOU GOT AWAY
                    fighting_pirates = False
            if attack_input.upper() == "F":
                if self.fight():                # TRUE IF FIGHT IS OVER
                    fighting_pirates = False
            if self.game.ship_health <= 0:
                fighting_pirates = False
            self.ship_damage()

    def ship_damage(self):
        damage_taken = random.randint(0, self.number_of_pirates * 5)
        self.game.ship_health -= damage_taken
        if self.game.ship_health <= 0:
            print("Your ship has been destroyed!\n")
        self.game.ship_health = 0


    def fight(self):
        fight_strength = 1 if self.game.cannons == 0 else self.game.cannons + 1
        pirates_hit = random.randint(0, fight_strength + 1)
        pirates_killed = pirates_hit if self.number_of_pirates >= pirates_hit else self.number_of_pirates
        self.number_of_pirates -= pirates_killed
        if self.number_of_pirates <= 0:
            return True
        else:
            return False
    
    def try_to_run(self):
        print("You decide to escape! \n")
        result = random.randint(0,100)
        if result <= self.change_for_escape:
            print("You manage to sail away to safety...")
            return True
        else:
            print("You failed to out-run the pirates!")
            return False
