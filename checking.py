

class Checking:
    def __init__(self):
        self.checkin_account_balance = 0
        
    
    def withDrawFunds(self,amount):
        
        if (self.checkin_account_balance > amount) and (amount > 0):
            self.checkin_account_balance -= amount
           
        else:
            print(f'your account balance is ${self.checkin_account_balance}')
            print(f'you cannot withdraw ${amount}')
        return ''
    def depositFunds(self,amount):
        self.checkin_account_balance += amount
        return ''
        
    def viewBalance(self):
        return f'Your Account blance is ${self.checkin_account_balance})'
    

            
           

        
     
    