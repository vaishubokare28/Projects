class Bank:
    def __init__(self, name, accountno, balance=100000): 
        self.name = name
        self.accountno = accountno
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! You only have {self.balance:.2f} in your account.")
        else:
            self.balance = self.balance - amount
            print(f"Withdrawal successful! Your new balance is {self.balance:.2f}.")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
        else:
            self.balance = self.balance + amount
            print(f"Deposit successful! Your new balance is {self.balance:.2f}.")

    def check_balance(self):
        print(f"Your current balance is {self.balance:.2f}.")


name = input("Enter your name: ")
accountno = input("Enter your account number: ")

obj1 = Bank(name, accountno)

while True:
    print('''
    1. Check Balance
    2. Withdraw Amount
    3. Deposit Amount
    4. Exit
    ''')

    ch = int(input("Enter your choice: "))

    if ch == 1:
        obj1.check_balance()
    elif ch == 2:
        amt = float(input("Enter amount to withdraw: "))
        obj1.withdraw(amt)
    elif ch == 3:
        amt = float(input("Enter amount to deposit: "))
        obj1.deposit(amt)
    elif ch == 4:
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
