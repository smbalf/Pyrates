import os
import datetime
from product import Product
from city import City


GAME_TITLE = '''
╔════════════════════════════╗
║          PYRATES           ║
╚════════════════════════════╝'''

DIVIDER = "☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲"

# for use later ⚔ ☠ ☩ ☽ † ✡ ✠ ✢ ☪ ¢ £ ⁂ ❂ ✴ 🗡🛡 🏳 


class GameManager(object):
    def __init__(self, firm_name, cash, debt, cannons, bank, shiphold):
        self.firm_name = firm_name
        self.cash = cash
        self.debt = debt
        self.cannons = cannons
        self.bank = 0
        self.shiphold = shiphold
        Product.create_products()
        City.create_cities()
        self.current_city = City.cities[0]
        self.current_date = datetime.datetime(1820,1,1)

    def buy(self):
        input("What would you like to buy?")

    def sell(self):
        input("What would you like to sell?")

    def visit_bank(self):
        input("How much would you like to deposit?")

    def leave_port(self, cities, current_date):
        i = 1
        for city in cities:
            print("{0}) {1}".format(i, city.name))
            i += 1
        select_city = input("\nWhich city wish to travel to?: \n")
        current_date += datetime.timedelta(days=1)
        return cities[int(select_city) - 1], current_date

    def display_products(self):
        for product in Product.products:
            print(product.name + " - " + str(product.price))

    def StartUp(self):
        game_running = True
        while game_running:
            ##### GAME INTERFACE ######
            os.system("cls")
            print(GAME_TITLE)
            print(DIVIDER)
            print(f"Firm name: {self.firm_name}")
            print(f"Cash: {self.cash}")
            print(f"Debt: {self.debt}")
            print(f"Cannons: {self.cannons}")
            print(f"City: {self.current_city.name}")
            print("Date: {:%B %d, %Y}".format(self.current_date))
            print(DIVIDER)
            print("-----City Products-----")
            self.display_products()
            has_bank_string = ""
            if self.current_city.has_bank == True:
                has_bank_string = "[V]isit Bank,"
            print("Menu: [L]eave Port, [B]uy, [S]ell, %s [T]ransfer Warehouse, [M]oney Lender, [Q]uit" % has_bank_string)
            menu_option = input("What would you like to do?: \n")
            if menu_option == "l" or "L":
                self.current_city, self.current_date = self.leave_port(City.cities, self.current_date)
            elif menu_option == "b" or "B":
                self.buy()
            elif menu_option == "s" or "S":
                self.sell()
            elif menu_option == "V" or "v" and self.current_city.has_bank == True:
                self.visit_bank()
            elif menu_option == "q" or "Q":
                game_running = False
        