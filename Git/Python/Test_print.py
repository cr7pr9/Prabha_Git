import json
from dateutil.parser import parse
TypesList=[]
with open ('C:\\Users\\dell\\Desktop\\PD\\Client\\getAllEntities_2.JSON') as filedata:
    data = json.load(filedata)
    if data.get('commitmentas',{}).get('deliveryTypes',[]):
            for i in data.get('commitments',{}).get('deliveryTypes',[]):
               print(i['deliveryType'])
               TypesList.append(i['deliveryType'])
print(TypesList)