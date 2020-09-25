import json
from dateutil.parser import parse
with open ('C:\\Users\\dell\\Desktop\\PD\\Client\\getAllEntities_2.JSON') as filedata:
    data = json.load(filedata)
    dummy=1
    Delegated=None
    if dummy==1:
        try:
            print(type(data))
            #ke=d ata.get('basicInfo',None).get('childOrganizations',None)
            print('del'+str(Delegated))
            Delegated=data.get('loanCriteria',{}).get('correspondent',{}).get('correspondentDelegated',{}).get('loanTypes',None)
            print(('del')+str(Delegated))
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
            
        except Exception as e:
            print(str(e))
            Delegated=None