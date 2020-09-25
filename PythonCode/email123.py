import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64
import sys
import os.path
Attachment3 = MIMEMultipart()
Attachment3["From"] = "noreply@pnmac.com"
Attachment3["To"] = "prabhakar.boddapati@pnmac.com"
smtpObj = smtplib.SMTP('smtp.aws.pnmac.com',25)
Attachment3["Subject"] = "error email"
body="attached is error file"
Attachment3.attach(MIMEText(body, "plain"))
with open('C:\\Users\\dell\\Desktop\\MyFiles\\Start.SQL', "rb") as attachment:
    print("entered")
    part = MIMEBase("application", "octet-stream")   
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition",f"attachment; Filename= {'Jira.csv'}",)
    Attachment3.attach(part)
    text1 = Attachment3.as_string()
                        #Call Email Function for VersionData notifications to end users
    smtpObj.sendmail(Attachment3["From"], Attachment3["To"], text1)   # sending email with attachment   
