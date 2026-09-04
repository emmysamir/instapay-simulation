from validation import validate_username, validate_password, validate_phone

users = {}


def register():
    name = input("Enter your name: ")
    phone = input("Enter your phone: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not validate_phone(phone):
        print("Invalid phone number.")
        return

    if not validate_username(username):
        print("Username must be at least 3 characters.")
        return

    if not validate_password(password):
        print("Password must be at least 6 characters.")
        return

    if username in users:
        print("Username already exists.")
        return

    users[username] = {
        "username": username,
        "name": name,
        "phone": phone,
        "password": password,
        "balance": 0,
        "card": None,
        "transactions": []
    }

    print("Registration successful!")


def login():
    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username]["password"] == password:
            print("Login successful! Welcome", users[username]["name"])
            return username

        attempts -= 1
        print("Invalid username or password.")

        if attempts > 0:
            print("Attempts remaining:", attempts)

    print("Too many failed attempts.")
    return None


def find_user(username):
    if username in users:
        return users[username]

    return None