# -------------------------------------------------------------------------------------------------------------
# Developer Name : Avinash Kumar Nagumalli (Neelblue Technologies)
# Date : 9/03/2020
# Description : Convert External Users Json data into Stage table.
#               This Stage table will be used in Informatica DI to create
#               External Users Hub table.
# -------------------------------------------------------------------------------------------------------------

import sys
import pyodbc
import json
import os
import datetime
import yaml
import logging
from configparser import ConfigParser

# -------------------------------------------------------------------------------------------------------------
# Description : Class "external" contains one method "externalusers" where the method deletes data from their
#               respective staging table and reads data from Json files and inserts data into the table.
# -------------------------------------------------------------------------------------------------------------

class external():

    def __init__(self, cursor, config, server):
        self.cursor = cursor
        self.config = config
        self.server = server

# ------------------------------------------------------------------------------------------------
# Description : Deletes data from the Staging table "los_pcg_externalusers_stg"
#               and reads data from Json files and inserts into the above referred table
# @Input : Cursor, Config, List_processed
# @Output : Loading data into the staging table "los_pcg_externalusers_stg"
# Error : Stores name of error files in Log file "external_users_log"
# ------------------------------------------------------------------------------------------------

    def externalusers(self):

        list_processed = []

        arr = os.listdir(config["Path"]["Inbound_EXTUSRS"])

        for filenames in arr:
            if filenames.startswith('external_users'):
                list_processed.append(filenames)

        cursor.execute("DELETE from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_external_stg"])
        cursor.commit()
        k = 0
        j = 0
        for filename in list_processed:
            try:
                with open(config["Path"]["Inbound_EXTUSRS"]+"/"+filename) as filedata:
                    data = json.load(filedata)

                    for k in data:
                        if "id" in k:
                            PersonId = k['id']
                        else:
                            PersonId = None
                        if "phone" in k:
                            PhNum = k['phone']
                        else:
                            PhNum = None
                        if "orgId" in k:
                            CompId = k['orgId']
                        else:
                            CompId = CompId
                        if "organizationName" in k:
                            CompNm = k['organizationName']
                        else:
                            CompNm = CompNm
                        if "email" in k:
                            UserEmail = k['email']
                        else:
                            UserEmail = None
                        if "lastName" in k:
                            LstNm = k['lastName']
                        else:
                            LstNm = None
                        if "firstName" in k:
                            FstNm = k['firstName']
                        else:
                            FstNm = None
                        if "emailForLogin" in k:
                            LoginNm = k['emailForLogin']
                        else:
                            LoginNm = None
                        if "updatedDateTime" in k:
                            ModDtm = k['updatedDateTime']
                        else:
                            ModDtm = None
                        if "disabledLogin" in k:
                            DisabledLogin = k['disabledLogin']
                        else:
                            DisabledLogin = None

                        if "personas" in k:
                            for j in k['personas']:
                                if "entityName" in j:
                                    RoleNm = j['entityName']
                                else:
                                    RoleNm = None

                                logging.info("Json file read without errors "+str(filename))
                                cursor.execute("Insert into "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_external_stg"]+" ( DisabledLogin ,PersonId ,RoleNm ,PhNum ,CompId ,CompNm ,UserEmail ,LstNm ,FstNm ,LoginNm ,ModDtm) values (?,?,?,?,?,?,?,?,?,?,?)",
                                            DisabledLogin, PersonId, RoleNm, PhNum, CompId, CompNm, UserEmail, LstNm, FstNm, LoginNm, ModDtm)
                                cursor.commit()
            # except(RuntimeError, TypeError, NameError):
            except Exception as error:
                logging.error("Json file "+str(filename)+" caught with exception "+str(error))
                pass


if __name__ == '__main__':

    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y%H-%M-%S"))

    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    logging.basicConfig(filename=config["Path"]["Log_EXTUSRS"] +
                        "\\log_external_users_["+date+"].log", level=logging.INFO)

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
    extuser = external(cursor, config, server)
    if sys.argv[1] == 'ExternalUser':
        extuser.externalusers()
