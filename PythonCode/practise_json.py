import json
x={
'error': {
'code': 500,
'detail': {
'reason': '',
'code': '1',
'details': '{"Response":{"payLoad":"{\\"loan_id\\":\\"8c2e2c61-1eb3-4900-b9ba-12121\\"},"errorCode":"1","isSuccess":"False"}}'
},
'message': 'unknown fault'
}
}

#print("code",x['error']['detail']['code'])
print("message",(x['error']['detail']['details']))
#print("message",x['error']['message'])