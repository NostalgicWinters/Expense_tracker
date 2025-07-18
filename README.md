# 💸 Expense Tracker

A simple web-based expense tracking API built using **Flask** and **MySQL**. This application allows users to sign up, log in, and manage their financial transactions, including viewing, adding, deleting, and searching by category.

---

## 📚 Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Database Schema](#database-schema)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

---

## 📖 Introduction

This project is a backend service for tracking personal expenses. It supports:

- User authentication (sign up & login)
- Adding and deleting transactions
- Viewing all transactions per user
- Filtering transactions by category
- Automatic balance updates with each transaction

---

## ✨ Features

- RESTful API using Flask
- Persistent MySQL database
- CORS-enabled for frontend integration
- Secure user registration & login
- Search and filter expense records by category

---

## 🛠 Installation

### Prerequisites

- Python 3.7+
- MySQL Server
- `pip` package manager

### Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/NostalgicWinters/Expense_tracker.git
   cd Expense_tracker
2. **Install dependencies**
```bash
pip install flask flask-cors pymysql
```
3. **Set up MySQL Database**
Create a database named expense_manager and the required tables (see Database Schema).
4. **Run the server**
```bash
python server.py
```

