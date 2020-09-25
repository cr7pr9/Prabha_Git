import json 
with open ("C:\\Users\\dell\\Desktop\\Python\\du_messages (7).json") as data:

#Inset into JOB Table ( batchid, job name, status ) values (1,"DU","Open")

    try: 
        filedata = json.load(data)
        if("Loan Strengths/Weaknesses") in filedata["duMessages"]["messages"]:
            for lsw in filedata["duMessages"]["messages"]["Loan Strengths/Weaknesses"]:
                lenderMessageLineText = lsw["lenderMessageLine"]["text"]
                print(MsgTypeName)
                MsgTypeName = "Loan Strengths/Weaknesses"
                    
        #insert into DU_LonData()
        #Insrt into Control Table()
        print("ControlTable")
        
    except Exception as error:
        print((error))
     


