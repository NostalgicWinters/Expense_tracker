import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="sql@3000",
    database="expense_manager"
)

mycursor = mydb.cursor()

def signUp(username, email, password):
    mycursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    mydb.commit()

def logIn(email, password):
    mycursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    return mycursor.fetchone()

def add_transaction(user_id, amount, description, category, date):
    mycursor.execute("INSERT INTO transactions (user_id, amount, description, category, date) VALUES (%s, %s, %s, %s, %s)", (user_id, amount, description, category, date))
    mydb.commit()

def delete_transaction(transaction_id):
    mycursor.execute("DELETE FROM transactions WHERE id=%s", (transaction_id,))
    mydb.commit()    