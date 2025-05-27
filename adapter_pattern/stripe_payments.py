from payment_gateway import PaymentGateway

"""This is a compliant API"""
class StripeAPI(PaymentGateway):
    def __init__(self):
        self.amount = 0
        self.currency = None
        self.card_details = None

    def process_payments(self, amount, currency, card_details):
        self.amount = amount
        self.currency = currency
        self.card_details = card_details
        print(f"Amount {self.currency}{self.amount} processed for payment using {self.card_details}")
    
    def refund_paymet(self, transaction_id):
        print(f"Payment processed for the transaction id {transaction_id}")
