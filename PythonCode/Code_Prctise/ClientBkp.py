import json
from dateutil.parser import parse
with open ('C:\\Users\\dell\\Desktop\\PD\\Client\\getAllEntities_4.JSON') as filedata:
    data = json.load(filedata)
    DateOfFinancials = data.get('basicInfo',{}).get('businessInformation',{}).get('financialsLastUpdate',None)
    ClientApprovalDate = data.get('basicInfo',{}).get('approvalStatus',{}).get('approvedDate',None)
    AccountManager  = data.get('basicInfo',{}).get('primarySalesRepAe',{}).get('name',None)
    AccountManagerEffectiveDate = data.get('basicInfo',{}).get('primarySalesRepAe',{}).get('assignedDate',None)
    EIN =  data.get('basicInfo',{}).get('businessInformation',{}).get('taxId',None)
    if data.get('basicInfo',{}).get('approvalStatus',{}).get('currentStatus',None) == 'Active':
        ActiveStatus = 'Y'
    else:
        ActiveStatus = 'N'
    ClientAddress1=data.get('basicInfo',{}).get('address',{}).get('street1',None)
    ClientCity = data.get('basicInfo',{}).get('address',{}).get('city',None)
    #print(ClientCity)
    ClientID =data.get('basicInfo',{}).get('orgId',None)
    #print(ClientID)
    ClientName =data.get('basicInfo',{}).get('organizationName',None)
    #print(ClientName)
    ClientName_ID = ClientName.upper()+'_'+ClientID
    #print(ClientName_ID)
    ClientOriginalApprovalDate = data.get('basicInfo',{}).get('approvalStatus',{}).get('applicationDate',None)
    #print(ClientOriginalApprovalDate)
    ClientState = data.get('basicInfo',{}).get('address',{}).get('state',None)
    #print(ClientState)
    ClientStatusDate = data.get('basicInfo',{}).get('approvalStatus',{}).get('currentStatusDate',None)
    #print(ClientStatusDate)
    ClientZip=data.get('basicInfo',{}).get('address',{}).get('zip',None)
    #print(ClientZip)
    CompPh = data.get('basicInfo',{}).get('phoneNumber',None)
    #print(CompPh)
    if data.get('commitments',{}).get('deliveryTypes',[]):
        for i in data.get('commitments',{}).get('deliveryTypes',[]):
            if i['deliveryType']=='Bulk':
                DelMethBulkInd = 'Y'
            else:
                DelMethBulkInd = None
    else:
       DelMethBulkInd = None

    #Assigning default values to custom fields 

    ClientStatus=None
    ClientSecStatus=None
    ClientStatusGroup='INACTIVE'
    CorrespondentInd = 'N'
    SecondaryStsCd=None
    FHA203KApproved='N'
    HomeStyleIND='N'
    JumboApproved='N'
    JUMBOUndwType=None
    ProdFeatureTexasInd=None
    StatusReasons=None
    ThirdPartyOrigination='N'
    USDAOTCApproved=None
    OnboardingDate=None
    AutomatedIndexing=None
    DDFTier=None
    #VW_Authority has to be checked
    #Verification of the below fields is yet to be done
    SecurityReleaseRequirements=None
    OriginationMethod=None
    client_203K=None



    #starting custom fields
    for customFields in data.get('customFields',{}).get('fields',{}):
        if customFields['fieldName'] == 'Secondary Status':
            ClientSecStatus = customFields.get('fieldValue',None).upper()
        if customFields['fieldName'] == 'Primary Status':
            if customFields.get('fieldValue',None) == 'Approved':
                ClientStatus ='Approved'
            elif customFields.get('fieldValue',None) == 'Not Approved':
                ClientStatus ='Not Approved'
            elif customFields.get('fieldValue',None) == 'Prospect':
                ClientStatus ='Prospect'
            elif customFields.get('fieldValue',None) == 'Suspend - Allow Loan submisssions for Active locks':
                ClientStatus ='SUSPEND-ALLOW LOAN SUBMISSIONS FOR ACTIVE LOCKS'
            elif customFields.get('fieldValue',None) == 'Suspend - Disallow New loan Submissions':
                ClientStatus ='SUSPEND-DISALLOW NEW LOAN SUBMISSIONS'
            elif customFields.get('fieldValue',None) == "Terminated with AR's":
                ClientStatus ="TERMINATED - WITH AR'S"
            elif customFields.get('fieldValue',None) == "Terminate":
                ClientStatus = 'Terminated'
            else:
                ClientStatus =None
            if 'Test' in ClientName or ClientName== 'APPLE CORRESPONDENTS':
                ClientStatusGroup = 'Test Client'
            elif customFields.get('fieldValue',None) == "Approved":
                ClientStatusGroup = 'ACTIVE' 
            elif customFields.get('fieldValue',None) == "Prospect":
                ClientStatusGroup = 'Prospect'
            else:
                ClientStatusGroup = 'INACTIVE'
            
        if customFields['fieldName'] == 'Origination Method':
            if customFields['fieldValue']=='Correspondent' or customFields['fieldValue']=='Both':
                CorrespondentInd ='Y'
                ThirdPartyOrigination='Y'
            else:
                CorrespondentInd ='N'
            if customFields['fieldValue']=='Third Party Origination' or customFields['fieldValue']=='Both':
                ThirdPartyOrigination='Y'
            else:
                ThirdPartyOrigination='N'
            if customFields['fieldValue'] == 'TPO':
                OriginationMethod='Third Party Origination'
            elif customFields['fieldValue'] == 'Correspondent':
                OriginationMethod='Correspondent'
            elif customFields['fieldValue'] == 'Both':
                OriginationMethod='Both'
            else:
                OriginationMethod=None
        #SecondaryStsCd
        if customFields['fieldName'] == 'Secondary Status':
            if customFields['fieldValue'].upper()=='ALLOW RATE SHEETS':
                SecondaryStsCd='ARS'
            elif customFields['fieldValue'].upper()=='ASSET SALE':
                SecondaryStsCd='AS'
            elif customFields['fieldValue'].upper()=='BUSINESS MISMATCH - VOLUME':
                SecondaryStsCd='BMMV'
            elif customFields['fieldValue'].upper()=='BANKRUPTCY':
                SecondaryStsCd='BRY'
            elif customFields['fieldValue'].upper()=='EXCEPTIONS - LOB APPROVED':
                SecondaryStsCd='ELA'
            elif customFields['fieldValue'].upper()=='EXCEPTIONS - RISK APPROVED':
                SecondaryStsCd='ERA'
            elif customFields['fieldValue'].upper()=='FAILURE TO MAINTAIN APPROVAL REQUIREMENTS':
                SecondaryStsCd='FMAR'
            elif customFields['fieldValue'].upper()=='GOING CONCERN':
                SecondaryStsCd='GC'
            elif customFields['fieldValue'].upper()=='INACTIVE':
                SecondaryStsCd='INA'
            elif customFields['fieldValue'].upper()=='LOAN QUALITY REVIEW':
                SecondaryStsCd='LQR'
            elif customFields['fieldValue'].upper()=='LOB REJECTED':
                SecondaryStsCd='LR'
            elif customFields['fieldValue'].upper()=='NO EXCEPTIONS':
                SecondaryStsCd='NE'
            elif customFields['fieldValue'].upper()=='NO RATE SHEETS':
                SecondaryStsCd='NRS'
            elif customFields['fieldValue'].upper()=='ON HOLD':
                SecondaryStsCd='ONH'
            elif customFields['fieldValue'].upper()=='OUT OF BUSINESS':
                SecondaryStsCd='OOB'
            elif customFields['fieldValue'].upper()=='REGULATORY FINDING':
                SecondaryStsCd='RF'
            elif customFields['fieldValue'].upper()=='RISK REJECTED':
                SecondaryStsCd='RR'
            elif customFields['fieldValue'].upper()=='STOCK SALE':
                SecondaryStsCd='SS'
            elif customFields['fieldValue'].upper()=='WIND DOWN - ASSET SALE':
                SecondaryStsCd='WDAS'
            elif customFields['fieldValue'].upper()=='WIND DOWN - STOCK SALE':
                SecondaryStsCd='WDSS'
            else:
                SecondaryStsCd=None
        if customFields['fieldName'] == '203K':
            if len(customFields['fieldValue'])==0:
                FHA203KApproved='N'
            else:
                FHA203KApproved='Y'
        #HomeStyleIND
        if customFields['fieldName'] == 'HomeStyle':
            if len(customFields['fieldValue'])==0:
                HomeStyleIND='N'
            else:
                HomeStyleIND='Y'
        #JumboApproved
        if customFields['fieldName'] == 'Jumbo':
            if len(customFields['fieldValue'])==0:
                JumboApproved='N'
                JUMBOUndwType=None
            else:
                JumboApproved='Y'
                if customFields['fieldValue']=='Non-Delegated':
                    JUMBOUndwType='NDLT'
                elif customFields['fieldValue']=='Delegated':
                    JUMBOUndwType='DLT'
                elif customFields['fieldValue']=='Both':
                    JUMBOUndwType='BOTH'
                else:
                    JUMBOUndwType=None                       
        if customFields['fieldName'] == 'Texas A(6)':
            ProdFeatureTexasInd=(customFields['fieldValue'])
        if customFields['fieldName'] == 'Comments':
            StatusReasons=(customFields['fieldValue'])
        if customFields['fieldName'] == 'USDA OTC':
            USDAOTCApproved=(customFields['fieldValue'])
        if customFields['fieldName']   == 'Date Onboarded':
            OnboardingDate=parse((customFields['fieldValue'])).date()
        if customFields['fieldName']   == 'Automated Indexing':
            AutomatedIndexing=customFields['fieldValue']
        if customFields['fieldName']   == 'DDF Tier':
            if customFields['fieldValue'] == 'Tier 1':
                DDFTier='DT1'
            elif customFields['fieldValue'] == 'Tier 2':
                DDFTier='DT2'
            elif customFields['fieldValue'] == 'Tier 3':
                DDFTier='DT3'
            elif customFields['fieldValue'] == 'Tier 4':
                DDFTier='DT4'
            elif customFields['fieldValue'] == 'Tier 5':
                DDFTier='DT5'
            else:
                DDFTier=None
        # Verified till here 
        #SecurityReleaseRequirements
        if customFields['fieldName'] == 'Security Release Requirements':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'Self Effecting BL':
                SecurityReleaseRequirements='SEBL'
            elif customFields['fieldValue'] == 'Security Release':
                SecurityReleaseRequirements='SREL'
            elif customFields['fieldValue'] == 'Security Release - Post Purchase':
                SecurityReleaseRequirements='SREP'
            elif customFields['fieldValue'] == 'Exempt':
                SecurityReleaseRequirements='EXPT'
            elif customFields['fieldValue'] == 'Not Supported':
                SecurityReleaseRequirements='NSUP'
            else:
                SecurityReleaseRequirements=None
    #print(SecurityReleaseRequirements)
    #OriginationMethod
        if customFields['fieldName'] == 'Origination Method':
            #print(customFields['fieldValue'])
            
        #client_203K
        if customFields['fieldName'] == '203K':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'TPO':
                client_203K='Third Party Origination'
            elif customFields['fieldValue'] == 'Correspondent':
                client_203K='Correspondent'
            elif customFields['fieldValue'] == 'Both':
                client_203K='Both'
            else:
                OriginationMethod=None

        

            

        
        
        

            

    
            
                    



            
    

            
        
        
            

            