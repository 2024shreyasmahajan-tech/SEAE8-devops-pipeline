# Login module

users = {
    "admin@caresync.com": "admin123",
    "staff@caresync.com": "staff123"
}

def login(email, password):
    if email in users and users[email] == password:
        return True
    return False


# Login validation
if __name__ == "__main__":
    email = input("Enter email: ")
    password = input("Enter password: ")

    if login(email, password):
        print("Login successful!")
    else:
        print("Invalid email or password.")
