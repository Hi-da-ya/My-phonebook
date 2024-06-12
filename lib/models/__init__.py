import sqlite3

#establishing a connection to the database 
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()