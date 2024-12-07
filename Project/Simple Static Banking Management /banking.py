class Banking:
    def __init__(self, user_name, intial_balance):
        self.name = user_name
        self.balance = intial_balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            # self.balance = self.balance + amount
            return amount
    def get_balance(self):
        return self.balance
    
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            return amount
        else:
            return f"Insufficient Balance"
        
ostad = Banking("Ostad", 10000)
print(f"Account name : {ostad.name}")
print(f"Initial balance is : {ostad.balance}")
print(f"Deposit balance : {ostad.deposit(1000)}")
print(f"After deposit, Your balance is : {ostad.get_balance()}")
print(f"Withdraw balance : {ostad.withdraw(2000)}")
print(f"After withdraw, Your balance is : {ostad.get_balance()}")
