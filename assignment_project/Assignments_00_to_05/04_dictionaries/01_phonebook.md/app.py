# Phonebook dictionary
phonebook = {}

while True:
    print("\nPhonebook Menu:")
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. Display all contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter contact name: ")
        number = input("Enter phone number: ")
        phonebook[name] = number
        print(f"Contact {name} added successfully!")

    elif choice == "2":
        name = input("Enter contact name to search: ")
        if name in phonebook:
            print(f"{name}: {phonebook[name]}")
        else:
            print(f"{name} not found in phonebook.")

    elif choice == "3":
        name = input("Enter contact name to delete: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Contact {name} deleted successfully!")
        else:
            print(f"{name} not found in phonebook.")

    elif choice == "4":
        if phonebook:
            print("\nPhonebook Contacts:")
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        else:
            print("Phonebook is empty.")

    elif choice == "5":
        print("Exiting phonebook. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")
