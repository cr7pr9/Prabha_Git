import requests

url = "https://na1.ai.dm-us.informaticacloud.com/active-bpel/rt/p_ssvr_ClientConfig_Mailroom"

payload = "{\"orgId\":\"204\"}"
headers = {
  'Authorization': 'Basic aW5mb3JtYXRpY2EtZGV2LmR3QHBubWFjLmNvbTpqallhSG8zZU1PaFY=',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
