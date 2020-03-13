# This is  python program to make  credit card  class.

# This is main credit card class.
class creditcard:
    def __init__(self,customer_name,bank_name,acc_number,card_limit,balance = 0):
        self.customer_name = customer_name
        self.bank_name = bank_name
        self.acc_number = acc_number
        self.card_limit = card_limit
        self.balance = balance
    
    def charge(self,price):
        '''
        This is charge function which return True when balance
        is not exceed the credit card limit and otherwise return False.
        '''
        if price + self.balance > self.card_limit:
            print("Your total balance amount is exceeding the card limit.")
            return False    

        else:
            self.balance = self.balance + price
            print("You spend Rs.{}".format(price))
            print("Now you have only Rs.{} amount left in your credit card limit.".format(self.card_limit - self.balance))
            return True
        
    def make_payment(self,amount):
        if amount >= 0:
            self.balance = self.balance - amount
        else:
            raise ValueError("amount should be positive.")
    
    def show_creditcard_detail(self):
        print("-------------------- CREDIT CARD DETAIL -----------------------")
        print("customer name: {}                    bank name: {}".format(self.customer_name,self.bank_name))
        print("account  number: {}         credit card limit: Rs.{}".format(self.acc_number,self.card_limit))
        print("Balance: Rs.{}".format(self.balance))
        print("Now you have only Rs.{} amount left in your credit card limit.".format(self.card_limit - self.balance))
     
# This is predaitory credit card class(which is subclass of credit card class)

class predaitory_creditcard(creditcard):
    def __init__(self,customer_name,bank_name,acc_number,card_limit,annual_percentage_rate):
        self.annual_percentage_rate = annual_percentage_rate
        super().__init__(customer_name,bank_name,acc_number,card_limit)
    
    def charge(self,price):
        success = super().charge(price)
        if not success:
            self.balance = self.balance + 5        # Rs.5 is for penaltiy
        return success
    
    def process_month(self):
        if self.balance > 0:
            monthly_factor = pow(1 + self.annual_percentage_rate,1/12)
            self.balance = self.balance * monthly_factor
    


name = "Jhon cartar"
bank = "True Bank"
account_number = "2133-1231-1231-4323"
limit = 25000

card1 = creditcard(name,bank,account_number,limit,1000)
card1.show_creditcard_detail()
print("------------------------")
card1.charge(12000)
card1.make_payment(5000)
card1.show_creditcard_detail()


# p_name = "Harry kan"
# p_bank = "City Bank"
# p_account_number = "7868-5465-3455-3454"
# p_limit = 35000

# p_card1 = predaitory_creditcard(p_name,p_bank,p_account_number,p_limit,0.08)
# p_card1.show_creditcard_detail()
# print("--------------------------")
# p_card1.charge(14000)
# print("--------------------------")
# p_card1.charge(24000)
# p_card1.show_creditcard_detail()
