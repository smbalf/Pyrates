import random
from product import Product



class City(object):
    cities = []
    def __init__(self, num, name, has_bank, has_shipyard):
        self.num = num
        self.name = name
        self.has_bank = has_bank == "True"
        self.has_shipyard = has_shipyard == "True"
        self.create_city_products()

    def create_city_products(self):
        self.city_products = []
        for product in Product.products:
            self.city_products.append(CityProduct(self, product))
            #for every 'product' in Product.products list, append to city_products

    @classmethod
    def create_city(cls, **kwargs):
        cls.cities.append(City(**kwargs))


class CityProduct(object):
    def __init__(self, city, product):
        self.city = city
        self.product = product  
        self.generate_random_price()

    def generate_random_price(self):
        self.price = random.randint(self.product.minprice, self.product.maxprice)