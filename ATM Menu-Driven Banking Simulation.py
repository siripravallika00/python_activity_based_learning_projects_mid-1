
balance = 5000
choice = 0

while choice != 4:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount")
        elif amount <= balance:
            balance = balance - amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    elif choice == 3:
        print("Current balance =", balance)

    elif choice == 4:
        print("Thank you")

    else:
        print("Invalid choice")
