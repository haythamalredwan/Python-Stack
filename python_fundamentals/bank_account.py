class BankAccount:
    def __init__(self, int_rate = 0.01, balance = 0):
        self.balance = balance
        self.int_rate = int_rate
    
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0 :
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5  
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance:", "$" + str(self.balance))
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance *= (1+self.int_rate)
        return self

haytham = BankAccount(0.01 , 20000)
ahmad = BankAccount(0.01 , 0)

haytham.deposit(1500).deposit(2500).deposit(3200).withdraw(17000).yield_interest().display_account_info()

ahmad.deposit(5000).deposit(5000).withdraw(2500).withdraw(2500).withdraw(2500).withdraw(2600).yield_interest().display_account_info()
          

