from furniture_factory import FurnitureFactory

ff = FurnitureFactory()
chair = ff.get_chair()
print(chair.get_description())