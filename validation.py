def validate_username(username):
    return len(username) >= 3


def validate_password(password):
    return len(password) >= 6


def validate_phone(phone):
    return len(phone) == 11 and phone.isdigit()


def validate_amount(amount):
    return amount > 0


def validate_card_number(card_number):
    return len(card_number) == 16 and card_number.isdigit()


def validate_cvv(cvv):
    return len(cvv) == 3 and cvv.isdigit()