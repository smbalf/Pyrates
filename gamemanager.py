import os
import datetime
import random
from pirateattack import PirateEncounter
from product import Product
from city import City, CityProduct
from gamedata import load_city_data, load_product_data


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
        self.ship_health = 100
        self.min_ship_health = 0
        #Product.create_products()
        #City.create_cities()
        load_city_data(City)
        load_product_data(Product)
        self.current_city = City.cities[0]
        self.current_date = datetime.datetime(1620,1,1)

    def leave_port(self, cities, current_date):
        for city in cities:
            print(f"{city.num}) {city.name}")
        select_city = input("\nWhich city wish to travel to?: \n")
        current_date += datetime.timedelta(days=1)
        return cities[int(select_city) - 1], current_date


##### TRADE THINGS ######
    def display_products(self, products):
        for product in products:
            print(f"{product.num}) {product.name} - {product.price} - {product.shipqty}")

    def check_price_change(self, products):
        result = random.randint(0,100)
        if result >= 55:
            for city_product in products:
                city_product.generate_random_price()

    def buy(self, products):
        buy_select = input(f"Which product do you want to buy? (1-{str(len(Product.products))}) - Press [C] to cancel.")
        if buy_select.upper() == "C":
            return
        city_product = products[int(buy_select) - 1]
        qty_to_buy = input(f"How many {city_product.name} do you wish to buy?")
        cost_to_buy = city_product.price * int(qty_to_buy)
        print(f"This will cost you £{str(cost_to_buy)}.")
        if cost_to_buy <= self.cash:
            if self.current_shiphold + int(qty_to_buy) <= self.maxshiphold:
                self.cash -= cost_to_buy
                city_product.shipqty += int(qty_to_buy)
                self.current_shiphold += int(qty_to_buy)
            else:
                print("There is not enough room on your ship!")
                input(PRESS_ANY_KEY)
        else:
            print("You don't have enough money.")
            input(PRESS_ANY_KEY)

    def sell(self, products):
        sell_select = input(f"Which product do you want to sell? (1-{str(len(Product.products))}) - Press [C] to cancel.")
        if sell_select == "c":
            return
        city_product = products[int(sell_select) - 1]
        qty_to_sell = input(f"How many {city_product.name} do you wish to sell?")
        if int(qty_to_sell) <= city_product.shipqty:
            self.cash += int(qty_to_sell) * city_product.price
            city_product.shipqty -= int(qty_to_sell)
            self.current_shiphold -= int(qty_to_sell)
        else:
            print("You don't have that many to sell!")
            input(PRESS_ANY_KEY)
###########################


##### BANKING THINGS ######
    def visit_bank(self):
        input("How much would you like to deposit?")

    def visit_moneylender(self):
        payback = input("How much would you like to pay back?")
        if int(payback) <= self.cash:
            self.debt -= int(payback)
            self.cash -= int(payback)
        borrow = input("How much would you like to borrow? Note: 5% interest with 2x principal repayment.")
        if int(borrow) <= 10000:
            self.debt += int(borrow) * 2
            self.cash += int(borrow)
        else:
            input("You can't borrow more than £10,000!")

    def increase_debt(self):
        self.debt *= 1.05
############################

    def start_up(self):
        game_running = True
        while game_running:

            ##### GAME INTERFACE ######
            os.system("cls")
            print(GAME_TITLE)
            print(DIVIDER)
            print(f"Firm name: {self.firm_name}")
            print(f"Cash: {self.cash}")
            print("Debt: {:.0f}".format(self.debt))
            print(f"Current Hold: {self.current_shiphold}")
            print(f"Cannons: {self.cannons}")
            print(f"City: {self.current_city.name}")
            print(f"Ship Health: {self.ship_health}")
            print("Date: {:%B %d, %Y}".format(self.current_date))
            print(DIVIDER)
            print("-------- City Products --------")
            self.display_products(Product.products)
            print("-------------------------------\n")
            ##### END OF INTERFACE ######

            if self.ship_health <= self.min_ship_health:
                game_running = False
            has_bank_string = ""
            has_moneylender_string = ""
            if self.current_city.has_bank == True:
                has_bank_string = " [V]isit Bank,"
            if self.current_city.has_moneylender == True:
                has_moneylender_string = " [M]oneylender,"
            print("Menu: [L]eave Port, [B]uy, [S]ell,%s [T]ransfer Warehouse,%s [Q]uit" % (has_bank_string, has_moneylender_string))
            menu_option = input("What would you like to do?")
            if menu_option.upper() == "L":
                self.current_city, self.current_date = self.leave_port(City.cities, self.current_date)
                self.check_price_change(Product.products)
                self.increase_debt()
                pirates = PirateEncounter(self)
            elif menu_option.upper() == "B":
                self.buy(Product.products)
            elif menu_option.upper() == "S":
                self.sell(Product.products)
            elif menu_option.upper() == "V" and self.current_city.has_bank == True:
                self.visit_bank()
            elif menu_option.upper() == "M":
                self.visit_moneylender()
            elif menu_option.upper() == "Q":
                game_running = False
