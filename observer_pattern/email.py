from stock_observer import StockObserver

class Email(StockObserver):
    def perform_action(self, name, price):
        print(f"EMAIL: Your stock {name} is now Rs. {price}.")
