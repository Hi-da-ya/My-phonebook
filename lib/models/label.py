from __init__ import cursor, conn

class Label:
    all = {}

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
Label.create_table()