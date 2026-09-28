from storage import load_contacts, save_contacts
from validation import valid_name, valid_phone, valid_email

def get_contact_details():
    while True:
        name = input("Enter name: ").strip()
        if valid_name(name):
            break
        print("Please enter a valid name.")

    while True:
        phone = input("Enter 10-digit phone number: ").strip()
        if valid_phone(phone):
            break
        print("Phone number must contain exactly 10 digits.")

    while True:
        email = input("Enter email: ").strip()
        if valid_email(email):
            break
        print("Please enter a valid email.")

    address = input("Enter postal address: ").strip()
    return {"name": name, "phone": phone, "email": email, "address": address}

def add_contact():
    contacts = load_contacts()
    contacts.append(get_contact_details())
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return
    for i, contact in enumerate(contacts, 1):
        print(f"\nContact {i}")
        print(f"Name    : {contact['name']}")
        print(f"Phone   : {contact['phone']}")
        print(f"Email   : {contact['email']}")
        print(f"Address : {contact['address']}")

def search_contacts():
    contacts = load_contacts()
    keyword = input("Enter name or phone to search: ").strip().lower()
    results = [c for c in contacts if keyword in c["name"].lower() or keyword in c["phone"]]
    if not results:
        print("No matching contact found.")
        return
    for c in results:
        print(f"{c['name']} | {c['phone']} | {c['email']} | {c['address']}")

def update_contact():
    contacts = load_contacts()
    name = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contact.update(get_contact_details())
            save_contacts(contacts)
            print("Contact updated successfully!")
            return
    print("Contact not found.")

def delete_contact():
    contacts = load_contacts()
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")
