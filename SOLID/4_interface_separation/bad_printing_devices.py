from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def photocopy(self, document):
        pass

class OldFashionedPrinter(Printer):
    def print(self, document):
        print("I can print very well")

    def photocopy(self, document):
        """This is the problem. Old fashioned printers can't take photocopy.
        By making the OldFashionedPrinter inherit / override Printer
        which is a very fat interface / abstract class having a lot of 
        functionality that may not be relevant to all types of printers,
        we are making the interface disastrous and making the APIs unfriendly to
        users. Users might get an impression Old fashioned printers can also 
        print - which is just not the case."""
        raise Exception("Why am I asked to do something which I don't know?")