# -------------------------------------------------------------------------------------------------------------
# Developer Name    : Poornima Joshi (Sonata Software Ltd)
# Date              : 21/08/2020
# Description       : Reads the XML files from the Inbound directory and inserts data by parsing 
#                       the XML files into stage tables below which is controlled by the batch-process.
#                       LSM_XML_Loan_Stg
#                       LSM_XML_Asset_Stg
#                       LSM_XML_ClosingCost_Stg
#                       LSM_XML_Income_Stg
#                       LSM_XML_IntegratedDiscFees_Stg
#                       LSM_XML_Liability_Stg
#                       LSM_XML_Borrower_Stg 
#
# -------------------------------------------------------------------------------------------------------------


import xml.etree.ElementTree as ET
import pyodbc
import yaml
import datetime
import logging
import sys
import os
import time
import os.path
from email_notification import *
from configparser import ConfigParser



# -------------------------------------------------------------------------------------------------------------
# Description : Class "loanlogics" contains methods "BatchOpen","ParsingLoanDataXml","ProcessXmlFileList", 
#		        "BatchFailed","TruncateStageTables" and "BatchUnprocessed" where these methods reads filenames
#		        from Inbound diectory and writes an entry in "XML_LSM_LDM_SourceFileList" as OPEN for processing,
#		        Parses and loads the data into stage tables. Post succesfull completion archives the xml files 
#		        into to Archival directory and failed files are moved to Unprocesses directory. At last batches
#               are updated as FAILED or COMPLETED based on run status in table "XML_LSM_LDM_SourceFileList".
# -------------------------------------------------------------------------------------------------------------

class loanlogics():

    def __init__(self, cursor, config, server, date):
        self.cursor = cursor
        self.config = config
        self.server = server
        self.date = date


# ------------------------------------------------------------------------------------------------
# Description : Read the XML file names from Inbound and write into XML_LSM_LDM_SourceFileList as open 
#               for parsing 
# ------------------------------------------------------------------------------------------------
    
    def BatchOpen(self):

        logging.info("Script: LoanLogics_LoandataXml_Load.py")
        logging.info("*********Logging the details of Batchopen process of Loandata*********")
        logging.info("Batch Table  'XML_LSM_LDM_SourceFileList' Insert:")
        
        try:
            list_processed = []
            arr = os.listdir(src_file_path)
            
            #List *Loandata.xml files from Inbound Dir
            for filenames in arr:
                if filenames.endswith ('Loandata.xml'):
                    list_processed.append(filenames)
            
            #Check if no files for processing in current run, then exit the process
            if not list_processed:
                logging.info("There are no Loandata xml files with batch status as OPEN in current run")
                sys.exit()
            else:
                pass
            
            for filename in list_processed:            
                logging.info("Checking for the status of the file " +filename +" in 'XML_LSM_LDM_SourceFileList' table ")
                
                cursor.execute("select XML_Processing_Status,IICS_Processing_Status from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" where XMLFileName=? and XML_Processing_Status !=? and XMLFileName like ? ",filename,'OPEN','%Loandata.xml')
                result = cursor.fetchall()
                rowcount=len(result)

                #Check for new batch: Opens new batch
                if rowcount==0:
                    
                    logging.info("Inserting to 'XML_LSM_LDM_SourceFileList' table as batch OPEN "+filename)
                    cursor.execute("INSERT INTO "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +"( XMLFileName, XML_Processing_Status,IICS_Processing_Status, StartDateTime) VALUES (?,?,?,?)", filename,'OPEN','OPEN',time.strftime('%Y-%m-%d %H:%M:%S'))
                    sql_conn.commit()
                
                elif rowcount>0:
                    for row in result:
                        # Check for existing batch: If already processed successfully 
                        if (row[0]== 'COMPLETED' and row[1] == 'COMPLETED'):

                            logging.info("The Loandata file "+filename+" is already processed ")
                        
                        # Check for existing batch: If failed or not completed
                        elif ((row[0]=='FAILED') or (row[1] != 'COMPLETED')):
                            
                            logging.info("Either XML_Processing_Status or IICS_Processing_Status is not completed, hence updating the batch file to OPEN " +filename)

                            cursor.execute("Update "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" set XML_Processing_Status=?, StartDateTime=? where XMLFileName=? ",'OPEN',time.strftime('%Y-%m-%d %H:%M:%S'),filename)
                            sql_conn.commit()
            
            logging.info("Insert/Update to 'XML_LSM_LDM_SourceFileList' table based on Batch Status successful")

        except Exception as error:
            logging.error("Listing and inserting Loandata files to 'XML_LSM_LDM_SourceFileList' caught with exception %s"+str(error))
            raise

# ------------------------------------------------------------------------------------------------
# Description : Read the XMLFilenames from the XML_LSM_LDM_SourceFileList which are "OPEN" for parsing
#               and calls the module to insert content of Loandata into stage tables
# ------------------------------------------------------------------------------------------------


    def ProcessXmlFileList(self):

        logging.info("*********Logging the details of ProcessXmlFileList: *********")
        logging.info("Processing the Loandata xml files in 'XML_LSM_LDM_SourceFileList' table status as OPEN.")

        try:
        
            logging.info("Get the filelist,BatchID which are batch OPEN from 'XML_LSM_LDM_SourceFileList' table and loop:")
            
            cursor.execute("select BatchID,StartDateTime,XMLFileName from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" where XML_Processing_Status=? and XMLFileName like ?" ,'OPEN','%Loandata.xml')
            rows = list( cursor )
            for data in rows:
                BatchID=data[0]
                CreateTs=data[1]
                filename=data[2]

                logging.info(filename)
                
                content = open(config["LoanLogics"]["Inbound"]+filename, mode='r', encoding='utf-8-sig').read()
                open(config["LoanLogics"]["Inbound"]+filename , mode='w', encoding='utf-8').write(content)

                xmlparse=loanlogicsobj.ParsingLoanDataXml(filename,BatchID,CreateTs)
                
                if xmlparse==1:
                    logging.info("File parsing completed for: "+filename)
                
                    logging.info("Updating the batch to completed for "+filename)
                    
                    cursor.execute("Update "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" set XML_Processing_Status=?,Comments=? where XMLFileName=?",'COMPLETED','Stage Load Successful',filename)
                    sql_conn.commit()
                    
                    logging.info("Batch completed successfully for  " +filename)

                else:

                    logging.error("Caught with an Exception while parsing the file: "+filename)
                    
                    loanlogicsobj.BatchFailed(filename)

                    logging.error("Updated the batch to failed for file successfully:"+filename)
                    
                    loanlogicsobj.BatchUnprocessed()

                    logging.error("Moved the batch failed to unprocessed directory successfully:"+filename)

                    SendEmail('LoanLogics')
                    
                    logging.error("Successfully sent an email nofication in case of file parsing failure ")

                    sys.exit(1)

        except Exception as e:

            logging.error("Caught with an Exception while processing file: "+filename + "Error: "+str(e))

            raise

# ------------------------------------------------------------------------------------------------
# Description : Parse the xml files which are listed in XML_LSM_LDM_SourceFileList table taking the 
#               input as xmlfilename and inserts data into LSM_XML_Loan_Stg,LSM_XML_Asset_Stg,
#               LSM_XML_ClosingCost_Stg,LSM_XML_Income_Stg,LSM_XML_IntegratedDiscFees_Stg,
#               LSM_XML_Liability_Stg,LSM_XML_Borrower_Stg        
# @Input : filename,CreateTs,BatchID
# ------------------------------------------------------------------------------------------------

    def ParsingLoanDataXml(self,filename,BatchID,CreateTs):

        logging.info("Started parsing the LoanData XML file : %s", str(filename))

        #Initilization
        loanId=None
        loanNumber=None
        LoanNum=None
        name=None
        value=None
        Num=None
        Num_b=None
        seq = 0

        try:
        
            tree = ET.parse(src_file_path+filename)
            root = tree.getroot()
            list = root.attrib

            # -----------------------------------------------------------------
            # LSM_XML_Loan_Stg Load
            #

            for x in list: 
                if 'loanId' in x:
                    loanId=list.get(x)
                if 'loanNumber' in x:
                    loanNumber=list.get(x)   
                    LoanNum=loanNumber[0:10]
                    for child in root:
                        if ("IntegratedDiscFees" not in child.tag) and ("URLA1003" not in child.tag) and ("ClosCostQkDataEnt" not in child.tag):
                            l_details=child.attrib
                            name=l_details.get('name')
                            value=l_details.get('value')
                            if name==None or name=='':
                                name='Unknown Name Field'
                                cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Loan_Stg"] +"  (BatchID,LoanNum,CreateTs, LoanID, LoanNumber, Name, Value, FileType) VALUES (?,?,?,?,?,?,?,?)",BatchID, LoanNum,CreateTs,loanId,loanNumber,name, value, 'Loan')
                                sql_conn.commit()
                            else:
                                cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Loan_Stg"] +"  (BatchID,LoanNum,CreateTs, LoanID, LoanNumber, Name, Value, FileType) VALUES (?,?,?,?,?,?,?,?)",BatchID, LoanNum,CreateTs,loanId,loanNumber,name, value, 'Loan')
                                sql_conn.commit()
                    
                    logging.info("Loan Stage Table 'LSM_XML_Loan_Stg' loaded successfully")   
            # -----------------------------------------------------------------
            # # LSM_XML_Borrower_stg Load
            #
            for URLA1003 in root.iter('URLA1003'):
                if 'Num' in URLA1003.attrib:
                    Num = URLA1003.get('Num')
                for Borrower in URLA1003.iter('Borrower'):
                    
                    if 'Num' in Borrower.attrib:
                        Num_b = Borrower.get('Num')
                        for x in Borrower:
                            if ("Income" not in x.tag) and ("Sex" not in x.tag) and ("Race" not in x.tag) and ("Ethnicity" not in x.tag):
                                b_details = x.attrib
                                name = b_details.get('name')
                                value = b_details.get('value')
                                if name == None or name == '':
                                    name = 'Unknown Name Field'
                                    cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Borrower_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Num, Num_b, Name, Value, FileType) VALUES (?,?,?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,Num,Num_b,name, value, 'Borrower')
                                    sql_conn.commit()
                                else:
                                    cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Borrower_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Num, Num_b, Name, Value, FileType) VALUES (?,?,?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,Num,Num_b,name, value, 'Borrower')
                                    sql_conn.commit()

                    logging.info("Borrower Stage Table'LSM_XML_Borrower_Stg' loaded successfully")

            # -----------------------------------------------------------------
            # # LSM_XML_Income_stg:
            #
                    for Income in Borrower.iter('Income'):
                        for child in Income:
                            i_details = child.attrib
                            name = i_details.get('name')
                            value = i_details.get('value')
                            if name == None or name == '':
                                name = 'Unknown Name Field'
                                cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Income_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Num, Num_b, Name, Value, FileType) VALUES (?,?,?,?,?,?,?,?,?)",BatchID, LoanNum,CreateTs,loanNumber,Num,Num_b,name, value, 'Income')
                                sql_conn.commit()
                            else:
                                cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Income_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Num, Num_b, Name, Value, FileType) VALUES (?,?,?,?,?,?,?,?,?)",BatchID, LoanNum,CreateTs,loanNumber,Num,Num_b,name, value, 'Income')
                                sql_conn.commit()

                        logging.info("Income Stage Table 'LSM_XML_Income_Stg' loaded successfully")

            # -----------------------------------------------------------------
            # # LSM_XML_Asset_stg:
            #
                for Asset in URLA1003.iter('Asset'):
                    for j in Asset:
                        b_details = j.attrib
                        name = b_details.get('name')
                        value = b_details.get('value')
                        if name == None or name == '':
                            name = 'Unknown Name Field'
                            cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Asset_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Num, Name, Value,AssetSeq#, FileType) VALUES (?,?,?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,Num,name, value,seq,'Asset')
                            sql_conn.commit()
                        else:
                            cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Asset_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Num, Name, Value,AssetSeq#, FileType) VALUES (?,?,?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,Num,name, value,seq,'Asset')
                            sql_conn.commit()

                        logging.info("Asset Stage Table 'LSM_XML_Asset_Stg' loaded successfully")

            # -----------------------------------------------------------------
            # # LSM_XML_Liability_stg:
            #

                for Liability in URLA1003.iter('Liability'):
                    for k in Liability:
                        c_details = k.attrib
                        name = c_details.get('name')
                        value = c_details.get('value')
                        if name == None or name == '':
                            name = 'Unknown Name Field'
                            cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Liablty_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Num, Name, Value,LiabilitySeq#, FileType) VALUES (?,?,?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,Num,name, value,seq, 'Liability')
                            sql_conn.commit()
                        else:
                            cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Liablty_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Num, Name, Value,LiabilitySeq#, FileType) VALUES (?,?,?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,Num,name, value,seq, 'Liability')
                            sql_conn.commit()

                    logging.info("Liability Stage Table 'LSM_XML_Liability_stg' loaded successfully") 
            
            # -----------------------------------------------------------------
            # # LSM_XML_IntegratedDiscFees_stg:
            #
            for IntegratedDiscFees in root.iter('IntegratedDiscFees'):
                for x in IntegratedDiscFees:
                    i_details = x.attrib
                    name = i_details.get('name')
                    value = i_details.get('value')
                    if name == None or name == '':
                        name = 'Unknown Name Field'
                        cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_IntDisFee_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Name, Value,IDFSeq#, FileType) VALUES (?,?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,name, value,seq, 'IntegratedDiscFees')
                        sql_conn.commit()
                    else:
                        cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_IntDisFee_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Name, Value,IDFSeq#, FileType) VALUES (?,?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,name, value,seq, 'IntegratedDiscFees')
                        sql_conn.commit()

                logging.info("IntegratedDiscFees Stage Table 'LSM_XML_IntegratedDiscFees_Stg' loaded successfully")


            # -----------------------------------------------------------------
            # # LSM_XML_ClosingCost_stg:
            #
            for ClosCostQkDataEnt in root.iter('ClosCostQkDataEnt'):
                for x in ClosCostQkDataEnt:
                    i_details = x.attrib
                    name = i_details.get('name')
                    value = i_details.get('value')
                    if name == None or name == '':
                        name = 'Unknown Name Field'
                        cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_ClCost_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Name, Value,FileType) VALUES (?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,name, value, 'ClosingCost')
                        sql_conn.commit()
                    else:
                        cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_ClCost_Stg"] +"  (BatchID,LoanNum, CreateTs, LoanNumber, Name, Value,FileType) VALUES (?,?,?,?,?,?,?)", BatchID,LoanNum,CreateTs,loanNumber,name, value, 'ClosingCost')
                        sql_conn.commit()

                logging.info("ClosingCost Stage Table 'LSM_XML_ClosingCost_Stg' loaded successfully")
            

        except Exception as err:
            logging.error("File parsing failed for  "+filename +" with Error:"+str(err))
            return 0
        return 1
# ------------------------------------------------------------------------------------------------
# Description : Update the batch file to failed if XMLFilenames in the current run parsed
#               unsuccessfully 
# ------------------------------------------------------------------------------------------------

    def BatchFailed(self,filename):
        
        logging.info("Started updating the batch failed in 'XML_LSM_LDM_SourceFileList' for file : "+ filename)
        
        try:
            #Update the processed XML_Processing_Status to failed for the file failed in the current run 
            cursor.execute("Update "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +"  set XML_Processing_Status=?,Comments=? where XMLFileName=? and  XML_Processing_Status=?",'FAILED','Batch Failed',filename,'OPEN')
            sql_conn.commit()            
            
            logging.info("Updating the batch to failed in 'XML_LSM_LDM_SourceFileList' successfull for file : "+filename)
        
        except Exception as e:

            logging.error("Exception while Updating the 'XML_Processing_Status' to failed in 'XML_LSM_LDM_SourceFileList' for file: "+filename+"Error: "+str(e))
            

# ------------------------------------------------------------------------------------------------
# Description : Truncates stage tables for the current run hence strategy for stage load is
#               truncate and reload 
# ------------------------------------------------------------------------------------------------

    def TruncateStageTables(self):


        logging.info("*********Logging the details of TruncateStageTables: *********")
        logging.info("Started truncating the stage tables for Loandata ")
        try:

            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Loan_Stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LSM_Loan_Stg"])
            
            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Borrower_Stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LSM_Borrower_Stg"])

            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Income_Stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LSM_Income_Stg"])

            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Asset_Stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LSM_Asset_Stg"])

            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_Liablty_Stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LSM_Liablty_Stg"])

            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_IntDisFee_Stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LSM_IntDisFee_Stg"])

            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LSM_ClCost_Stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LSM_ClCost_Stg"])

            sql_conn.commit()
        
            logging.info("Truncating the stage tables for Loandata successful ")
        
        except Exception as e:
            
            logging.error("Exception while truncating the stage tables : "+str(e))

            raise


    # ------------------------------------------------------------------------------------------------
    # Description : Incase of parsing failure, the failed batch files are moved to unprocessed 
    #               directory.
    # ------------------------------------------------------------------------------------------------

    def BatchUnprocessed(self):

        try:
            logging.info("Get the Loan filelist which are batch FAILED from 'XML_LSM_LDM_SourceFileList' table :")
            
            #Checck for the failed batch in XML_LSM_LDM_SourceFileList
            data=cursor.execute("select XMLFileName from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" where XML_Processing_Status=? and XMLFileName like ?" ,'FAILED','%Loandata.xml')
            filelist=[]

            for row in data:
                filelist.append(row[0])

            #Moving the failed batch files to 'Unprocessed' directory
            for filename in filelist:

                logging.info(filename)
                if os.path.exists(src_file_path+filename)==True:
                    os.replace(src_file_path+filename, src_unprocessed_path+filename)
                
                logging.info("Filename with batch FAILED moved to Unprocessed directory successfully:"+filename)
        
        except Exception as e:

            logging.error("Exception while moving the batch failed to unprocessed directory: "+filename+"Error: "+str(e))        


if __name__ == '__main__':

    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y-%H-%M-%S"))

    dt = str(currentdate.strftime("%m%d%Y"))
    

    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
       config = yaml.safe_load(stream)    

    src_file_path = config["LoanLogics"]["Inbound"]
    log_file_path = config["LoanLogics"]["Log_Path"]
    archive_file_path = config["LoanLogics"]["Archive_Path"]
    src_unprocessed_path=config["LoanLogics"]["Unprocessed"]

    #Check for directories

    CHECK_INB_FOLDER = os.path.isdir(config["LoanLogics"]["Inbound"])
    if not CHECK_INB_FOLDER:
        os.makedirs(config["LoanLogics"]["Inbound"])
    else:
        pass
    CHECK_LOG_FOLDER = os.path.isdir(config["LoanLogics"]["Log_Path"])
    if not CHECK_LOG_FOLDER:
        os.makedirs(config["LoanLogics"]["Log_Path"])
    else:
        pass
    CHECK_ARCH_FOLDER = os.path.isdir(config["LoanLogics"]["Archive_Path"])
    if not CHECK_ARCH_FOLDER:
        os.makedirs(config["LoanLogics"]["Archive_Path"])
    else:
        pass
    CHECK_UNPROC_FOLDER = os.path.isdir(config["LoanLogics"]["Unprocessed"])
    if not CHECK_UNPROC_FOLDER:
        os.makedirs(config["LoanLogics"]["Unprocessed"])
    else:
        pass

    logging.basicConfig(filename=config["LoanLogics"]["Log_Path"] +"\\log_LoanLogics_Loandata_["+date+"].log", level=logging.INFO)
    

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
    
    loanlogicsobj = loanlogics(cursor, config, server, date)

    if sys.argv[1] == 'Loandata':

        loanlogicsobj.TruncateStageTables()
        loanlogicsobj.BatchOpen()
        loanlogicsobj.ProcessXmlFileList()
    
    
