class Bank_Application:
    def __init__(self,initial_balance=0):
        self.balance=initial_balance
    def deposit(self):
        amount=int(input("Enter the money"))
        self.balance+=amount
        print(f"{amount} deposited successful. current balance{self.balance}")
    def withdraw(self):
        amount=int(input("Enter the money"))
        if amount>self.balance:
            print(f"{amount} Insufficient Balance")
        else:
            self.balance-=amount
            print(f"{amount} withdraw successfully. Remaining balance is Rs.{self.balance}")        
    def balance(self):
        print(f"Current Balance: {self.balance}")
    def exit(self):
        print("Thanks for using ATM ")  
        bank_apply=Bank_Application(initial_balance=35000)
    while True:
        print("1.Deposit")
        print("2.withdraw")
        print("3.Current_balance")
        print("4.Exit")
        choice=int(input("Enter the choice:"))
        if choice==1:
            bank_apply.deposit()
        elif choice==2:
            bank_apply.withdraw()
        elif choice==3:
            bank_apply.balance()
        elif choice==4:
            bank_apply.exit()
        else:
            print("Invalid Data")