import random
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=Singleton):
    def __init__(self):
        self.id = random.choice(range(1,101))
        print(f"creating a db instance with id {self.id}")
d1 = Database()
d2 = Database()
print(d1 == d2)

