import os
import shutil
from os import path
import subprocess
import json

path = "C:\\Users\\informatica\\Kanan\\DESKTOP"
test_path = "C:\\Users\\informatica\\lmp_support\\DesktopUnderwriter"
fileName="du_messages"

env = os.environ['APP_ENV']

CHECK_FOLDER = os.path.isdir(path)
if not CHECK_FOLDER:
    os.makedirs(path)
else:
    pass

process = subprocess.Popen(r'aws s3 cp s3://kanan-tpi-object-store-'+env+' C:\\Users\\informatica\\Kanan\\DESKTOP --exclude "*ServiceLink/*" --exclude "*TPIExecutables/*" --exclude "*ValuationPartners/*" --exclude "*XML_Success/*" --exclude "*foldersweep/*" --exclude "*income-verification/*" --exclude "*archive/*" --exclude "*compliance-review/*" --exclude "*loantools/*" --exclude "*logs/*" --exclude "*tdm_logs/*" --exclude "*transfer/*"  --exclude "*.zip" --recursive ')
try:
    print('Running in process', process.pid)
    process.wait(timeout=10)
except subprocess.TimeoutExpired:
    print('Timed out - killing', process.pid)
    process.kill()
print("Done")

list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir()]
dir_list = next(os.walk(path))[1]

print(list_subfolders_with_paths)
print(dir_list)
test_path
for files in list_subfolders_with_paths:
    arr = os.listdir(files)
    for file in arr:
        if file.startswith(fileName):
            print(len(path))
            #os.rename(files+"\\"+file ,test_path+"\\"+"default_json_"+files[len(path)+1:]+".json")
            with open(files+"\\"+file) as filedata:
                data = str(json.load(filedata))
                f = open(test_path+"\\du_messages_"+files[len(path)+1:]+".json", "w")
                f.write(data)
                f.close()

for folder in list_subfolders_with_paths:
    arr = os.listdir(files)
    for file in arr:
        try: 
            os.remove(folder+"\\"+file) 
        except OSError as error: 
            print(error) 
    try:
        os.rmdir(folder)
    except OSError as error:
        print(error)

os.rmdir(path)

filenmelist =[]
list = []
for path in os.listdir(test_path):
    full_path = os.path.join(test_path, path)
    if os.path.isfile(full_path):
        print(full_path)
        list.append(full_path)

head = "PATH\n"
dev = open(test_path+"\\samplepath.txt", "w")
dev.write(head)
for data in list:
    dev.write(data+"\n")
dev.close()
