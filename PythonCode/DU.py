import pyodbc
import json
import datetime
import os

#logging.basicConfig(filename=config["DesktopUnderwriter"]["Log_DU"]+"\\log_dumessages_jsonedit_["+date+"].log", level=logging.INFO)
arr = os.listdir("C:\\Users\\dell\\Desktop\\DeploymentDocs\\du_processed\\")
for filename in arr:
            try:
                if filename.startswith("du_messages"):
                    with open("C:\\Users\\dell\\Desktop\\DeploymentDocs\\du_processed\\"+filename) as filedata:
                        data= filedata.read()
                        filedata = open("C:\\Users\\dell\\Desktop\\DeploymentDocs\\du_processed\\\\"+filename, "w")
                        filedata.write(data)
                        filedata.close()
                        logging.info("Json file edited without errors "+str(filename))
            except Exception as error:
                #logging.error("Json file "+str(filename)+" caught with exception "+str(error))
                pass