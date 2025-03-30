# Contact management system

contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    search = input("Enter name or phone number to search: ")
    found_contacts = [c for c in contacts if search in c['name'] or search in c['phone']]
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"{contact['name']} - {contact['phone']} - {contact['email']} - {contact['address']}")
    else:
        print("No matching contact found.")

def update_contact():
    search = input("Enter name or phone number to update: ")
    for contact in contacts:
        if search in contact['name'] or search in contact['phone']:
            print("Contact found. Enter new details (leave blank to keep current value):")
            contact['name'] = input(f"Name ({contact['name']}): ") or contact['name']
            contact['phone'] = input(f"Phone ({contact['phone']}): ") or contact['phone']
            contact['email'] = input(f"Email ({contact['email']}): ") or contact['email']
            contact['address'] = input(f"Address ({contact['address']}): ") or contact['address']
            print("Contact updated successfully!")
            return
    print("No matching contact found.")

def delete_contact():
    search = input("Enter name or phone number to delete: ")
    for contact in contacts:
        if search in contact['name'] or search in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("No matching contact found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
