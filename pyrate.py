import os
import datetime
from gamemanager import GameManager
from product import Product
from city import City
os.system('cls')



##### GAME FUNCTIONS #####
def welcome_message():
    print("Welcome to Pyrates!\n")

def get_pirate_name():
    pirate_name = input("What is your name?:\n")
    return pirate_name

def get_vessel_name():
    vessel_name = input("What shall you name your vessel?:\nThe ")
    return vessel_name

# SHOULD ADD "ARE YOU SURE?" HERE
def get_starting_options():
    starting_options = input("How do you wish to start? [1] Cash & No Cannons [2] Cannons & No Cash.\n")
    if starting_options == "1":
        opts = (250,0)
    else:
        opts = (0,5)
    return opts
  

##### GAME OPTIONS #####
welcome_message()
pirate_name = get_pirate_name()
vessel_name = get_vessel_name()
cash, cannons = get_starting_options()

game = GameManager(name=pirate_name, vessel=vessel_name, cash=cash, cannons=cannons, shiphold=500, shiphealth=100)

##### START THE GAME! #####
game.start_up()