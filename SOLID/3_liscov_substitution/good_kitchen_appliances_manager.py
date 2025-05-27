class KitchenAppliancesManager:
    def on(self):
        pass

    def off(self):
        pass

    def set_temparature(self):
        pass

class KitchenAppliancesWithTempManager(KitchenAppliancesManager):
    def set_temparature(self):
        pass


class Toaster(KitchenAppliancesWithTempManager):
    def on(self):
        print("switched on the Toaster")
    
    def off(self):
        print("switched off the Toaster")
    
    def set_temparature(self, temparature):
        print(f"Set the temparature of the toaster to {temparature}")

class Blender(KitchenAppliancesManager):
    def on(self):
        print("switched on the Blender")
    
    def off(self):
        print("switched off the Blender")

# In this we figured out that not all appliances adjust temparature
# So, the base class KitchenAppliancesManager should not have any methods related to temparature
# Alternatively, we can have a derived class KitchenAppliancesWithTempManager which inherits from KitchenAppliancesManager
# This derived class KitchenAppliancesWithTempManager can be used to deal with appliances that need to adjust temparature
