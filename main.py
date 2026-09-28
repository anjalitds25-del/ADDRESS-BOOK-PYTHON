from contact_manager import add_contact, view_contacts, search_contacts, update_contact, delete_contact

def show_menu():
    print("\n========== ADDRESS BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("==================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you for using Address Book!")
            break
        else:
            print("Invalid choice. Please enter 1 to 6.")

if __name__ == "__main__":
    main()
