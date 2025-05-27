from stock_observer import StockObserver

class Dashboard(StockObserver):
    def perform_action(self, name, price):
        print(f"Dashboard: Your stock {name} is now Rs. {price}.")
