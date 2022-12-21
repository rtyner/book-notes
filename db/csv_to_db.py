#!/bin/env python3
import sqlite3
import csv

conn = sqlite3.connect('books.db')
cursor = conn.cursor()

with open('defs.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        words, definition, book = row
        cursor.execute('''
        INSERT INTO books(words, definition, book)
        VALUES (?, ?, ?)
    ''',(words,definition,book))
conn.commit()
conn.close()