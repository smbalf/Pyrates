import random



class Product(object):
    products = []
    def __init__(self, name, minprice, maxprice):
        self.name = name
        self.minprice = int(minprice)
        self.maxprice = int(maxprice)
        self.shipqty = 0
        self.warehouseqty = 0

    @classmethod
    def create_product(cls, **kwargs):
        cls.products.append(Product(**kwargs))