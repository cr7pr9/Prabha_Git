# -------------------------------------------------------------------------------------------------------------
# Developer Name : Avinash Kumar Nagumalli (Neelblue Technologies)
# Date : 9/03/2020
# Description : Convert  Trade Management  Json data into Stage tables.
#               These Stage table will be used in Informatica DI to create
#               CommitmentDetails Hub, PairOff Hub tables.
# -------------------------------------------------------------------------------------------------------------

import sys
import pyodbc
import json
import os
import datetime
import yaml
import logging
from configparser import ConfigParser

# -------------------------------------------------------------------------------------------------------------
# Description : Class "trade" contains two methods "trademanagementstage" and "trademanagementpairoff"
#               where the methods deletes data from their respective staging tables and reads data
#               from Json files and inserts data into their respective tables.
# -------------------------------------------------------------------------------------------------------------

class client():

    def __init__(self, cursor, config, server, date):
        self.cursor = cursor
        self.config = config
        self.server = server
        self.date = date

# -------------------------------------------------------------------------------------------------------------
# Description : Deletes data from the Staging table "Los_pcg_commitmentDetails_stg"
#               and reads data from Json files and inserts into the above referred table.
# @Input : Cursor, Config
# @Output : Loading data into the staging table "Los_pcg_commitmentDetails_stg"
# Error : Stores name of error files in Log file "trade_management_log"
# -------------------------------------------------------------------------------------------------------------

    def clientbasicinfo(self):

        # logging.basicConfig(filename=config["Path"]["Log_TRD"] +"\\log_trade_management_["+date+"].log", level=logging.INFO)

        list_processed = []
        arr = os.listdir("C:\\Users\\DELL\\Desktop\\Client")


        for filenames in arr:
            if filenames.startswith('getAllEntities'):
                list_processed.append(filenames)

        for filename in list_processed:
            try:
                with open("C:\\Users\\DELL\\Desktop\\Client"+"\\"+filename) as filedata:
                    data = json.load(filedata)

                    if "basicInfo" in data:
                        if "id" in data['basicInfo']:
                            ID = data['basicInfo']['id']
                        else:
                            ID = None

                        if "canAcceptFirstPayments" in data['basicInfo']:
                            if data['basicInfo']['canAcceptFirstPayments'] == False:
                                AcptFstPmtInd = "N"
                            else:
                                AcptFstPmtInd = "Y"
                        else:
                            AcptFstPmtInd = None

                        if "noAfterHourWires" in data['basicInfo']:
                            if data['basicInfo']['noAfterHourWires'] == False:
                                NoLateWireInd = "N"
                            else:
                                NoLateWireInd = "Y"
                        else:
                            NoLateWireInd = None

                        if "channelTypes" in data['basicInfo']:
                            RqstTyp = data['basicInfo']['channelTypes']
                        else:
                            RqstTyp = None 

                        if "tpoId" in data['basicInfo']:
                            ThirdPartyOrganizationId = data['basicInfo']['tpoId']
                        else:
                            ThirdPartyOrganizationId = None 

                        if "timeZone" in data['basicInfo']:
                            ClientTimeZone = data['basicInfo']['timeZone']
                        else:
                            ClientTimeZone = None 

                        if "companyLegalName" in data['basicInfo']:
                            CoLegalName = data['basicInfo']['companyLegalName']
                        else:
                            CoLegalName = None

                        if "organizationName" in data['basicInfo']:
                            ClientName = data['basicInfo']['organizationName']
                        else:
                            ClientName = None 

                        if "orgId" in data['basicInfo']:
                            ClientName_ID = data['basicInfo']['orgId']
                        else:
                            ClientName_ID = None

                        if "organizationType" in data['basicInfo']:
                            OfficeTypCd = data['basicInfo']['organizationType']
                        else:
                            OfficeTypCd = None

                        if "phoneNumber" in data['basicInfo']:
                            CompPh = data['basicInfo']['phoneNumber']
                        else:
                            CompPh = None

                        if "businessInformation" in data['basicInfo']:
                            if "stateOfIncorporation" in data['basicInfo']['businessInformation']:
                                StateofIncorporation = data['basicInfo']['businessInformation']['stateOfIncorporation']
                            else:
                                StateofIncorporation = None

                            if "financialsLastUpdate" in data['basicInfo']['businessInformation']:
                                DateOfFinancials = data['basicInfo']['businessInformation']['financialsLastUpdate']
                            else:
                                DateOfFinancials = None 

                            if "eoExpirationDate" in data['basicInfo']['businessInformation']:
                                ExpiryDtm = data['basicInfo']['businessInformation']['eoExpirationDate']
                            else:
                                ExpiryDtm = None

                            if "taxId" in data['basicInfo']['businessInformation']:
                                EIN = data['basicInfo']['businessInformation']['taxId']
                            else:
                                EIN = None

                            if "mersOriginatingOrgId" in data['basicInfo']['businessInformation']:
                                MERSID = data['basicInfo']['businessInformation']['mersOriginatingOrgId']
                            else:
                                MERSID = None

                            if "companyNetWorth" in data['basicInfo']['businessInformation']:
                                TangibleNetWorth = data['basicInfo']['businessInformation']['companyNetWorth']
                            else:
                                TangibleNetWorth = None

                            if "dateOfIncorporation" in data['basicInfo']['businessInformation']:
                                ClientFoundedDate = data['basicInfo']['businessInformation']['dateOfIncorporation']
                            else:
                                ClientFoundedDate = None

                            if "nmlsId" in data['basicInfo']['businessInformation']:
                                ClientNMLSNum = data['basicInfo']['businessInformation']['nmlsId']
                                NMLSID = data['basicInfo']['businessInformation']['nmlsId']
                            else:
                                ClientNMLSNum = None
                                NMLSID = None

                            if "lei" in data['basicInfo']['businessInformation']:
                                LEI = data['basicInfo']['businessInformation']['lei']
                            else:
                                LEI = None

                        if "approvalStatus" in data['basicInfo']:
                            if "approvedDate" in data['basicInfo']['approvalStatus']:
                                ClientApprovalDate = data['basicInfo']['approvalStatus']['approvedDate']
                            else:
                                ClientApprovalDate = None

                            if "currentStatus" in data['basicInfo']['approvalStatus']:
                                ActiveStatus = data['basicInfo']['approvalStatus']['currentStatus']
                            else:
                                ActiveStatus = None

                            if "applicationDate" in data['basicInfo']['approvalStatus']:
                                ClientOriginalApprovalDate = data['basicInfo']['approvalStatus']['applicationDate']
                            else:
                                ClientOriginalApprovalDate = None

                            if "currentStatusDate" in data['basicInfo']['approvalStatus']:
                                ClientStatusDate = data['basicInfo']['approvalStatus']['currentStatusDate']
                            else:
                                ClientStatusDate = None

                        if "primarySalesRepAe" in data['basicInfo']:
                            if "name" in data['basicInfo']['primarySalesRepAe']:
                                AccountManager = data['basicInfo']['primarySalesRepAe']['name']
                            else:
                                AccountManager = None

                            if "assignedDate" in data['basicInfo']['primarySalesRepAe']:
                                AccountManagerEffectiveDate = data['basicInfo']['primarySalesRepAe']['assignedDate']
                            else:
                                AccountManagerEffectiveDate = None

                            if "email" in data['basicInfo']['primarySalesRepAe']:
                                AccountManager_Email = data['basicInfo']['primarySalesRepAe']['email']
                            else:
                                AccountManager_Email = None

                            if "userId" in data['basicInfo']['primarySalesRepAe']:
                                AsgnToId = data['basicInfo']['primarySalesRepAe']['userId']
                            else:
                                AsgnToId = None

                        if "address" in data['basicInfo']:
                            if "city" in data['basicInfo']['address']:
                                AccountManager_LocationCity = data['basicInfo']['address']['city']
                            else:
                                AccountManager_LocationCity = None

                            if "state" in data['basicInfo']['address']:
                                ClientState = data['basicInfo']['address']['state']
                            else:
                                ClientState = None

                            if "street1" in data['basicInfo']['address']:
                                ClientAddress1 = data['basicInfo']['address']['street1']
                            else:
                                ClientAddress1 = None

                            if "zip" in data['basicInfo']['address']:
                                ClientZip = data['basicInfo']['address']['zip']
                            else:
                                ClientZip = None

                    if "commitments" in data:
                        if "bestEffort" in data['commitments']:
                            BEApproved = data['commitments']['bestEffort']
                        else:
                            BEApproved = None 

                        if "mandatory" in data['commitments']:
                            MandoApproved = data['commitments']['mandatory']
                        else:
                            MandoApproved = None

                        if "bestEffortDailyVolumeLimit" in data['commitments']:
                            DailyVolumelimit = data['commitments']['bestEffortDailyVolumeLimit']
                        else:
                            DailyVolumelimit = None

                        if "maxCommitmentAmount" in data['commitments']:
                            MaxCommitmentAmount = data['commitments']['maxCommitmentAmount']
                        else:
                            MaxCommitmentAmount = None

                        if "deliveryTypes" in data['commitments']:
                            for i in data['commitments']['deliveryTypes']:
                                if "deliveryType" in i:
                                    if "Bulk" in i['deliveryType']:
                                        DelMethBulkInd = 'Y'
                                    else:
                                        DelMethBulkInd = 'N'

                                    if "Aot" in i['deliveryType']:
                                        AOTApproved = 'Y'
                                    else:
                                        AOTApproved = 'N'

                                    if "BulkAot" in i['deliveryType']:
                                        BulkAOTApproved = 'Y'
                                    else:
                                        BulkAOTApproved = 'N'

                                    if "CoIssue" in i['deliveryType']:
                                        CoissueIndicator = 'Y'
                                    else:
                                        CoissueIndicator = 'N'
                                else:
                                    pass

                                logging.info("Json file read without errors "+str(filename))
                                cursor.execute("Insert into TestDB01.dbo.basicinfo (ID,AcptFstPmtInd,NoLateWireInd,RqstTyp,ThirdPartyOrganizationId,ClientTimeZone,CoLegalName,ClientName,ClientName_ID,OfficeTypCd,CompPh,StateofIncorporation,DateOfFinancials,ExpiryDtm,EIN,MERSID,TangibleNetWorth,ClientFoundedDate,ClientNMLSNum,NMLSID,LEI,ClientApprovalDate,ActiveStatus,ClientOriginalApprovalDate,ClientStatusDate,AccountManager,AccountManagerEffectiveDate,AccountManager_Email,AsgnToId,AccountManager_LocationCity,ClientState,ClientAddress1,ClientZip,BEApproved,MandoApproved,DailyVolumelimit,MaxCommitmentAmount,DelMethBulkInd,AOTApproved,BulkAOTApproved,CoissueIndicator) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",ID,AcptFstPmtInd,NoLateWireInd,RqstTyp,ThirdPartyOrganizationId,ClientTimeZone,CoLegalName,ClientName,ClientName_ID,OfficeTypCd,CompPh,StateofIncorporation,DateOfFinancials,ExpiryDtm,EIN,MERSID,TangibleNetWorth,ClientFoundedDate,ClientNMLSNum,NMLSID,LEI,ClientApprovalDate,ActiveStatus,ClientOriginalApprovalDate,ClientStatusDate,AccountManager,AccountManagerEffectiveDate,AccountManager_Email,AsgnToId,AccountManager_LocationCity,ClientState,ClientAddress1,ClientZip,BEApproved,MandoApproved,DailyVolumelimit,MaxCommitmentAmount,DelMethBulkInd,AOTApproved,BulkAOTApproved,CoissueIndicator)
                                cursor.commit()

            # except(RuntimeError, TypeError, NameError):
            except Exception as error:
                print(error)
                logging.error("Json file "+str(filename)+" caught with exception "+str(error))
                pass


# -------------------------------------------------------------------------------------------------------------
# Description : Deletes data from the Staging table "pairoff_commitmentDetails_stg"
#               and reads data from Json files and inserts into the above referred table.
# @Input : Cursor, Config
# @Output : Loading data into the staging table "pairoff_commitmentDetails_stg"
# Error : Stores name of error files in Log file "trade_management_log"
# -------------------------------------------------------------------------------------------------------------

    def clientloancriteria(self):

        # logging.basicConfig(filename=config["Path"]["Log_TRD"] +"\\log_trade_management_["+date+"].log", level=logging.INFO)

        list_processed = []
        arr = os.listdir("C:\\Users\\DELL\\Desktop\\Client")


        for filenames in arr:
            if filenames.startswith('getAllEntities'):
                list_processed.append(filenames)

        for filename in list_processed:
            try:
                with open("C:\\Users\\DELL\\Desktop\\Client"+"\\"+filename) as filedata:
                    data = json.load(filedata)
                    if "basicInfo" in data:
                        if "id" in data['basicInfo']:
                            ID = data['basicInfo']['id']
                        else:
                            ID = None
                        if "orgId" in data['basicInfo']:
                            ClientID = data['basicInfo']['orgId']
                        else:
                            ClientID = None
                        if "organizationName" in data['basicInfo']:
                            ClientName = data['basicInfo']['organizationName']
                        else:
                            ClientName = None
                        if ("orgId" in data['basicInfo']) and ("organizationName" in data['basicInfo']):
                            ClientName_ID = ClientName+"_"+ClientID
                        else:
                            ClientName_ID = None
                    
                    if "tpocSetup" in data:
                        if "isTestAccount" in data['tpocSetup']:
                            Priority = data['tpocSetup']['isTestAccount']
                        else:
                            Priority = None

                    if "loanCriteria" in data:
                        if "correspondent" in data['loanCriteria']:
                            if "Conventional" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes'] and "Conventional" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                CONVUndwType = "BOTH"
                            elif "Conventional" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                CONVUndwType = "NDLT"
                            elif "Conventional" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes']:
                                CONVUndwType = "DELT"
                            else:
                                CONVUndwType = None

                            if "Va" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes'] and "Va" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                VAUndwType = "BOTH"
                            elif "Va" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                VAUndwType = "NDLT"
                            elif "Va" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes']:
                                VAUndwType = "DELT"
                            else:
                                VAUndwType = None
                            
                            if "Fha" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes'] and "Fha" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                FHAUndwType = "BOTH"
                            elif "Fha" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                FHAUndwType = "NDLT"
                            elif "Fha" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes']:
                                FHAUndwType = "DELT"
                            else:
                                FHAUndwType = None
                            
                            if "Usda" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes'] and "Usda" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                USDAUndwType = "BOTH"
                            elif "Usda" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                USDAUndwType = "NDLT"
                            elif "Usda" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes']:
                                USDAUndwType = "DELT"
                            else:
                                USDAUndwType = None

                            if "Usda" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes']:
                                RuralApproved = "Y"
                            elif "Usda" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                RuralApproved = "Y"
                            else:
                                RuralApproved = "N"
                            
                            if "Va" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes'] or "Va" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                VAApproved = "Y"
                            else:
                                VAApproved = "N"

                            if "Conventional" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes'] or "Conventional" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                ConventionalApproved = "Y"
                            else:
                                ConventionalApproved = "N"

                            if "Fha" in data['loanCriteria']['correspondent']['correspondentDelegated']['loanTypes'] or "Fha" in data['loanCriteria']['correspondent']['correspondentNonDelegated']['loanTypes']:
                                FHAApproved = "Y"
                            else:
                                FHAApproved = "N"

                        if "vaId" in data['loanCriteria']:
                            VALenderCode = data['loanCriteria']['vaId']
                        else:
                            VALenderCode = None

                        if "fhaApprovedDate" in data['loanCriteria']:
                            FHAApprovalDate = data['loanCriteria']['fhaApprovedDate']
                        else:
                            FHAApprovalDate = None

                        if "fhaId" in data['loanCriteria']:
                            FHALenderID = data['loanCriteria']['fhaId']
                        else:
                            FHALenderID = None 

                        if "fhmlcApproved" in data['loanCriteria']:
                            FHLMCApproved = data['loanCriteria']['fhmlcApproved']
                        else:
                            FHLMCApproved = None

                        if "fnmaApproved" in data['loanCriteria']:
                            FNMAApproved = data['loanCriteria']['fnmaApproved']
                        else:
                            FNMAApproved = None

                        if "vaApprovedDate" in data['loanCriteria']:
                            VAApprovalDate = data['loanCriteria']['vaApprovedDate']
                        else:
                            VAApprovalDate = None

                        if "fhaSponsorId" in data['loanCriteria']:
                            FHASponsorCd = data['loanCriteria']['fhaSponsorId']
                        else:
                            FHASponsorCd = None 

                        if "fhaStatus" in data['loanCriteria']:
                            FHAStatus = data['loanCriteria']['fhaStatus']
                        else:
                            FHAStatus = None

                        if "fhaDirectEndorsement" in data['loanCriteria']:
                            FHADirectEndorsement = data['loanCriteria']['fhaDirectEndorsement']
                        else:
                            FHADirectEndorsement = None

                        if "vaSponsorId" in data['loanCriteria']:
                            VASponsorCd = data['loanCriteria']['vaSponsorId']
                        else:
                            VASponsorCd = None

                        if "vaStatus" in data['loanCriteria']:
                            VAStatus = data['loanCriteria']['vaStatus']
                        else:
                            VAStatus = None

                        if "fannieMaeId" in data['loanCriteria']:
                            FannieMaeID = data['loanCriteria']['fannieMaeId']
                        else:
                            FannieMaeID = None 

                        if "freddieMacId" in data['loanCriteria']:
                            FreddieMacID = data['loanCriteria']['freddieMacId']
                        else:
                            FreddieMacID = None

                        if "ausMethod" in data['loanCriteria']:
                            AUSMethod = data['loanCriteria']['ausMethod']
                        else:
                            AUSMethod = None
                    if "warehouse" in data:
                        if "warehouseBankDetails" in data['warehouse']:
                            if "warehouseBankId" in data['warehouse']['warehouseBankDetails'][0]:
                                WarehouseBankID = data['warehouse']['warehouseBankDetails'][0]['warehouseBankId']
                            else:
                                WarehouseBankID = None

                            if "description" in data['warehouse']['warehouseBankDetails'][0]:
                                BenificiaryDtls = data['warehouse']['warehouseBankDetails'][0]['description']
                            else:
                                BenificiaryDtls = None

                            if "creditAccountName" in data['warehouse']['warehouseBankDetails'][0]:
                                FurhterCreditAccountName = data['warehouse']['warehouseBankDetails'][0]['creditAccountName']
                            else:
                                FurhterCreditAccountName = None
                                
                            if "creditAccountNumber" in data['warehouse']['warehouseBankDetails'][0]:
                                FurhterCreditAccountNumber = data['warehouse']['warehouseBankDetails'][0]['creditAccountNumber']
                            else:
                                FurhterCreditAccountNumber = None
                            
                            if "timeZone" in data['warehouse']['warehouseBankDetails'][0]:
                                WHBankTimeZone = data['warehouse']['warehouseBankDetails'][0]['timeZone']
                            else:
                                WHBankTimeZone = None
                            
                            if "accountNumber" in data['warehouse']['warehouseBankDetails'][0]:
                                AccountNumber = data['warehouse']['warehouseBankDetails'][0]['accountNumber']
                            else:
                                AccountNumber = None
                            
                            if "accountName" in data['warehouse']['warehouseBankDetails'][0]:
                                AccountName = data['warehouse']['warehouseBankDetails'][0]['accountName']
                            else:
                                AccountName = None

                            if "contactName" in data['warehouse']['warehouseBankDetails'][0]:
                                WarehouseContactFirstName = data['warehouse']['warehouseBankDetails'][0]['contactName']
                            else:
                                WarehouseContactFirstName = None
                            
                            if "contactName" in data['warehouse']['warehouseBankDetails'][0]:
                                WarehouseContactLastName = data['warehouse']['warehouseBankDetails'][0]['contactName']
                            else:
                                WarehouseContactLastName = None

                            if "contactEmail" in data['warehouse']['warehouseBankDetails'][0]:
                                WarehourseContactEmail = data['warehouse']['warehouseBankDetails'][0]['contactEmail']
                            else:
                                WarehourseContactEmail = None

                            if "contactPhone" in data['warehouse']['warehouseBankDetails'][0]:
                                WarehouseContactPhone = data['warehouse']['warehouseBankDetails'][0]['contactPhone']
                            else:
                                WarehouseContactPhone = None

                            if "contactFax" in data['warehouse']['warehouseBankDetails'][0]:
                                WarehouseContactFaxNumber = data['warehouse']['warehouseBankDetails'][0]['contactFax']
                            else:
                                WarehouseContactFaxNumber = None

                            if "isApproved" in data['warehouse']['warehouseBankDetails'][0]:
                                WarehouseApprovedCheckbox = data['warehouse']['warehouseBankDetails'][0]['isApproved']
                            else:
                                WarehouseApprovedCheckbox = None

                            if "statusDate" in data['warehouse']['warehouseBankDetails'][0]:
                                WarehouseStatusDate = data['warehouse']['warehouseBankDetails'][0]['statusDate']
                            else:
                                WarehouseStatusDate = None

                    if "dba" in data:
                        if "dbaDetails" in data['dba']:
                            for i in data['dba']['dbaDetails']:
                                if "name" in i:
                                    DBA = i['name']
                                else:
                                    DBA = None

                                if "externalOrgId" in i:
                                    ExternalOrgId = i['externalOrgId']
                                else:
                                    ExternalOrgId = None
                                
                                logging.info("Json file read without errors "+str(filename))
                                # query = "Insert into table1 (col1,col2,.....) values ("+ID+","+CONVUndwType+","+VAUndwType+")"
                                cursor.execute("Insert into TestDB01.dbo.basicinfo (ID,CONVUndwType,VAUndwType,FHAUndwType,USDAUndwType,RuralApproved,VAApproved,ConventionalApproved,FHAApproved,VALenderCode,FHAApprovalDate,FHALenderID,FHLMCApproved,FNMAApproved,VAApprovalDate,FHASponsorCd,FHAStatus,FHADirectEndorsement,VASponsorCd,VAStatus,FannieMaeID,FreddieMacID,AUSMethod,Priority,DBA,ExternalOrgId) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",ID,CONVUndwType,VAUndwType,FHAUndwType,USDAUndwType,RuralApproved,VAApproved,ConventionalApproved,FHAApproved,VALenderCode,FHAApprovalDate,FHALenderID,FHLMCApproved,FNMAApproved,VAApprovalDate,FHASponsorCd,FHAStatus,FHADirectEndorsement,VASponsorCd,VAStatus,FannieMaeID,FreddieMacID,AUSMethod,Priority,DBA,ExternalOrgId)
                                cursor.commit()

                                
            # except(RuntimeError, TypeError, NameError):
            except Exception as error:
                logging.error("Json file "+str(filename)+" caught with exception "+str(error))
                pass


# -------------------------------------------------------------------------------------------------------------
# Description : Deletes data from the Staging table "pairoff_commitmentDetails_stg"
#               and reads data from Json files and inserts into the above referred table.
# @Input : Cursor, Config
# @Output : Loading data into the staging table "pairoff_commitmentDetails_stg"
# Error : Stores name of error files in Log file "trade_management_log"
# -------------------------------------------------------------------------------------------------------------

    def clientcustomfields(self):

        # logging.basicConfig(filename=config["Path"]["Log_TRD"] +"\\log_trade_management_["+date+"].log", level=logging.INFO)

        list_processed = []
        arr = os.listdir("C:\\Users\\DELL\\Desktop\\Client")


        for filenames in arr:
            if filenames.startswith('getAllEntities'):
                list_processed.append(filenames)

        for filename in list_processed:
            try:
                with open("C:\\Users\\DELL\\Desktop\\Client"+"\\"+filename) as filedata:
                    data = json.load(filedata)
                    if "basicInfo" in data:
                        if "id" in data['basicInfo']:
                            ID = data['basicInfo']['id']
                        else:
                            ID = None

                    if "customFields" in data:
                        if "fields" in data['customFields']:
                            for i in data['customFields']['fields']:
                                if "Secondary Status" in i['fieldName']:
                                    ClientSecStatus = i['fieldValue']
                                else:
                                    ClientSecStatus = None
                                    pass

                                if "Secondary Status" in i['fieldName']:
                                    SecondaryStsCd = i['fieldValue']
                                else:
                                    SecondaryStsCd = None
                                    pass

                                if "Primary Status" in i['fieldName']:
                                    ClientStatus = i['fieldValue']
                                else:
                                    ClientStatus = None
                                    pass

                                if "Primary Status" in i['fieldName']:
                                    ClientStatusGroup = i['fieldValue']
                                else:
                                    ClientStatusGroup = None
                                    pass

                                if "Origination Method" in i['fieldName']:
                                    CorrespondentInd = i['fieldValue']
                                else:
                                    CorrespondentInd = None
                                    pass

                                if "203K" in i['fieldName']:
                                    FHA203KApproved = i['fieldValue']
                                else:
                                    FHA203KApproved = None
                                    pass

                                if "203K" in i['fieldName']:
                                    client_203K = i['fieldValue']
                                else:
                                    client_203K = None
                                    pass

                                if "HomeStyle" in i['fieldName']:
                                    HomeStyleIND = i['fieldValue']
                                else:
                                    HomeStyleIND = None
                                    pass 

                                if "HomeStyle" in i['fieldName']:
                                    HomeStyle = i['fieldValue']
                                else:
                                    HomeStyle = None
                                    pass

                                if "Jumbo" in i['fieldName']:
                                    JumboApproved = i['fieldValue']
                                else:
                                    JumboApproved = None
                                    pass

                                if "Jumbo" in i['fieldName']:
                                    JUMBOUndwType = i['fieldValue']
                                else:
                                    JUMBOUndwType = None
                                    pass 

                                if "Texas A(6)" in i['fieldName']:
                                    ProdFeatureTexasInd = i['fieldValue']
                                else:
                                    ProdFeatureTexasInd = None
                                    pass

                                if "Comments" in i['fieldName']:
                                    StatusReasons = i['fieldValue']
                                else:
                                    StatusReasons = None
                                    pass

                                if "Origination Method" in i['fieldName']:
                                    ThirdPartyOrigination = i['fieldValue']
                                else:
                                    ThirdPartyOrigination = None
                                    pass

                                if "USDA OTC" in i['fieldName']:
                                    USDAOTCApproved = i['fieldValue']
                                else:
                                    USDAOTCApproved = None
                                    pass

                                if "Date Onboarded" in i['fieldName']:
                                    OnboardingDate = i['fieldValue']
                                else:
                                    OnboardingDate = None
                                    pass

                                if "Automated Indexing" in i['fieldName']:
                                    AutomatedIndexing = i['fieldValue']
                                else:
                                    AutomatedIndexing = None
                                    pass

                                if "DDF Tier" in i['fieldName']:
                                    DDFTier = i['fieldValue']
                                else:
                                    DDFTier = None
                                    pass 

                                if "Security Release Requirements" in i['fieldName']:
                                    SecurityReleaseRequirements = i['fieldValue']
                                else:
                                    SecurityReleaseRequirements = None
                                    pass

                                if "Origination Method" in i['fieldName']:
                                    OriginationMethod = i['fieldValue']
                                else:
                                    OriginationMethod = None
                                    pass 

                                if "VA Renovation" in i['fieldName']:
                                    VARenovation = i['fieldValue']
                                else:
                                    VARenovation = None
                                    pass

                                if "Conventional Tiers" in i['fieldName']:
                                    ConventionalTiers = i['fieldValue']
                                else:
                                    ConventionalTiers = None
                                    pass

                                if "FHA Tiers" in i['fieldName']:
                                    FHATier = i['fieldValue']
                                else:
                                    FHATier = None
                                    pass 

                                if "Primary Status" in i['fieldName']:
                                    StatusCd = i['fieldValue']
                                else:
                                    StatusCd = None
                                    pass

                                if "VA Tiers" in i['fieldName']:
                                    VATiers = i['fieldValue']
                                else:
                                    VATiers = None
                                    pass

                                if "USDA Tiers" in i['fieldName']:
                                    USDATiers = i['fieldValue']
                                else:
                                    USDATiers = None
                                    pass

                                if "Jumbo Tiers" in i['fieldName']:
                                    JumboTiers = i['fieldValue']
                                else:
                                    JumboTiers = None
                                    pass

                                if "Other Tiers" in i['fieldName']:
                                    OtherTiers = i['fieldValue']
                                else:
                                    OtherTiers = None
                                    pass

                                if "Rate Sheet Email Distribution" in i['fieldName']:
                                    RateSheetEmailDistribution = i['fieldValue']
                                else:
                                    RateSheetEmailDistribution = None
                                    pass

                                if "Allowed Lock Extensions Coun" in i['fieldName']:
                                    AllowedLockExtensionsCount = i['fieldValue']
                                else:
                                    AllowedLockExtensionsCount = None
                                    pass

                                if "Max Lock Extension Days" in i['fieldName']:
                                    MaxLockExtensionDays = i['fieldValue']
                                else:
                                    MaxLockExtensionDays = None
                                    pass

                                if "Max Aggregate Lock Extension Days" in i['fieldName']:
                                    MaxAggregateLockExtensionDays = i['fieldValue']
                                else:
                                    MaxAggregateLockExtensionDays = None
                                    pass

                                if "Max Days After Lock Expiration" in i['fieldName']:
                                    MaxDaysAfterLockExpiration = i['fieldValue']
                                else:
                                    MaxDaysAfterLockExpiration = None
                                    pass

                                if "Max Days After Lock Expiration For Conv" in i['fieldName']:
                                    MaxDaysAfterLockExpirationForConv = i['fieldValue']
                                else:
                                    MaxDaysAfterLockExpirationForConv = None
                                    pass

                                if "Max Days After Lock Expiration For FHA" in i['fieldName']:
                                    MaxDaysAfterLockExpirationForFHA = i['fieldValue']
                                else:
                                    MaxDaysAfterLockExpirationForFHA = None
                                    pass

                                if "Max Days After Lock Expiration For Jumbo" in i['fieldName']:
                                    MaxDaysAfterLockExpirationForJumbo = i['fieldValue']
                                else:
                                    MaxDaysAfterLockExpirationForJumbo = None
                                    pass

                                if "Max Days After Lock Expiration For USDA" in i['fieldName']:
                                    MaxDaysAfterLockExpirationForUSDA = i['fieldValue']
                                else:
                                    MaxDaysAfterLockExpirationForUSDA = None
                                    pass

                                if "Max Days After Lock Expiration For VA" in i['fieldName']:
                                    MaxDaysAfterLockExpirationForVA = i['fieldValue']
                                else:
                                    MaxDaysAfterLockExpirationForVA = None
                                    pass

                                if "Lock Days - 30" in i['fieldName']:
                                    LockDays30 = i['fieldValue']
                                else:
                                    LockDays30 = None
                                    pass

                                if "Lock Days - 45" in i['fieldName']:
                                    LockDays45 = i['fieldValue']
                                else:
                                    LockDays45 = None
                                    pass

                                if "Lock Days - 75" in i['fieldName']:
                                    LockDays75 = i['fieldValue']
                                else:
                                    LockDays75 = None
                                    pass

                                if "Relock Days - 15" in i['fieldName']:
                                    RelockDays15 = i['fieldValue']
                                else:
                                    RelockDays15 = None
                                    pass

                                if "Relock Days - 30" in i['fieldName']:
                                    RelockDays30 = i['fieldValue']
                                else:
                                    RelockDays30 = None
                                    pass

                            logging.info("Json file read without errors "+str(filename))
                            cursor.execute("Insert into "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_trade_stg"]+" (ID,ClientSecStatus,SecondaryStsCd,ClientStatus,ClientStatusGroup,CorrespondentInd,FHA203KApproved,client_203K,HomeStyleIND,HomeStyle,JumboApproved,JUMBOUndwType,ProdFeatureTexasInd,StatusReasons,ThirdPartyOrigination,USDAOTCApproved,OnboardingDate,AutomatedIndexing,DDFTier,SecurityReleaseRequirements,OriginationMethod,VARenovation,ConventionalTiers,FHATier,StatusCd,VATiers,USDATiers,JumboTiers,OtherTiers,RateSheetEmailDistribution,AllowedLockExtensionsCount,MaxLockExtensionDays,MaxAggregateLockExtensionDays,MaxDaysAfterLockExpiration,MaxDaysAfterLockExpirationForConv,MaxDaysAfterLockExpirationForFHA,MaxDaysAfterLockExpirationForJumbo,MaxDaysAfterLockExpirationForUSDA,MaxDaysAfterLockExpirationForVA,LockDays30,LockDays45,LockDays75,RelockDays15,RelockDays30) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",ID,ClientSecStatus,SecondaryStsCd,ClientStatus,ClientStatusGroup,CorrespondentInd,FHA203KApproved,client_203K,HomeStyleIND,HomeStyle,JumboApproved,JUMBOUndwType,ProdFeatureTexasInd,StatusReasons,ThirdPartyOrigination,USDAOTCApproved,OnboardingDate,AutomatedIndexing,DDFTier,SecurityReleaseRequirements,OriginationMethod,VARenovation,ConventionalTiers,FHATier,StatusCd,VATiers,USDATiers,JumboTiers,OtherTiers,RateSheetEmailDistribution,AllowedLockExtensionsCount,MaxLockExtensionDays,MaxAggregateLockExtensionDays,MaxDaysAfterLockExpiration,MaxDaysAfterLockExpirationForConv,MaxDaysAfterLockExpirationForFHA,MaxDaysAfterLockExpirationForJumbo,MaxDaysAfterLockExpirationForUSDA,MaxDaysAfterLockExpirationForVA,LockDays30,LockDays45,LockDays75,RelockDays15,RelockDays30)
                            cursor.commit()

            # except(RuntimeError, TypeError, NameError):
            except Exception as error:
                logging.error("Json file "+str(filename)+" caught with exception "+str(error))
                pass

if __name__ == '__main__':

    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y%H-%M-%S"))
                
    with open("C:\\Users\\DELL\\Desktop\\22-04-2020\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    server = ConfigParser()
    server.read('C:\\Users\\DELL\\Desktop\\22-04-2020\\INFA_API_Shared\\ODBC\\ODBC.ini')
    # app_env = os.environ['APP_ENV']

    # if 'dev' in app_env:
    #     servername = server["SqlServer_Connection"]["servername_dev"]
    # elif 'qa' in app_env:
    #     servername = server["SqlServer_Connection"]["servername_qa"]
    # elif 'stg' in app_env:
    #     servername = server["SqlServer_Connection"]["servername_stg"]
    # else:
    #     servername = server["SqlServer_Connection"]["servername_prod"]

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=USER;'
                          'Database=TestDB01;'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()
    clientobj = client(cursor, config, server, date)
    clientobj.clientloancriteria()
    # if sys.argv[1]=='BasicInfo':
    #     clientobj.clientbasicinfo()
    # elif  sys.argv[1]=='LoanCriteria':
    #     clientobj.clientloancriteria()
    # elif  sys.argv[1]=='CustomFields':
    #     clientobj.clientcustomfields()