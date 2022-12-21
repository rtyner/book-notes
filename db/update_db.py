#!/usr/bin/env python3
import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO books (words, definition, book)
    VALUES (?, ?, ?)
''',('denouement', 'the climax of a chain of events, usually when something something is decided', 'crime and punishment'))

conn.commit()
conn.close()