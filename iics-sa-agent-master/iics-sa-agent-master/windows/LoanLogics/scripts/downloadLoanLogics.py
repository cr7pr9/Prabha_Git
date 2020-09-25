# -------------------------------------------------------------------------------------------------------------
# Developer Name : Avinash Kumar Nagumalli (Neelblue Technologies)
# Date : 21/04/2020
# Description : Downloads xml files from AWS S3 bucket and the downloaded xml files are
#               stored in a temporary directory  and the formate of the xml files are
#               changed according to the requirement. Lastly creates samplexml.txt file
#               to save the paths of all edited xml files.
# -------------------------------------------------------------------------------------------------------------

import re
import os
import shutil
from os import path
import boto3
import yaml

with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

CHECK_FOLDER = os.path.isdir(config["LoanLogics"]["Temp_Path"])
if not CHECK_FOLDER:
    os.makedirs(config["LoanLogics"]["Temp_Path"])
else:
    pass

env = os.environ['APP_ENV']

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('kanan-tpi-object-store-'+env)
try:
    for object_summary in my_bucket.objects.filter(Prefix="archive/"):
        file = object_summary.key.split('/')
        try:
            if file[2]=='loantools':
                if file[3].endswith('.xml'):
                    if file[3].startswith('._'):
                        pass
                    else:
                        s3.Bucket('kanan-tpi-object-store-'+env).download_file(object_summary.key,config["LoanLogics"]["Temp_Path"]+"\\"+ file[3])
        except Exception as error:
            pass
except:  
    pass


arr = os.listdir(config["LoanLogics"]["Temp_Path"])
for file in arr:
    try:
        header = '<?xml version="1.0"?> \n'
        content = open(config["LoanLogics"]["Temp_Path"]+"\\"+file, mode='r', encoding='utf-8-sig').read()
        open(config["LoanLogics"]["Temp_Path"]+"\\"+file , mode='w', encoding='utf-8').write(content)
        formated_data = open(config["LoanLogics"]["Temp_Path"]+"\\"+file,encoding ="utf8").read()
        data = str(formated_data)
        if data.startswith('<?xml version="1.0"'):
            if data.startswith('<?xml version="1.0"?>'):
                data1 = data.replace('<?xml version="1.0"?>','')
            elif data.startswith('<?xml version="1.0" encoding="UTF-8"?>'):
                data1 = data.replace('<?xml version="1.0" encoding="UTF-8"?>','')
        xml_data = data1.replace('\r', '')
        xml_data2 = xml_data.replace('\n','')
        xml_data2+='|'
        header+=xml_data2
        os.remove(config["LoanLogics"]["Temp_Path"]+"\\"+file)
        data = open(config["LoanLogics"]["Temp_Path"]+"\\"+file, "w")
        data.write(header)
        data.close()
    except Exception as err:
        pass

list = []
for path in os.listdir(config["LoanLogics"]["Temp_Path"]):
    if path.endswith('xml'):
        full_path = os.path.join(config["LoanLogics"]["Temp_Path"], path)
        if os.path.isfile(full_path):
            list.append(full_path)
    else:
        pass

data = open(config["LoanLogics"]["Sample_Path"]+"\\samplexml.txt", "w")
for path in list:
    data.write(path+"\n")
data.close()



