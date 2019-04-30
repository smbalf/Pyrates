import random



class Product(object):
    products = []
    def __init__(self, num, name, minprice, maxprice):
        self.num = num
        self.name = name
        self.minprice = int(minprice)
        self.maxprice = int(maxprice)
        self.shipqty = 0
        self.warehouseqty = 0
        self.generate_random_price()

    def generate_random_price(self):
        self.price = random.randint(self.minprice, self.maxprice)    

    @classmethod
    def create_product(cls, **kwargs):
        cls.products.append(Product(**kwargs))