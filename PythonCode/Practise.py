import os 

FileList = os.listdir('C:\\Users\\dell\\Desktop\\IICSPractise')

for i in FileList :
    if i.endswith('csv') or i.endswith('x') :
        pass
    else:
        if '.' in i :
            with open ('C:\\Users\\dell\\Desktop\\IICSPractise\write.txt','a') as fileWrire:
                fileWrire.write(i+'\n')
                print(i+' is a file')

        else:
            print(i+' is a folder')
        