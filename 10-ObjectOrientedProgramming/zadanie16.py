class Bank_account():
    def __init__(self):
        self.balance=0
    def account(self,number):
        self.account=number
    def balance(self,number):
        self.balance=number
    def deposit(self,amount):
        self.balance+=amount
    def show_status(self):
        print(f"Bank account no: {self.account} balance: {self.balance}")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
        else:
            print("Insufficient funds on the account")
bank1=Bank_account()
bank1.account("12 3456 5555 9090 1111 0000 7722")
bank1.show_status()
bank1.deposit(25.30)
bank1.show_status()
bank1.withdraw(31.70)
bank1.show_status()
bank1.withdraw(14)
bank1.show_status()