import sys
import json
import os
import yaml

with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
    config = yaml.safe_load(stream)

file_path=config["Path"]["Inbound_STIP"]

get_stip = []
get_users=[]
for path in os.listdir(file_path):
    if path.startswith("get_stipdetails_"):
        full_path_get_all = os.path.join(file_path, path)
        if os.path.isfile(full_path_get_all):
            get_stip.append(full_path_get_all)
    if path.startswith("get_stipdetailsusers"):
        full_path_get_all = os.path.join(file_path, path)
        if os.path.isfile(full_path_get_all):
            get_users.append(full_path_get_all)
        
         
header = "PATH\n"
data = open(config["Path"]["Path_Files"]+"\\stipdetails_sample.txt", "w")
data.write(header)
for path in get_stip:
    data.write(path+"\n")
data.close()
data_users = open(config["Path"]["Path_Files"]+"\\stipdetailsusers_sample.txt", "w")
data_users.write(header)
for path in get_users:
    data_users.write(path+"\n")
data_users.close()


