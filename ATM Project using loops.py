#create simple project using loop
#ATM projet in python that uses loop concepts to perform basic banking operations like:
#checking balance
#depositing money
#withdrawing money
#exiting

balance = 1000  

while True:
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"Your current balance is: {balance}")

    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance = balance + amount
            print(f"{amount} deposited successfully. New balance: {balance}")
        else:
            print("Invalid deposit amount.")

    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        if 0 < amount <= balance:
            balance = balance + amount
            print(f"{amount} withdrawn successfully. Remaining balance: {balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    elif choice == "4":
        print("Thank you for using our ATM. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.")