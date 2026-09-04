from validation import validate_amount, validate_card_number, validate_cvv


def show_balance(user):
    print("Current Balance:", user["balance"], "EGP")


def deposit(user):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    if validate_amount(amount):
        user["balance"] += amount

        user["transactions"].append({
            "type": "Deposit",
            "amount": amount
        })

        print("Deposit successful!")
        print("New Balance:", user["balance"], "EGP")
    else:
        print("Invalid amount. Amount must be greater than 0.")


def withdraw(user):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    if not validate_amount(amount):
        print("Invalid amount. Amount must be greater than 0.")
        return

    if amount > user["balance"]:
        print("Insufficient balance.")
        return

    user["balance"] -= amount

    user["transactions"].append({
        "type": "Withdraw",
        "amount": amount
    })

    print("Withdrawal successful!")
    print("Remaining Balance:", user["balance"], "EGP")


def link_card(user):
    card_number = input("Enter card number: ")
    card_holder = input("Enter card holder name: ")
    expiry_date = input("Enter expiry date: ")
    cvv = input("Enter CVV: ")

    if not validate_card_number(card_number):
        print("Invalid card number.")
        return

    if not validate_cvv(cvv):
        print("Invalid CVV.")
        return

    user["card"] = {
        "card_number": card_number,
        "card_holder": card_holder,
        "expiry_date": expiry_date,
        "cvv": cvv
    }

    print("Card linked successfully!")


def transfer(user, recipient):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    if not validate_amount(amount):
        print("Invalid amount.")
        return

    if amount > user["balance"]:
        print("Insufficient balance.")
        return

    confirmation = input("Confirm transfer? (yes/no): ")

    if confirmation.lower() != "yes":
        print("Transfer cancelled.")
        return

    user["balance"] -= amount
    recipient["balance"] += amount

    user["transactions"].append({
        "type": "Transfer",
        "amount": amount,
        "to": recipient["username"]
    })

    recipient["transactions"].append({
        "type": "Received",
        "amount": amount,
        "from": user["username"]
    })

    print("Transfer successful!")
    print("Your new balance:", user["balance"], "EGP")


def show_transactions(user):
    print("\n===== Transaction History =====")

    if len(user["transactions"]) == 0:
        print("No transactions yet.")
        return

    for transaction in user["transactions"]:
        print(transaction)


def show_last_5_transactions(user):
    print("\n===== Last 5 Transactions =====")

    if len(user["transactions"]) == 0:
        print("No transactions yet.")
        return

    last_transactions = user["transactions"][-5:]

    for transaction in last_transactions:
        print(transaction)