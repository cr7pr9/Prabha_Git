# -------------------------------------------------------------------------------------------------------------
# Developer Name : Poornima Joshi (Sonata Software)
# Date : 21/08/2020
# Description : Downloads xml files from AWS S3 bucket by reading the inputs from Even Bridge using
#               Lambda handler and stores into the Inbound directory
#               Arguments:
#               Args_1:LoanID
#               Args_2:BucketName
#               Args_3:Path&Filename to Loandata.xml
#               Args_4:Path&Filename to LoanDocMetadata.xml
# -------------------------------------------------------------------------------------------------------------

import os
from os import path
import boto3
import yaml
import sys
import datetime
import logging

def DownloadXmlFiles(loan_id,bucket,xml_key,xml_meta_key):

    #check if the Indound dir is presnt
    CHECK_FOLDER = os.path.isdir(config["LoanLogics"]["Inbound"])
    if not CHECK_FOLDER:
        os.makedirs(config["LoanLogics"]["Inbound"])
    else:
        pass 

    logging.info("Started downloading the files from S3")

    try:
        s3 = boto3.resource('s3')
        loan_file = xml_key.split('/')
        loan_metadata_file= xml_meta_key.split('/')
        my_bucket = s3.Bucket(bucket)
        s3.Bucket(bucket).download_file(xml_key,dest_file_path+loan_file[3])
        s3.Bucket(bucket).download_file(xml_meta_key,dest_file_path+loan_metadata_file[3])

        logging.info("Imported the files " +xml_key +" and " + xml_meta_key + " onto Indound Directorty." )

    
    except Exception as e:
        
        logging.error("Caught with an Exception during import :" + str(e))
        
        raise
        
if __name__ == '__main__':

    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y-%H-%M-%S")) 

    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
       config = yaml.safe_load(stream)    

    dest_file_path = config["LoanLogics"]["Inbound"]
    log_file_path = config["LoanLogics"]["Log_Path"]

        
    logging.basicConfig(filename=config["LoanLogics"]["Log_Path"] +
                    "\\log_LoanLogic_DownloadS3XmlFiles_["+date+"].log", level=logging.INFO)


    #Calling the module to downlaod the files from S3 location

    DownloadXmlFiles(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
