import sys
import pyodbc
import datetime
import yaml
import os
import logging
from configparser import ConfigParser

class mailrom_reprocess():

    def __init__(self, cursor, config, server, date):
        self.cursor = cursor
        self.config = config
        self.server = server
        self.date = date

    def Query_with_Payload(self, payload):
        cursor.execute("Select id,retrycount from los_pcg.mailroom_reprocess where payload = '"+payload+"'")
        rows = cursor.fetchall()
    
        if not rows:
            return 'N'
        else:
            return list(list(rows)[0])


    def Insert_to_Table(self,payload,service_url):
        cursor.execute('Insert into los_pcg.mailroom_reprocess (payload,serviceurl) values (?,?)',payload,service_url)
        cursor.commit()

    def Update_retry_count(self,retrycount,id):
        cursor.execute('Update  los_pcg.mailroom_reprocess  set retrycount = ? ,errordtm= current_timestamp where id = ?',retrycount,id)
        cursor.commit()

 

if __name__ == "__main__":
    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y%H-%M-%S"))          
    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)
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

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server='+servername+';'
                          'Database='+server["SqlServer_Connection"]["DBname"]+';'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    
    mailroom_obj = mailrom_reprocess(cursor, config, server, date)
    
    if (mailroom_obj.Query_with_Payload(sys.argv[1])=='N'):
        mailroom_obj.Insert_to_Table(sys.argv[1],sys.argv[2])
    else:
        id = mailroom_obj.Query_with_Payload(sys.argv[1])[0]
        retrycount = mailroom_obj.Query_with_Payload(sys.argv[1])[1]+1
        mailroom_obj.Update_retry_count(retrycount,id)


    



    

    
