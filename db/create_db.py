#!/usr/bin/env python3

import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE books (
        words TEXT,
        definition TEXT,
        book TEXT
    )
''')

conn.commit()
conn.close()