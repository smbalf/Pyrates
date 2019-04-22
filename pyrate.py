import os


##### STUFF ######
GAME_TITLE = '''
╔═════════════════╗
║     PYRATES     ║
╚═════════════════╝'''

DIVIDER = "☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲"

# for use later ⚔ ☠ ☩ ☽ † ✡ ✠ ✢ ☪ ¢ £ ⁂ ❂ ✴ 🗡🛡 🏳 

##### GAME FUNCTIONS #####
def welcome_message():
    print("Welcome to Pyrates!\n")

def get_firm_name():
    firm_name = input("Please enter your firm name:\n")
    return firm_name

def get_starting_options():
    starting_options = input("How do you wish to start? [1] Cash & Debt [2] Cannons & No Cash/Debt.\n")

    if starting_options == "1":
        opts = (250,250,0)
    else:
        opts = (0,0,5)
    return opts

def leave_port():
    pass

def buy():
    input("What would you like to buy?")

def sell():
    input("What would you like to sell?")

##### START GAME #####
welcome_message()
firm_name = get_firm_name()
cash, debt, cannons = get_starting_options()

game_running = True
while game_running:
    ##### GAME INTERFACE ######
    os.system("cls")
    print(GAME_TITLE)
    print(DIVIDER)
    print("Firm name: %s" % firm_name)
    print("Cash: {}".format(cash))
    print(f"Debt: {debt}")
    print("Cannons: %d" % cannons)
    print("City: [current city")
    print("Date: ")
    print(DIVIDER)
    print("Menu: [L]eave Port, [B]uy, [S]ell, [V]isit Bank, [M]oney Lender, [Q]uit")
    menu_option = input("What would you like to do?: \n")
    if menu_option == "l" or "L":
        leave_port()
    elif menu_option == "b" or "B":
        buy()
    elif menu_option == "s" or "S":
        sell()
    elif menu_option == "q" or "Q":
        game_running = False