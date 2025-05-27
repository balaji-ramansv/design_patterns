
from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount, currency, card_details):
        pass

    @abstractmethod
    def refund_payment(self, transaction_id):
        pass