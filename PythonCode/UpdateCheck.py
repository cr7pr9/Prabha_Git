import pyodbc 
id1 = '0012w000002umTFAAY'
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LATITUDEWB;'
                      'Database=Practise;')               
cursor = conn.cursor()
data=list(cursor.execute('SELECT  Id FROM dbo.SF_TGT'))

idList =[]  
for id in data:
     list.append(idList,id[0])
#print(str(tuple(idList)))
data1=cursor.execute('UPDATE dbo.SF_TGT SET IsDeleted = 10 where Id in ' + str(tuple(idList)))
print(str(data1))
cursor.commit()
