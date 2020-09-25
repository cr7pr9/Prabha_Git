import json 
with open ("C:\\Users\\dell\\Desktop\\Python\\du_messages (7).json") as data:
    try: 
        filedata = json.load(data)
        for lsw in filedata["duMessages"]["messages"]["Loan Strengths/Weaknesses"]:
            if("lenderParameter") in lsw:
                for lp in lsw["lenderParameter"]:
                    parameterValue= dict(lp).get("parameterValue")
                    parameterName = dict(lp).get("parameterName")
                    parameterNumber= dict(lp).get("parameterNumber")
    except Exception as err:
        print(err)