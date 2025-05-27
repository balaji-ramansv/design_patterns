from stripe_payments import StripeAPI
from paypal_adapter import PaypalAdapter
from square_adapter import SquareAdapter

class PaymentProcessor:
    _payment_apis = {
        "square": SquareAdapter,
        "paypal": PaypalAdapter,
        "stripe": StripeAPI
    }
    
    @classmethod
    def get_payment_processor(cls, payment_api):
        return cls._payment_apis[payment_api]()
        
        