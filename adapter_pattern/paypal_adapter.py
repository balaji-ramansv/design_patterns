from payment_gateway import PaymentGateway
from paypal_legacy import PaypalLegacy

class PaypalAdapter(PaymentGateway):
    def __init__(self):
        self.paypal_legacy = PaypalLegacy()

    def process_payment(self, amount, currency, card_details):
        self.paypal_legacy.make_paypal_payment(amount=amount, currency=currency, card_info=card_details)
    
    def refund_payment(self, transaction_id):
        self.paypal_legacy.initiate_paypal_refund(transaction_ref=transaction_id)