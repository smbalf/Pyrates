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

def leave_port(city_list):
    i = 1
    for city in city_list:
        print("{0}) {1}".format(i, city["name"]))
        i = i + 1
    select_city = input("\nWhich city wish to travel to?: \n")
    return city_list[int(select_city) - 1]
        

def buy():
    input("What would you like to buy?")

def sell():
    input("What would you like to sell?")

def visit_bank():
    input("How much would you like to deposit?")

cities = ({"name": "Hong Kong", "has_warehouse": True, "has_bank": True},
            {"name": "Shanghai", "has_warehouse": False, "has_bank": False},
            {"name": "London", "has_warehouse": False, "has_bank": False})

current_city = cities[0]


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
    print(f"Firm name: {firm_name}")
    print(f"Cash: {cash}")
    print(f"Debt: {debt}")
    print(f"Cannons: {cannons}")
    print(f"City: {current_city['name']}")
    print("Date: ")
    print(DIVIDER)
    has_bank_string = ""
    if current_city["has_bank"] == True:
        has_bank_string = "[V]isit Bank,"
    print("Menu: [L]eave Port, [B]uy, [S]ell, %s [T]ransfer Warehouse, [M]oney Lender, [Q]uit" % has_bank_string)
    menu_option = input("What would you like to do?: \n")
    if menu_option == "l" or "L":
        current_city = leave_port(cities)
    elif menu_option == "b" or "B":
        buy()
    elif menu_option == "s" or "S":
        sell()
    elif menu_option == "V" or "v" and current_city["has_bank"] == True:
        visit_bank()
    elif menu_option == "q" or "Q":
        game_running = False