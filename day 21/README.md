
We will build:

* ✅ User Registration
* ✅ User Login
* ✅ JWT Token Generation
* ✅ Protected Route
* ✅ SQLite Database

---

# 📁 Project Structure

```
jwt_flask_app/
│
├── jwtt.py

```

---

# 🛠 Step 1: Install Required Packages

Open terminal inside project folder:

```bash
pip install flask flask-jwt-extended
```

Or create `requirements.txt`:

```
flask
flask-jwt-extended
```

Then run:

```bash
pip install -r requirements.txt
```

---

# 🗄 Step 2: Create `app.py`

Create a file named:

```
app.py
```

Paste this full working code:

```python
from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
import sqlite3
import datetime

app = Flask(__name__)

# Secret key for JWT
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

DATABASE = "database.db"


# ----------------------------
# Database Connection
# ----------------------------
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# ----------------------------
# Create Table
# ----------------------------
def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


create_table()


# ----------------------------
# Register User
# ----------------------------
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()

    try:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"message": "Username already exists"}), 400
    finally:
        conn.close()


# ----------------------------
# Login User
# ----------------------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, password)
    ).fetchone()
    conn.close()

    if user:
        access_token = create_access_token(
            identity=username,
            expires_delta=datetime.timedelta(hours=1)
        )
        return jsonify(access_token=access_token)

    return jsonify({"message": "Invalid credentials"}), 401


# ----------------------------
# Protected Route
# ----------------------------
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)


# ----------------------------
# Run App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
```

---

# ▶ Step 3: Run the Application

In terminal:

```bash
python jwtt.py
```

You should see:

```
Running on http://127.0.0.1:5000/
```

---

# 🧪 Step 4: Test Using Postman or Curl

---

## 🔹 Register User

**POST**

```
http://127.0.0.1:5000/register
```

Body (JSON):

```json
{
  "username": "admin",
  "password": "1234"
}
```

---

## 🔹 Login

**POST**

```
http://127.0.0.1:5000/login
```

Body:

```json
{
  "username": "admin",
  "password": "1234"
}
```

You will get:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJh..."
}
```

---

## 🔹 Access Protected Route

**GET**

```
http://127.0.0.1:5000/protected
```

Add Header:

```
Authorization: Bearer <your_token_here>
```

Response:

```json
{
  "logged_in_as": "admin"
}
```

---

# 🔐 How JWT Works (Step-by-Step)

1. User logs in
2. Server verifies credentials
3. Server creates JWT token
4. Client stores token
5. Client sends token in headers
6. Server verifies token before allowing access

---

# ⚠️ Important (Production Notes)

* ❌ Never store passwords as plain text
* ✅ Use `werkzeug.security.generate_password_hash`
* ✅ Use HTTPS
* ✅ Use environment variables for secret key

---

We use **JWT (JSON Web Token)** for **secure authentication and authorization** in web applications.

Let’s break it down clearly 👇

---

# 🔐 What is JWT?

JWT = **JSON Web Token**

It is a **compact, secure token** that is sent between client and server to prove identity.

Example JWT:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

It contains:

1. Header
2. Payload (user data)
3. Signature

---

# 🎯 Why We Use JWT

## 1️⃣ Stateless Authentication

Traditional method (Session-based):

* Server stores session in memory or database
* Client stores only session ID

JWT method:

* Server does NOT store session
* All user info is inside the token
* Server only verifies the signature

✔ Better for scalable systems
✔ No session storage needed

---

## 2️⃣ Secure Communication

JWT is digitally signed using a secret key.

If someone modifies the token:

👉 Signature verification fails
👉 Access denied

---

## 3️⃣ Perfect for APIs

JWT works very well with:

* REST APIs
* Mobile apps
* React / Angular frontend
* Microservices

Because:

* Token is sent in headers
* No cookies required

---

## 4️⃣ Works Across Domains

Sessions rely on cookies (same domain issues).
JWT works with:

```
Authorization: Bearer <token>
```

So it works easily between frontend and backend on different domains.

---

# 🔄 How JWT Works (Step-by-Step)

1. User logs in
2. Server verifies credentials
3. Server creates JWT
4. Client stores token
5. Client sends token in header:

   ```
   Authorization: Bearer <token>
   ```
6. Server verifies token
7. Access granted

---

# 📦 What’s Inside JWT?

Payload example:

```json
{
  "sub": "admin",
  "exp": 1712345678
}
```

It can contain:

* User ID
* Username
* Roles
* Expiry time

---

# ⚡ JWT vs Sessions

| Feature                | JWT       | Session      |
| ---------------------- | --------- | ------------ |
| Server storage         | ❌ No      | ✅ Yes        |
| Scalable               | ✅ Yes     | ⚠️ Harder    |
| Works for APIs         | ✅ Perfect | ❌ Less ideal |
| Easy for microservices | ✅ Yes     | ❌ No         |

---

# 🚀 When Should You Use JWT?

✅ REST APIs
✅ Mobile apps
✅ Microservices
✅ Single Page Applications (React, Angular, Vue)

---

# ⚠️ When NOT to Use JWT

❌ Very small apps
❌ Traditional server-rendered apps
❌ When you need instant logout (JWT is stateless)

---

# 🧠 Interview Answer (Short Version)

> We use JWT for stateless, secure authentication in APIs.
> It allows scalable systems without server-side session storage.


