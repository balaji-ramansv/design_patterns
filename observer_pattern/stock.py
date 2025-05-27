from stock_subject import StockSubject

class Stock(StockSubject):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._observers = []
    
    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self):
        for observer in self._observers:
            observer.perform_action(self.name, self.price)
    
    def set_price(self, price):
        if self.price != price:
            self.price = price
            self.notify_observers()