import sqlite3


import sqlite3
entries = []

connection = sqlite3.connect("workdata.db")

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXIST entries (content TEXT, date TEXT);")

def add_entry(entry_content, entry_date):
    with connection:
        connection.execute("INSERT INTO entries VALUES ('Test Content', '09-09-2022');")

def get_entries():
    return entries 
