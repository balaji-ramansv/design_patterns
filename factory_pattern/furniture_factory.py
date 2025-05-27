from furniture import Chair, Table, Sofa

class FurnitureFactory:
    def get_chair(self):
        chair = Chair()
        return chair
    
    def get_table(self):
        table = Table()
        return table
    
    def get_sofa(self):
        sofa = Sofa()
        return sofa