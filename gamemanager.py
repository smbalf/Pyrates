import os
import datetime
import random
import time
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
        self.pirate_name = kwargs["name"]
        self.vessel_name = kwargs["vessel"]
        self.cash = kwargs["cash"]
        self.cannons = kwargs["cannons"]
        self.bank = 0
        self.maxshiphold = kwargs["shiphold"]
        self.maxshiphealth = kwargs["shiphealth"]
        self.min_shiphealth = 0
        self.current_shiphold = 0
        self.current_shiphealth = 100
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
        if result >= 10:
            for city_product in products:
                city_product.generate_random_price()

    def buy(self, products):
        buy_select = input(f"Which product do you want to buy? (1-{str(len(Product.products))}) - Press [C] to cancel.")
        try:
            if int(buy_select) > len(Product.products):
                return
            city_product = products[int(buy_select) - 1]
            afford = int(self.cash / city_product.price)
            print(f"You can afford {afford} {city_product.name}")
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
        except ValueError:
            print(f"Try again {self.pirate_name}...")
            time.sleep(1)
        if buy_select.upper() == "C":
            return

    def sell(self, products):
        sell_select = input(f"Which product do you want to sell? (1-{str(len(Product.products))}) - Press [C] to cancel.")
        try:
            if int(sell_select) > len(Product.products):
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
        except ValueError:
            print(f"Try again {self.pirate_name}...")
            time.sleep(1)
        if sell_select == "c":
            return
###########################

##### BANKING THINGS ######
    def visit_bank(self):
        deposit = input("How much would you like to deposit?")
        try:
            if int(deposit) <= self.cash:
                self.bank += int(deposit)
                self.cash -= int(deposit)
            else:
                print("You don't have that much!")
            print(f"You currently have £{str(self.bank)} in the bank.")
            withdraw = input("How much would you like to withdraw?\n")
            if int(withdraw) <= self.bank:
                self.cash += int(withdraw)
                self.bank -= int(withdraw)
        except ValueError:
            print(f"Try again {self.pirate_name}...")
            time.sleep(1)
        else:
            print("You don't have that much!")
############################

##### SHIPYARD ######

    def shipyard(self):
        print(f"Welcome to the shipyard {self.pirate_name}")
        shipyard_option = input(f"What shall we do for the {self.vessel_name}? [C]annons, [R]epair, [I]ncrease Shiphold")
        # BUYING CANNONS
        if shipyard_option.upper() == "C":
            cannon_price = 500
            print(f"Cannons cost £{str(cannon_price)} to be fitted.")
            buy_cannons = input("How many would you like to fit?\n")
            cannon_cost = int(buy_cannons) * cannon_price
            try:
                if cannon_cost <= self.cash:
                    self.cannons += int(buy_cannons)
                    self.cash -= cannon_cost
                elif cannon_cost > self.cash:
                    print("You can't afford that many a cannon!")
                    time.sleep(2)
            except ValueError:
                print(f"Try again {self.pirate_name}...")
                time.sleep(2)
        # BUYING REPAIRS TO VESSEL
        elif shipyard_option.upper() == "R": #and self.current_shiphealth == self.maxshiphealth:
            if self.current_shiphealth == self.maxshiphealth:
                print(f"The {self.vessel_name} is already in fine shape!")
                time.sleep(2)
            else:
                repair_price = 10
                repair_damage = (self.maxshiphealth - self.current_shiphealth)
                repair_cost = (repair_damage) * repair_price
                print(f"To fully repair the {self.vessel_name} will cost £{str(repair_cost)}")
                repair_vessel = input("Shall we start the [R]epairs or [N]ot Cap'n?")
                if repair_vessel.upper() == "N":
                    return                
                try:
                    if repair_vessel.upper() == "R" and repair_cost <= self.cash:
                        self.current_shiphealth += repair_damage
                        self.cash -= repair_cost
                    elif repair_vessel.upper() == "R" and repair_cost > self.cash:
                        print(f"You can't afford to repair the {self.vessel_name} Cap'n...")
                        time.sleep(3)
                except ValueError:
                    print(f"Try again {self.pirate_name}...")
                    time.sleep(2)
        # BUYING MORE VESSEL STORAGE SPACE
        elif shipyard_option.upper() == "I":
            print(f"The {self.vessel_name} can hold up to {str(self.maxshiphold)}.")
            expand_hold = input("Shall we [I]ncrease the shiphold or [N]ot?\n")
            if expand_hold.upper() == "N":
                return  
            try:
                if expand_hold.upper() == "I":
                    expand_price = 50
                    print(f"Every extra cargo space will cost you £{expand_price} Cap'n.")
                    expand_option = input("How much extra cargo space shall we add?")
                    expand_cost = expand_price * int(expand_option)
                    if expand_cost <= self.cash:
                        self.maxshiphold += int(expand_option)
                        self.cash -= expand_cost
                    elif expand_cost > self.cash:
                        print("You can't afford that much space Cap'n!")
                        time.sleep(2)
            except ValueError:
                print(f"Try again {self.pirate_name}...")
                time.sleep(1)
  



######################

    def start_up(self):
        game_running = True
        while game_running:

            ##### GAME INTERFACE ######
            os.system("cls")
            print(GAME_TITLE)
            print(DIVIDER)
            print(f"Ahoy {self.pirate_name}!")
            print(f"Welcome aboard the {self.vessel_name}")
            print(f"Cash: {self.cash}")
            print(f"Current Hold: {self.current_shiphold}/{self.maxshiphold}")
            print(f"Ship Health: {self.current_shiphealth}/{self.maxshiphealth}")
            print(f"Cannons: {self.cannons}")
            print(f"City: {self.current_city.name}")
            print("Date: {:%B %d, %Y}".format(self.current_date))
            print(DIVIDER)
            print("-------- City Products --------")
            self.display_products(Product.products)
            print("-------------------------------\n")
            ##### END OF INTERFACE ######

            if self.current_shiphealth <= self.min_shiphealth:
                game_running = False

            has_bank_string = ""
            if self.current_city.has_bank == True:
                has_bank_string = " [V]isit Bank,"
            
            has_shipyard_string = ""
            if self.current_city.has_shipyard == True:
                has_shipyard_string = " [S]hipyard,"

            ##### GAME MENU #####
            print(F"Menu: [L]eave Port, [T]rade,{has_shipyard_string}{has_bank_string} [Q]uit")  #this then should change to new one since = true
            menu_option = input("What would you like to do?")
            if menu_option.upper() == "L":
                self.current_city, self.current_date = self.leave_port(City.cities, self.current_date)
                self.check_price_change(Product.products)
                #ADD CHECK SO PRICES DON'T CHANGE IN SAME CITY...
                pirates = PirateEncounter(self)
            elif menu_option.upper() == "T":
                trade_option = input("Would you like to [B]uy or [S]ell goods?")
                if trade_option.upper() == "B":
                    self.buy(Product.products)
                elif trade_option.upper() == "S":
                    self.sell(Product.products)
            elif menu_option.upper() == "S":
                self.shipyard()
            elif menu_option.upper() == "V" and self.current_city.has_bank == True:
                self.visit_bank()
            elif menu_option.upper() == "Q":
                game_running = False
