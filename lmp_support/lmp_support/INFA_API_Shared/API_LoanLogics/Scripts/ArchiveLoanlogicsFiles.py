# -------------------------------------------------------------------------------------------------------------
# Developer Name    : Poornima Joshi (Sonata Software Ltd)
# Date              : 21/08/2020
# Description       : The script used to archive the XML files which are successfully processed to stage and
#                       main tables by reading the flags from batch table 'XML_LSM_LDM_SourceFileList'
#                       Input: fileExt (Ex: Loandata/LoanDocMetadata)
#
# -------------------------------------------------------------------------------------------------------------


import os
import sys
import pyodbc
import datetime
import logging
import yaml
import os.path
from configparser import ConfigParser



def FileArchival(fileExt):

    logging.basicConfig(filename=config["LoanLogics"]["Log_Path"] +
                    "\\log_LoanLogics_ArchiveFiles_["+date+"].log", level=logging.INFO)

    #File Archival
    logging.info("Started Archiving the " +fileExt+" files..")
    
    try:
        list_processed = []
        arr = os.listdir(scr_file_path)

        #get the list of filenames to be archived
        for filenames in arr:
            if filenames.endswith (fileExt+'.xml'):
                list_processed.append(filenames)
            
        for filename in list_processed:  

            cursor.execute("select XML_Processing_Status,IICS_Processing_Status from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" where XMLFileName=? and XML_Processing_Status !=? ",filename,'OPEN')
            result = cursor.fetchall()
            rowcount=len(result)
            if rowcount>0:
                #Check for the batch file status completed
                for row in result:
                    if (row[0]== 'COMPLETED' and row[1] == 'COMPLETED'):
                        logging.info("Archiving the files .. ")
                        scr_file_name = filename
                        file_path = scr_file_path + scr_file_name
                        if os.path.exists(file_path)==True:
                            os.replace(file_path, archive_file_path+filename)
                        
        logging.info("Archived the processed " +fileExt+" XML files to Archival folder successfully. ")

    except Exception as e:
        logging.error("File Archival failed for "+fileExt+" with exception: "+str(e))
        raise


if __name__ == '__main__':

    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y-%H-%M-%S"))

    dt = str(currentdate.strftime("%m%d%Y"))
    
    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
       config = yaml.safe_load(stream)    

    scr_file_path = config["LoanLogics"]["Inbound"]
    log_file_path = config["LoanLogics"]["Log_Path"]
    archive_file_path = config["LoanLogics"]["Archive_Path"]


    server = ConfigParser()
    server.read('C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\ODBC\\ODBC.ini')
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


    sql_conn = pyodbc.connect('Driver={SQL Server};'
                    'Server='+servername+';'
                    'Database='+server["SqlServer_Connection"]["DBname"]+';'
                    'Trusted_Connection=yes;')
    cursor = sql_conn.cursor()

    #Calling the script for archival
    
    FileArchival(sys.argv[1])
