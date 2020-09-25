# -------------------------------------------------------------------------------------------------------------
# Developer Name    : Poornima Joshi (Sonata Software Ltd)
# Date              : 21/08/2020
# Description       : Reads the LoanDocMetaData XML files from the Inbound directory and inserts data by parsing 
#                       the XML files into stage tables below which is controlled by the batch-process.
#                       LDM_XML_DocData_Stg
#                       LSM_XML_Finding_Stg
#
# ------------------------------------------------------------------------------------------------------------

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
# Description : Class "loanlogics" contains methods "BatchOpen","ProcessMetadataXmlFileList",,"BatchFailed"
#               "ParsingLoanMetaDataXml","TruncateStageTables" and "BatchUnprocessed" where these methods reads 
#               filenames from Inbound diectory and writes an entry in "XML_LSM_LDM_SourceFileList" as OPEN for 
#		        processing,Parses and loads the data into stage tables. Post succesfull completion archives  
#		        files into to Archival directory and failed files are moved to Unprocesses directory. At last 
#               batches are updated as FAILED or COMPLETED based on run status in table "XML_LSM_LDM_SourceFileList"
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

        logging.info("Script: LoanLogics_MetadataXml_Load.py")
        logging.info("*********Logging the details of Batchopen process of LoanDocMetadata*********")
        logging.info("Batch Table  'XML_LSM_LDM_SourceFileList' Insert:")

        try:
            list_processed = []
            arr = os.listdir(src_file_path)
            
            #List *LoanDocMetaData.xml files from Inbound Dir
            for filenames in arr:
                if filenames.endswith ('LoanDocMetaData.xml'):
                    list_processed.append(filenames)
            
            #Check if no files for processing in current run, then exit the process
            if not list_processed:
                logging.info("There are no LoanDocMetaData xml files with batch status as OPEN in current run")
                sys.exit()
            else:
                pass

            for filename in list_processed:
                logging.info("Checking for the status of the file " +filename +" in 'XML_LSM_LDM_SourceFileList' table ")
                
                cursor.execute("select XML_Processing_Status,IICS_Processing_Status from  "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" where XMLFileName=? and XML_Processing_Status !=? and XMLFileName like ? ",filename,'OPEN','%LoanDocMetaData.xml')
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

                            cursor.execute("Update  "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" set XML_Processing_Status=?,StartDateTime=? where XMLFileName=? ",'OPEN',time.strftime('%Y-%m-%d %H:%M:%S'),filename)
                            sql_conn.commit()
                            
            logging.info("Insert/Update to 'XML_LSM_LDM_SourceFileList' table based on Batch Status successful")
        
        except Exception as error:
            
            logging.error("Listing and inserting LoanMetadata files to 'XML_LSM_LDM_SourceFileList' caught with exception %s"+str(error))
            raise

# ------------------------------------------------------------------------------------------------
# Description : Read the XMLFilenames from the XML_LSM_LDM_SourceFileList which are "OPEN" for parsing
#               and calls the module to insert content of LoanDocMeatadata into stage tables
# ------------------------------------------------------------------------------------------------


    def ProcessMetadataXmlFileList(self):

        logging.info("*********Logging the details of ProcessXmlFileList: *********")
        logging.info("Processing the LoanMetadata xml files in 'XML_LSM_LDM_SourceFileList' table status as OPEN.")
        
        try:
            
            logging.info("Get the filelist,BatchID which are batch OPEN from 'XML_LSM_LDM_SourceFileList' table and loop:")
            
            cursor.execute("select BatchID,StartDateTime,XMLFileName from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +"  where XML_Processing_Status=? and XMLFileName like ?" ,'OPEN','%LoanDocMetaData.xml')
            rows = list( cursor )
            for data in rows:
                BatchID=data[0]
                CreateTs=data[1]
                filename=data[2]

                logging.info(filename) 

                content = open(config["LoanLogics"]["Inbound"]+filename, mode='r', encoding='utf-8-sig').read()
                open(config["LoanLogics"]["Inbound"]+filename , mode='w', encoding='utf-8').write(content)

                #Start the stage table insert by parsing the xml file

                LDM_xmlparse=loanlogicsobj.ParsingLoanMetaDataXml(filename,BatchID,CreateTs)
                
                #Get the return code from parse and DB insert, 1 for success, 0 for failure
                if LDM_xmlparse==1:

                    logging.info("File parsing completed for: "+filename)
                    logging.info("Updating the batch to completed for "+filename)

                    cursor.execute("Update "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" set XML_Processing_Status=?,Comments=? where XMLFileName=?",'COMPLETED','Stage Load Successful',filename)
                    sql_conn.commit()
                    logging.info("Batch completed successfully for  " +filename)

                else:
                    
                    logging.error("Caught with an Exception while parsing the file: "+filename)
            
                    loanlogicsobj.BatchFailed(filename)

                    logging.info("Updated the batch to failed for file successfully:"+filename)

                    loanlogicsobj.BatchUnprocessed()

                    logging.info("Moved the batch failed to unprocessed directory successfully:"+filename)

                    SendEmail('LoanLogics')

                    logging.info("Successfully sent an email nofication in case of file parsing failure ")

                    sys.exit(1)
       
                
        except Exception as e: 

            logging.error("Caught with an Exception while processing file: "+filename + "Error: "+str(e))

            raise


# ------------------------------------------------------------------------------------------------
# Description : Parse the xml files which are listed in XML_LSM_LDM_SourceFileList table taking the 
#               input as xmlfilename and inserts data into LDM_XML_Finding_Stg,LDM_XML_DocData_Stg       
# @Input : filename,CreateTs,BatchID
# ------------------------------------------------------------------------------------------------

    def ParsingLoanMetaDataXml(self,filename,BatchID,CreateTs):
   
        logging.info("Started parsing the LoanDocMetadaData XML file : %s", str(filename))

        #Initilization
        ClientID=None
        ClientName=None
        LoanNumber=None
        LoanId=None
        ProductId=None
        Description=None
        Status=None
        FindingTypeCode=None
        LoanFindingID=None
        DocumentDate=None
        DocumentId=None
        DocumentTypeId=None
        VersionId=None
        DocumentName=None
        PageStart=None
        PageStop=None
        IsMissing=None
        Name=None
        DescriptorID=None
        Value=None

        try :

            tree = ET.parse(src_file_path+filename)
            root = tree.getroot()
            
            # -----------------------------------------------------------------
            # LDM_XML_Finding_Stg Load
            #
            logging.info("Loading the LDM_XML_Finding_Stg table.. ")
            
            for i in root.iter():
                if i.tag=='ClientID':
                    ClientID=i.text
                if i.tag=='ClientName' :
                    ClientName=i.text
                if i.tag=='ProductId':
                    ProductId=i.text
                if i.tag=='LoanNumber':
                    LoanNumber=i.text
                    LoanNum=LoanNumber[0:10]
                if i.tag=='LoanId':
                    LoanId=i.text

                
                #Load for 'Findings' details
                if i.tag=='Findings':
                    for fi in i.iter("Findings"):
                        for fn in i.iter("Finding"):
                            f_details=fn.attrib
                            Description=f_details.get('Description')
                            Status=f_details.get('Status')
                            FindingTypeCode=f_details.get('FindingTypeCode')
                            LoanFindingID=f_details.get('LoanFindingID')
                            cursor.execute("INSERT INTO " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LDM_Finding_stg"]+ "(LoanNum,CreateTs, ClientID, ClientName, LoanNumber, LoanId, ProductId, Description, Status, FindingTypeCode, LoanFindingID, FileType,BatchID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", LoanNum,CreateTs,ClientID, ClientName, LoanNumber, LoanId, ProductId, Description, Status, FindingTypeCode, LoanFindingID,'Finding',BatchID)
                            sql_conn.commit()
                    logging.info("Loading the LDM_XML_Finding_Stg table successful.. ")

            # -----------------------------------------------------------------
            # LDM_XML_DocData_Stg Load: -Insert 1
            #            
                logging.info("Loading the LDM_XML_DocData_Stg table.. ")

                #Load for 'CombinedImageFile' and 'Documents' details:

                if i.tag=="CombinedImageFile":
                    for cif in i.iter("CombinedImageFile"):
                        FileName=cif.findtext("FileName")
                        for j in i.iter("Documents"):
                            for k in j.iter("Image"):
                                DocumentDate=k.attrib["DocumentDate"]
                                DocumentId=k.attrib["DocumentId"]
                                DocumentTypeId=k.attrib["DocumentTypeId"]
                                VersionId=k.attrib["VersionId"]
                                
                                DocumentName=k.findtext("DocumentName")
                                PageStart=k.findtext("PageStart")
                                PageStop=k.findtext("PageStop")
                                IsMissing=k.findtext("IsMissing")
                                
                                logging.info("Reading Docdata Details... ")
                                for l in k.iter("DocData"):
                                    Name=l.attrib["Name"]
                                    Value=l.attrib["Value"]
                                    DescriptorID=l.attrib["DescriptorID"]
                                
                                    cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LDM_DocData_stg"]+"(LoanNum,CreateTs,ID, ClientID, ClientName, LoanNumber, LoanId, ProductId, FileName, DocumentDate, DocumentId, DocumentTypeId, VersionId,DocumentName,PageStart,PageStop, IsMissing,DescriptorID,Name,Value,FileType,BatchID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", LoanNum,CreateTs,0,ClientID, ClientName,  LoanNumber, LoanId, ProductId, FileName, DocumentDate, DocumentId, DocumentTypeId, VersionId,DocumentName,PageStart,PageStop, IsMissing,DescriptorID,Name,Value,'DocData',BatchID)
                                    sql_conn.commit()
                                
                    logging.info("Loading the LDM_XML_DocData_Stg table successful for the records with Docdata info.. ")
            
            # --------------------------------------------------------------------------------------------
            # LDM_XML_DocData_Stg Load:Insert(For Missing indicators)uses below values when no docdata tag
            # DescriptorID = 0
            # Name = 'LoanLogics is Document Missing Indicator'                

                if i.tag=="CombinedImageFile":
                    for cif in i.iter("CombinedImageFile"):
                        FileName=cif.findtext("FileName")
                        for j in i.iter("Documents"):
                            for k in j.iter("Image"):
                                DocumentDate=k.attrib["DocumentDate"]
                                DocumentId=k.attrib["DocumentId"]
                                DocumentTypeId=k.attrib["DocumentTypeId"]
                                VersionId=k.attrib["VersionId"]
                               
                                DocumentName=k.findtext("DocumentName")
                                PageStart=k.findtext("PageStart")
                                PageStop=k.findtext("PageStop")
                                IsMissing=k.findtext("IsMissing")
                        
                                DescriptorID = 0
                                Name = 'LoanLogics is Document Missing Indicator'
                                Value = IsMissing
                                
                                cursor.execute("INSERT INTO  " +server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LDM_DocData_stg"]+"(LoanNum,CreateTs,ID, ClientID, ClientName, LoanNumber, LoanId, ProductId, FileName, DocumentDate, DocumentId, DocumentTypeId, VersionId,DocumentName,PageStart,PageStop, IsMissing,DescriptorID,Name,Value,FileType,BatchID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", LoanNum,CreateTs,0,ClientID, ClientName,  LoanNumber, LoanId, ProductId, FileName, DocumentDate, DocumentId, DocumentTypeId, VersionId,DocumentName,PageStart,PageStop, IsMissing,DescriptorID,Name,Value,'DocData',BatchID)
                                sql_conn.commit()
                            
                    logging.info("Loading the LDM_XML_DocData_Stg table successful for the records with 'Document Missing Indicator' .. ")

                    
            logging.info("Stage table load completed for LoanDocMetadata.")
                
            
        except Exception as err:
            logging.error("Caught with an exception while parsing "+filename+ "Error:" + str(err) )
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

            logging.error("Exception while Updating the batch to failed in 'XML_LSM_LDM_SourceFileList' for file: "+filename+"Error: "+str(e))


# ------------------------------------------------------------------------------------------------
# Description : Truncates stage tables for the current run hence strategy for stage load is
#               truncate and reload 
# ------------------------------------------------------------------------------------------------


    def TruncateStageTable(self):

        logging.info("*********Logging the details of TruncateStageTables: *********")
        logging.info("Started truncating the stage tables for LoanDocMetadata ")

        try:
            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LDM_DocData_stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LDM_DocData_stg"])

            cursor.execute("delete from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LDM_Finding_stg"])
            logging.info("Successfully truncated table:" + config["LoanLogics"]["tb_LDM_Finding_stg"])
            
            sql_conn.commit()
            
            logging.info("Truncating the stage tables for LoanDocMetadata successful ")
        
        except Exception as e:

            logging.error("Exception while truncating the stage tables : "+str(e))

            raise

# ------------------------------------------------------------------------------------------------
# Description : Incase of parsing failure, the failed batch files are moved to unprocessed 
#               directory.
# ------------------------------------------------------------------------------------------------


    def BatchUnprocessed(self):

        try:
            logging.info("Get the LoanMetaData filelist which are batch FAILED from 'XML_LSM_LDM_SourceFileList' table :")
            
            #Checck for the failed batch in XML_LSM_LDM_SourceFileList
            data=cursor.execute("select XMLFileName from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["LoanLogics"]["tb_LoanLogics_SrcList"] +" where XML_Processing_Status=? and XMLFileName like ?" ,'FAILED','%LoanDocMetaData.xml')
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

    logging.basicConfig(filename=config["LoanLogics"]["Log_Path"] +"\\log_LoanLogics_LoanDocMetaData_["+date+"].log", level=logging.INFO)

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
    

    if sys.argv[1]=='LoanDocMetaData':

        loanlogicsobj.TruncateStageTable()
        loanlogicsobj.BatchOpen()
        loanlogicsobj.ProcessMetadataXmlFileList()
