import os
import datetime
from gamemanager import GameManager
from product import Product
from city import City
os.system('cls')


##### GAME FUNCTIONS #####
def welcome_message():
    print("Welcome to Pyrates!\n")

def get_firm_name():
    firm_name = input("Please enter your firm name:\n")
    return firm_name

# SHOULD ADD "ARE YOU SURE?" HERE
def get_starting_options():
    starting_options = input("How do you wish to start? [1] Cash & Debt [2] Cannons & No Cash/Debt.\n")
    if starting_options == "1":
        opts = (2500,250,0)
    else:
        opts = (0,0,5)
    return opts
  

##### GAME OPTIONS #####
welcome_message()
firm_name = get_firm_name()

cash, debt, cannons = get_starting_options()

game = GameManager(name=firm_name,cash=cash,debt=debt,cannons=cannons,shiphold=500)

##### START THE GAME! #####
game.StartUp()