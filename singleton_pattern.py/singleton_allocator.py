class Database:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        print("Loading DB")    

d1 = Database()
d2 = Database()

print(d1 == d2)

