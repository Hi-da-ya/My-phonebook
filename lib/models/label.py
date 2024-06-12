from __init__ import cursor, conn

class Label:
    all = {}

    def __init__(self, name,  id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<label {self.id}: {self.name}>"

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

    #create labels table
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Label instances """
        sql = """
            CREATE TABLE IF NOT EXISTS labels (
            id INTEGER PRIMARY KEY,
            name TEXT
            )
        """
        cursor.execute(sql)

        conn.commit()

    #method to delete table
    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Label instances """
        sql = """
            DROP TABLE IF EXISTS labels;
        """
        cursor.execute(sql)

        conn.commit()

    def save(self):
        """ Insert a new row with the name values of the current label instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO labels (name)
            VALUES (?)
        """

        cursor.execute(sql, (self.name))

        conn.commit()

        self.id = cursor.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """ Initialize a new Label instance and save the object to the database """
        label = cls(name)
        label.save()
        return label
    
    #method to delete label
    def delete(self):
        """Delete the table row corresponding to the current label instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM labels WHERE id = ?
        """

        cursor.execute(sql, (self.id,))

        conn.commit() 
        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        self.id = None
    
    #method to update label
    def update(self):
        """Update the table row corresponding to the current label instance."""
        sql = """
            UPDATE labels
            SET name = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.name, self.id))
        conn.commit()

    
    
    #method that retrieves data from the database
    @classmethod
    def from_db(cls, row):
        #Returns Label object having the attribute values from the table row.
        # Check the dictionary for  existing instance using the row's primary key
        label = cls.all.get(row[0])
        if label:
            # ensure attributes match row values in case local instance was modified
            label.name = row[1]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            label = cls(row[1])
            label.id = row[0]
            cls.all[label.id] = label
        return label
    
    #method that retrieves all labels and displays them as a list
    @classmethod
    def view_all(cls):
        sql = """
            SELECT * FROM labels
        """

        rows = cursor.execute(sql).fetchall()

        return [cls.from_db(row) for row in rows]
    
    #method that searches for a label by name
    @classmethod
    def search_by_name(cls, name):
        sql = """
            SELECT * FROM labels WHERE name is ?
        """

        row = cursor.execute(sql, (name,)).fetchone()
        return cls.from_db(row) if row else None
    
    #method that returns a list of assosciated contacts
    def contacts(self):
        """Return list of contacts associated with current label"""
        from contact import Contact
        sql = """
            SELECT * FROM contacts
            WHERE label_id = ?
        """
        cursor.execute(sql, (self.id,),)

        rows = cursor.fetchall()
        return [Contact.from_db(row) for row in rows]
        
Label.create_table()