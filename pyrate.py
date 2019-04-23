import os
import datetime
import random
os.system('cls')

##### STUFF ######
GAME_TITLE = '''
╔═════════════════╗
║     PYRATES     ║
╚═════════════════╝'''

DIVIDER = "☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲"

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
  
def buy():
    input("What would you like to buy?")

def sell():
    input("What would you like to sell?")

def visit_bank():
    input("How much would you like to deposit?")

def leave_port(cities, current_date):
    i = 1
    for city in cities:
        print("{0}) {1}".format(i, city.name))
        i += 1
    select_city = input("\nWhich city wish to travel to?: \n")
    current_date += datetime.timedelta(days=1)
    return cities[int(select_city) - 1], current_date

def display_products():
    for product in Product.products:
        print(product.name + " - " + str(product.price))


###### PRODUCT CLASS #####
class Product(object):
    products = []
    def __init__(self, name, minprice, maxprice):
        self.name = name
        self.minprice = minprice
        self.maxprice = maxprice
        self.price = random.randint(self.minprice,self.maxprice)
    @classmethod
    def create_products(cls):
        cls.products.append(Product("General Goods", 3, 20))
        cls.products.append(Product("Arms", 10, 75))


##### CREATE PRODUCTS ######
Product.create_products()

##### CITY CLASS #####
class City(object):
    cities = []
    def __init__(self, name, has_warehouse, has_bank):
        self.name = name
        self.has_warehouse = has_warehouse
        self.has_bank = has_bank
    @classmethod
    def create_cities(cls):
        cls.cities.append(City("Hong Kong", True, True))
        cls.cities.append(City("Shanghai", False, False))
        cls.cities.append(City("London", False, False))


##### CREATE CITIES ######
City.create_cities()

##### START GAME #####
welcome_message()
firm_name = get_firm_name()
cash, debt, cannons = get_starting_options()

current_city = City.cities[0]
current_date = datetime.datetime(1820,1,1)

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
    print(f"City: {current_city.name}")
    print("Date: {:%B %d, %Y}".format(current_date))
    print(DIVIDER)
    print("-----City Products-----")
    display_products()
    has_bank_string = ""
    if current_city.has_bank == True:
        has_bank_string = "[V]isit Bank,"
    print("Menu: [L]eave Port, [B]uy, [S]ell, %s [T]ransfer Warehouse, [M]oney Lender, [Q]uit" % has_bank_string)
    menu_option = input("What would you like to do?: \n")
    if menu_option == "l" or "L":
        current_city, current_date = leave_port(City.cities, current_date)
    elif menu_option == "b" or "B":
        buy()
    elif menu_option == "s" or "S":
        sell()
    elif menu_option == "V" or "v" and current_city.has_bank == True:
        visit_bank()
    elif menu_option == "q" or "Q":
        game_running = False