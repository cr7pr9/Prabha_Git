import json
from dateutil.parser import parse
with open ('C:\\Users\\dell\\Desktop\\PD\\Client\\getAllEntities_2.JSON') as filedata:
    data = json.load(filedata)
    Delegated=None
    try:
        print(type(data))
        ke=data.get('basicInfo',None).get('childOrganizations',None)
        key1=data.get('loanCriteria',None).get('correspondent',None).get('correspondentDelegjated',None).get('loanTypes',None)
        print(key1)
        #print((data))
        d1=(data['basicInfo']["businessInformation"]["useSsnFormat"])
        print(d1)
        d2 = data["basicInfo"]["childOrganizations"]
        d3=data['dba']['dbaDetails'][0]['externalOrgId']
        compnam= data["basicInfo"]["organizationName"]
        LoantypesDeligated=data["loanCriteria"]['correspondent']['correspondentDelegated']['loanTypes']
        LoanTypesNonDeligated=data["loanCriteria"]['correspondent']['correspondentNonDelegated']['loanTypes']
        print(LoantypesDeligated)
        if 'Va' in LoantypesDeligated and 'Va' in LoanTypesNonDeligated :
            print(('BOTH'))
        elif 'Va' in LoantypesDeligated:
            print('DLT')
        elif 'Va' in LoanTypesNonDeligated:
            print('NDLT')
        else:
            print(None)
        #Djvndfjndjkdnjknvjknvfjknvfjfvnjvnvjvnjkvjv
        #print(d3)
        for customfields in data["customFields"]["fields"]:
            #print(customfields)
            if (customfields['fieldName'])   == 'Secondary Status':
                print(customfields['fieldValue'])
            if (customfields['fieldName'])   == 'Date Onboarded':
                datetime=parse((customfields['fieldValue']))
                print((customfields['fieldValue']))
                print((datetime.date()))
    except Exception as e:
        print(str(e))