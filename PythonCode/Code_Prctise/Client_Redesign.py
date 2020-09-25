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
    ClientID =data.get('basicInfo',{}).get('orgId',None)
    ClientName =data.get('basicInfo',{}).get('organizationName',None)
    ClientName_ID = ClientName.upper()+'_'+ClientID
    ClientOriginalApprovalDate = data.get('basicInfo',{}).get('approvalStatus',{}).get('applicationDate',None)
    ClientState = data.get('basicInfo',{}).get('address',{}).get('state',None)
    ClientStatusDate = data.get('basicInfo',{}).get('approvalStatus',{}).get('currentStatusDate',None)
    ClientZip=data.get('basicInfo',{}).get('address',{}).get('zip',None)
    CompPh = data.get('basicInfo',{}).get('phoneNumber',None)
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
    HomeStyle =None
    VARenovation=None
    ConventionalTiers=None
    FHATier=None
    StatusCd=None
    VATiers=None
    USDATiers=None
    JumboTiers=None
    OtherTiers=None
    RateSheetEmailDistribution=None
    AllowedLockExtensionsCount=None
    MaxLockExtensionDays=None				
    MaxAggregateLockExtensionDays=None
    MaxDaysAfterLockExpiration=None
    MaxDaysAfterLockExpirationForConv=None
    MaxDaysAfterLockExpirationForFHA=None
    MaxDaysAfterLockExpirationForJumbo=None
    MaxDaysAfterLockExpirationForUSDA=None
    MaxDaysAfterLockExpirationForVA=None
    LockDays30=None
    LockDays45=None
    LockDays75=None
    RelockDays15=None
    RelockDays30=None




        #starting custom fields
    for customFields in data.get('customFields',{}).get('fields',{}):
        if customFields['fieldName'] == 'Secondary Status':
            ClientSecStatus = customFields.get('fieldValue',None).upper()
        if customFields['fieldName'] == 'Primary Status':
            if customFields.get('fieldValue',None) == 'Approved':
                ClientStatus ='Approved'
                StatusCd='APRV'
            elif customFields.get('fieldValue',None) == 'Not Approved':
                ClientStatus ='Not Approved'
                StatusCd='NAPR'
            elif customFields.get('fieldValue',None) == 'Prospect':
                ClientStatus ='Prospect'
                StatusCd='PRPT'
            elif customFields.get('fieldValue',None) == 'Suspend - Allow Loan submisssions for Active locks':
                ClientStatus ='SUSPEND-ALLOW LOAN SUBMISSIONS FOR ACTIVE LOCKS'
                StatusCd='SUS1'
            elif customFields.get('fieldValue',None) == 'Suspend - Disallow New loan Submissions':
                ClientStatus ='SUSPEND-DISALLOW NEW LOAN SUBMISSIONS'
                StatusCd='SUS2'
            elif customFields.get('fieldValue',None) == "Terminated with AR's":
                ClientStatus ="TERMINATED - WITH AR'S"
                StatusCd='TEAR'
            elif customFields.get('fieldValue',None) == "Terminate":
                ClientStatus = 'Terminated'
                StatusCd='TERM'
            else:
                ClientStatus =None
                StatusCd=None
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
            if customFields['fieldValue']==None  or len(customFields['fieldValue'])==0:
                FHA203KApproved='N'
            else:
                FHA203KApproved='Y'
        #HomeStyleIND
        if customFields['fieldName'] == 'HomeStyle':
            if customFields['fieldValue']==None or len(customFields['fieldValue'])==0 :
                HomeStyleIND='N'
            else:
                HomeStyleIND='Y'
        #JumboApproved
        if customFields['fieldName'] == 'Jumbo':
            if customFields['fieldValue']==None  or len(customFields['fieldValue'])==0:
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
        if customFields['fieldName'] == '203K':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'Investor Services':
                client_203K='INVS'
            elif customFields['fieldValue'] == 'Admin Services':
                client_203K='ADMS'
            elif customFields['fieldValue'] == 'Admin Services Plus':
                client_203K='ADSP'
            else:
                client_203K=None
        if customFields['fieldName'] == 'HomeStyle':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'Investor Services':
                HomeStyle='INVS'
            elif customFields['fieldValue'] == 'Admin Services':
                HomeStyle='ADMS'
            else:
                HomeStyle=None
        #VA Renovation
        if customFields['fieldName'] == 'VA Renovation':
            VARenovation =customFields['fieldValue'] 
    #ConventionalTiers
        if customFields['fieldName'] == 'Conventional Tiers':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'Conv Tier 1':
                ConventionalTiers='1'
            elif customFields['fieldValue'] == 'Conv Tier 2':
                ConventionalTiers='2'
            elif customFields['fieldValue'] == 'Conv Tier 3':
                ConventionalTiers='3'
            else:
                ConventionalTiers=None
        #FHATier
        if customFields['fieldName'] == 'FHA Tiers':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'FHA Tier 1':
                FHATier='1'
            elif customFields['fieldValue'] == 'FHA Tier 2':
                FHATier='2'
            elif customFields['fieldValue'] == 'FHA Tier 3':
                FHATier='3'
            else:
                FHATier=None       
        if customFields['fieldName'] == 'VA Tiers':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'VA Tier 1':
                VATiers='1'
            elif customFields['fieldValue'] == 'VA Tier 2':
                VATiers='2'
            elif customFields['fieldValue'] == 'VA Tier 3':
                VATiers='3'
            else:
                VATiers=None  
    #USDATiers\
        if customFields['fieldName'] == 'USDA Tiers':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'USDA Tier 1':
                USDATiers='1'
            elif customFields['fieldValue'] == 'USDA Tier 2':
                USDATiers='2'
            elif customFields['fieldValue'] == 'USDA Tier 3':
                USDATiers='3'
            else:
                USDATiers=None  
        if customFields['fieldName'] == 'Jumbo Tiers':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'Jumbo Tier 1':
                JumboTiers='1'
            elif customFields['fieldValue'] == 'Jumbo Tier 2':
                JumboTiers='2'
            elif customFields['fieldValue'] == 'Jumbo Tier 3':
                JumboTiers='3'
            else:
                JumboTiers=None
        if customFields['fieldName'] == 'Other Tiers':
            #print(customFields['fieldValue'])
            if customFields['fieldValue'] == 'Other Tier 1':
                OtherTiers='1'
            elif customFields['fieldValue'] == 'Other Tier 2':
                OtherTiers='2'
            elif customFields['fieldValue'] == 'Other Tier 3':
                OtherTiers='3'
            else:
                OtherTiers=None
        if customFields['fieldName'] == 'Rate Sheet Email Distribution':
            RateSheetEmailDistribution= customFields['fieldValue']
        #AllowedLockExtensionsCount
        if customFields['fieldName'] == 'Allowed Lock Extensions Count':
            AllowedLockExtensionsCount= customFields['fieldValue']
        if customFields['fieldName'] == 'Max Lock Extension Days':
            MaxLockExtensionDays = customFields['fieldValue']
        if customFields['fieldName'] == 'Max Aggregate Lock Extension Days':
            MaxAggregateLockExtensionDays = customFields['fieldValue']
        if customFields['fieldName'] == 'Max Days After Lock Expiration':
            MaxDaysAfterLockExpiration = customFields['fieldValue']
        if customFields['fieldName'] == 'Max Days After Lock Expiration For Conv':
            MaxDaysAfterLockExpirationForConv = customFields['fieldValue']
        if customFields['fieldName'] == 'Max Days After Lock Expiration For FHA':
            MaxDaysAfterLockExpirationForFHA = customFields['fieldValue']
        if customFields['fieldName'] == 'Max Days After Lock Expiration For Jumbo':
            MaxDaysAfterLockExpirationForJumbo = customFields['fieldValue']
        if customFields['fieldName'] == 'Max Days After Lock Expiration For USDA':
            MaxDaysAfterLockExpirationForUSDA = customFields['fieldValue']
        if customFields['fieldName'] == 'Max Days After Lock Expiration For VA':
            MaxDaysAfterLockExpirationForVA = customFields['fieldValue']
        #LockDays30
        #Lock Days - 30
        if customFields['fieldName'] == 'Lock Days - 30':
            LockDays30 = customFields['fieldValue']
        if customFields['fieldName'] == 'Lock Days - 45':
            LockDays45 = customFields['fieldValue']
        if customFields['fieldName'] == 'Lock Days - 75':
            LockDays75 = customFields['fieldValue']
        if customFields['fieldName'] == 'Relock Days - 15':
            RelockDays15= customFields['fieldValue']
        if customFields['fieldName'] == 'Relock Days - 30':
            RelockDays30 = customFields['fieldValue']