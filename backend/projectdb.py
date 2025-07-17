import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="sql@3000",
    database="expense_manager"
)

mycursor = mydb.cursor()

def signUp(username, email, password, balance):
    mycursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
    mydb.commit()
    user_id = mycursor.lastrowid
    mycursor.execute("INSERT INTO balance (user_id, balance) VALUES (%s,%s)",(user_id,balance))
    mydb.commit()
    return user_id

def logIn(email, password):
    mycursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (email, password))
    return mycursor.fetchone()

def add_transaction(user_id, amount, description, category, date):
    mycursor.execute("INSERT INTO transactions (user_id, amount, description, category, date) VALUES (%s, %s, %s, %s, %s)", (user_id, amount, description, category, date))
    mydb.commit()
    mycursor.execute("UPDATE balance SET balance = balance + %s WHERE user_id = %s",(amount,user_id))
    mydb.commit()

def delete_transaction(transaction_id, amount, user_id):
    mycursor.execute("DELETE FROM transactions WHERE id=%s", (transaction_id,))
    mydb.commit()
    mycursor.execute("UPDATE balance SET balance = balance - %s WHERE user_id = %s",(amount,user_id))   
    mydb.commit()

def view_transactions(user_id):
    mycursor.execute("SELECT * FROM transactions WHERE user_id=%s", (user_id,))
    return mycursor.fetchall() 

def search_transactions(user_id, category):
    if category is None:
        mycursor.execute("SELECT * FROM transactions WHERE user_id=%s", (user_id,))
    else:
        mycursor.execute("SELECT * FROM transactions WHERE user_id=%s AND category=%s", (user_id, category))
    return mycursor.fetchall()