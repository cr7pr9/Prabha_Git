import pyodbc
import json
import os
import zipfile
import yaml
import datetime
import shutil
import glob

currentdate = datetime.datetime.now()
date = str(currentdate.strftime("%d-%m-%Y%H-%M-%S"))

   
def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
            ziph.write(os.path.join(root, file))
            
with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\PathFiles\\stipdetails_sample.txt", 'r') as stream:
    next(stream)
    filenames = stream.readlines()
    
    
for line in filenames:
    print(line.strip())
    shutil.move(line.strip(),config["Path"]["Temp_STIP"])
    
zipf = zipfile.ZipFile( config["Path"]["Archive_STIP"]+"\\"+"Stip_Details_"+date+".zip" , 'w', zipfile.ZIP_DEFLATED)
zipdir( config["Path"]["Temp_STIP"] , zipf)
zipf.close()

files = glob.glob(config["Path"]["Temp_STIP"]+"/"+'*')
for f in files:
    os.remove(f)

