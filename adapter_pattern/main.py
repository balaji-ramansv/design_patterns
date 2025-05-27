from payment_processor import PaymentProcessor


if __name__ == "__main__":
    pp = PaymentProcessor.get_payment_processor(payment_api="paypal")
    print(type(pp))
    pp.process_payment(1000, "Rs. ", "1234 5678 9101")