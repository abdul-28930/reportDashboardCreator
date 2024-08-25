import sqlite3
import hashlib

def create_connection():
    conn = sqlite3.connect('quiz_users.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT
                    )''')
    conn.commit()
    return conn

def hash_password(password):
    # using SHA-256 to hash the pass
    return hashlib.sha256(password.encode()).hexdigest()

def register():
    conn = create_connection()
    cursor = conn.cursor()

    username = input("Enter a username: ")
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    if cursor.fetchone():
        print("Username already exists. Please choose another one.")
        return

    password = input("Enter a password: ")
    hashed_password = hash_password(password)

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    print("Account created successfully!")

def login():
    conn = create_connection()
    cursor = conn.cursor()

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
    if cursor.fetchone():
        print(f"Welcome back, {username}!")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

def main():
    print("1. Register")
    print("2. Login")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        username = login()
        if username:
            print(f"You are logged in as {username}")
            return username
    else:
        print("Invalid choice.")
    return None

if __name__ == "__main__":
    main()
