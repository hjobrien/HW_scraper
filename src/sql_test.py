import sqlite3

conn = sqlite3.connect('main copy.db')
c = conn.cursor()

# c.execute('''CREATE TABLE foo (bar real, baz real, buzz real)''')
# c.execute("INSERT INTO foo VALUES (3,4,5)")

params = (30111307098, 0, 0, 0, None, None, 0, None, 17191, 0, None, 0, None,
          'notification ID', 1, None, 43200.0, 30110954415, 1, None, 'Test', None)

#                                         (30111307097, 0, 0, 0, None, None, 0, '2,3,4,5,12,19,25,29,32,34,36,41,42,43,44,61,63,65,66', 17191, None, None, None, None, 'PV2skO0927I#ldwdSYm9L', 1, None, 43200.0, 30110954415, 1, None, '10.2', None)
c.execute("INSERT INTO assignments VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", params)

conn.commit()

for row in c.execute('SELECT * FROM assignments'):
    print(row)

conn.close()
