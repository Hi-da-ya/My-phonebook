from __init__ import cursor, conn
from label import Label

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
        if isinstance(phone_no, int) and len(phone_no):
            self._phone_no = phone_no
        else:
            raise ValueError(
                "phone_no must be an integer"
            )

    @property
    def label_id(self):
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        if type(label_id) is int and Label.find_by_id(label_id):
            self._label_id = label_id
        else:
            raise ValueError(
                "label_id must reference a Label in the database")

    #method to create contacts table
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Contact instances """
        sql = """
            CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY,
            name TEXT,
            phone_no INTEGER,
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

    

Contact.create_table()