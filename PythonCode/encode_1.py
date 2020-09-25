import sys
sourceEncoding = "UTF-8 BOM"
targetEncoding = "UTF-8"
source = open("C:\\Users\\dell\\Downloads\\8125038235_20190308020500029_Loandata.xml")
target = open("C:\\Users\\dell\\Downloads\\8125038235_20190308020500029_Loandata_encode.xml", "w")

data=source.read()
encodedData=data.encode('UTF-8')
target.write(str(encodedData))

# s = content.read()
        # u = s.encode("utf-8")
        # data = str(u)
        # #data = unicode(str(content), "utf-8")
        # print(data)

# import chardet    
# rawdata = open('C:\\Users\\dell\\Downloads\\8125038235_20190308020500029_Loandata.xml', "r").read()
# #rawdata=bytes(123)
# result = chardet.detect((rawdata))
# charenc = result['encoding']
# print(str(charenc))