# app.py

from flask import Flask, render_template, request
from database import init_db, check_user

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if check_user(username, password):
        return "Login Successful"
    else:
        return "Invalid Credentials"


if __name__ == "__main__":
    app.run(debug=True)
