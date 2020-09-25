
string = "admin01sdbsdhvsdbh"
add=''
for i in string:
    add= (str(add)+str(ord(i.lower())-96)).replace('-','')
print(add) 
