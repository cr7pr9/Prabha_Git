from simple_salesforce import Salesforce
import json
sf = Salesforce(username='prabha.boddapati4@gmail.com', password='Prabha@0409', security_token='52INtn8s2AstLy8nNpCZTtXe')
data = sf.query("Select Name,Id  from Account where Id ='0012w00000LzKcUAAV'")
put_dict=json.loads(json.dumps(data))
print(put_dict['records'][0]['Name'])