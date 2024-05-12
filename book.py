import os
import fnmatch

def print_separator():
    print("=" * 50)

def print_header(header_text):
    print_separator()
    print(f"{header_text.center(50)}")
    print_separator()

def contact_book_menu():
    print_header(" CONTACT BOOK MENU ")
    print("[1] Add New Contact")
    print("[2] View Contacts")
    print("[3] Modify Contact")
    print("[4] Delete Contact")
    print("[5] Exit")
    print_separator()
    cb_menu = input("Please select an option from the menu >>  ")

    if cb_menu == "1":
        cb_add_new()
    elif cb_menu == "2":
        cb_view_menu()
    elif cb_menu == "3":
        cb_modify()
    elif cb_menu == "4":
        cb_delete()
    elif cb_menu == "5":
        exit("Thank you for using the Contact Book. Have a great day!")
    else:
        print("Invalid option. Please select a number from 1 to 5.")
        contact_book_menu()

def cb_view_menu():
    print_header(" VIEW CONTACTS ")
    print("[1] Search by Name")
    print("[2] View Entire Directory")
    print_separator()
    category = input("Select an option >> ")

    if category == "1":
        cb_search_name()
    elif category == "2":
        cb_view_directory()
    else:
        print("Invalid option. Please select either 1 or 2.")
        cb_view_menu()

def cb_add_new():
    print_header(" ADD NEW CONTACT ")
    l_name = input("Last Name: ")
    f_name = input("First Name: ")
    if os.path.exists(l_name + " " + f_name + ".txt"):
        print("Contact already exists. Do you want to update it?")
        overwrite = input("Yes [Y] / No [N]: ").lower()

        if overwrite == "y":
            print("Please enter new contact information:")
        elif overwrite == "n":
            print("Operation canceled.")
            return
        else:
            print("Invalid option. Operation canceled.")
            return

    mid_name = input("Middle Name: ")
    m_number = input("Mobile Number: ")
    department = input("Department: ")
    email_add = input("Email Address: ")
    lines = [f_name, mid_name, l_name, department, m_number, email_add]
    with open(l_name + " " + f_name + '.txt', "w") as file_handler:
        for line in lines:
            file_handler.write(f'{line}\n')
    print("Contact added successfully!")
    print_separator()

def cb_search_name():
    print_header(" SEARCH CONTACT BY NAME ")
    l_name = input("Last Name: ")
    f_name = input("First Name: ")
    filename = l_name + " " + f_name + ".txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            contact_info = file.readlines()
            print("Contact Found:")
            for line in contact_info:
                print(line.strip())
    else:
        print("Contact not found.")
    print_separator()

def cb_view_directory():
    print_header(" VIEW ENTIRE DIRECTORY ")
    contacts = [file for file in os.listdir('.') if fnmatch.fnmatch(file, '*.txt')]
    if contacts:
        print("Contacts in the Directory:")
        for contact in contacts:
            print(contact)
        print(f"Total contacts: {len(contacts)}")
    else:
        print("No contacts found in the directory.")
    print_separator()

def cb_modify():
    print_header(" MODIFY CONTACT ")
    l_name = input("Last Name: ")
    f_name = input("First Name: ")
    filename = l_name + " " + f_name + ".txt"
    if os.path.exists(filename):
        with open(filename, "r+") as file:
            contact_info = file.readlines()
            print("Current Contact Information:")
            for line in contact_info:
                print(line.strip())
            print_separator()
            field_to_modify = input("Enter the number of the field to modify >> ")
            if field_to_modify.isdigit() and 1 <= int(field_to_modify) <= 6:
                new_value = input("Enter the new value: ")
                contact_info[int(field_to_modify) - 1] = new_value + "\n"
                file.seek(0)
                file.truncate()
                file.writelines(contact_info)
                print("Contact information updated successfully!")
            else:
                print("Invalid field number.")
    else:
        print("Contact not found.")
    print_separator()

def cb_delete():
    print_header(" DELETE CONTACT ")
    l_name = input("Last Name: ")
    f_name = input("First Name: ")
    filename = l_name + " " + f_name + ".txt"
    if os.path.exists(filename):
        os.remove(filename)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")
    print_separator()

while True:
    contact_book_menu()
