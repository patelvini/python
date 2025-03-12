from abc import ABC ,abstractmethod

class Payment(ABC):
    def print_slip(self,amount):
        print("Purchase amount = ",amount)

    @abstractmethod
    def payment(self,pay_amount):
        pass

class CreditCardPayment(Payment):
    def payment(self,pay_amount):
        print("Credit card payment of ", pay_amount)

class MobileWalletPayment(Payment):
    def payment(self,pay_amount):
        print("Mobile wallet payment of ", pay_amount)


#object creation

CCP = CreditCardPayment()
MWP = MobileWalletPayment()

# calling methods of a class using object

CCP.payment(1000)
CCP.print_slip(1000)
print(isinstance(CCP,Payment))

MWP.payment(500)
MWP.print_slip(500)
print(isinstance(MWP,Payment))
        
    
