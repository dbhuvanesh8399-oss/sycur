from flask import Flask, request
import sqlite3
import subprocess
import os

app = Flask(__name__)

# 1. Hardcoded credentials
USERNAME = "admin"
PASSWORD = "admin123"

# 2. SQL Injection vulnerability
@app.route("/user")
def get_user():
    user_id = request.args.get("id")

    conn = sqlite3.connect("test.db")
    query = "SELECT * FROM users WHERE id = " + user_id

    result = conn.execute(query).fetchall()
    conn.close()

    return str(result)


# 3. Command Injection vulnerability
@app.route("/ping")
def ping():
    host = request.args.get("host")

    result = subprocess.getoutput("ping -c 1 " + host)

    return result


# 4. Cross-Site Scripting (XSS)
@app.route("/search")
def search():
    keyword = request.args.get("q")

    return f"<h1>Search Result: {keyword}</h1>"


# 5. Debug mode enabled
if __name__ == "__main__":
    app.run(debug=True)
