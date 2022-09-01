from checking import Checking

class BankAccount(Checking):
    def __init__(self):
        Checking.__init__(self)
        self.account_number = 0
        self.pin_number = 0
    
    def set_account_number(self,a_number):
        self.account_number = a_number
        
    def get_account_number(self):
        return self.account_number
    
    def set_pin(self,pin_n):
        self.pin_number = pin_n
        
    def get_pin(self):
        return self.pin_number
    


def customersAccountsExist(account_number,pin_number):
    Accounts = {66927412:1234,950460723:7855}
    
    for acc_n, pin in Accounts.items():
        if (acc_n == account_number) and (pin == pin_number):
            return True
    return False
        
def account_Choice():
        print("Select the account you want to access:")
        print("  type 1- Checking")
        print("  type 2- Saving")
        print("  type 3- Exit")  
        return ''
    
def ChekingAndSavingMenu():
    print("Choose an option:")
    print("  type 1- View Balance")
    print("  type 2- Withdraw Funs")
    print("  type 3- Deposit Funds")
    print("  type 4- Exit")  
    return ''
    

Customer = BankAccount()

account_number = int(input("Enter your account number: "))
pin_number = int(input("Eneter your pin: "))

if customersAccountsExist(account_number,pin_number):
    
    Customer.set_account_number(account_number)
    Customer.set_pin(pin_number)
    
    do_loop = True
    
    while do_loop:
        print(account_Choice())
        user_choice = int(input("Choice: "))
        
        if (user_choice == 1):
            print(ChekingAndSavingMenu())
            checking_choice = int(input("Choice: "))
            
            if (checking_choice== 1):
                print("Your balance is", Customer.checkin_account_balance)
                checking_choice  = int(input("Choice: "))
                
            if (checking_choice  == 2):
                amount_to_withdraw = float(input("Enter Amount to withdraw: "))
                print(Customer.withDrawFunds(amount_to_withdraw))
                print("Your new balance is ",Customer.checkin_account_balance)
                checking_choice = int(input("Choice: "))
                
            if (checking_choice  == 3):
                amount_to_deposit = float(input("Enter amount: "))
                Customer.depositFunds(amount_to_deposit)
                print("your new balance is ",Customer.checkin_account_balance)
                
            if (checking_choice == 4):
                 print(account_Choice())
                 user_choice   = int(input("Choice: "))
                 
        if (user_choice == 4):
            do_loop = False
                
            
            
        
        
else:
    print("Your Account number or pin number is incorrect!!")
    
    






