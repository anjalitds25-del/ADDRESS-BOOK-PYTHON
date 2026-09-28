def valid_name(name):
    return bool(name.strip()) and all(ch.isalpha() or ch.isspace() for ch in name)

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def valid_email(email):
    return "@" in email and "." in email.split("@")[-1]
