class PaypalLegacy:
    def __init__(self):
        self.amount = 0
        self.currency = None
        self.card_info = None

    def make_paypal_payment(self, amount, currency, card_info):
        self.amount = amount
        self.currency = currency
        self.card_info = card_info
        print(f"Paypal has processed payment of {currency}{amount} using card {card_info}")
    
    def initiate_paypal_refund(self, transaction_ref):
        print(f"Paypal has processed the refund for the transaction {transaction_ref}")