#lib/functionality.py
from models.contact import Contact
from models.label import Label

def create_contact():
    name = input("Enter name: ")
    phone_no = input("Enter phone number: ")
    label_id = input("Enter label id: ")
    try:
        contact = Contact.create(name, phone_no, label_id)
        print(f'Successfully created: {contact}')
    except Exception as e:
        print("An error occurred while creating contact: ", e)

def delete_contact():
    contact_id = input("Enter contact's id: ")
    if contact := Contact.search_by_id(contact_id):
        contact.delete()
        print (f"Contact with id {contact_id} successfull deleted")
    else:
        print(f'Contact with id {contact_id} not found!')

def update_contact():
    id_ = input("Enter the contact's id: ")
    if contact := Contact.search_by_id(id_):
        try:
            name = input("Enter the contacts's new name: ")
            contact.name = name
            phone_no= input("Enter the contact's new phone number: ")
            contact.phone_no= phone_no
            label_id = input("Enter the contacts's new label id: ")
            contact.label_id = label_id
            contact.update()
            print(f'Successfully updated: {contact}')
        except Exception as e:
            print("Error updating contact: ", e)
    else:
        print(f'contact {id} not found')

def find_contact_by_name():
    name = input("Enter the contact's name: ")
    contact = Contact.search_by_name(name)
    print(contact) if contact else print(
        f'contact {name} not found') 

def list_contacts():
    contacts = Contact.view_all()
    for contact in contacts:
        print(contact)

def list_label_contacts():
    name = input("Enter the label's name: ")
    if label := Label.search_by_name(name):
        for contact in label.contacts():
            print(contact)
    else:
        print(f'label {name} not found')

def list_label():
    label = Label.view_all()
    for label in label:
        print(label)


def find_label_by_name():
    name = input("Enter the label's name: ")
    label = Label.search_by_name(name)
    print(label) if label else print(
        f'label {name} not found')

def create_label():
    name = input("Enter the label's name: ")
    try:
        label = Label.create(name)
        print(f'Success: {label}')
    except Exception as exc:
        print("Error creating label: ", exc)


def update_label():
    id_ = input("Enter the label's id: ")
    if label := Label.search_by_id(id_):
        try:
            name = input("Enter the label's new name: ")
            label.name = name
            label.update()
            print(f'Success: {label}')
        except Exception as exc:
            print("Error updating label: ", exc)
    else:
        print(f'label {id_} not found')


def delete_label():
    id_ = input("Enter the label's id: ")
    if label := Label.find_by_id(id_):
        label.delete()
        print(f'label {id_} deleted')
    else:
        print(f'label {id_} not found')

def exit_program():
    print("Exiting program.....")
    exit()        
