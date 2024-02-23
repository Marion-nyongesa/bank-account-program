#bank account program
class BankAccount:
    def __init__( self, account_number, balance, date_of_openning,customer_name):
        
        self.account-number == account_number
        self.balance = balance
        self.date_of_openning == datetime.date.today()
        self.customer_name == customer_name
    def deposit(self):
         self.balance += amount
         return amount
    
    def withdraw(self):
         if self.balance< amount:
             return "insufficient balance"
         else:
             self.balance-=amount
             return amount
    
    
    def check_balance(self):
            return self.balance
    def customer_details(self):
           return   self.customer_name, self.account_number, self.balance ,date_of_openning
    
account= BankAccount(account_number," 65744332",customer_name== "marion nyongesa" ,date_of_openning== "13/06/2007")
print(account.customer_details())
account.deposit(1000)
print(account.check_balance())
account.withdrawal(500)
print(account.check_balance)



                     










                     
