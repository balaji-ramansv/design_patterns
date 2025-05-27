from abc import ABC, abstractmethod

class Furniture(ABC):
    @abstractmethod
    def get_description(self):
        pass

class Chair(Furniture):
    def get_description(self):
        return "A comfortable chair"
    
class Table(Furniture):
    def get_description(self):
        return "A sturdy table"

class Sofa(Furniture):
    def get_description(self):
        return "A cozy sofa"

