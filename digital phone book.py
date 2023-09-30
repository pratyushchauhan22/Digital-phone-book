# Define a dictionary to store contacts
phone_book = {}

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    phone_book[name] = number
    print(f"Contact '{name}' added successfully!")

def search_contact():
    name = input("Enter contact name to search: ")
    if name in phone_book:
        print(f"Name: {name}, Number: {phone_book[name]}")
    else:
        print(f"Contact '{name}' not found in the phone book.")

def display_contacts():
    if phone_book:
        print("Contacts in the phone book:")
        for name, number in phone_book.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("The phone book is empty.")

def main_menu():
    while True:
        print("\nDigital Phone Book Menu:")
        print("1. Add a Contact")
        print("2. Search for a Contact")
        print("3. Display All Contacts")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            display_contacts()
        elif choice == "4":
            print("Exiting the Phone Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

