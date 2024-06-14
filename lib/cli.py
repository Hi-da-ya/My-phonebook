#lib/cli.py
from functionality import (
    list_contacts,
    create_contact,
    update_contact,
    delete_contact,
    find_contact_by_name,
    list_label_contacts,
    list_label,
    create_label,
    exit_program,
    delete_label,
    update_label
)
def main():
    while True:
        options()
        choice = input("> ")
        if choice == "1":
            list_contacts()
        elif choice == "2":
            create_contact()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            find_contact_by_name()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            list_label_contacts()
        elif choice == "7":
            list_label()
        elif choice == "8":
            create_label()
        elif choice == "00":
            exit_program()            
        else:
            print("Invalid choice!!!")


def options():
    print("=====My Phone book=====")
    print("Please select an option: ")
    print("1. View all contacts")
    print("2. Create new contact")
    print("3. Edit existing contact")
    print("4. Search contact by name")
    print("5. Delete existing contact")
    print("6. View list of contacts in a label")
    print("7. View all labels")
    print("8. Create new label")
    print("00. Exit")

                              
                

if __name__ == "__main__":
    main()