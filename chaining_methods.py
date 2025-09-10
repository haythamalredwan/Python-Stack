class User:
    def __init__(self, name):
        self.name = name
        self.account_balance = 0
    

    #Making Deposite
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    #Making Withdrawal
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    #Display User Balance
    def display_user_balance(self):
        print("User:",self.name+",","Balance:","$"+str(self.account_balance))
        return self

    #Transfare Money
    def transfare_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount 
        return self

#Creating Users
haytham = User("Haytham alredwan")
ahmad = User("Ahmad saed")
khaled = User("Khaled sami")

#First User Transaction
haytham.make_deposit(10000).make_deposit(70000).make_deposit(3000).make_withdrawal(15000).display_user_balance()

#Second User Transaction
ahmad.make_deposit(8500).make_deposit(9200).make_withdrawal(4230).make_withdrawal(5666).display_user_balance()

#Third User Transaction
khaled.make_deposit(22000).make_withdrawal(7255).make_withdrawal(2365).make_withdrawal(4790).display_user_balance()

#Bouns: Transfare Money
haytham.transfare_money(khaled,2000).display_user_balance()
khaled.display_user_balance()


