from flask import Flask, jsonify, request
from flask_cors import CORS
import projectdb

app = Flask(__name__)
CORS(app)

@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    if not username or not email or not password:
        return {"error": "Missing fields"}, 400
    projectdb.signUp(username, email, password)
    return {"success": True, "message": "User signed up successfully"}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    if not email or not password:
        return {"error": "Missing feilds"}, 400
    projectdb.logIn(email, password)
    user = projectdb.mycursor.fetchone()
    if user:
        return {"success": True, "message": "Login successful", "user": {"username": user[1], "email": user[2]}}
    else:
        return {"error": "Invalid email or password"}, 401
    
@app.route("/add", methods=["POST"])
def add_transaction():
    data = request.get_json()
    amount = data.get("amount")
    description = data.get("description")
    category = data.get("category")
    date = data.get("date")
    user_id = data.get("user_id")
    if not amount or not category or not date:
        return {"error": "Missing fields"}, 400
    projectdb.add_transaction(user_id, amount, description, category, date)

if __name__ == "__main__":
    app.run(debug=True)