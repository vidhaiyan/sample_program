import sqlite3
import os

def create_connection(db_file):
    """ Create a database connection to the SQLite database specified by db_file.
        :param db_file: database file
        :return: Connection object or None
    """
    connection = None
    try:
        if os.path.exists(db_file):
            print(db_file)
            connection = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
            return connection
        else:
            print("Database file does not exist")
            return None
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

create_connection()