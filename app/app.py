from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="flaskdb"
    )

@app.route("/")
def home():
    return "Auto Deployment Working 🚀🚀"

@app.route("/db")
def db_check():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db = cursor.fetchone()
    cursor.close()
    conn.close()
    return f"Connected to database: {db[0]}"

@app.route("/add-user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True)

    if not data or "name" not in data or "email" not in data:
        return {"error": "Invalid JSON payload"}, 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (data["name"], data["email"])
    )
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "User added successfully"}

@app.route("/users")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/")
def home():
    return "Auto Deployment Working 🚀🚀"

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
=======
# ---------- DB CHECK ----------
@app.route("/db")
def db_check():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db = cursor.fetchone()
    cursor.close()
    conn.close()
    return f"Connected to database: {db[0]}"

# ---------- ADD USER ----------
@app.route("/add-user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True)

    if not data or "name" not in data or "email" not in data:
        return {"error": "Invalid JSON payload"}, 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s)",
        (data["name"], data["email"])
    )
    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "User added successfully"}

# ---------- GET USERS ----------
@app.route("/users", methods=["GET"])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

>>>>>>> af4dbfa (Add Flask MySQL CRUD APIs and update gitignore)
