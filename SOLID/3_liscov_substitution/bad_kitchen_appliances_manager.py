class KitchenAppliancesManager:
    def on(self):
        pass

    def off(self):
        pass

    def set_temparature(self):
        pass

class Toaster(KitchenAppliancesManager):
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
    
    def set_temparature(self, temparature):
        """OOPS this method is irrelevant for Blender. So this breaks Liskov's substitution"""
        print("Oops this is disstrous. Temparature can't be set for Blender")

# According to Liscov's substitution a derived class should be able to inherit
# override and use all the methods of its base class
