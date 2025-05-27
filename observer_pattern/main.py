from stock import Stock
from email import Email
from sms import Sms
from dashboard import Dashboard

if __name__ == "__main__":
    sbi = Stock("SBIN", 400)
    email_sender = Email()
    sms_sender = Sms()
    dashboard_displayer = Dashboard()

    sbi.add_observer(email_sender)
    sbi.add_observer(sms_sender)
    sbi.add_observer(dashboard_displayer)

    sbi.set_price(400)
    sbi.set_price(450)
