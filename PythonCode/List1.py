import pyodbc 
id1 = '0012w000002umTFAAY'
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LATITUDEWB;'
                      'Database=Practise;')               
cursor = conn.cursor()
data=list(cursor.execute('SELECT top 10 Id FROM dbo.SF_TGT'))
idList =[]  
for id in data:
     list.append(idList,id[0])
print(id1   in idList)
