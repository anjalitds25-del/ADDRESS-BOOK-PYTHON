
import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter postal address: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
        print("Address:", contact["address"])


def search_contact(contacts):
    name = input("Enter name to search: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("Contact found:")
            print(contact)
            return

    print("Contact not found.")


def update_contact(contacts):
    name = input("Enter name to update: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("Leave a field blank to keep its current value.")

            new_name = input("New name: ").strip()
            new_phone = input("New phone: ").strip()
            new_email = input("New email: ").strip()
            new_address = input("New address: ").strip()

            if new_name:
                contact["name"] = new_name
            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            save_contacts(contacts)
            print("Contact updated successfully.")
            return

    print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter name to delete: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            save_contacts(contacts)
            print("Contact deleted successfully.")
            return

    print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n===== ADDRESS BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank you for using Address Book!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
