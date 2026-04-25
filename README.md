# 🏦 ATM Banking System (Python CLI Project)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Project](https://img.shields.io/badge/Level-Beginner-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📝 Project Overview

The **ATM Banking System** is a simple command-line application built using Python that simulates basic ATM functionalities.  
Users can securely perform operations like checking account balance, depositing money, withdrawing money, and viewing transaction history using PIN authentication.

This project is ideal for beginners to understand how real-world systems can be modeled using programming.

---

## 🎯 Objectives

- Apply Python fundamentals to a real-world scenario  
- Understand menu-driven program structure  
- Learn how to manage data using dictionaries and lists  
- Implement basic authentication logic (PIN system)  

---

## 🚀 Features

- 🔐 Secure PIN verification before transactions  
- 💰 Deposit money into account  
- 💸 Withdraw money with balance validation  
- 📊 Check current account balance  
- 📄 View complete transaction history  
- 🖥️ User-friendly command-line interface  

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Core Concepts:**
  - Functions  
  - Lists & Dictionaries  
  - Conditional Statements  
  - Loops  

---
## 📂 Project Structure

atm-system/
│── main.py # Main ATM program
│── README.md # Project documentation


---

## ⚙️ How the System Works

### 👤 Account Information
User account details are stored in a dictionary:


details = {
"name": "pratyush",
"age": 19,
"pin": 1234,
"balance": 1000000
}


---

### 💰 Deposit Operation

1. User enters deposit amount  
2. System asks for PIN  
3. If PIN is correct:
   - Amount is added to balance  
   - Transaction is recorded  

---

### 💸 Withdrawal Operation

1. User enters withdrawal amount  
2. System checks available balance  
3. User enters PIN  
4. If valid:
   - Amount is deducted  
   - Transaction is recorded  

---

### 📄 Transaction History

Transactions are stored in a list:

transaction_history = []


Each transaction is saved as:

("Deposit", amount)
("Withdraw", amount)


---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

git clone https://github.com/Pratyush235936/atm-system.git


### 2️⃣ Navigate to Project Folder

cd atm-system


### 3️⃣ Run the Program

python main.py


---

## 🖥️ Application Menu

Display Balance
Deposit Money
Withdraw Money
Statement
Exit

---

## 🔒 Security Note

- PIN is required before any transaction  
- However, PIN is currently hardcoded and visible in code  
- This project is for **learning purposes only**, not for real banking use  

---

## ⚠️ Limitations

- ❌ Supports only one user account  
- ❌ No data persistence (data resets after program exit)  
- ❌ No limit on incorrect PIN attempts  
- ❌ No encryption or advanced security  

---

## 📌 Future Enhancements

- 🔐 Add PIN attempt limit and account lock  
- 👥 Support multiple users  
- 💾 Store data using files or databases  
- 🧱 Convert to Object-Oriented Programming (OOP)  
- 🖼️ Add graphical interface (Tkinter)  
- 📊 Add transaction timestamps  

---

## 🧠 Learning Outcomes

- Build real-world simulation using Python  
- Practice structured programming  
- Understand basic authentication logic  
- Improve problem-solving skills  

---

## 👨‍💻 Author

**Pratyush Yadav**  
🔗 GitHub: https://github.com/Pratyush235936  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support & Contribution

If you found this project helpful:

- ⭐ Star the repository  
- 🍴 Fork the project  
- 🛠️ Suggest improvements  

---

## 💬 Feedback

Feel free to open issues or contribute to improve this project!
