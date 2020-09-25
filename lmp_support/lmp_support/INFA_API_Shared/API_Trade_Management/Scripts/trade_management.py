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


class trade():

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

    def trademanagementstage(self):
        logging.basicConfig(filename=config["Path"]["Log_TRD"] +
                        "\\log_trade_management_["+date+"].log", level=logging.INFO)

        list_processed = []
        arr = os.listdir(config["Path"]["Inbound_TRD"])

        for filenames in arr:
            if filenames.startswith('CommitmentDetails'):
                list_processed.append(filenames)

        cursor.execute("DELETE from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_trade_stg"])
        cursor.commit()
        for filename in list_processed:
            try:
                with open(config["Path"]["Inbound_TRD"]+"/"+filename) as filedata:
                    data = json.load(filedata)
                    if "commitmentDate" in data:
                        commitmentDate = data["commitmentDate"]
                    else:
                        commitmentDate = None
                    if "commitmentType" in data:
                        commitmentType = data['commitmentType']
                    else:
                        commitmentType = None
                    if "expirationDate" in data:
                        expirationDate = data["expirationDate"]
                    else:
                        expirationDate = None
                    if "weightedAvgBulkPrice" in data:
                        weightedAvgBulkPrice = data["weightedAvgBulkPrice"]
                    else:
                        weightedAvgBulkPrice = None
                    if "percentWac" in data:
                        percentWac = data["percentWac"]
                    else:
                        percentWac = None
                    if "loanCount" in data:
                        loancount = data["loanCount"]
                    else:
                        loancount = None
                    if "tradeInfoContract" in data:
                        if "commitmentNumber" in data["tradeInfoContract"]:
                            tpoIdtradeInfoContract = str(data['tradeInfoContract']['commitmentNumber'])
                        else:
                            tpoIdtradeInfoContract = None
                    if "tpoDetails" in data:
                        if "organizationId" in data['tpoDetails']:
                            orgId = int(data['tpoDetails']['organizationId'])
                        else:
                            orgId = None
                    if "tpoDetails" in data:
                        if "tpoCompanyName" in data['tpoDetails']:
                            tpoCompanyName = data['tpoDetails']['tpoCompanyName']
                        else:
                            tpoCompanyName = None
                    if "tradeInfoContract" in data:
                        if "maxAmount" in data['tradeInfoContract']:
                            maxAmount = data['tradeInfoContract']['maxAmount']
                        else:
                            maxAmount = None
                    if "tradeInfoContract" in data:
                        if "minAmount" in data['tradeInfoContract']:
                            minAmount = data['tradeInfoContract']['minAmount']
                        else:
                            minAmount = None
                    if "tradeInfoContract" in data:
                        if "status" in data["tradeInfoContract"]:
                            Status = data["tradeInfoContract"]["status"]
                        else:
                            Status = None
                    if "aotInformation" in data:
                        if "aotSecurityTerm" in data["aotInformation"]:
                            Term = data["aotInformation"]["aotSecurityTerm"]
                        else:
                            Term = None
                    if "aotInformation" in data:
                        if "status" in data["aotInformation"]:
                            StatusCd = data["aotInformation"]["status"]
                        else:
                            StatusCd = None
                    if "CommitmentType" in data:
                        CommitmentTypCd = data["CommitmentType"]
                    else:
                        CommitmentTypCd = None
                    if "aotInformation" in data:
                        if "aotSettlementDate" in data["aotInformation"]:
                            ConfirmationSentDt = data["aotInformation"]["aotSettlementDate"]
                        else:
                            ConfirmationSentDt = None
                    if "tradeInfoContract" in data:
                        if "tradeAmount" in data["tradeInfoContract"]:
                            ThresholdAmt = data["tradeInfoContract"]["tradeAmount"]
                        else:
                            ThresholdAmt = None
                    if "tradeInfoContract" in data:
                        if "tolerance" in data["tradeInfoContract"]:
                            ThresholdPerc = data["tradeInfoContract"]["tolerance"]
                        else:
                            ThresholdPerc = None
                    if "authorizedTrader" in data:
                        if "entityName" in data["authorizedTrader"]:
                            LastAsgAuthTrader = data["authorizedTrader"]["entityName"]
                        else:
                            LastAsgAuthTrader = None
                    else:
                        LastAsgAuthTrader = None
                    if "tpoDetails" in data:
                        if "organizationId" in data["tpoDetails"]:
                            PoolTypeId = data["tpoDetails"]["organizationId"]
                        else:
                            PoolTypeId = None
                    if "deliveryType" in data:
                        CmmtSubTyp = data["deliveryType"]
                    else:
                        CmmtSubTyp = None
                    if "commitmentDate" in data:
                        EffectDtm = data["commitmentDate"]
                    else:
                        EffectDtm = None
                    if "numberOfLoans" in data:
                        TotalLoans = data["numberOfLoans"]
                    else:
                        TotalLoans = None
                    if "tradeInfoContract" in data:
                        if "id" in data["tradeInfoContract"]:
                            CMMTInfoId = data["tradeInfoContract"]["id"]
                        else:
                            CMMTInfoId = None
                    if "tradeInfoContract" in data:
                        if "id" in data["tradeInfoContract"]:
                            TradeNumber = data["tradeInfoContract"]["id"]
                        else:
                            TradeNumber = None
                    if "deliveredAmount" in data:
                        TotalDeliveredAmt = data["deliveredAmount"]
                    else:
                        TotalDeliveredAmt = None
                    if "assignedAmount" in data:
                        AssignedAmount = data["assignedAmount"]
                    else:
                        AssignedAmount = None
                    if "assignmentPercentage" in data:
                        AssignmentPercentage = data["assignmentPercentage"]
                    else:
                        AssignmentPercentage = None
                    if "lastPublishedDateTime" in data:
                        lastPublishedDateTime = data["lastPublishedDateTime"]
                    else:
                        lastPublishedDateTime = None
                    if "purchasedPercentage" in data:
                        PurchasePercentage = data["purchasedPercentage"]
                    else:
                        PurchasePercentage = None
                    if "totalPairOffAmount" in data:
                        totalPairOffAmount = data["totalPairOffAmount"]
                    else:
                        totalPairOffAmount = None
                    if "totalPairOffGainLoss" in data:
                        totalPairOffGainLoss = data["totalPairOffGainLoss"]
                    else:
                        totalPairOffGainLoss = None                    
                    if "aotInformation" in data:
                        if "aotOriginalTradeDate" in data["aotInformation"]:
                            AOTOriginalTradeDate = data["aotInformation"]["aotOriginalTradeDate"]
                        else:
                            AOTOriginalTradeDate = None
                    if "aotInformation" in data:
                        if "aotOriginalTradeDealer" in data["aotInformation"]:
                            AOTOriginalTradeDealer = data["aotInformation"]["aotOriginalTradeDealer"]
                        else:
                            AOTOriginalTradeDealer = None
                    if "aotInformation" in data:
                        if "aotSecurityCoupon" in data["aotInformation"]:
                            AOTSecurityCoupon = data["aotInformation"]["aotSecurityCoupon"]
                        else:
                            AOTSecurityCoupon = None
                    if "aotInformation" in data:
                        if "aotSecurityPrice" in data["aotInformation"]:
                            AOTSecurityPrice = data["aotInformation"]["aotSecurityPrice"]
                        else:
                            AOTSecurityPrice = None
                    if "aotInformation" in data:
                        if "aotSecurityType" in data["aotInformation"]:
                            AOTSecurityType = data["aotInformation"]["aotSecurityType"]
                        else:
                            AOTSecurityType = None
                    if "tradeInfoContract" in data:
                        if "description" in data["tradeInfoContract"]:
                            Description = data["tradeInfoContract"]["description"]
                        else:
                            Description = None
                    if "openAmount" in data:
                        OpenAmount = data["openAmount"]
                    else:
                        OpenAmount = None
                    if "deliveredPercentage" in data:
                        deliveredPercentage = data["deliveredPercentage"]
                    else:
                        deliveredPercentage = None
                    if "maxNetOpen" in data:
                        MaxNetOpen = data["maxNetOpen"]
                    else:
                        MaxNetOpen = None
                    if "minNetOpen" in data:
                        MinNetOpen = data["minNetOpen"]
                    else:
                        MinNetOpen = None
                    if "pairOffAmount" in data:
                        PairOffAmount = data["pairOffAmount"]
                    else:
                        PairOffAmount = None
                    if "percentAssignmentCompletion" in data:
                        PercentAssignmentCompletion = data["percentAssignmentCompletion"]
                    else:
                        PercentAssignmentCompletion = None
                    if "rejectedAmount" in data:
                        RejectedAmount = data["rejectedAmount"]
                    else:
                        RejectedAmount = None
                    if "rejectedPercentage" in data:
                        RejectedPercentage = data["rejectedPercentage"]
                    else:
                        RejectedPercentage = None
                    if "totalGainLoss" in data:
                        TotalGainLoss = data["totalGainLoss"]
                    else:
                        TotalGainLoss = None
                    if "tradeInfoContract" in data:
                        if "id" in data["tradeInfoContract"]:
                            ID = data["tradeInfoContract"]["id"]
                        else:
                            ID = None
                    if "tradeInfoContract" in data:
                        if "tradeIndicator" in data["tradeInfoContract"]:
                            TradeIndicator = str(data["tradeInfoContract"]["tradeIndicator"])
                        else:
                            TradeIndicator = None
                    
                    if "options" in data:
                        if "value" in data["options"]:
                            CommitmentFundType = data["options"]["value"]
                        else:
                            CommitmentFundType = None
                    else:
                        CommitmentFundType = None
                    if "options" in data:
                        if "value" in data["options"]:
                            OriginationRepresentationAndWarrantyType = data["options"]["value"]
                        else:
                            OriginationRepresentationAndWarrantyType = None
                    else:
                        OriginationRepresentationAndWarrantyType = None
                    # if "tradeInfoContract" in data:
                    #     if "id" in data['tradeInfoContract']:
                    #         id = data['tradeInfoContract']['id']
                    #     else:
                    #         id = None
                    logging.info("Json file read without errors "+str(filename))
                    cursor.execute("Insert into "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_trade_stg"]+" (loancount ,percentWac  ,CommitmentDate  ,commitmentNumber  ,CommitmentType ,ExpirationDate  ,orgId  ,tpoCompanyName  ,maxAmount  ,minAmount  ,Status  ,weightedAvgBulkPrice, Term, StatusCd, CommitmentTypCd, ConfirmationSentDt, ThresholdAmt, ThresholdPerc, LastAsgAuthTrader, PoolTypeId, CmmtSubTyp, EffectDtm, TotalLoans, CMMTInfoId, TradeNumber, TotalDeliveredAmt, AssignedAmount, AssignmentPercentage, lastPublishedDateTime, PurchasePercentage, totalPairOffAmount, totalPairOffGainLoss, AOTOriginalTradeDate, AOTOriginalTradeDealer, AOTSecurityCoupon, AOTSecurityPrice, AOTSecurityType, Description,OpenAmount, deliveredPercentage, MaxNetOpen, MinNetOpen, PairOffAmount, PercentAssignmentCompletion, RejectedAmount, RejectedPercentage, TotalGainLoss, ID, TradeIndicator, CommitmentFundType, OriginationRepresentationAndWarrantyType) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                 loancount, percentWac, commitmentDate, tpoIdtradeInfoContract, commitmentType, expirationDate, orgId, tpoCompanyName, maxAmount, minAmount, Status, weightedAvgBulkPrice, Term, StatusCd, CommitmentTypCd, ConfirmationSentDt, ThresholdAmt, ThresholdPerc, LastAsgAuthTrader, PoolTypeId, CmmtSubTyp, EffectDtm, TotalLoans, CMMTInfoId,TradeNumber, TotalDeliveredAmt, AssignedAmount, AssignmentPercentage, lastPublishedDateTime, PurchasePercentage, totalPairOffAmount, totalPairOffGainLoss, AOTOriginalTradeDate, AOTOriginalTradeDealer, AOTSecurityCoupon, AOTSecurityPrice, AOTSecurityType, Description,OpenAmount, deliveredPercentage, MaxNetOpen, MinNetOpen, PairOffAmount, PercentAssignmentCompletion, RejectedAmount, RejectedPercentage, TotalGainLoss, ID, TradeIndicator, CommitmentFundType, OriginationRepresentationAndWarrantyType)
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

    def trademanagementpairoff(self):
        logging.basicConfig(filename=config["Path"]["Log_TRD"] +
                        "\\log_trade_pairoff_["+date+"].log", level=logging.INFO)

        list_processed=[]
        arr = os.listdir(config["Path"]["Inbound_TRD"])

        for filenames in arr:
            if filenames.startswith('CommitmentDetails'): 
                list_processed.append(filenames)

        cursor.execute("DELETE from "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_tradepairoff_stg"])
        cursor.commit()
        for filename in list_processed:
            try:
                with open(config["Path"]["Inbound_TRD"]+"/"+filename) as filedata:
                    data = json.load(filedata)

                if "tradeInfoContract" in data:
                    if "commitmentNumber" in data['tradeInfoContract']:
                        CommitmentNum = str(data['tradeInfoContract']['commitmentNumber'])
                    else:
                         CommitmentNum = None
                    if "id" in data['tradeInfoContract']:
                            TradeNumber = data['tradeInfoContract']['id']
                    else:
                        TradeNumber = None
                    if "pairOffs" in data:
                        for i in data['pairOffs']:
                            if "calculatedPairOffFee" in i:
                                CalculatedPairOffFeeAmount = i['calculatedPairOffFee']
                            else:
                                 CalculatedPairOffFeeAmount = None
                        
                            if "comments" in i:
                                Comments = i['comments']
                            else:
                                Comments = None
                        
                            if "displayCalculatedPairOffFee" in i:
                                DisplayCalculatedPairOffFeeAmount = i['displayCalculatedPairOffFee']
                            else:
                                DisplayCalculatedPairOffFeeAmount = None
                        
                            if "displayedTradeAmount" in i:
                                    DisplayedTradeAmount = i['displayedTradeAmount']
                            else:
                                DisplayedTradeAmount = None
                            
                            if "index" in i:
                                PairOff_Index = i['index']
                            else:
                                PairOff_Index = None
                        
                            if "date" in i:
                                PairOffDate = i['date']
                            else:
                                PairOffDate = None

                            if "pairOffFeePercentage" in i:
                                PairOffFeePercentage = i['pairOffFeePercentage']
                            else:
                                PairOffFeePercentage = None
                        
                            if "requestedBy" in i:
                                RequestedBy = i['requestedBy']
                            else:
                                RequestedBy = None
                        
                            if "tradeAmount" in i:
                                TradeAmount = i['tradeAmount']
                            else:
                                TradeAmount = None

                            logging.info("Json file read without errors "+str(filename))
                            cursor.execute("Insert into "+server["SqlServer_Connection"]["DBname"]+"."+server["SqlServer_Connection"]["schema_name"]+"."+config["DB_ObjectNames"]["tb_tradepairoff_stg"]+" (CalculatedPairOffFeeAmount ,Comments ,DisplayCalculatedPairOffFeeAmount ,DisplayedTradeAmount ,PairOff_Index ,PairOffDate ,PairOffFeePercentage ,RequestedBy ,TradeAmount ,TradeNumber, CommitmentNum) values (?,?,?,?,?,?,?,?,?,?,?)",
                                CalculatedPairOffFeeAmount, Comments, DisplayCalculatedPairOffFeeAmount, DisplayedTradeAmount, PairOff_Index, PairOffDate, PairOffFeePercentage, RequestedBy, TradeAmount, TradeNumber, CommitmentNum)
                            cursor.commit()
            # except(RuntimeError, TypeError, NameError):
            except Exception as error:
                logging.error("Json file "+str(filename)+" caught with exception "+str(error))
                pass

if __name__ == '__main__':

    currentdate = datetime.datetime.now()
    date = str(currentdate.strftime("%d-%m-%Y%H-%M-%S"))
                
    with open("C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\Global_Config\\config.yaml", 'r') as stream:
        config = yaml.safe_load(stream)

    server = ConfigParser()
    server.read('C:\\Users\\informatica\\lmp_support\\INFA_API_Shared\\ODBC\\ODBC.ini')
    app_env = os.environ['APP_ENV']

    if app_env == 'prd':
        servername = server["SqlServer_Connection"]["servername_prod"]
    elif app_env == 'dev2':
        servername = server["SqlServer_Connection"]["servername_dev2"]
    elif app_env == 'qa':
        servername = server["SqlServer_Connection"]["servername_qa"]
    elif app_env == 'qa2':
        servername = server["SqlServer_Connection"]["servername_qa2"]
    elif app_env == 'stg':
        servername = server["SqlServer_Connection"]["servername_stg"]
    elif app_env == 'stg2':
        servername = server["SqlServer_Connection"]["servername_stg2"]
    else:
        servername = server["SqlServer_Connection"]["servername_dev"]

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server='+servername+';'
                          'Database='+server["SqlServer_Connection"]["DBname"]+';'
                          'Trusted_Connection=yes;')
    cursor = conn.cursor()

    tradeobj = trade(cursor, config, server, date)
    if sys.argv[1]=='TradeMng':
        tradeobj.trademanagementstage()
    elif  sys.argv[1]=='Pairoff':
        tradeobj.trademanagementpairoff()
