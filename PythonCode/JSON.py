import json 
with open ("C:\\Users\\dell\\Desktop\\Python\\Unstructure.JSON") as data_check:
    raw_data_chk = data_check.read()

with open ("C:\\Users\\dell\\Desktop\\Python\\Unstructure.json") as data:
    content = json.load(data)
    if  raw_data_chk.startswith('"{'):
        cnt = content.replace('Loan Strengths/Weaknesses":','LoanStrengthsWeaknesses":')
    else:
        cnt = raw_data_chk.replace('Loan Strengths/Weaknesses":','LoanStrengthsWeaknesses":')
    content = cnt.replace('Loan Strengths/Weaknesses":','LoanStrengthsWeaknesses":').replace('Risk/Eligibility":','RiskEligibility":').replace('Verification/Approval Conditions":','VerificationApprovalConditions":')
    f=open("C:\\Users\\dell\\Desktop\\Python\\structure.JSON","w")
    f.write(content)
    f.close
