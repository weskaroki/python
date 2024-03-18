class Bank_account:
    def __init__(self,account_number,balance, date_of_opening,customer_name):
        self.account_number= account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def describe (self):
        print(f"{self.customer_name},your account, {self.account_number},opened on,{self.date_of_opening},has a balance of{self.balance}")
    def widthdraw(self):
        self.balance-=5000
    def deposit(self):
        self.balance+=20000
customer1 = Bank_account(1005,100000,'17th march','John')
print(customer1.describe())
customer1.widthdraw()
print(customer1.balance)
customer1.deposit()
print(customer1.balance)


