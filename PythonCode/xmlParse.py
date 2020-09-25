import xml.etree.ElementTree as ET
tree = ET.parse('country_data.xml')
root = tree.getroot()
#print(root.attrib)
for child in root:
     print (str(child.find('rank').text))
#for neighbor in root.iter('neighbor'):
     #print(neighbor.attrib)
print(root.findall('country'))
for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
     print(name, rank)