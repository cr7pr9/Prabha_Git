# -------------------------------------------------------------------------------------------------------------
# Developer         : Poornima Joshi (Sonata Software Ltd)
# CreatedDate       : 21/08/2020
# Description       : The script is used to Trigger the DI jobs using REST API calls and 
#                     Insert the status into SQL server table, so that even if Even handler pushes the files
#                     and if any of the instance is in 'RUNNING' state, the execution of taskflow will never
#                     take the place
#                       
# -------------------------------------------------------------------------------------------------------------

import requests
import pyodbc
import json
import yaml
import time
import sys
import datetime
import logging
from iics_aws_secret_mgr import *
from configparser import ConfigParser
from email_notification import *

# -------------------------------------------------------------------------------------------------------------
# Description : Class "jobtrigger" contains methods "CheckStatusAndJobTrigger","GetRunId",
#		        "GetRunStatus","StatusInsert" and "StatusUpdate" where these methods get the status 
#               from "API Trigger" table compared against the actual status using REST API call and 
#               trigger the  DI taskflow based on thge status response. If the job Status is
#               "RUNNING" no more execution will take place, If not the taskflow will be triggeered
#               and record will be inserted into API Trigger table
# -------------------------------------------------------------------------------------------------------------

class jobtrigger():

    def __init__(self, cursor, config, server, date):
        self.cursor = cursor
        self.config = config
        self.server = server
        self.date = date


# ------------------------------------------------------------------------------------------------
# Description : Checks the status of the  DI job and Based on the status decides on
#               resubmitting the job again.
# ------------------------------------------------------------------------------------------------

    def CheckStatusAndJobTrigger(self,api_folder,object_name,obj_url,api_name):
      

        #Assigning the output

        TaskflowName=object_name
        FolderName=api_folder
        Status='RUNNING'
        StartTime=None
        EndTime=None

        try:

            #Check the status of DI job for the previous Run id's

            logging.info("Get the status of DI job for the previous Run id's if any..")
    
            
            
            cursor.execute("select TaskflowName,RunId,Status from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DI_Taskflows"]["TB_DI_Taskflows"] +" where TaskflowName= ? and FolderName=? and Status=?",object_name,api_folder,'RUNNING')
            
            result = cursor.fetchall()
            rowcount=len(result)

            #Init Run: When there are no records in the table 
            if  (rowcount==0):

                #Trigger the new instance of DI job to get the run ID
                logging.info("Triggering the  DI instance to get the new RunID...")
                RunId=jobtrgobj.GetRunId(icSessionId,obj_url)

                #Insert the an entry for new RunId of DI job into table 
                logging.info("Inserting an entry of new RunId of DI job into table...")
                jobtrgobj.StatusInsert(TaskflowName,FolderName,RunId,Status)

                logging.info("Exiting the program hence Job is in Running state..")
                sys.exit()

            else:
                #If there are any entries with RunId as 'RUNNING'
                for row in result:
                    if (rowcount>0 and (row[2]=='RUNNING')):
                        #If the previous DI instance is 'RUNNING' in API trigger table 

                        Prev_RunId=row[1]


                        #Get the status of the new RunId of DI job
                        logging.info("Get the actual status of previous DI instance RunID...")
                        
                        Prev_RunId,Prev_StartTime,Prev_EndTime,Prev_Run_Status=jobtrgobj.GetRunStatus(icSessionId,Prev_RunId)
                        #Assign the output

                        

                        
                        
                        if Prev_Run_Status=='SUCCESS' or Prev_Run_Status=='FAILED':
                            
                            
                            #If the current status of previous RunId is either 'SUCCESS' or 'FAILED'

                            logging.info("Updating actual status of when prev RunId is not completed in DB for %s :"+TaskflowName)
                            jobtrgobj.StatusUpdate(Prev_RunId,Prev_StartTime,Prev_EndTime,Prev_Run_Status)
                            
                            #Trigger the new instance of DI job to get the run ID
                            logging.info("Triggering the DI instance to get the new RunID...")
                            RunId=jobtrgobj.GetRunId(icSessionId,obj_url)                        
                            
                            #Insert the current status of new RunId of DI job into trigger table 
                            logging.info("Inserting the current status of new RunId of DI job into API Trigger table...")
                            jobtrgobj.StatusInsert(TaskflowName,FolderName,RunId,Status)
                            logging.info("Triggered the DI JOB Successfully")
                            sys.exit()
            

                        elif Prev_Run_Status=='RUNNING' :
                            #If the status of Actual RunId is 'RUNNING'
                            logging.info("The job is in progress for RunId: "+str(Prev_RunId))

                            #send an email
                            SendEmail(api_name)
                            sys.exit()
                            #Change :email notifcation required it shoud be based on environment  

        except Exception as e:
            logging.error(api_name +" Job has been caught with an exception: "+str(e))
            raise


# ------------------------------------------------------------------------------------------------
# Description : Triggers the  DI job and returs the RunID using the REST API call            
# @Input : icSessionId (from Login API)
# ------------------------------------------------------------------------------------------------

    def GetRunId(self,icSessionId,obj_url):

        logging.info("Starting the Job to get the RunId... ")
        
        url = obj_url 
        
        #"https://na1.dm-us.informaticacloud.com/active-bpel/rt/tf_LoanLogics-10"

        payload = {}
       
        headers = {
          'Content-Type': 'application/json',
          'INFA-SESSION-ID': icSessionId
        }
        
        try:
            res = requests.request("POST", url, headers=headers, data = json.dumps(payload))
            
            job_res=json.loads(res.text)

            RunId=job_res['RunId']
     
            
        except requests.exceptions.HTTPError as e:
            logging.error('Failed on request %s', url)
            if e.response.status_code != 200:
                error = e.response.json()
                code = error['code']
                msg = error['description']
                logging.error(str(msg))
            raise

        return RunId

# ------------------------------------------------------------------------------------------------
# Description : Returns the status of the DI instance using the RunId by REST API call            
# @Input : icSessionId (from Login API), RunId
# ------------------------------------------------------------------------------------------------


    def GetRunStatus(self,icSessionId,RunId):

        logging.info("Getting the Job status for RunId... "+str(RunId))
        
        url = "https://na1.dm-us.informaticacloud.com/active-bpel/services/tf/status/"+str(RunId)
        
        payload = {}

        headers = {
          'Content-Type': 'application/json',
          'INFA-SESSION-ID': icSessionId
        }

        try:
            res = requests.request("GET", url, headers=headers, data = json.dumps(payload))
            run_status_res=json.loads(res.text)
            RunId=run_status_res['runId']
            StartTime=datetime.datetime.strptime(run_status_res['startTime'],"%Y-%m-%dT%H:%M:%SZ")
            Status=run_status_res['status']
            
            if run_status_res['endTime'] =='null' or run_status_res['endTime'] =='':
                EndTime=None
            else:
                EndTime=datetime.datetime.strptime(run_status_res['endTime'],"%Y-%m-%dT%H:%M:%SZ")
                

        except requests.exceptions.HTTPError as e:
            logging.error('Failed on request %s', url)
            if e.response.status_code != 200:
                error = e.response.json()
                logging.error(error['code'])
                logging.error(error['description'])
            raise 
        
        
        return RunId,StartTime,EndTime,Status


# ------------------------------------------------------------------------------------------------
# Description : Insert an entry in the Returns the status of database table 
#               for each new instance trigger of  DI             
# @Input : TaskflowName,FolderName,RunId,StartTime,EndTime,Status
# ------------------------------------------------------------------------------------------------


    def StatusInsert(self,TaskflowName,FolderName,RunId,Status):

        logging.info("Inserting an entry in trigger table for New DI instance...")

        try:
            
            cursor.execute("INSERT INTO "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DI_Taskflows"]["TB_DI_Taskflows"]+
                           "(TaskflowName,FolderName,RunId,Status,LoadDate) VALUES (?,?,?,?,?)", TaskflowName,FolderName,RunId,Status,datetime.datetime.now())
            sql_conn.commit()
            logging.info("The DI job details has been inserted in trigger table successfully")
            
        except Exception as e:

            logging.error("Insert to 'trigger' table caught with an exception "+str(e))
            raise
             

# ------------------------------------------------------------------------------------------------
# Description : Update the status/Endtime/Starttime for the existing RunId for each trigger for
#               LoanLogics DI in trigger table            
# @Input : RunId,StartTime,EndTime,Status
# ------------------------------------------------------------------------------------------------

        
    def StatusUpdate(self,RunId,StartTime,EndTime,Status):

        logging.info("Updating an entry in table for existing DI instance RunId : "+str(RunId))
        
        try:
            cursor.execute("UPDATE "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DI_Taskflows"]["TB_DI_Taskflows"]+" SET EndTime=?,Status=?,StartTime=? where RunId=?", EndTime,Status,StartTime,RunId)
            sql_conn.commit()
            logging.info("The status has benn upated in table successfully")

        except Exception as e:

             logging.error("Update on table caught with an exception "+str(e))
             raise

if __name__ == '__main__':
    
    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y-%H-%M-%S"))
       
    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)


    #Check for directories

    CHECK_LOG_FOLDER = os.path.isdir(config["LoanLogics"]["Log_Path"])
    if not CHECK_LOG_FOLDER:
        os.makedirs(config["LoanLogics"]["Log_Path"])
    else:
        pass

    logging.basicConfig(filename=config["LoanLogics"]["Log_Path"] +"\\log_LoanLogics_Trigger_["+date+"].log", level=logging.INFO)

    logging.info("******Logging info for 'LoanLogicsTrigger.py'******")
    
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

    
    
    #Reading credentials for IICS login
    
    ENVIRONMENT = os.environ['APP_ENV']
    
    if ENVIRONMENT=='dev':
      secret_name = 'development/correspondent/iics-sa-dw'
    elif ENVIRONMENT=='qa':
      secret_name = 'qa/correspondent/iics-sa-dw'
    elif ENVIRONMENT=='stg':
      secret_name = 'staging/correspondent/iics-sa-dw'
    else :
      secret_name = 'production/correspondent/iics-sa-dw'
    
    credentials=get_credentials(secret_name)
    
    uid=list(credentials.keys())[0]
    pwd=list(credentials.values())[0]


    #API call to get sessionId

    url = "https://dm-us.informaticacloud.com/saas/public/core/v3/login"
    
    payload = {
    "username":uid,
    "password":pwd
    }

    headers = {
      'Content-Type': 'application/json'
    }

    try: 
        response = requests.request("POST", url, headers=headers, data = json.dumps(payload))
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        logging.error('Failed on request %s', url)
        if e.response.status_code != 200:
            error = e.response.json()
            code = error['code']
            msg = error['description']
            logging.error(str(msg))
        raise 

    res=json.loads(response.text)
    icSessionId=res['userInfo']['sessionId']

    logging.info("Session established successfully....")

    jobtrgobj = jobtrigger(cursor, config, server, date)

    #Check the status of DI job and trigger the  job accordingly
    
    
    #jobtrgobj.CheckStatusAndJobTrigger('ED_CORR_PROD_LOAN_LOGICS_MAILROOM','tf_LoanLogics','https://na1.dm-us.informaticacloud.com/active-bpel/rt/tf_LoanLogics-14','DI_Taskflows')
    jobtrgobj.CheckStatusAndJobTrigger(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
    

