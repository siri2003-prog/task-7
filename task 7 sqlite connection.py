Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import sqlite3
>>> conn = sqlite3.connect("school.db")
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    conn = sqlite3.connect("school.db")
sqlite3.OperationalError: unable to open database file
>>> cursor = conn.cursor()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    cursor = conn.cursor()
NameError: name 'conn' is not defined
>>> cursor.execute('''CREATE TABLE IF NOT EXSISTS schoolstudent(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER)''')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cursor.execute('''CREATE TABLE IF NOT EXSISTS schoolstudent(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER)''')
NameError: name 'cursor' is not defined
>>> data = [("john", 23),("joe", 25)]
>>> cursor.executemany('''INSERT INTO schoolstudent (name, age) VALUES (?,?)''',data)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    cursor.executemany('''INSERT INTO schoolstudent (name, age) VALUES (?,?)''',data)
NameError: name 'cursor' is not defined
>>> cursor.executemany('''INSERT INTO schoolstudent (name, age) VALUES (?,?)''', data)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    cursor.executemany('''INSERT INTO schoolstudent (name, age) VALUES (?,?)''', data)
NameError: name 'cursor' is not defined
>>> conn.commit()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    conn.commit()
NameError: name 'conn' is not defined
>>> conn.close()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    conn.close()
NameError: name 'conn' is not defined
>>> [DEBUG ON]
>>> [DEBUG OFF]
