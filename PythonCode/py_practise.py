import os
import sys
#Contains full list of files of the given directory
directory = sys.argv[1]
fullList = os.listdir(directory)
fileList = []
folderList =[]
for item in fullList:
    if '.py' in item:
        fileList.append(item)
    else: 
        folderList.append(item)
print(fileList)
