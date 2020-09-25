import json
from dateutil.parser import parse
import datetime
with open('C:\\Users\\dell\\Desktop\\PD\\Client\\getAllEntities_23.JSON') as filedata:
                    
                    #batchID = list(data_list)[0]
                    
                    data = json.load(filedata)
                    #logging.info("Json File "+str(filename)+" with batchID "+str(batchID)+" started loading the data into Client-STG Table "+str(server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_trade_stg"]))

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
                    ClientName_ID = (str(ClientName).upper()+'_'+str(ClientID)).replace('None','')
                    ClientOriginalApprovalDate = data.get('basicInfo',{}).get('approvalStatus',{}).get('applicationDate',None)
                    ClientState = data.get('basicInfo',{}).get('address',{}).get('state',None)
                    ClientStatusDate = data.get('basicInfo',{}).get('approvalStatus',{}).get('currentStatusDate',None)
                    ClientZip=data.get('basicInfo',{}).get('address',{}).get('zip',None)
                    if ClientZip != None:
                        ClientZip = ClientZip[0:10]
                    CompPh = data.get('basicInfo',{}).get('phoneNumber',None)
                    del_LoanList=(data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]))
                    non_del_LoanList =(data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]))
                    if 'Fha' in del_LoanList and 'Fha' in non_del_LoanList:
                        FHAUndwType='BOTH'
                    elif 'Fha' in del_LoanList:
                        FHAUndwType='DELT'
                    elif 'Fha' in non_del_LoanList:
                        FHAUndwType='NDLT'
                    else: 
                        FHAUndwType=None
                    if 'Conventional' in del_LoanList and 'Conventional' in non_del_LoanList:
                        CONVUndwType='BOTH'
                    elif 'Conventional' in del_LoanList:
                        CONVUndwType='DELT'
                    elif 'Conventional' in non_del_LoanList:
                        CONVUndwType='NDLT'
                    else: 
                        CONVUndwType=None
                    if 'Va' in del_LoanList and 'Va' in non_del_LoanList:
                        VAUndwType='BOTH'
                    elif 'Va' in del_LoanList:
                        VAUndwType='DELT'
                    elif 'Va' in non_del_LoanList:
                        VAUndwType='NDLT'
                    else: 
                        VAUndwType=None
                    
                    if 'Usda' in del_LoanList and 'Usda' in non_del_LoanList:
                        USDAUndwType='BOTH'
                    elif 'Usda' in del_LoanList:
                        USDAUndwType='DELT'
                    elif 'Usda' in non_del_LoanList:
                        USDAUndwType='NDLT'
                    else: 
                        USDAUndwType=None
                    if USDAUndwType==None:
                        RuralApproved='N'
                    else:
                        RuralApproved='Y'
                    if VAUndwType==None:
                        VAApproved='N'
                    else:
                        VAApproved='Y'
                    if CONVUndwType==None:
                        ConventionalApproved='N'
                    else:
                        ConventionalApproved='Y'
                    if FHAUndwType==None:
                        FHAApproved='N'
                    else:
                        FHAApproved='Y'
                    YrsinBusiness=data.get('basicInfo',{}).get('businessInformation').get('yearsInBusiness',None)
                    BillingZip=data.get('basicInfo',{}).get('billingAddress',{}).get('zip',None)
                    BillingState=data.get('basicInfo',{}).get('billingAddress',{}).get('state',None)
                    BillingCity=data.get('basicInfo',{}).get('billingAddress',{}).get('city',None)
                    BillingAddress=data.get('basicInfo',{}).get('billingAddress',{}).get('street1',None)
                    ID=data.get('basicInfo',{}).get('id',None)
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
                    LockDays15=None
                    LockDays60=None
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
                            elif customFields.get('fieldValue',None) == 'Suspend - Allow Loan submissions for Active locks':
                                                                        #Suspend - Allow Loan Submissions for Active locks
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

                        if customFields['fieldName'] == 'HomeStyle':
                            if customFields['fieldValue']==None or len(customFields['fieldValue'])==0 :
                                HomeStyleIND='N'
                            else:
                                HomeStyleIND='Y'

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
                            if len(customFields['fieldValue']) > 0 :
                                OnboardingDate=str(parse((customFields['fieldValue'])).date())
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

                        if customFields['fieldName'] == 'Security Release Requirements':
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
                            if customFields['fieldValue'] == 'Investor Services':
                                client_203K='INVS'
                            elif customFields['fieldValue'] == 'Admin Services':
                                client_203K='ADMS'
                            elif customFields['fieldValue'] == 'Admin Services Plus':
                                client_203K='ADSP'
                            else:
                                client_203K=None
                        if customFields['fieldName'] == 'HomeStyle':
                            if customFields['fieldValue'] == 'Investor Services':
                                HomeStyle='INVS'
                            elif customFields['fieldValue'] == 'Admin Services Plus':
                                HomeStyle='ADSP'
                            else:
                                HomeStyle=None
          
                        if customFields['fieldName'] == 'VA Renovation':
                            VARenovation =customFields['fieldValue'] 

                        if customFields['fieldName'] == 'Conventional Tiers':
                            if customFields['fieldValue'] == 'Conv Tier 1':
                                ConventionalTiers='1'
                            elif customFields['fieldValue'] == 'Conv Tier 2':
                                ConventionalTiers='2'
                            elif customFields['fieldValue'] == 'Conv Tier 3':
                                ConventionalTiers='3'
                            else:
                                ConventionalTiers=None
                       
                        if customFields['fieldName'] == 'FHA Tiers':
                            if customFields['fieldValue'] == 'FHA Tier 1':
                                FHATier='1'
                            elif customFields['fieldValue'] == 'FHA Tier 2':
                                FHATier='2'
                            elif customFields['fieldValue'] == 'FHA Tier 3':
                                FHATier='3'
                            else:
                                FHATier=None       
                        if customFields['fieldName'] == 'VA Tiers':
                            
                            if customFields['fieldValue'] == 'VA Tier 1':
                                VATiers='1'
                            elif customFields['fieldValue'] == 'VA Tier 2':
                                VATiers='2'
                            elif customFields['fieldValue'] == 'VA Tier 3':
                                VATiers='3'
                            else:
                                VATiers=None  
                   
                        if customFields['fieldName'] == 'USDA Tiers':
                            
                            if customFields['fieldValue'] == 'USDA Tier 1':
                                USDATiers='1'
                            elif customFields['fieldValue'] == 'USDA Tier 2':
                                USDATiers='2'
                            elif customFields['fieldValue'] == 'USDA Tier 3':
                                USDATiers='3'
                            else:
                                USDATiers=None  
                        if customFields['fieldName'] == 'Jumbo Tiers':
                            
                            if customFields['fieldValue'] == 'Jumbo Tier 1':
                                JumboTiers='1'
                            elif customFields['fieldValue'] == 'Jumbo Tier 2':
                                JumboTiers='2'
                            elif customFields['fieldValue'] == 'Jumbo Tier 3':
                                JumboTiers='3'
                            else:
                                JumboTiers=None
                        if customFields['fieldName'] == 'Other Tiers':
                            
                            if customFields['fieldValue'] == 'Other Tier 1':
                                OtherTiers='1'
                            elif customFields['fieldValue'] == 'Other Tier 2':
                                OtherTiers='2'
                            elif customFields['fieldValue'] == 'Other Tier 3':
                                OtherTiers='3'
                            else:
                                OtherTiers=None
                        if customFields['fieldName'] == 'Rate Sheet Email Distribution':
                            if customFields['fieldValue'] == 'Y':
                                RateSheetEmailDistribution = 'Y'
                            else:
                                RateSheetEmailDistribution = 'N'
                        if customFields['fieldName'] == 'Allowed Lock Extensions Count':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                AllowedLockExtensionsCount= int(str(customFields['fieldValue'])[0:9])
                        if customFields['fieldName'] == 'Max Lock Extension Days':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                MaxLockExtensionDays = int(str(customFields['fieldValue'])[0:9])
                        if customFields['fieldName'] == 'Max Aggregate Lock Extension Days':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                MaxAggregateLockExtensionDays = int(str(customFields['fieldValue'])[0:9])
                        if customFields['fieldName'] == 'Max Days After Lock Expiration':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                MaxDaysAfterLockExpiration = int(str(customFields['fieldValue'])[0:9])
                        if customFields['fieldName'] == 'Max Days After Lock Expiration For Conv':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                MaxDaysAfterLockExpirationForConv = int(str(customFields['fieldValue'])[0:9])
                        if customFields['fieldName'] == 'Max Days After Lock Expiration For FHA':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                MaxDaysAfterLockExpirationForFHA = int(str(customFields['fieldValue'])[0:9])
                        if customFields['fieldName'] == 'Max Days After Lock Expiration For Jumbo':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                MaxDaysAfterLockExpirationForJumbo = int(str(customFields['fieldValue'])[0:9])
                        if customFields['fieldName'] == 'Max Days After Lock Expiration For USDA':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                MaxDaysAfterLockExpirationForUSDA = int(str(customFields['fieldValue'])[0:9])
                        if customFields['fieldName'] == 'Max Days After Lock Expiration For VA':
                            if customFields['fieldValue'] != None and len(customFields['fieldValue'])>0:
                                MaxDaysAfterLockExpirationForVA = int(str(customFields['fieldValue'])[0:9])
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
                        if customFields['fieldName'] == 'Lock Days - 15':
                            LockDays15= customFields['fieldValue']
                        if customFields['fieldName'] == 'Lock Days - 60':
                            LockDays60 =customFields['fieldValue']
                    
                    ExternalOrgId = data.get('basicInfo',{}).get('id',None)
                    ThirdPartyOrganizationId = data.get('basicInfo',{}).get('tpoId',None)
                    AsgnToId = data.get('basicInfo',{}).get('primarySalesRepAe',{}).get('userId',None)
                    ClientTimeZone = data.get('basicInfo',{}).get('timeZone',None)    
                    CoLegalName = data.get('basicInfo',{}).get('companyLegalName',None)
                    if CoLegalName != None:
                        CoLegalName = CoLegalName[0:50]
                    StateofIncorporation = data.get('basicInfo',{}).get('businessInformation',{}).get('stateOfIncorporation',None)
                    organizationType = data.get('basicInfo',{}).get('organizationType',None)
                    if organizationType == 'Company': organizationType = 'CORP'
                    elif organizationType == 'Limited Liability Company': organizationType = 'LLC'
                    elif organizationType == 'Partnership': organizationType = 'PSHP'
                    else: organizationType = None
                    OrgType=organizationType    

                    LEI = data.get('basicInfo',{}).get('businessInformation',{}).get('lei',None)
                    FHASponsorCd = data.get('loanCriteria',{}).get('fhaSponsorId',None)
                    FHAStatus = data.get('loanCriteria',{}).get('fhaStatus',None)
                    FHADirectEndorsement = data.get('loanCriteria',{}).get('fhaDirectEndorsement',None)
                    if FHADirectEndorsement == 'Principal/Agent':
                        FHADirectEndorsement = 'AGEN'

                    VASponsorCd = data.get('loanCriteria',{}).get('vaSponsorId',None)       
                    VAStatus = data.get('loanCriteria',{}).get('vaStatus',None)
                    FannieMaeID = data.get('loanCriteria',{}).get('fannieMaeId',None)       
                    FreddieMacID = data.get('loanCriteria',{}).get('freddieMacId',None)       
                    AUSMethod = data.get('loanCriteria',{}).get('ausMethod',None)
                    DailyVolumelimit = data.get('commitments',{}).get('bestEffortDailyVolumeLimit',None)
                    MaxCommitmentAmount = data.get('commitments',{}).get('maxCommitmentAmount',None)
                    if data.get('commitments',{}).get('deliveryTypes',[]):
                        for i in data.get('commitments',{}).get('deliveryTypes',[]):
                            if i['deliveryType']== 'CoIssue':
                                CoissueIndicator = 'Y'
                            else:
                                CoissueIndicator = 'N'
                    else:
                        CoissueIndicator = None

                    ExpiryDtm = data.get('basicInfo',{}).get('businessInformation',{}).get('dateOfIncorporation',None)
                    MERSID = data.get('basicInfo',{}).get('businessInformation',{}).get('mersOriginatingOrgId',None)
                    OfficeTypCd = data.get('basicInfo',{}).get('organizationType',None)
                    if OfficeTypCd != None:
                        OfficeTypCd = OfficeTypCd[0:4]
                    TrailingDoc_Assigned_Analyst_email = data.get('basicInfo',{}).get('primarySalesRepAe',{}).get('email',None)
                    ServiceEmail = TrailingDoc_Assigned_Analyst_email.upper()
                    if data.get('basicInfo',{}).get('tpocSetup',{}).get('isTestAccount',None)==True:
                        Priority='TEST'
                    else:
                        Priority=''
                    if 'Correspondent' in data.get('basicInfo',{}).get('channelTypes',[]):
                        RqstTyp='CORR'
                    else:
                        RqstTyp=None
                    VALenderCode=data.get('loanCriteria',{}).get('vaId',None)
                    TangibleNetWorth = data.get('basicInfo',{}).get('businessInformation',{}).get('companyNetWorth',None)
                    AccountManager_Email = data.get('basicInfo',{}).get('primarySalesRepAe',{}).get('email',None)
                    AccountManager_LocationCity = data.get('basicInfo',{}).get('address',{}).get('city',None)
                    if data.get('basicInfo',{}).get('canAcceptFirstPayments',None)==True:
                        AcptFstPmtInd='Y'
                    else:
                        AcptFstPmtInd='N'
                    if data.get('commitments',{}).get('bestEffort',None)==True:
                        BEApproved = 'Y'
                    elif data.get('commitments',{}).get('bestEffort',None)==False:
                        BEApproved = 'N'
                    else:
                        BEApproved = None
                    delTypeList=[]
                    for i in data.get('commitments',{}).get('deliveryTypes',[]):
                        delTypeList.append( i['deliveryType'])
                    if 'Bulk' in delTypeList:
                        DelMethBulkInd = 'Y'
                    else:
                        DelMethBulkInd = 'N'
                    if 'BulkAot' in delTypeList:
                        BulkAOTApproved='Y'
                    else:
                        BulkAOTApproved='N'  
                    if 'Aot' in delTypeList:
                        AOTApproved='Y'
                    else:
                        AOTApproved='N'
                    ClientFoundedDate = data.get('basicInfo',{}).get('businessInformation',{}).get('dateOfIncorporation',None)
                    ClientNMLSNum = data.get('basicInfo',{}).get('businessInformation',{}).get('nmlsId',None)
                    NMLSID = data.get('basicInfo',{}).get('businessInformation',{}).get('nmlsId',None)
                    if data.get('basicInfo',{}).get('noAfterHourWires',None)==True:
                        NoLateWireInd = 'Y'
                    else:
                        NoLateWireInd ='N'
                    ext_ID = data.get('basicInfo',{}).get('id',None)
                    if data.get('dba',{}).get('dbaDetails',[]):
                        extOrgIdList=[]
                        for i in data.get('dba',{}).get('dbaDetails',[]):
                            extOrgIdList.append(i['externalOrgId'])
                        if ext_ID in extOrgIdList:
                            for i in data.get('dba',{}).get('dbaDetails',[]):
                                if ext_ID == i['externalOrgId']:
                                    DBA = i['name']
                        else:
                            DBA=None
                    else:
                        DBA = None
                    if data.get('basicInfo',{}).get('faxNumber',None)==None:
                        FaxNumber=None
                    else:
                        if int(data.get('basicInfo',{}).get('faxNumber',None).replace('-','')[0:10]) > 2147483647:
                            FaxNumber=data.get('basicInfo',{}).get('faxNumber',None).replace('-','')[0:9]
                        else:
                            FaxNumber=data.get('basicInfo',{}).get('faxNumber',None).replace('-','')[0:10]
                    VAApprovalDate=data.get('loanCriteria',{}).get('vaApprovedDate',None)
                    if ClientTimeZone !=None:
                        if 'PacificTime' in ClientTimeZone:
                            ClientTimeZone='PST'
                        elif 'AlaskaTime' in ClientTimeZone:
                            ClientTimeZone='AKST'
                        elif 'AtlanticTime' in ClientTimeZone:
                            ClientTimeZone='AST'
                        elif 'CentralTime' in ClientTimeZone:
                            ClientTimeZone='CST'
                        elif 'MountainTime' in ClientTimeZone:
                            ClientTimeZone='MST'
                        elif 'EasternTime' in ClientTimeZone:
                            ClientTimeZone='EST'
                        elif 'HawaiiTime' in ClientTimeZone:
                            ClientTimeZone='HST'
                    FHAApprovalDate=data.get('loanCriteria',{}).get('fhaApprovedDate',None)
                    FHALenderID=data.get('loanCriteria',{}).get('fhaId',None)
                    if FHALenderID != None:
                        FHALenderID = FHALenderID[0:5]
                    if data.get('loanCriteria',{}).get('fhmlcApproved',None)==True:
                        FHLMCApproved='Y'
                    else:
                        FHLMCApproved='N'
                    currentdate = datetime.datetime.now()
                    LastRefreshDate = str(currentdate.strftime("%Y-%m-%d %H:%M:%S"))
                    if data.get('commitments',{}).get('mandatory',None)==True:
                        MandoApproved = 'Y'
                    else:
                        MandoApproved = 'N'
                    RepurchaseClientContact_Name=data.get('basicInfo',{}).get('primarySalesRepAe',{}).get('name',None)
                    TaxID=data.get('basicInfo',{}).get('businessInformation',{}).get('taxId',None)
                    if data.get('loanCriteria',{}).get('fnmaApproved',None)==True:
                        FNMAAApproved='Y'
                    else:
                        FNMAAApproved='N'
print(OfficeTypCd)
print(FHAUndwType)
print(NoLateWireInd)
print(JUMBOUndwType)