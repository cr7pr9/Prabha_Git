# -------------------------------------------------------------------------------------------------------------
# Developer Name : Avinash Kumar Nagumalli (Neelblue Technologies)
# Date : 03/06/2020
# Description : Dowloads folders from AWS S3 bucket ,edits the downloaded json files 
#               and deletes the temporarily created directory.Lastly creates samplepath.txt 
#               file to save the paths of all edited json files.
# -------------------------------------------------------------------------------------------------------------

import sys
import pyodbc
import json
import datetime
import yaml
import logging
from configparser import ConfigParser
import os
import shutil
from os import path
import json
import boto3

# -------------------------------------------------------------------------------------------------------------
# Description : Class "dumessages" contains methods "json_edit", "dir_delete", "pathfile" and "controltable" 
#               where these methods dowloads folders from AWS S3 bucket ,edits the downloaded json files 
#               and deletes the temporarily created directory.Lastly creates samplepath.txt 
#               file to save the paths of all edited json file and lastly inserts paths file names into 
#               table"LL_DU_FileList_LogControl".
# -------------------------------------------------------------------------------------------------------------

class dumessages():

    def __init__(self, cursor, config, server, date, idList, idList_unprocessed):
        self.cursor = cursor
        self.config = config
        self.server = server
        self.date = date
        self.idList = idList
        self.idList_unprocessed = idList_unprocessed

# ------------------------------------------------------------------------------------------------
# Description : Edits the json files and places the downloaded json files 
#               in files_load_path.
# @Input : temp_path, files_load_path
# ------------------------------------------------------------------------------------------------

    def json_edit(self):
        logging.basicConfig(filename=config["DesktopUnderwriter"]["Log_DU"]+"\\log_dumessages_jsonedit_["+date+"].log", level=logging.INFO)
        arr = os.listdir(config["DesktopUnderwriter"]["Temp_Path"])
        for filename in arr:
            try:
                if filename.startswith(config["DesktopUnderwriter"]["File_Prefix"]):
                    with open (config["DesktopUnderwriter"]["Temp_Path"]+"\\"+filename) as data_check:
                        raw_data_chk = data_check.read()
                        data_check.close()
                    with open(config["DesktopUnderwriter"]["Temp_Path"]+"\\"+filename) as filedata:
                        data_raw2 = json.load(filedata)
                        if ('InvalidCasefileId' in raw_data_chk or 'invalid_data' in raw_data_chk) or 'caseFileId' not in raw_data_chk:
                            pass
                        else:
                            if raw_data_chk.startswith('"{'):
                                fildata = data_raw2
                                logging.info("Json file edited "+str(filename))
                            else:
                                fildata = raw_data_chk
                                logging.info("Json file loaded "+str(filename))
                            filedata = open(config["DesktopUnderwriter"]["Files_Load_Path"]+"\\"+filename, "w")
                            data1 = fildata.replace('Loan Strengths/Weaknesses":','LoanStrengthsWeaknesses":').replace('Risk/Eligibility":','RiskEligibility":').replace('Verification/Approval Conditions":','VerificationApprovalConditions":')
                            filedata.write(data1)
                            filedata.close()
                            logging.info("Json file moved to main directory "+str(filename))
            except Exception as error:
                logging.error("Json file "+str(filename)+" caught with exception "+str(error))
                pass

# ------------------------------------------------------------------------------------------------
# Description : Deletes the temporary directory.
# @Input : temp_path, files_load_path
# ------------------------------------------------------------------------------------------------

    def dir_delete(self):
        arr = os.listdir(config["DesktopUnderwriter"]["Temp_Path"])
        for file in arr:
            os.remove(config["DesktopUnderwriter"]["Temp_Path"]+"\\"+file) 
        os.rmdir(config["DesktopUnderwriter"]["Temp_Path"])
        

# ------------------------------------------------------------------------------------------------
# Description : Creates a Samplepath.txt file which contains all the 
#               paths of newly created json files.
# @Input : temp_path, files_load_path
# ------------------------------------------------------------------------------------------------

    def pathfile(self):
        delta_list = []
        for filename in os.listdir(config["DesktopUnderwriter"]["Files_Load_Path"]):
            if filename.startswith(config["DesktopUnderwriter"]["File_Prefix"]):
                full_path = os.path.join(config["DesktopUnderwriter"]["Files_Load_Path"], filename)
                if os.path.isfile(full_path) and filename not in idList:
                    delta_list.append(full_path)
            else:
                pass

        header = "PATH\n"
        data = open(config["DesktopUnderwriter"]["Sample_Path"]+"\du_filelist.txt", "w")
        data.write(header)
        for path in delta_list:
            data.write(path+"\n")
        data.close()

# ------------------------------------------------------------------------------------------------
# Description : Creates a Samplepath.txt file which contains all the 
#               paths of newly created json files.
# @Input : temp_path, files_load_path
# ------------------------------------------------------------------------------------------------

    def controltable(self):
        logging.basicConfig(filename=config["DesktopUnderwriter"]["Log_DU"] +"\\log_dumessages_controltable_["+date+"].log", level=logging.INFO)
        for filename in os.listdir(config["DesktopUnderwriter"]["Files_Load_Path"]):
            try:
                if filename.startswith(config["DesktopUnderwriter"]["File_Prefix"]):
                    full_path = os.path.join(config["DesktopUnderwriter"]["Files_Load_Path"], filename)
                    if os.path.isfile(full_path) and filename not in idList:
                        FolderName = config["DesktopUnderwriter"]["File_Prefix"]
                        FileName = filename
                        Isprocessed_Flag = "Y"
                        logging.info("Json file read without errors "+str(filename))
                        if FileName in idList_unprocessed:
                            logging.info("Json file data updated in Table 'LL_DU_FileList_LogControl' "+str(filename))
                            
                            cursor.execute("UPDATE "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_dumessasges"]+" SET ISPROCESSED_FLAG= 'Y', rowcreatedtm = CURRENT_TIMESTAMP WHERE FILENAME = '"+FileName+"'")
                            cursor.commit()
                        else:
                            logging.info("Json file data inserted in Table 'LL_DU_FileList_LogControl' "+str(filename))
                            cursor.execute("Insert into "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_dumessasges"]+" (FolderName, FileName, Isprocessed_Flag) values (?,?,?)",FolderName, FileName, Isprocessed_Flag)
                            cursor.commit()
                else:
                    logging.info("None of JSON files has been processed as all the JSON files are already processed and logged into control table")
                    pass
            except Exception as error:
                logging.error("Json file "+str(filename)+" caught with exception "+str(error))

        arr_list = os.listdir(config["DesktopUnderwriter"]["Files_Load_Path"])
        for file in arr_list:
            print(file)
            if os.path.isfile(os.path.join(config["DesktopUnderwriter"]["Files_Load_Path"], file)):
                os.remove(config["DesktopUnderwriter"]["Files_Load_Path"]+"\\"+file)
        
# ------------------------------------------------------------------------------------------------
# Description : Downloads directories from AWS S3 bucket and connects to the database
#               gets list of filenames from table "LL_DU_FileList_LogControl".
# ------------------------------------------------------------------------------------------------

if __name__ == '__main__':

    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y%H-%M-%S"))
    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    server = ConfigParser()
    server.read(
        'C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\ODBC\\ODBC.ini')
        
    app_env = os.environ['APP_ENV']

    if app_env == 'prd':
        servername = server["SqlServer_Connection"]["servername_prod"]
    elif app_env == 'dev2':
        servername = server["SqlServer_Connection"]["servername_dev2"]
    elif app_env == 'qa':
        servername = server["SqlServer_Connection"]["servername_qa"]
    elif app_env == 'qa2':
        servername = server["SqlServer_Connection"]["servername_qa2"]
    elif app_env == 'stg':
        servername = server["SqlServer_Connection"]["servername_stg"]
    elif app_env == 'stg2':
        servername = server["SqlServer_Connection"]["servername_stg2"]
    else:
        servername = server["SqlServer_Connection"]["servername_dev"]

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server='+servername+';'
                          'Database='+server["SqlServer_Connection"]["DBname"]+';'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    data = cursor.execute("SELECT FILENAME FROM "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_dumessasges"]+" WHERE ISPROCESSED_FLAG='Y'")
    idList =[]  
    for id in data:
        idList.append(id[0])
    
    data_unprocessed = cursor.execute("SELECT FileName from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_dumessasges"]+" WHERE ISPROCESSED_FLAG='N'")
    idList_unprocessed =[]  

    for id_up in data_unprocessed:
        idList_unprocessed.append(id_up[0])
    CHECK_FOLDER = os.path.isdir(config["DesktopUnderwriter"]["Temp_Path"])
    if not CHECK_FOLDER:
        os.makedirs(config["DesktopUnderwriter"]["Temp_Path"])
    else:
        pass
    CHECK_FOLDER2 = os.path.isdir(config["DesktopUnderwriter"]["Log_DU"])
    if not CHECK_FOLDER2:
        os.makedirs(config["DesktopUnderwriter"]["Log_DU"])
    else:
        pass
    CHECK_FOLDER3 = os.path.isdir(config["DesktopUnderwriter"]["Files_Load_Path"])
    if not CHECK_FOLDER3:
        os.makedirs(config["DesktopUnderwriter"]["Files_Load_Path"])
    else:
        pass
    app_env = os.environ['APP_ENV']
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket('kanan-tpi-object-store-'+app_env)
    try:
        for object_summary in my_bucket.objects.filter(Prefix="archive/"):
            filename_split = object_summary.key.split('/')
            if 'du-messages' in filename_split[2]:
                if filename_split[3].endswith('json') and filename_split[3].startswith(config["DesktopUnderwriter"]["File_Prefix"]) and (config["DesktopUnderwriter"]["File_Prefix"]+"_"+filename_split[1]+'.json' not in idList): 
                    s3.Bucket('kanan-tpi-object-store-'+app_env).download_file(object_summary.key,config["DesktopUnderwriter"]["Temp_Path"]+"\\"+config["DesktopUnderwriter"]["File_Prefix"]+"_"+ filename_split[1]+'.json')
                else:
                    pass
    except Exception as error:
        pass

    dumessages = dumessages(cursor, config, server, date, idList,idList_unprocessed)

    if sys.argv[1] == 'ControlTable':
        dumessages.controltable()
        dumessages.dir_delete()
    elif sys.argv[1] == 'DUMessages':
        dumessages.json_edit()
        dumessages.dir_delete()
        dumessages.pathfile()
