# TASK REQUIREMENT CUSTOM EXCEPTION HANDLING 
# PROJECT ONLINE SHOPPING PAYMENT VALIDATION SYSTEM OBJECTIVE
class PaymentError(Exception):
    pass
class InvalidAmountError(PaymentError):
    pass
class InsufficientBalanceError(PaymentError):
    pass
class InvalidPaymentMethodError(PaymentError):
    pass
class Payment():
    allowed_methods = ["upi","credit card","debit card"]
    def __init__(self,customer_name,balance,payment_method):
        self.customer_name = customer_name
        self.balance = balance
        self.payment_method = payment_method
    def process_payment(self,amount):
        if amount <= 0:
            raise InvalidAmountError("Amount Must Be Greater Than Zero")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient Balance")
        if self.payment_method not in self.allowed_methods:
            raise InvalidPaymentMethodError("Invalid Payment Method")
        self.balance = self.balance - amount
customer =Payment ("Rahul",5000,"upi")
amount= 1500
try:
    customer.process_payment(amount)
except  InvalidAmountError as error:
    print("Error:",error)
except InsufficientBalanceError as error:
    print("Error:",error)
except InvalidPaymentMethodError as error:
    print("Error:",error)
else:
    print("Payment Succesfull")
    print("Customer:", customer.customer_name)
    print("Amount Paid:₹",amount)
    print("Remaining Balance:₹", customer.balance)
finally:
    print("Payment Processing Completed. ")


        

            
