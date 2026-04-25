details = {
    "name": "pratyush",
    "age": 19,
    "pin": 1234,
    "balance": 1000000
}

transaction_history = []

def check_pin():
    entered_pin = int(input("Enter your PIN: "))
    if entered_pin == details["pin"]:
        return True
    else:
        print("Wrong PIN ❌")
        return False


def display_balance():
    print(f"Your current balance is: ₹{details['balance']}")


def deposit_money():
    if check_pin():   # 🔐 PIN check first
        amount = float(input("Enter the amount to deposit: "))
        details["balance"] += amount
        transaction_history.append(("Deposit", amount))
        print(f"₹{amount} deposited successfully.")
        print(f"New balance: ₹{details['balance']}")


def withdraw_money():
    if check_pin():   # 🔐 PIN check first
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= details["balance"]:
            details["balance"] -= amount
            transaction_history.append(("Withdraw", amount))
            print(f"₹{amount} withdrawn successfully.")
            print(f"New balance: ₹{details['balance']}")
        else:
            print("Insufficient balance ❌")


def statement():
    print(f"\nName: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Current Balance: ₹{details['balance']}")
    print("Transaction History:")
    for t in transaction_history:
        print(f"{t[0]}: ₹{t[1]}")


def bank():
    print("Welcome to ABC Bank 🙏")
    
    while True:
        print("\n1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            display_balance()
        elif choice == 2:
            deposit_money()
        elif choice == 3:
            withdraw_money()
        elif choice == 4:
            statement()
        elif choice == 5:
            print("Thank you for using our services 🙏")
            break
        else:
            print("Invalid choice ❌")


bank()