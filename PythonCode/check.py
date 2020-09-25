import json 
with open ("C:\\Users\\dell\\Desktop\\Python\\du_messages (7).json") as data:
    try: 
        filedata = json.load(data)
        if("Loan Strengths/Weaknesses") in filedata["duMessages"]["messages"]:
            for lsw in filedata["duMessages"]["messages"]["Loan Strengths/Weaknesses"]:
                lenderMessageLineText = lsw["lenderMessageLine"]["text"],
                MsgTypeName = "Loan Strengths/Weaknesses"
                messageID = lsw["messageID"]
                messageName = lsw["messageName"]
                messageSubType1 =lsw["messageSubType1"]
                messageSubType2 = lsw["messageSubType2"]
                messageStructure =lsw["messageStructure"]   
        if("Observations") in filedata["duMessages"]["messages"]:
            for obs in filedata["duMessages"]["messages"]["Observations"]:
                lenderMessageLineText = obs["lenderMessageLine"]["text"],
                MsgTypeName = "Observations"
                messageID = obs["messageID"]
                messageName = obs["messageName"]
                messageSubType1 =obs["messageSubType1"]
                messageSubType2 = obs["messageSubType2"]
                messageStructure =obs["messageStructure"]
                
        if("PotentialRedFlags") in filedata["duMessages"]["messages"]:
            for pr in filedata["duMessages"]["messages"]["PotentialRedFlags"]:
                lenderMessageLineText = pr["lenderMessageLine"]["text"],
                MsgTypeName = "PotentialRedFlags"
                messageID = pr["messageID"]
                messageName = pr["messageName"]
                messageSubType1 =pr["messageSubType1"]
                messageSubType2 = pr["messageSubType2"]
                messageStructure =pr["messageStructure"]
               
        if("Risk/Eligibility") in filedata["duMessages"]["messages"]:
            for re in filedata["duMessages"]["messages"]["Risk/Eligibility"]:
                lenderMessageLineText = re["lenderMessageLine"]["text"],
                MsgTypeName = "Risk/Eligibility"
                messageID = re["messageID"]
                messageName = re["messageName"]
                messageSubType1 =re["messageSubType1"]
                messageSubType2 = re["messageSubType2"]
                messageStructure =re["messageStructure"]
                print(messageID)
        if("Verification/Approval Conditions") in filedata["duMessages"]["messages"]:
            for vac in filedata["duMessages"]["messages"]["Verification/Approval Conditions"]:
                lenderMessageLineText = vac["lenderMessageLine"]["text"],
                MsgTypeName = "Risk/Eligibility"
                messageID = vac["messageID"]
                messageName = vac["messageName"]
                messageSubType1 =vac["messageSubType1"]
                messageSubType2 = vac["messageSubType2"]
                messageStructure =vac["messageStructure"]
                print(messageID)
        if("CollateralUnderwriter") in filedata["duMessages"]["messages"]:
            for cu in filedata["duMessages"]["messages"]["CollateralUnderwriter"]:
                lenderMessageLineText = cu["lenderMessageLine"]["text"],
                MsgTypeName = "Risk/Eligibility"
                messageID = cu["messageID"]
                messageName = cu["messageName"]
                messageSubType1 =cu["messageSubType1"]
                messageSubType2 = cu["messageSubType2"]
                messageStructure =cu["messageStructure"]
                print(messageID)
        if("LenderGuidanceforApplicants") in filedata["duMessages"]["messages"]:
            for lga in filedata["duMessages"]["messages"]["LenderGuidanceforApplicants"]:
                lenderMessageLineText = lga["lenderMessageLine"]["text"],
                MsgTypeName = "Risk/Eligibility"
                messageID = lga["messageID"]
                messageName = lga["messageName"]
                messageSubType1 =lga["messageSubType1"]
                messageSubType2 = lga["messageSubType2"]
                messageStructure =lga["messageStructure"]	
        			
    except Exception as error:
        print(str(error))
     


