# -------------------------------
# 🏦 Simple ATM / Banking System
# -------------------------------

# Dictionary storing user account details
details = {
    "name": "pratyush",     # Account holder name
    "age": 19,              # Account holder age
    "pin": 1234,            # Secure PIN for authentication
    "balance": 1000000      # Initial account balance (₹)
}

# List to store transaction history (Deposit/Withdraw)
transaction_history = []


# -------------------------------
# 📌 Display current balance
# -------------------------------
def display_balance():
    # Shows available balance to the user
    print(f"Your current balance is: ₹{details['balance']}")


# -------------------------------
# 💰 Deposit money into account
# -------------------------------
def deposit_money():
    
    # Ask user for deposit amount
    amount = float(input("Enter the amount to deposit: "))
    
    # Ask for PIN BEFORE processing transaction
    pin = int(input("Enter your PIN to confirm deposit: "))
    
    if pin == details["pin"]:
        # Add amount only if PIN is correct
        details["balance"] += amount
        
        # Store transaction as tuple (type, amount)
        transaction_history.append(("Deposit", amount))
        
        print(f"₹{amount} deposited successfully.")
        print(f"New balance: ₹{details['balance']}")
    
    else:
        # Transaction cancelled if PIN is wrong
        print("PIN verification failed ❌ Deposit cancelled.")


# -------------------------------
# 💸 Withdraw money from account
# -------------------------------
def withdraw_money():
    
    # Ask user for withdrawal amount
    amount = float(input("Enter the amount to withdraw: "))
    
    # Check if sufficient balance is available
    if amount <= details["balance"]:
        
        # Ask for PIN BEFORE processing transaction
        pin = int(input("Enter your PIN to confirm withdrawal: "))
        
        if pin == details["pin"]:
            # Deduct amount only if PIN is correct
            details["balance"] -= amount
            
            # Store transaction
            transaction_history.append(("Withdraw", amount))
            
            print(f"₹{amount} withdrawn successfully.")
            print(f"New balance: ₹{details['balance']}")
        
        else:
            # Cancel if PIN is wrong
            print("PIN verification failed ❌ Withdrawal cancelled.")
    
    else:
        # Not enough balance
        print("Insufficient balance ❌")


# -------------------------------
# 📄 Print account statement
# -------------------------------
def statement():
    print("--- Account Statement ---")
    
    # Display user details
    print(f"Name: {details['name']}")
    print(f"Age: {details['age']}")
    print(f"Current Balance: ₹{details['balance']}")
    
    print("Transaction History:")
    
    # Check if any transactions exist
    if len(transaction_history) == 0:
        print("No transactions yet.")
    
    else:
        # Loop through transaction list
        for t in transaction_history:
            print(f"{t[0]}: ₹{t[1]}")


# -------------------------------
# 🖥️ Main menu-driven ATM system
# -------------------------------
def bank():
    print("Welcome to ABC Bank 🙏")
    
    # Infinite loop until user exits
    while True:
        print("1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")
        
        # Take user input for menu selection
        choice = int(input("Enter your choice: "))
        
        # Execute function based on choice
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
            break  # Exit program
        
        else:
            print("Invalid choice ❌ Please try again.")


# -------------------------------
#  Start the program
# -------------------------------
bank()
