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


class Specification:
    def is_satisfied(self):
        pass

class Filter:
    def filter(self):
        pass

class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item):
        return item.size == self.size

class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item):
        return item.color == self.color

class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(
            map(lambda spec: spec.is_satisfied(item), self.args)
        )

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


kerchief = Product('Kerchief', Color.BLUE, Size.SMALL)
flag = Product('flag', Color.BLUE, Size.MEDIUM)
blanket = Product('blanket', Color.RED, Size.LARGE)
towel = Product('towel', Color.GREEN, Size.MEDIUM)

products = [kerchief, flag, blanket, towel]
bf = BetterFilter()
blue = ColorSpecification(color=Color.BLUE)

# for i in bf.filter(products, blue):
#     print(i.name)


medium = SizeSpecification(size=Size.MEDIUM)

for i in bf.filter(products, AndSpecification(blue, medium)):
    print(i.name)

# A good design is to follow enterprise patern wherein we 
# have a Specification class and Filter class.
# This is more robust and scalable.
# When any new attributed are added to the Product class
# we simply extend by creating new 1) enum class, and 
# 2) Specification
# Hence this is a better design