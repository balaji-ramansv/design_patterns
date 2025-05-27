from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Photocopier(ABC):
    @abstractmethod
    def photocopy(self, document):
        pass


"""By keeping the interface Printer thin and non fat, I (OldFashionedPrinter)
am able to implement it."""
class OldFashionedPrinter(Printer):
    def print(self, document):
        print(f"I can print the {document} very well")

"""I am a modern printer. I can implement both Printer and Photocopier."""
class ModernPrinter(Printer, Photocopier):
    def print(self, document):
        print(f"I can print the {document} very well")
    
    def photocopy(self, document):
        print(f"I can photocopy the {document} very well")