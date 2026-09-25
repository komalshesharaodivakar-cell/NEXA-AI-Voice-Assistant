# for, while using break, continue and pass

Pin = "1234"
balance = 5000

# Pin check
for attempt in range(3):
    entered_pin = input("Enter PIN: ")

    if entered_pin == "":
        print("Empty input")
        continue

    if entered_pin == Pin:
        print("Login successful")
        break
    else:
        print("Wrong PIN")
        pass  # does not do anything

else:
    print("Card blocked")
    exit()

# ATM Menu

balance = 5000
choice = ""

while choice != "3":
    print("\n===== ATM Menu =====")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Exit")

    choice = input("Enter choice: ")
    if choice == "":
        print("Empty choice")

    elif choice == "1":
        print("Balance =", balance)
    elif choice == "2":
        amount = int(input("Enter withdraw amount: "))
        if amount <= 0:
            print("Invalid amount")

        if amount <= balance:                            #instead of using if we can use elif
            balance = balance - amount
            print("Withdraw successful")
            print("Remaining balance =", balance)
        else:
            print("Insufficient balance")
            pass
    elif choice == "3":
        print("Thank you, visit again")
        break                                           #if we want we can break
    else:
        print("Invalid choice")
        pass