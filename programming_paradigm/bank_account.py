class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance=initial_balance

    def deposit(self,amount):
        if amount>0:
            self.account_balance+=amount
            return True
        else:
            return("Amount should be positive")
            return False

    def withdraw(self,amount):
        if amount<0:
            print("Amount should be positive")
            return False
        if amount>self.account_balance:
            print(("Amount should be less than account balance"))
            return False
        self.account_balance-=amount


    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")