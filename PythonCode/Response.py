import json
# x={
    # "error": {
        # "code": 500,
        # "detail": {
            # "reason": "",
            # "code": "{\"Response\":{\"code\":\"1\",\"message\":\"Loan Logics Python Script Error\",\"isSuccess\":\"False\"}}",
            # "details": ""
        # },
        # "message": "unknown fault"
    # }
# }

# x={
    # "error": {
        # "code": 500,
        # "detail": {
            # "reason": "",
            # "code": "{\"Response\":{\"code\":\"HTTP_404\",\"message\":\"{\\\"code\\\":\\\"SMOS-102\\\",\\\"summary\\\":\\\"No HTTP resource was found that matches the request URI.\\\"}\",\"isSuccess\":\"False\"}}",
            # "details": ""
        # },
        # "message": "unknown fault"
    # }
# }

x={
    "error": {
        "code": 500,
        "detail": {
            "reason": "",
            "code": "{\"Response\":{\"code\":\"HTTP_404\",\"message\":\"\",\"isSuccess\":\"False\"}}",
            "details": ""
        },
        "message": "unknown fault"
    }
}
a=x['error']['detail']['code']

b=x['error']['detail']['code']

c=b.replace('{"Response":','')

d=c[:-1]
e=json.loads(d)
#print(e)
#print(e['code'],e['message'],e['iSuccess'])
print(e['isSuccess'])
print(e['code'])
print(e['message'])
