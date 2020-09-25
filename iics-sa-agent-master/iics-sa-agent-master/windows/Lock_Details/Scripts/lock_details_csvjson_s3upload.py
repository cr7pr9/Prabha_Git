# -------------------------------------------------------------------------------------------------------------
# Developer Name : Avinash Kumar Nagumalli (Neelblue Technologies)
# Date : 13/08/2020
# Description : Converts the CSV files to JSON files and then uploads them into S3 bucket.
# -------------------------------------------------------------------------------------------------------------

import pandas as pd
import pyodbc
import sys
import datetime
import yaml
from configparser import ConfigParser
import time
import os.path
import os
from os import path
import boto3
from botocore.exceptions import ClientError

# ---------------------------------------------------------------------------------------------------------------
# Description : Converts CSV files to JSON files and updates the Table "os_pcg_lockdetails_snapshot_values".
# @Input : config, date, cursor, server
# ---------------------------------------------------------------------------------------------------------------

def csv_to_json(config, date, cursor, server):
    files_processed = []
    arr = os.listdir(config["LockDetails"]["Csv_Path"])

    for filenames in arr:
        if filenames.startswith("BatchID_"):
            files_processed.append(filenames)

    try:
        for filename in files_processed:
            csv_file = pd.DataFrame(pd.read_csv(config["LockDetails"]["Csv_Path"]+"\\"+filename, sep = ",", names = ["LoanNum","LockRequestID","RowCreateDTM","AppSource","TestLoanFlag","BatchId","SequenceNumber","2150","2959","2953","3043","3902","3910","3911","LR_CX_P_AUSTYPE","LR_CX_P_SELLERLOANNUMBER","LR_CX_P_DEBTRATIO","2867","LR_CX_P_AUSRECOMMENDATION","LR_CX_P_ENOTEFLAG","LR_3533","LR_CX_P_SPECIALTYPRODUCT","LR_CX_TOTAL_LOAN_AMOUNT","2152","2029","LR_CX_EXTENSION_DAYS","LR_CX_P_TOTALLTV","2952","LR_CX_EXTENSION_COUNT","LR_CX_RELOCK_COUNT","2942","2943","2949","2944","2950","2945","2947","2946","2951","LR_CX_P_RENOVATIONCOMPLETEFLAG","3036","LR_CX_P_SUBORDINATIONTYPE","LR_CX_P_BUYDOWNFLAG","3844","LR_CX_P_UNDERWRITINGMETHOD","LR_CX_P_BASECLTV","LR_CX_P_BASELTV","LR_CX_LOAN_LASTNAME","LR_CX_P_TOTALCLTV","2962","LR_CX_P_RESERVESMONTHS","LR_CX_P_BORROWERCOUNT","LR_CX_PRICE_RUN_DATE_TIME","LR_CX_LOCK_DATE_TIME","2151","2853","3529","0"], index_col = False))
            csv_file = csv_file.iloc[1:]
            csv_file.to_json(config["LockDetails"]["Json_Path"]+"\\"+filename[:-4]+".json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
            os.remove(config["LockDetails"]["Csv_Path"]+"\\"+filename)
    except Exception as error:
        print(error,"ERR01")
        pass
        
    jsonfiles = []
    arr = os.listdir(config["LockDetails"]["Json_Path"])

    for filenames in arr:
        if filenames.startswith("BatchID_"):
            jsonfiles.append(filenames)
    try:
        for filename in jsonfiles:
            cursor.execute("UPDATE los_pcg.los_pcg_lockdetails_snapshot_values SET is_JSON_Generated = 'Y' ,JSONGeneratedTime = CURRENT_TIMESTAMP where BatchID=?",filename[8:-5])
            cursor.commit()
    except Exception as err:
        print(err)
        pass

# ---------------------------------------------------------------------------------------------------------------
# Description : Uploads the Converted JSON files into S3 bucket.
# @Input : config, date, app_env
# ---------------------------------------------------------------------------------------------------------------

def S3_upload(config, date, app_env):
    bucket = 'kirby-landing-'+app_env
    directory_name = "snapshot"
    arr = os.listdir(config["LockDetails"]["Json_Path"])

    list_processed = []

    for path in arr:
        if path.startswith("BatchID_"):
            list_processed.append(path)
        
    for file in list_processed:
        file_name = config["LockDetails"]["Json_Path"]+'\\'+file
        filename = file[:-5]
        s3_filepath = directory_name+'/'+filename+"_"+date+".json"
        # Generate Directory & Upload the file
        s3_client = boto3.client('s3')
        try:
            dir_gen = s3_client.put_object(Bucket=bucket, Key=(directory_name+'/'))
            response = s3_client.upload_file(file_name, bucket, s3_filepath)
            os.remove(config["LockDetails"]["Json_Path"]+"\\"+file)
        except ClientError as e:
            print(e)
            pass

# ------------------------------------------------------------------------------------------------
# Description : Main() Function 
# ------------------------------------------------------------------------------------------------

def main():
    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y%H-%M-%S"))

    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    server = ConfigParser()
    server.read('C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\ODBC\\ODBC.ini')

    CHECK_FOLDER = os.path.isdir(config["LockDetails"]["Csv_Path"])
    if not CHECK_FOLDER:
        os.makedirs(config["LockDetails"]["Csv_Path"])
    else:
        pass
    CHECK_FOLDER2 = os.path.isdir(config["LockDetails"]["Json_Path"])
    if not CHECK_FOLDER2:
        os.makedirs(config["LockDetails"]["Json_Path"])
    else:
        pass

    app_env = os.environ['APP_ENV']
    
    if app_env == 'prod':
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

    # CSV_to_JSON & S3_Upload Funtions Initiation 
    csv_to_json(config, date, cursor, server)
    S3_upload(config, date, app_env)

main()
