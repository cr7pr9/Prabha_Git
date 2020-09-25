import json
from dateutil.parser import parse
import datetime
from datetime import datetime

with open ('C:\\Users\\dell\\Desktop\\PD\\Client\\getAllEntities_50.JSON') as filedata:
    data = json.load(filedata)
    if data.get('warehouse',{}).get("warehouseBankDetails", []):
        for i in range(0,len(data.get('warehouse',{}).get("warehouseBankDetails", []))) :
            WH_Data=data.get('warehouse',{}).get("warehouseBankDetails", [])[i]
            ClientID=data.get('basicInfo',{}).get('orgId',None)
            ClientName=data.get('basicInfo',{}).get('organizationName',None)
            ClientName_ID = (str(ClientName).upper()+'_'+str(ClientID)).replace('NONE','').replace('None','')
            BenificiaryDtls=WH_Data.get('description',None)
            FurhterCreditAccountName=WH_Data.get('creditAccountName',None)
            FurhterCreditAccountNumber=WH_Data.get('creditA ccountNumber',None)
            WHBankTimeZone= data.get('basicInfo',{}).get('timeZone',None) 
            AccountNumber=WH_Data.get('accountNumber',None) 
            AccountName=str(WH_Data.get('accountName',None)).upper().replace('NONE','')
            Name=WH_Data.get('contactname',None)
            if Name==None:
                WarehouseContactFirstName=None
                WarehouseContactLastName=None
            elif Name != None and len(Name.split())>1:
                WarehouseContactFirstName=Name.split()[0]
                WarehouseContactLastName=''
            else:
                WarehouseContactFirstName=Name.split()[0]
                WarehouseContactLastName=Name.split[1]
            WarehourseContactEmail=WH_Data.get('contactEmail',None)
            WarehouseContactPhone=WH_Data.get('contactPhone',None)
            WarehouseContactFaxNumber=WH_Data.get('contactFax',None)
            if WH_Data.get('isApproved',None)== True:
                WarehouseApprovedCheckbox='APPR'
            else:
                WarehouseApprovedCheckbox='NAPR'
            WarehouseStatusDate=str(parse(WH_Data.get('statusDate',None)).date())
            WarehouseBankID=WH_Data.get('warehouseBankId',None)
            ExternalOrgID=data.get('basicInfo',{}).get('id',None)
            AbaNumber=WH_Data.get('abaNumber',None)
            BankName=WH_Data.get('bankName',None)
            Address1=WH_Data.get('address1',None)
            Address2=WH_Data.get('address2',None)
            City=WH_Data.get('city',None)
            State=WH_Data.get('state',None)
            Zip=WH_Data.get('zip',None)
            AppSource='EM'
            isApproved=str(WH_Data.get('isApproved',None)).lower()
            print(isApproved)
            query="INSERT INTO clg_reporting.los_pcg.los_pcg_Warehouse_Client_Info_stg (AbaNumber ,AccountName ,AccountNumber ,Address1 ,Address2 ,BankName ,BenificiaryDtls ,City ,ClientID ,ClientName ,ClientName_ID ,ExternalOrgId ,FurhterCreditAccountName ,FurhterCreditAccountNumber ,State ,WHBankTimeZone ,WarehourseContactEmail ,WarehouseApprovedCheckbox ,WarehouseBankID ,WarehouseContactFaxNumber ,WarehouseContactFirstName ,WarehouseContactLastName ,WarehouseContactPhone ,WarehouseStatusDate ,Zip ,isApproved,BatchId,Warehouse_Seq_Key) Values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            params=(AbaNumber ,AccountName ,AccountNumber ,Address1 ,Address2 ,BankName ,BenificiaryDtls ,City ,ClientID ,ClientName ,ClientName_ID ,ExternalOrgID ,FurhterCreditAccountName ,FurhterCreditAccountNumber ,State ,WHBankTimeZone ,WarehourseContactEmail ,WarehouseApprovedCheckbox ,WarehouseBankID ,WarehouseContactFaxNumber ,WarehouseContactFirstName ,WarehouseContactLastName ,WarehouseContactPhone ,WarehouseStatusDate ,Zip ,isApproved,BatchId,SeqNum)