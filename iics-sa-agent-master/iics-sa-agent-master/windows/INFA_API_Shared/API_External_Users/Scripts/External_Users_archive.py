import pyodbc
import json
import os
import zipfile
import yaml
import datetime

currentdate = datetime.datetime.now()
date = str(currentdate.strftime("%d-%m-%Y%H-%M-%S"))

with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
   config = yaml.safe_load(stream)

list_processed=[]

arr = os.listdir(config["Path"]["Inbound_EXTUSRS"])

for filename in arr:
   if filename.startswith('external_users'): 
       list_processed.append(filename)

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
            ziph.write(os.path.join(root, file))


zipf = zipfile.ZipFile( config["Path"]["Archive_EXTUSRS"]+"\\"+"ExternalUsers_"+date+".zip" , 'w', zipfile.ZIP_DEFLATED)
zipdir( config["Path"]["Inbound_EXTUSRS"] , zipf)
zipf.close()

for filename in list_processed:
    os.remove(config["Path"]["Inbound_EXTUSRS"]+"/"+filename )
