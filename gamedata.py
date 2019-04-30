import csv


def load_city_data(city):
    with open(r'Pyrates\cities.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            city.create_city(**row)

def load_product_data(product):
    with open(r'Pyrates\products.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            product.create_product(**row)
