from abc import ABC, abstractmethod

class StockObserver(ABC):
    @abstractmethod
    def perform_action(self):
        pass