# Simple In-Memory Contact Manager
# No files or JSON - data resets when program ends

contacts = []  # List to hold contacts as dicts

def add_contact():
    name = input("Enter name: ").strip()
    if not name:
        print("Name can't be empty!")
        return
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()
    
    contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
    contacts.append(contact)
    print(f"Added {name}!")

def view_contacts():
    if not contacts:
        print("No contacts yet.")
        return
    print("\n--- Your Contacts ---")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']} ({c['email']})")
        print(f"   Address: {c['address']}\n")

def search_contacts():
    if not contacts:
        print("No contacts.")
        return
    query = input("Search by name or phone: ").strip().lower()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone'].lower()]
    if not found:
        print("Nothing found.")
        return
    print("\n--- Matches ---")
    for i, c in enumerate(found, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

def update_contact():
    view_contacts()
    if not contacts:
        return
    try:
        idx = int(input("Pick number to update: ")) - 1
        if 0 <= idx < len(contacts):
            c = contacts[idx]
            print(f"Updating {c['name']}")
            new_name = input(f"Name ({c['name']}): ").strip()
            if new_name: c['name'] = new_name
            new_phone = input(f"Phone ({c['phone']}): ").strip()
            if new_phone: c['phone'] = new_phone
            new_email = input(f"Email ({c['email']}): ").strip()
            if new_email: c['email'] = new_email
            new_addr = input(f"Address ({c['address']}): ").strip()
            if new_addr: c['address'] = new_addr
            print("Updated!")
        else:
            print("Bad pick.")
    except ValueError:
        print("Enter a number.")

def delete_contact():
    view_contacts()
    if not contacts:
        return
    try:
        idx = int(input("Pick number to delete: ")) - 1
        if 0 <= idx < len(contacts):
            removed = contacts.pop(idx)
            print(f"Deleted {removed['name']}.")
        else:
            print("Bad pick.")
    except ValueError:
        print("Enter a number.")

# Main Loop
while True:
    print("\n1. Add | 2. View | 3. Search | 4. Update | 5. Delete | 6. Quit")
    choice = input("Choice: ").strip()
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contacts()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Bye!")
        break
    else:
        print("Try 1-6.")