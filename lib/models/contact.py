from __init__ import cursor, conn

class Contact:
    all = {}

    #create contacts table
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
Contact.create_table()