from payment_gateway import PaymentGateway
from square_legacy import SquareLegacy

class SquareAdapter(PaymentGateway):
    def __init__(self):
        self.square_legacy = SquareLegacy()

    def process_payment(self, amount, currency, card_details):
        self.square_legacy.square_process_transaction(value=amount, currency_code=currency, card_data=card_details)
    
    def refund_payment(self, transaction_id):
        self.square_legacy.square_return_fund(ref_id=transaction_id)