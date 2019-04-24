import os
import datetime
from product import Product
from city import City


GAME_TITLE = '''
╔════════════════════════════╗
║          PYRATES           ║
╚════════════════════════════╝'''
PRESS_ANY_KEY = "Press any key to continue... \n"
DIVIDER = "☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲☲"

# for use later ⚔ ☠ ☩ ☽ † ✡ ✠ ✢ ☪ ¢ £ ⁂ ❂ ✴ 🗡🛡 🏳 


class GameManager(object):
    def __init__(self,**kwargs):
        self.firm_name = kwargs["name"]
        self.cash = kwargs["cash"]
        self.debt = kwargs["debt"]
        self.cannons = kwargs["cannons"]
        self.bank = 0
        self.maxshiphold = kwargs["shiphold"]
        self.current_shiphold = 0
        Product.create_products()
        City.create_cities()
        self.current_city = City.cities[0]
        self.current_date = datetime.datetime(1820,1,1)

    def leave_port(self, cities, current_date):
        i = 1
        for city in cities:
            print("{0}) {1}".format(i, city.name))
            i += 1
        select_city = input("\nWhich city wish to travel to?: \n")
        current_date += datetime.timedelta(days=1)
        return cities[int(select_city) - 1], current_date

    def buy(self):
        buy_select = input("Which product to you want to buy? (1-%s) - Press [c] to cancel." %  str(len(Product.products)))
        if buy_select == "c":
            return
        city_product = self.current_city.city_products[int(buy_select)-1]
        qty_to_buy = input("How many %s do you wish to buy?" % city_product.product.name)
        cost_to_buy = city_product.price * int(qty_to_buy)
        print("This will cost you " + str(cost_to_buy))
        if cost_to_buy <= self.cash:
            if self.current_shiphold + int(qty_to_buy) <= self.maxshiphold:
                self.cash -= cost_to_buy
                city_product.product.shipqty += int(qty_to_buy)
                self.current_shiphold += int(qty_to_buy)
            else:
                print("There is not enough room on your ship!")
                input(PRESS_ANY_KEY)
        else:
            print("You don't have enough money.")
            input(PRESS_ANY_KEY)


    def sell(self):
        sell_select = input("Which product to you want to sell? (1-%s) - Press [c] to cancel." %  str(len(Product.products)))
        if sell_select == "c":
            return
        city_product = self.current_city.city_products[int(sell_select)-1]
        qty_to_sell = input("How many %s do you wish to sell?" % city_product.product.name)
        if int(qty_to_sell) <= city_product.product.shipqty:
            self.cash += int(qty_to_sell) * city_product.price
            city_product.product.shipqty -= int(qty_to_sell)
            self.current_shiphold -= int(qty_to_sell)
        else:
            print("You don't have that many to sel!")
            input(PRESS_ANY_KEY)


    def visit_bank(self):
        input("How much would you like to deposit?")

    def display_products(self):
        i = 1
        for cityproduct in self.current_city.city_products:
            print(str(i) + ") " + cityproduct.product.name + "\n   £" + str(cityproduct.price) + " - You hold: " + str(cityproduct.product.shipqty))
            i += 1

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
            print("Menu: [L]eave Port, [B]uy, [S]ell, %s [T]ransfer Warehouse, [Q]uit" % has_bank_string)
            menu_option = input("What would you like to do?")
            if menu_option == "l":
                self.current_city, self.current_date = self.leave_port(City.cities, self.current_date)
            elif menu_option == "b":
                self.buy()
            elif menu_option == "s":
                self.sell()
            elif menu_option == "v" and self.current_city.has_bank == True:
                self.visit_bank()
            elif menu_option == "q":
                game_running = False
        