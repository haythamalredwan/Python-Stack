class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    #Making Deposite
    def make_deposit(self, amount):
        self.account_balance += amount
    
    #Making Withdrawal
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    #Display User Balance
    def display_user_balance(self):
        print("User:",self.name+",","Balance:","$"+str(self.account_balance))

    #Transfare Money
    def transfare_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount 

#Creating Users
haytham = User("Haytham alredwan")
ahmad = User("Ahmad saed")
khaled = User("Khaled sami")

#First User Transaction
haytham.make_deposit(10000)
haytham.make_deposit(70000)
haytham.make_deposit(3000)
haytham.make_withdrawal(15000)
haytham.display_user_balance()

#Second User Transaction
ahmad.make_deposit(8500)
ahmad.make_deposit(9200)
ahmad.make_withdrawal(4230)
ahmad.make_withdrawal(5666)
ahmad.display_user_balance()

#Third User Transaction
khaled.make_deposit(22000)
khaled.make_withdrawal(7255)
khaled.make_withdrawal(2365)
khaled.make_withdrawal(4790)
khaled.display_user_balance()

#Bouns: Transfare Money
haytham.transfare_money(khaled,2000)
haytham.display_user_balance()
khaled.display_user_balance()


