import requests
IdList=['1562','1000','989']

#jnjvjnjvnsjn

for id in IdList:
    url = "https://na1.ai.dm-us.informaticacloud.com/active-bpel/rt/p_API_SSVR_getTradeDetails_Mailroom"
    payload = '{"tradeId":"'+id+'"}'
    headers = {
    'Authorization': 'Basic aW5mb3JtYXRpY2EtZGV2LmR3QHBubWFjLmNvbTpqallhSG8zZU1PaFY=',
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data = payload)
    print(str(response.text.encode('utf8'))+'  id: '+id )
#0012w00000LEHexAAH