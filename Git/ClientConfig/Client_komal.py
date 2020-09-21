import json
import datetime
from dateutil.parser import parse
with open ('C:\\Users\\dell\\Desktop\\PD\\Client\\getAllEntities_2.JSON') as filedata:
    data = json.load(filedata)
    if data.get('commitments',{}).get('deliveryTypes',[]):
        for i in data.get('commitments',{}).get('deliveryTypes',[]):
            if i['deliveryType']=='Bulk':
                DelMethBulkInd = 'Y'
            # elif i['deliveryType']=='Aot':
            #     AOTApproved='Y' 
            # elif i['deliveryType']=='BulkAot':
            #     BulkAOTApproved='Y'           
    else:
       DelMethBulkInd = None
    # #    AOTApproved = None
    # #    BulkAOTApproved = None
    # # if 'Aot' in data.get('commitments',{}).get('deliveryTypes',[]):
    # #     AOTApproved = 'Y'
    #    AOTApproved = None
    # if 'BulkAot' in data.get('commitments',{}).get('deliveryTypes',[]):
    #     BulkAOTApproved = 'Y'
    # else:
    #     BulkAOTApproved = None
    ExpiryDtm = data.get('basicInfo',{}).get('businessInformation',{}).get('dateOfIncorporation',None)
    MERSID = data.get('basicInfo',{}).get('businessInformation',{}).get('mersOriginatingOrgId',None)
    OfficeTypCd = data.get('basicInfo',{}).get('organizationType',None)
    if data.get('basicInfo',{}).get('tpocSetup',{}).get('isTestAccount',None)==True:
        Priority='TEST'
    else:
        Priority=None
    if 'Correspondent' in data.get('basicInfo',{}).get('channelTypes',[]):
        RqstTyp='CORR'
    else:
        RqstTyp=None
    VALenderCode=data.get('loanCriteria',{}).get('vaId',None)
    if 'Va' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]) and 'Va' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]) :
        VAUndwType='BOTH'
    elif 'Va' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]):
        VAUndwType='NDLT'
    elif 'Va' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]):
        VAUndwType='DELT'
    else:
        VAUndwType=None
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
    # check date
    ClientFoundedDate = data.get('basicInfo',{}).get('businessInformation',{}).get('dateOfIncorporation',None)
    ClientNMLSNum = data.get('basicInfo',{}).get('businessInformation',{}).get('nmlsId',None)
    NMLSID = data.get('basicInfo',{}).get('businessInformation',{}).get('nmlsId',None)
    if data.get('basicInfo',{}).get('noAfterHourWires',None)==True:
        NoLateWireInd = 'Y'
    else:
        NoLateWireInd ='N'
    if 'Conventional' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]):
        ConventionalApproved='Y'
    elif 'Conventional' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]):
        ConventionalApproved='Y'
    else:
        ConventionalApproved='N'
    if 'Conventional' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]) and 'Conventional' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]) :
        CONVUndwType='BOTH'
    elif 'Conventional' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]):
        CONVUndwType='NDLT'
    elif 'Conventional' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]):
        CONVUndwType='DELT'
    else:
        CONVUndwType=None
    ID = data.get('basicInfo',{}).get('id',None)
    if data.get('dba',{}).get('dbaDetails',[]):
        for i in data.get('dba',{}).get('dbaDetails',[]):
            if ID == i['externalOrgId']:
                DBA = i['name']
    # add time +3
    FHAApprovalDate = data.get('loanCriteria',{}).get('fhaApprovedDate',None)
    if 'Fha' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]):
        FHAApproved='Y'
    elif 'Fha' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]):
        FHAApproved='Y'
    else:
        FHAApproved='N'
    FHALenderID = data.get('loanCriteria',{}).get('fhaId',None)
    if 'Fha' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]) and 'Fha' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]) :
        FHAUndwType='BOTH'
    elif 'Fha' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]):
        FHAUndwType='NDLT'
    elif 'Fha' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]):
        FHAUndwType='DELT'
    else:
        FHAUndwType=None
    if data.get('loanCriteria',{}).get('fhmlcApproved',None) == True:
        FHLMCApproved = 'Y'
    else:
        FHLMCApproved='N'
    if data.get('loanCriteria',{}).get('fnmaApproved',None) == True:
        FNMAApproved = 'Y'
    else:
        FNMAApproved='N'
    currentdate = datetime.datetime.now()
    # 2020-09-18 08:09:00
    LastRefreshDate = str(currentdate.strftime("%Y-%m-%d %H:%M:%S"))
    if data.get('commitments',{}).get('mandatory',None)==True:
        MandoApproved = 'Y'
    else:
        MandoApproved = 'N'
    if 'Usda' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]):
        RuralApproved='Y'
    elif 'Usda' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]):
        RuralApproved='Y'
    else:
        RuralApproved='N'
    # Service email doubt
    if 'Usda' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]) and 'Usda' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]) :
        USDAUndwType='BOTH'
    elif 'Usda' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentNonDelegated',{}).get('loanTypes',[]):
        USDAUndwType='NDLT'
    elif 'Usda' in data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',[]):
        USDAUndwType='DELT'
    else:
        USDAUndwType=None
    for vars in dir():
        if not vars.startswith("var"):
             print (vars)