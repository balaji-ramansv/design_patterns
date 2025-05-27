from stock_observer import StockObserver

class Sms(StockObserver):
    def perform_action(self, name, price):
        print(f"SMS: Your stock {name} is now Rs. {price}.")
