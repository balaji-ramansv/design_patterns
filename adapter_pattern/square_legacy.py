class SquareLegacy:
    def __init__(self):
        self.value = 0
        self.currency_code = None
        self.card_data = None

    def square_process_transaction(self, value, currency_code, card_data):
        self.value = value
        self.currency_code = currency_code
        self.card_data = card_data
        print(f"Square has processed payment of {currency_code}{value} using card {card_data}")
    
    def square_return_fund(self, ref_id):
        print(f"Square has processed the refund for the transaction {ref_id}")