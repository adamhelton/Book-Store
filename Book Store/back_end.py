import sqlite3

def connect():
    conn = sqlite3.connect('books.db')
    cur = conn.cusor()
    cur.execute('CREATE TABLE IF NOT EXISTS BOOK (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    cur = conn.cusor()
    cur.execute('INSERT INTO book VALUES (NULL, ?,?,?,?,)', (title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    cur = conn.cusor()
    cur.execute('SELECT * FROM book')
    rows = cur.fetchall()
    conn.close()
    return rows

connect()
insert('The Sea', 'Adam Helton', 2019, 80748592738)
print(view)

