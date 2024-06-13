from . import cursor, conn
from .label import Label
import re

class Contact:
    all = {}

    def __init__(self, name, phone_no, label_id, id=None):
        self.id = id
        self.name = name
        self.phone_no = phone_no
        self.label_id = label_id

    def __repr__(self):
        return (
            f"<contact{self.id}: {self.name}, {self.phone_no}, " +
            f"label ID: {self.label_id}>"
        )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    
    @property
    def phone_no(self):
        return self._phone_no

    @phone_no.setter
    def phone_no(self, phone_no):
        if self.validate_number(phone_no):
            self._phone_no = phone_no
        else:
            raise ValueError("Invalid phone number format")

    def validate_number(self, phone_no):
        pattern = r'^\+?\d{1,3}\d{9}$'
        return re.match(pattern, str(phone_no)) is not None        

    @property
    def label_id(self):
        return self._label_id

    def label_id(self, label_id):
        if label_id is None:
            # Optionally, you can set a default label_id here
            self._label_id = None
        elif isinstance(label_id, int) and label_id in Label.search_by_id(label_id):
            self._label_id = label_id
        else:
            raise ValueError("label_id must reference a Label in the database or be None")

    #method to create contacts table
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Contact instances """
        sql = """
            CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone_no TEXT,
            label_id INTEGER,
            FOREIGN KEY (label_id) REFERENCES labels(id))
        """
        cursor.execute(sql)

        conn.commit()

    #method to delete contacts table
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Contact instances """
        sql = """
            DROP TABLE IF EXISTS contacts;
        """
        cursor.execute(sql)

        conn.commit()

    #method that saves the contact
    def save(self):
        sql = """
                INSERT INTO contacts (name, phone_no, label_id)
                VALUES (?, ?, ?)
        """

        cursor.execute(sql, (self.name, self.phone_no, self.label_id))

        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    #method that deletes a contact  
    def delete(self):
        """Delete the table row corresponding to the current Contact instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM contacts
            WHERE id = ?
        """

        cursor.execute(sql, (self.id,))

        conn.commit()

        del type(self).all[self.id]
        self.id = None

    #method to update a contact 
    def update(self):
        sql = """
            UPDATE contacts
            SET name = ?, phone_no = ?, label_id = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.phone_no, self.label_id, self.id))

        conn.commit() 

    #method that creates a new Contact instance and saves it to the database
    @classmethod
    def create(cls, name, phone_no, label_id):
        contact= cls(name, phone_no, label_id)
        contact.save()
        return contact 

    #method that retrieves data from the database
    @classmethod
    def from_db(cls, row):
        #Returns Contact object having the attribute values from the table row.
        # Check the dictionary for  existing instance using the row's primary key
        contact = cls.all.get(row[0])
        if contact:
            # ensure attributes match row values in case local instance was modified
            contact.name = row[1]
            contact.phone_no= row[2]
            contact.label_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            contact = cls(row[1], row[2], row[3])
            contact.id = row[0]
            cls.all[contact.id] = contact
        return contact
    
    #method that retrieves all contacts and displays them as a list
    @classmethod
    def view_all(cls):
        sql = """
            SELECT * FROM contacts
        """

        rows = cursor.execute(sql).fetchall()

        return [cls.from_db(row) for row in rows]
    
    #method that searches for a contact by name
    @classmethod
    def search_by_name(cls, name):
        sql = """
            SELECT * FROM contacts WHERE name = ?
        """

        row = cursor.execute(sql, (name,)).fetchone()
        return cls.from_db(row) if row else None
    
    @classmethod
    def search_by_id(cls, id):
        sql = """
            SELECT * FROM contacts WHERE id = ?
        """

        row = cursor.execute(sql, (id,)).fetchone()
        return cls.from_db(row) if row else None


Contact.create_table()