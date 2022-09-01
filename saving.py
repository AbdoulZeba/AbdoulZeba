
from checking import Checking


class Saving:
    def __init__(self):
        self.saving_account_balance = 0
        
    
    def withDrawFunds(self,amount):
        
        if (self.saving_account_balance > amount) and (amount > 0):
            self.saving_account_balance -= amount
           
        else:
            print(f'your account balance is ${self.saving_account_balance}')
            print(f'you cannot withdraw ${amount}')
        return ''
    def depositFunds(self,amount):
        self.saving_account_balance += amount
        return ''
        
    def viewBalance(self):
        return f'Your Account blance is ${self.saving_account_balance})'