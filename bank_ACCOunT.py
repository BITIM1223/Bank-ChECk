class BankAccount:
    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
    def check_balance(self):
        print(f"You Current Balance is {self.balance:.2f}")
print("Welcome To The Bank!")
name = input("What is your name?: ")
account = BankAccount(name)
while True:
    print("What would you like to do?")
    print("1: Let's See your balance!")
    print("2: Deposit Change/Money")
    print("3: Withdraw Your Money")
    print("4: Exit application")
    choice = input("Which will be your choice?: ")
    if choice == "1": 
        account.check_balance()
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        print(f"Good Bye {account.name}")
        break

    else:
        print("Choice Is Invalid, choose 1 of the 4 options.")

    
