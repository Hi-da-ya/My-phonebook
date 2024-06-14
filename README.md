# My-phonebook
## Description

My phonebook is simply a contact managing application. It is a convinient was of keeping track of your contacts.

The application itself is built by python and it's a cli application. As a user you are able to create new contacts, delete and even update existing contacts. The application also has features that enable users to search for contacts by their names.

Below is an overview of how to run and use the application

## Technologies used
1. Python 
2. SQLITE 

## Installation and Setting up
1. **Clone this repository**:

```
git clone git@github.com:Hi-da-ya/My-phonebook.git
```

2.Navigate to this repository's directory
3. **Installing dependancies:** 
To install dependancies run ```pipenv install``` in your terminal

4. **Enter your virtual environment** by running ```pipenv shell```

5. **Start the application**: This is done by running ```python3 lib/cli.py``` in the terminal
Alternatively you can run ```chmod +x cli.py``` while in the lib directory of the application followed by ```./cli.py```


## Navigating the application
Once you start and run the application successfully, a list of options will be displayed and you can select an option of your choice:

```sh
===== My Phone book =====
Please select an option: 
1. View all contacts
2. Create new contact
3. Edit existing contact
4. Search contact by name
5. Delete existing contact
6. View list of contacts in a label
7. View all labels
8. Create new label
00. Exit
```
Have fun!!!