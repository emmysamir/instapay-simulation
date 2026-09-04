from auth import register, login, find_user, users
from operations import (
    show_balance,
    deposit,
    withdraw,
    link_card,
    transfer,
    show_transactions,
    show_last_5_transactions
)


while True:
    print("\n===== InstaPay =====")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        register()

    elif choice == "2":
        username = login()

        if username:
            user = find_user(username)

            while True:
                print("\n===== Main Menu =====")
                print("1. View Balance")
                print("2. Link Card")
                print("3. Deposit")
                print("4. Withdraw")
                print("5. Transfer")
                print("6. Transaction History")
                print("7. Last 5 Transactions")
                print("8. Logout")

                choice = input("Choose: ")

                if choice == "1":
                    show_balance(user)

                elif choice == "2":
                    link_card(user)

                elif choice == "3":
                    deposit(user)

                elif choice == "4":
                    withdraw(user)

                elif choice == "5":
                    recipient_username = input("Enter recipient username: ")

                    if recipient_username not in users:
                        print("Recipient does not exist.")

                    elif recipient_username == username:
                        print("You cannot transfer money to yourself.")

                    else:
                        recipient = find_user(recipient_username)
                        transfer(user, recipient)

                elif choice == "6":
                    show_transactions(user)

                elif choice == "7":
                    show_last_5_transactions(user)

                elif choice == "8":
                    print("Logged out successfully.")
                    break

                else:
                    print("Invalid choice.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")