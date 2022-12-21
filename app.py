#!/usr/bin/env python3

from flask import Flask, render_template
import requests
import sqlite3
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('db/books.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    temp = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('templates/index.html', books=book)