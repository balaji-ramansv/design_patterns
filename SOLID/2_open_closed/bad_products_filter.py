# Open Closed Principle
# Open for extension
# Closed for modification

from enum import Enum

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class ProductFilter:
    def __init__(self, products):
        self.products = products
    
    def filter_by_color(self, color):
        for product in self.products:
            if product.color == color:
                yield product

    def filter_by_size(self, size):
        for product in self.products:
            if product.size == size:
                yield product

    # Now if we want to filter by both color and size
    # or filter by color or size, the number of combinations keeps going
    # longer. If we add more properties in addition to color and size like
    # weight, texture, the options get more longer and messier

    def filter_by_color_and_size(self, color, size):
        for product in self.products:
            if product.size == size and product.color == color:
                yield product

    def filter_by_color_or_size(self, color, size):
        for product in self.products:
            if product.size == size or product.color == color:
                yield product

kerchief = Product('Kerchief', Color.BLUE, Size.SMALL)
flag = Product('flag', Color.BLUE, Size.MEDIUM)
blanket = Product('blanket', Color.RED, Size.LARGE)
towel = Product('towel', Color.GREEN, Size.MEDIUM)

products = [kerchief, flag, blanket, towel]

filter = ProductFilter(products=products)
for p in filter.filter_by_color(color=Color.BLUE):
    print(p.name)