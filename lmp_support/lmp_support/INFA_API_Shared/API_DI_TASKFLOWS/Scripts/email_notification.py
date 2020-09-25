# -------------------------------------------------------------------------------------------------------------
# Developer         : Poornima Joshi (Sonata Software Ltd)
# CreatedDate       : 10/08/2020
# Description       : Script used to send an email notification in case of failure by taking the API_name as
#                       input and reads the global config entries using the API_name
#                       Input: API_Name 
# ------------------------------------------------------------------------------------------------------------- 

import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
import sys
import os.path
import glob
import datetime
import yaml


def SendEmail(API_Name):
    try:
  
        currentdate = datetime.datetime.now()
        dt = str(currentdate.strftime("%m%d%Y"))
        
        with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
            config = yaml.safe_load(stream) 

        log_file_path = config[API_Name]["Log_Path"]
        
        logfiles=glob.glob(log_file_path+config[API_Name]["Log_file"]+"*.log")
        latest_file = max(logfiles, key=os.path.getctime)

        
        subject= API_Name+config[API_Name]["subject"]+dt
        body = config[API_Name]["body"]  
        receiver_email = config[API_Name]["receiver_email"]
        sender_email = config[API_Name]["sender_email"]  

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ','.join(receiver_email)
        smtpObj = smtplib.SMTP('smtp.aws.pnmac.com',25)
        message["Subject"] = subject
        
        message.attach(MIMEText(body, "plain"))

        Title=(os.path.splitext(os.path.basename(latest_file))[0])
        FileExtension="log"
        Filename="%s.%s" % (Title,FileExtension)
        Filepath = "%s%s" % (log_file_path,Filename)
                    
        with open(Filepath, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header("Content-Disposition",f"attachment; Filename= {'Error_Log.log'}",)
            message.attach(part)
            text = message.as_string()
            smtpObj.sendmail(sender_email, receiver_email, text)
        
        print("Email sent successfully...")


        
    except Exception as e:
        print("Sending Email Notification failed with exception: "+str(e))

    

