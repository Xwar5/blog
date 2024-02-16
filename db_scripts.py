<<<<<<< HEAD
import sqlite3

db_name = "blog.db"
connection = None
cursor = None

def open():
    global connection, cursor
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

def close():
    cursor.close()
=======
import sqlite3

db_name = "blog.db"
connection = None
cursor = None

def open():
    global connection, cursor
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

def close():
    cursor.close()
>>>>>>> 3d399c182aa2fba67db394bd7d5d440955ae7326
    connection.close()