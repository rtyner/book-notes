#!/usr/bin/env python3
import sqlite3
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

word = input("Enter the word: ")
definition = input("Enter the definition: ")
book = input("Enter the book: ")

cursor.execute("""
    INSERT INTO books(words, definition, book)
    VALUES (?, ?, ?)
""", (word, definition, book))

conn.commit()
conn.close()