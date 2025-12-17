🧾 Expense Manager

A menu-driven Expense & Wallet Management System built using Object-Oriented Programming (OOP) principles in Python.
This project simulates a real-world expense tracking application with users, wallets, transactions, payments, and reports.

🚀 Features

👤 User Management

Regular & Premium users
Premium users get cashback benefits

💰 Wallet System

Encapsulated balance handling
Income & Expense transactions

💳 Payment System

Multiple payment methods (UPI, Card, Cash)
Wallet balance deduction
Polymorphic payment handling

📊 Reports & Analytics

Console-based wallet report
Total income, expenses, and balance
Detailed transaction summary

🧭 Menu-Driven CLI

User-friendly command-line interface
Dynamic user creation & operations

📂 Project Structure

expense_manager/
│
├── wallet/
│   ├── wallet.py
│   └── transaction.py
│
├── users/
│   ├── user.py
│   ├── regular_user.py
│   └── premium_user.py
│
├── payments/
│   ├── payment.py
│   ├── upi.py
│   ├── card.py
│   └── cash.py
│
├── reports/
│   ├── report.py
│   └── console_report.py
│
├── main.py
├── README.md
└── .gitignore

▶️ How to Run the Project

1️⃣ Clone the Repository
git clone https://github.com/ashishshukla5/expense-manager.git
cd expense-manager

2️⃣ Run the Application
python main.py

🧪 Sample Workflow

Create a user (Regular or Premium)
Add income and expense transactions
Make payments using UPI/Card/Cash
Apply cashback (Premium users only)
Generate wallet report

💼 Why This Project Matters

Designed using real-world architecture
Follows industry-standard OOP practices
Clean commit history & modular structure

Easily extendable to:
CSV/JSON persistence
Database integration
REST APIs (FastAPI/Django)

🔮 Future Enhancements

CSV export of transactions
File/database persistence
Unit testing
Authentication & authorization
REST API version

👨‍💻 Author

Ashish Shukla
Final Year B.Tech Student

⭐ If you like this project
Give it a ⭐ on GitHub and feel free to fork & extend it!