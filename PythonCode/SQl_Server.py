import pyodbc
conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=Practise;'
                          'Trusted_Connection=yes;')
cursor = conn.cursor()
print('connected')
cursor = conn.cursor()
cursor.execute('SELECT * FROM EMP')
rows=cursor.fetchall()
#print(str(cursor.description))
for i in cursor.description:
    print(list(i)[0])
for row in rows:
    #print(row)
    pass