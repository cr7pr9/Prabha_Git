# Program to convert an xml 
# file to json file 
  
# import json module and xmltodict 
# module provided by python 
import json 
import xmltodict
import sys
   
 
      
data_dict = xmltodict.parse(sys.args[1]) 
    
json_data = json.dumps(data_dict)  
      
    # Write the json data to output  
    # json file 
with open("C:\\Users\\dell\\Desktop\\Python\\data1.json", "w") as json_file: 
    
    json_file.write(json_data) 
    json_file.close() 
   # '<breakfast_menu><food><name>Belgian Waffles</name><price>$5.95</price><description>Two of our famous Belgian Waffles with plenty of real maple syrup</description><calories>650</calories></food></breakfast_menu>'
    