# create an empty list to store the name and phone
contacts = []

# create a function to add a contact to the list
def add_contacts(contacts):
    name = input ("Enter contact name: ")
    phone = input ("Enter contact phone: ")
    contact = {"name": name , "phone":phone}

    contacts.append(contact)
    print(f"✅ Contact {name} added successfully!")

# create a function to view contacts in the list in a numbered list
def view_contacts(contacts):
    if not contacts: 
        print("No contacts in the list")
    else: 
        print("📒 Contacts List:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")



while True :
    print("                                              ")
    print("----------------------------------------------")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Quit")

    choice= input("Enter your choice: ")

    if choice == "1":
        add_contacts(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        print("Bye Bye")
        break
    else:
        print("Please select a choice from 1 to 3")

