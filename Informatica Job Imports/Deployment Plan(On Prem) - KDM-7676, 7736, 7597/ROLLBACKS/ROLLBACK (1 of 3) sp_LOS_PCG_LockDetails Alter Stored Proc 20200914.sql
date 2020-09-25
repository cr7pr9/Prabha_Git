USE [PCG_Process]
GO
/****** Object:  StoredProcedure [dbo].[sp_LOS_PCG_LockDetails]    Script Date: 9/14/2020 2:32:30 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

/************************************************************* 
Created Date:	2019-11-25

Description:	Creates the PCG LOS  Lock Details tables for Active, Last 18 Months, and All loans.

				<<**>>If this procedure fails, it should be re-run.
				<<**>>Running this script requires write to pcg_process

EXECUTE [dbo].[sp_LOS_PCG_LockDetails] 'LAST18'

Change Log:		Date		Name				Description of Change
				----------	-------------		---------------------
				2019-11-25	Nitin Gangasagar	Create Procedure
				2019-12-16	Joosue Torres		Dashed Ln. 36 "SET LOCK_TIMEOUT 9000"
				2020-01-06  Romeo M				Removed PK for Dev Env *KANAN*
				2020-05-24	Andrew Breman		Moved to sync for kanan merge		
				2020-05-24  Praveen             Updated code as per revised mapping for KANA(KTEST-3208)
				2020-06-24	Jacob Leyba			Added Test Loan Flag
				2020-06-29	Jacob Leyba			Added Legacy_Loanprogram
				2020-07-20	Jacob Leyba			Added initpenddate_ddf and lastpenddate_ddf
				2020-08-18	Jacob Leyba			Updated Test loan flag based on client and not defaulting to "N"
***********************************************************************/

ALTER PROCEDURE [dbo].[sp_LOS_PCG_LockDetails]

@PopFlag		  VARCHAR(25) = 'ALL'		-- DEFAULT LOAN POPULATION IS LAST 18 MONTHS.  VALID VALUES ARE ('ACTIVE','LAST18','ALL')

AS

DECLARE @tries                INT;

SET NOCOUNT ON;

--SET LOCK_TIMEOUT 9000; -- TIME OUT IS NOW SET 2 SECONDS OVERRIDES THE SYSTEM DEFAULT OF INFINITY

 --BEGIN WRAPPER CODE

	DECLARE 
	@dbname			VARCHAR(150) = DB_NAME(),
	@schema			VARCHAR(25)  = Object_SCHEMA_NAME(@@PROCID),
	@spname			VARCHAR(150) = OBJECT_NAME(@@PROCID),
	@ERRORMESSAGE	VARCHAR(500),
	@ERRORLINE            VARCHAR(10),
	@ERRORNUMBER    INT 

	EXEC PCG_BusSpprt_DC.dbo.sp_SP_Start
		@dbname,
		@schema,
		@spname

 --END WRAPPER CODE

BEGIN TRY
/************************************************************* 
Created Date:	2019-11-20

Description:	Creates the PCG LOS Lock Details tables for All loans.

***********************************************************************/
DECLARE @StartDt DATETIME = DATEADD(mm,DATEDIFF(mm,0,DATEADD(MONTH, -18, GETDATE())),0)	-- THIS IS USED TO SPECIFY A DATE RANGE TO SELECT AFTER  -- GET 18 MONTHS OF DATA
DECLARE @StartDt_ActiveRun DATETIME = DATEADD(mm,DATEDIFF(mm,0,DATEADD(MONTH, -3, GETDATE())),0)	-- THIS IS USED TO SPECIFY A DATE RANGE TO SELECT AFTER  -- GET 3 month OF DATA for active pop

IF OBJECT_ID('tempdb..#xx_Temp_LS_Tables_LoanAppLoc1') Is Not Null DROP TABLE #xx_Temp_LS_Tables_LoanAppLoc1

SELECT lal.loannum
			,lal.loanappid
			,lal.loantranid	
			,[LAL].LstStsDtCd

INTO		#xx_Temp_LS_Tables_LoanAppLoc1

FROM		PNMAC_CORRLOSPROD.dbo.LoanAppLoc1 AS [LAL] WITH(NOLOCK)

------------WHERE		(
------------				(	@PopFlag = 'ACTIVE'
------------					AND EXISTS (SELECT * FROM prod_strategy.dbo.LOS_PCG_LoanDetails_Active zz WITH(NOLOCK) WHERE zz.LoanNum = [LAL].LoanNum)
------------				)
------------				OR
------------				(	@PopFlag = 'LAST18'
------------					AND EXISTS (SELECT * FROM prod_strategy.dbo.LOS_PCG_LoanDetails_Last18 zz WITH(NOLOCK) WHERE zz.LoanNum = [LAL].LoanNum)
------------				)
------------				OR
------------				(	@PopFlag = 'ALL'
------------					AND EXISTS (SELECT * FROM prod_strategy.dbo.LOS_PCG_LoanDetails_All zz WITH(NOLOCK) WHERE zz.LoanNum = [LAL].LoanNum) 
------------				)
------------			);



CREATE CLUSTERED INDEX IX_LS_PCG_LoanAppLoc1_LoanAppId
    ON #xx_Temp_LS_Tables_LoanAppLoc1 (LoanAppId) ;
 CREATE NONCLUSTERED INDEX NC_LS_PCG_LoanAppLoc1_LoanTranId
    ON #xx_Temp_LS_Tables_LoanAppLoc1 (LoanTranId) ;
 CREATE NONCLUSTERED INDEX NC_LS_PCG_LoanAppLoc1_LoanNum
    ON #xx_Temp_LS_Tables_LoanAppLoc1(LoanNum) 

-------------------------------------------------------------------------------------------------------------------------------------------------------

--02 #LockRqstInfoLoc1
	
IF OBJECT_ID('tempdb..#xx_Temp_LS_Tables_LockRqstInfoLoc1') Is Not Null DROP TABLE #xx_Temp_LS_Tables_LockRqstInfoLoc1;

SELECT LRIL.loannum
			,LRIL.loanappid
			,[AggrLockDays]				= LRIL.AggrLockDays
			,[AmortTerm]				= LRIL.AmortTerm
			,[AmortTypCd]				= LRIL.AmortTypCd
			,[AUSRecommendationCd]		= LRIL.AUSRecommendationCd
			,[BaseLoanAmt]				= LRIL.BaseLoanAmt
			,[BorrCount]				= LRIL.BorrCount
			,[CLTV]						= LRIL.CLTV
			,[Commitmenttypcd]			= LRIL.Commitmenttypcd
			,[CorrLoanNum]				= LRIL.CorrLoanNum
			,[DebtRatio]				= LRIL.DebtRatio
			,[DocLevelCd]				= LRIL.DocLevelCd
			,[DURecommendation]			= LRIL.DURecommendation
			,[ENoteInd]					= LRIL.ENoteInd
			,[EPMIInd]					= LRIL.EPMIInd
			,[FinalPrice]				= LRIL.FinalPrice
			,[HomeStyleInd]				= LRIL.HomeStyleInd
			,[HousingRatio]				= LRIL.HousingRatio
			,[IndexVal]					= LRIL.IndexVal
			,[InitialLockDays]			= LRIL.InitialLockDays
			,[InitialLockDt]			= LRIL.InitialLockDt
			,[IntRate]					= LRIL.IntRate
			,[LienPos]					= LRIL.LienPos
			,[LoanAmt]					= LRIL.LoanAmt
			,[LockDays]					= LRIL.LockDays
			,[LockedBy]					= LRIL.LockedBy
			,[LockExtDays]				= LRIL.LockExtDays
			,[LockRqstDtm]				= LRIL.LockRqstDtm
			,[LockRqstInfoId]			= LRIL.LockRqstInfoId
			,[LockStsCd]				= LRIL.LockStsCd
			,[LockTypCd]				= LRIL.LockTypCd
			,[LPRecommendation]			= LRIL.LPRecommendation
			,[LTV]						= LRIL.LTV
			,[Margin]					= LRIL.Margin
			,[MtgTypCd]					= LRIL.MtgTypCd
			,[NetPrice]					= LRIL.NetPrice
			,[NonQMInd]					= LRIL.NonQMInd
			,[NumOfLockExt]				= LRIL.NumOfLockExt
			,[NumOfRelocks]				= LRIL.NumOfRelocks
			,[NumOfUnits]				= LRIL.NumOfUnits
			,[Price]					= LRIL.Price
			,[PriceQuoteDtm]			= LRIL.PriceQuoteDtm
			,[Product]					= LRIL.Product
			,[PropAddr1]				= LRIL.PropAddr1
			,[PropAddr2]				= LRIL.PropAddr2
			,[PropCity]					= LRIL.PropCity
			,[PropCnty]					= LRIL.PropCnty
			,[PropertyVal]				= LRIL.PropertyVal
			,[PropOccupancyTypCd]		= LRIL.PropOccupancyTypCd
			,[PropSt]					= LRIL.PropSt
			,[PropTypCd]				= LRIL.PropTypCd
			,[PropZip]					= LRIL.PropZip
			,[PurposeCd]				= LRIL.PurposeCd
			,[QualifyingFico]			= LRIL.QualifyingFico
			,[RenovationInd]			= LRIL.RenovationInd
			,[RuralPropertyInd]			= LRIL.RuralPropertyInd
			,[selfemployedind]			= LRIL.selfemployedind
			,[SourceID]					= LRIL.SourceID
			,[SubOrdinateFinanceAmt]	= LRIL.SubOrdinateFinanceAmt
			,[SubOrdinateFinancingInd]  = LRIL.SubOrdinateFinancingInd
			,[TempBuydownCd]			= LRIL.TempBuydownCd
			,[Two3k]					= LRIL.Two3k
			,[CashOutAmount]			= LRIL.CashOutAmount
			,LockDt						= LRIL.LockDt
			,LockExpDt					= LRIL.LockExpDt
			,lockstatus					= CASE WHEN LRIL.LockStsCd IN ('CNCL', 'CORLCNL') 	   THEN 'CANCELLED' 
											   WHEN LRIL.LockTypCd = 'CNCL' 				   THEN 'CANCELLED' 
											   WHEN LRIL.LockTypCd = 'EXPD' 				   THEN 'EXPIRED' 
											   WHEN LRIL.LockTypCd = 'LOCK' 				   THEN 'LOCKED' 
											   WHEN	LRIL.LockTypCd = 'REJE'					   THEN 'REJECTED' 
											   WHEN LRIL.LockTypCd = 'LFPA'					   THEN 'LOCK FOR ELIGIBILITY REVIEW' 
											   WHEN LRIL.LockTypCd = 'LKEX'					   THEN 'LOCK EXTN.' 
											   WHEN	LRIL.LockTypCd = 'RELK'					   THEN 'RE-LOCK' 
											   WHEN LRIL.LockTypCd = 'RFPA'					   THEN 'REGISTER FOR ELIGIBILITY REVIEW' 
											   ELSE 'Uknown' 
										  END 
			,LRIL.PrepaymentPenaltyInd
			,LRIL.MonthlyReserves
			,LRIL.CreateDtm
			,LRIL.SourceID AS ClientID
			------Start of Kanan Adds
			--------,LRIL.RuralPropertyInd
			 ,CASE WHEN LRIL.PurposeCd = 'PRCH' THEN 'PURCHASE' WHEN LRIL.PurposeCd = 'REFI' THEN 'REFINANCE-CASHOUT' WHEN LRIL.PurposeCd = 'RFRT' THEN 'REFINANCE-RATEANDTERM'
                       ELSE 'Other' END AS [LoanPurpose]

			,                      CASE WHEN LRIL.PropOccupancyTypCd = 'SOLD' THEN 'Sold' WHEN LRIL.PropOccupancyTypCd = 'RTPR' THEN 'Primary Residence' WHEN LRIL.PropOccupancyTypCd = 'RTRL'
                       THEN 'Rental Living' WHEN LRIL.PropOccupancyTypCd = 'PNSL' THEN 'Pending Sale' WHEN LRIL.PropOccupancyTypCd = 'RTNO' THEN 'Non-Owner Occupied' WHEN LRIL.PropOccupancyTypCd
                       = 'RTSR' THEN 'SECOND HOME' ELSE NULL END AS [LockOccType]
			,                      CASE WHEN LRIL.PropTypCd = '1FAM' THEN 'Single Family' WHEN LRIL.PropTypCd = '24FM' THEN '2-4 UNIT FAMILY' WHEN LRIL.PropTypCd = 'CMMR' THEN 'COMMERCIAL RESIDENCE'
                       WHEN LRIL.PropTypCd = 'COND' THEN 'CONDOMINIUM' WHEN LRIL.PropTypCd = 'PUD' THEN 'PUD' when LRIL.PropTypCd = 'DTCN' then 'Detached Condo' ELSE  'Other' END AS [LockPropType]
			,NonDelInd = CASE WHEN LRIL.UNDWMethodTyp = 'NDLT' THEN 'Y' ELSE 'N' END
			,LRIL.AppraisedValue
			,LRIL.BaseLoanCLTV
			,LRIL.BaseLoanLTV
			,LRIL.BorrFICO
			,LRIL.BorrLstNm
			,LRIL.CoBorrFICO
			,LRIL.Comments
			,LRIL.ConfirmationNum
			,LRIL.EscrowWaivedInd
			,LRIL.GuaranteeFeeFinancedInd
			,LRIL.HomeOneInd
			,LRIL.HomePossibleAdvInd
			,LRIL.HomePossibleInd
			,LRIL.HomeReadyInd
			,LRIL.LifeFloor
			,LRIL.LoanType
			,LRIL.LockStsDtm
			,LRIL.ModDtm
			,LRIL.PeriodicCap
			,LRIL.PrepaymentTypCd
			,LRIL.TotalLoanCLTV
			,LRIL.TotalLoanLTV
			,LRIL.UNDWMethodTyp
			,ROW_NUMBER() OVER (PARTITION BY loannum ORDER BY createdtm DESC) as [rank]
			,Legacy_Loanprogram = LRIL.Product
			
INTO #xx_Temp_LS_Tables_LockRqstInfoLoc1

--from pnmac_corrlosprod.dbo.LockRqstInfoLoc1 LRIL  with(nolock)
from PNMAC_CorrPortalPROD.dbo.LockRqstInfo LRIL  with(nolock)

WHERE		(
				(	@PopFlag = 'ACTIVE'
					--AND EXISTS (SELECT * FROM prod_strategy.dbo.LOS_PCG_LoanDetails_Active zz WITH(NOLOCK) WHERE zz.LoanNum = [LRIL].LoanNum)
					and LRIL.CreateDtm >= @StartDt_ActiveRun
					AND EXISTS (SELECT *  FROM PNMAC_CorrPortalPROD.dbo.LockRqstInfo zz WITH(NOLOCK) WHERE zz.LoanNum = [LRIL].LoanNum and loannum <> ' ') 
				)
				--OR
				--(	@PopFlag = 'LAST18'
				--	AND EXISTS (SELECT * FROM pnmac_corrlosprod.dbo.LockRqstInfoLoc1 zz WITH(NOLOCK)  
				--	WHERE InitialLockDt >= @StartDt OR InitialLockDt >= @StartDt
				--	and zz.LoanNum = [LRIL].LoanNum
				--	)
					OR
			(	@PopFlag = 'LAST18'
				AND	(	
						--LRIL.InitialLockDt >= @StartDt
						--OR LRIL.InitialLockDt >= @StartDt

						(LRIL.CreateDtm >= @StartDt --------added jleyba 20200124
						OR LRIL.CreateDtm >= @StartDt)
				AND EXISTS (SELECT *  FROM PNMAC_CorrPortalPROD.dbo.LockRqstInfo zz WITH(NOLOCK) WHERE zz.LoanNum = [LRIL].LoanNum and loannum <> ' ') 


					)
				
				)
				OR
				(	@PopFlag = 'ALL'
					
					AND EXISTS (SELECT *  FROM PNMAC_CorrPortalPROD.dbo.LockRqstInfo zz WITH(NOLOCK) WHERE zz.LoanNum = [LRIL].LoanNum and loannum <> ' ') 
					--AND EXISTS (SELECT *  FROM PNMAC_CorrPortalPROD.dbo.LockRqstInfo zz WITH(NOLOCK) WHERE zz.LockRqstInfoId = [LRIL].LockRqstInfoId) 
					
					--SELECT *  FROM pnmac_corrlosprod.dbo.LockRqstInfoLoc1 zz WITH(NOLOCK) WHERE zz.LoanNum = [LRIL].LoanNum) 
				)
			);

CREATE CLUSTERED INDEX IX_LS_PCG_xxLockRqstInfoLoc1_LoanAppId
    ON #xx_Temp_LS_Tables_LockRqstInfoLoc1 (LoanAppId);

	delete from #xx_Temp_LS_Tables_LockRqstInfoLoc1
	where [rank] <> 1

--01 #AddnLoanAppLoc1

If OBJECT_ID('tempdb..#xx_Temp_LS_Tables_AddnLoanAppLoc1') Is Not Null drop table #xx_Temp_LS_Tables_AddnLoanAppLoc1;
SELECT ALAL.loanappid
			,ALAL.CommitmentNumber
			,ALAL.AddOnBuyPrice
			,ALAL.BuyPrice			
			,ALAL.Two3k
			,ROW_NUMBER() OVER (PARTITION BY loanappid ORDER BY createdtm DESC) as [rank]
INTO	#xx_Temp_LS_Tables_AddnLoanAppLoc1
FROM    pnmac_corrportalProd.dbo.AddnLoanApp ALAL WITH(NOLOCK)  

	delete from #xx_Temp_LS_Tables_AddnLoanAppLoc1
	where [rank] <> 1


CREATE CLUSTERED INDEX IX_LS_PCG_xxAddnLoanAppLoc1_LoanAppId
    ON #xx_Temp_LS_Tables_AddnLoanAppLoc1 (LoanAppId);

------------
If OBJECT_ID('tempdb..#xx_Temp_LS_Tables_CLGBELocks') Is Not Null drop table #xx_Temp_LS_Tables_CLGBELocks;
SELECT       Cl.LoanNum			
			,CL.CEMAFlag			
			,CL.FHA203kFlag
INTO	#xx_Temp_LS_Tables_CLGBELocks 
FROM    prod_strategy.dbo.CLGBELocks  CL WITH (NOLOCK)      


CREATE CLUSTERED INDEX IX_xx_LS_Tables_CLGBELocks
    ON #xx_Temp_LS_Tables_CLGBELocks (LoanNum);



--02 #CMMTinfo
If OBJECT_ID('tempdb..#xx_Temp_LS_Tables_CMMTinfo') Is Not Null drop table #xx_Temp_LS_Tables_CMMTinfo;

select cmmt1.PoolNum
			,cmmt1.CommitDT
			,cmmt1.CommitmentTypCd
			,cmmt1.CmmtSubTyp
			,cmmt1.Comments
			 ,cmmt1.cmmtinfoid
INTO	#xx_Temp_LS_Tables_CMMTinfo

FROM    PNMAC_CORRLOSPROD.dbo.CMMTinfo [cmmt1] WITH(NOLOCK)


CREATE CLUSTERED INDEX IX_LS_PCG_xxCMMTinfo_LoanAppId
    ON #xx_Temp_LS_Tables_CMMTinfo (PoolNum);


--03 #CMMTDetail
If OBJECT_ID('tempdb..#xx_Temp_LS_Tables_CMMTDetail') Is Not Null drop table #xx_Temp_LS_Tables_CMMTDetail;

select cmmt2.cmmtinfoid
			,cmmt2.refid
			,cmmt2.baseprice
			,ROW_NUMBER() OVER (PARTITION BY refid ORDER BY moddtm DESC) as [rank]
INTO	#xx_Temp_LS_Tables_CMMTDetail

FROM    PNMAC_CORRLOSPROD.dbo.CMMTDetail [cmmt2] WITH(NOLOCK)

	delete from #xx_Temp_LS_Tables_CMMTDetail
	where [rank] <> 1

CREATE CLUSTERED INDEX IX_LS_PCG_xxCMMTDetail_LoanAppId
    ON #xx_Temp_LS_Tables_CMMTDetail (cmmtinfoid);





-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

--04 #PartyCompDtl
If OBJECT_ID('tempdb..#xx_Temp_LS_Tables_PartyCompDtl') Is Not Null drop table #xx_Temp_LS_Tables_PartyCompDtl;

select b.CompDtlId
				,b.CompNm
INTO	#xx_Temp_LS_Tables_PartyCompDtl

FROM    PNMAC_CORRLOSPROD.dbo.PartyCompDtl [b] WITH(NOLOCK)

CREATE CLUSTERED INDEX IX_LS_PCG_xxPartyCompDtl_CompDtlId
    ON #xx_Temp_LS_Tables_PartyCompDtl (CompDtlId);


--05 #LoanStsAction
If OBJECT_ID('tempdb..#xx_Temp_LS_Tables_LoanStsAction') Is Not Null drop table #xx_Temp_LS_Tables_LoanStsAction;

select d.ActionCd
			, d .DisplayText

INTO	#xx_Temp_LS_Tables_LoanStsAction

FROM    PNMAC_CORRLOSPROD.dbo.LoanStsAction [d] WITH(NOLOCK)

CREATE CLUSTERED INDEX IX_LS_PCG_xxLoanStsAction_ActionCd
    ON #xx_Temp_LS_Tables_LoanStsAction (ActionCd);


----------08 # PNMAC_CorrPortalProd.dbo.LoanApp
------KANAN ADD
IF OBJECT_ID('tempdb..#LoanApp') IS NOT NULL DROP TABLE #LoanApp

SELECT loanappid
,InitCap
,LifeCap
,UWProgramSetNm
,loannum
,ROW_NUMBER() OVER (PARTITION BY loannum ORDER BY createdtm DESC) as [rank]
into #LoanApp

from PNMAC_CorrPortalProd.dbo.LoanApp

CREATE CLUSTERED INDEX IX_LS_PCG_loan_master_loanappid
    ON #LoanApp (loanappid);

delete from #LoanApp
where [rank] <> 1



----------08 # PNMAC_CorrPortalProd.dbo.AddnLoanApp
------KANAN ADD
IF OBJECT_ID('tempdb..#AddnLoanApp') IS NOT NULL DROP TABLE #AddnLoanApp

SELECT loanappid
,FrmEnhRef
,ROW_NUMBER() OVER (PARTITION BY loanappid ORDER BY moddtm DESC) as rank
into #AddnLoanApp

from PNMAC_CorrPortalProd.dbo.AddnLoanApp

CREATE CLUSTERED INDEX IX_LS_PCG_loan_master_loanappid
    ON #AddnLoanApp (loanappid);

delete from #AddnLoanApp where rank <> 1

-------------------------------------------------------------------------------------------------------------------------------------------------------
	If OBJECT_ID('DBO.LOS_PCG_LockDetails_Staging') Is Not Null drop table DBO.LOS_PCG_LockDetails_Staging;
-----------------------------------------------------------------------------------------------------------------------
-------commented out for Kanan
--SELECT	* 
--INTO	DBO.LOS_PCG_LockDetails_Staging
--FROM	DBO.LOS_PCG_LockDetails_Active 
--WHERE	1=2 

----------ALTER TABLE  PCG_Process.DBO.LOS_PCG_LockDetails_Staging

----------ALTER COLUMN loannum varchar(20) not null ;

----------Removed PK for Dev Env *KANAN*
--ALTER TABLE [dbo].[LOS_PCG_LockDetails_Staging] ADD  CONSTRAINT [PK_LOS_PCG_LockDetails_Staging_LoanNum] PRIMARY KEY CLUSTERED 
--(
--[LoanNum] ASC 
--)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY];

---------commented out for Kanan
--INSERT INTO DBO.LOS_PCG_LockDetails_Staging


SELECT		 
			LRIL.loannum
			,LRIL.loanappid
			,lal.loantranid
			,ALAL.CommitmentNumber
			/*FIELD ADDS */
			,LRIL.PrepaymentPenaltyInd
			,ALAL.AddOnBuyPrice
			,cmmt2.baseprice
			,ALAL.BuyPrice
			,LRIL.MonthlyReserves
			,cmmt1.CommitDT

			/*SUDHA's list 20191120 */

			/*LockRqstInfoLoc1 Source */
			,[AggrLockDays] = LRIL.AggrLockDays
			,[AmortTerm] = LRIL.AmortTerm
			,[AmortTypCd] = LRIL.AmortTypCd
			,[AUSRecommendationCd] = LRIL.AUSRecommendationCd
			,[BaseLoanAmt] = LRIL.BaseLoanAmt
			,[BorrCount] = LRIL.BorrCount
			,[CLTV] = LRIL.CLTV
			,[Commitmenttypcd] = LRIL.Commitmenttypcd
			,[CorrLoanNum] = LRIL.CorrLoanNum
			,[DebtRatio] = LRIL.DebtRatio
			,[DocLevelCd] = LRIL.DocLevelCd
			,[DURecommendation] = LRIL.DURecommendation
			,[ENoteInd] = LRIL.ENoteInd
			,[EPMIInd] = LRIL.EPMIInd
			,[FinalPrice] = LRIL.FinalPrice
			,[HomeStyleInd] = LRIL.HomeStyleInd
			,[HousingRatio] = LRIL.HousingRatio
			,[IndexVal] = LRIL.IndexVal
			,[InitialLockDays] = LRIL.InitialLockDays
			,[InitialLockDt] = LRIL.InitialLockDt
			,[IntRate] = LRIL.IntRate
			,[LienPos] = LRIL.LienPos
			,[LoanAmt] = LRIL.LoanAmt
			,[LockDays] = LRIL.LockDays
			,[LockedBy] = LRIL.LockedBy
			,[LockExtDays] = LRIL.LockExtDays
			,[LockRqstDtm] = LRIL.LockRqstDtm
			,[LockRqstInfoId] = LRIL.LockRqstInfoId
			,[LockStsCd] = LRIL.LockStsCd
			,[LockTypCd] = LRIL.LockTypCd
			,[LPRecommendation] = LRIL.LPRecommendation
			,[LTV] = LRIL.LTV
			,[Margin] = LRIL.Margin
			,[MtgTypCd] = LRIL.MtgTypCd
			,[NetPrice] = LRIL.NetPrice
			,[NonQMInd] = LRIL.NonQMInd
			,[NumOfLockExt] = LRIL.NumOfLockExt
			,[NumOfRelocks] = LRIL.NumOfRelocks
			,[NumOfUnits] = LRIL.NumOfUnits
			,[Price] = LRIL.Price
			,[PriceQuoteDtm] = LRIL.PriceQuoteDtm
			,[Product] = LRIL.Product
			,[PropAddr1] = LRIL.PropAddr1
			,[PropAddr2] = LRIL.PropAddr2
			,[PropCity] = LRIL.PropCity
			,[PropCnty] = LRIL.PropCnty
			,[PropertyVal] = LRIL.PropertyVal
			,[PropOccupancyTypCd] = LRIL.PropOccupancyTypCd
			,[PropSt] = LRIL.PropSt
			,[PropTypCd] = LRIL.PropTypCd
			,[PropZip] = LRIL.PropZip
			,[PurposeCd] = LRIL.PurposeCd
			,[QualifyingFico] = LRIL.QualifyingFico
			,[RenovationInd] = LRIL.RenovationInd
			,[RuralPropertyInd] = LRIL.RuralPropertyInd
			,[selfemployedind] = LRIL.selfemployedind
			,[SourceID] = LRIL.SourceID
			,[SubOrdinateFinanceAmt] = LRIL.SubOrdinateFinanceAmt
			,[SubOrdinateFinancingInd] = LRIL.SubOrdinateFinancingInd
			,[TempBuydownCd] = LRIL.TempBuydownCd
			,[Two3k] = ALAL.Two3k
			,[CashOutAmount] = LRIL.CashOutAmount
			/*CMMTinfo Source */
			/*mando locks Source */
			/*CLGBELocks Source */
			,CASE WHEN d .DisplayText IS NULL THEN 'Loan Not Delivered' ELSE d .DisplayText END AS [CurrentLoanSts]
			,LockDt											= LRIL.LockDt
			,LockExpDt										= LRIL.LockExpDt
			,lockstatus									= LRIL.lockstatus
			,CommitmentType_Mando = case when LRIL.Commitmenttypcd in('AOT','BULK','MAND') then  
															(CASE 
																WHEN cmmt1.CommitmentTypCd = 'BULK'			
																	AND cmmt1.CmmtSubTyp = 'AOT'
																	THEN 'Bulk'
																WHEN cmmt1.Comments LIKE 'MSR%'
																	OR cmmt1.CmmtSubTyp IN ('BB','BF','NBB','NBF')
																	THEN 'MSR'		
																WHEN cmmt1.CommitmentTypCd = 'AOT'
																	OR cmmt1.Comments LIKE 'AOT%'
																	OR cmmt1.CmmtSubTyp = 'AOT'
																	THEN 'AOT'
																WHEN cmmt1.CommitmentTypCd = 'DT'
																	OR cmmt1.Comments LIKE 'DT%'
																	OR cmmt1.CmmtSubTyp = 'DT'
																	THEN 'DT'
																WHEN cmmt1.CommitmentTypCd = 'MAND'
																	AND CHARINDEX('IN', cmmt1.Comments, CHARINDEX('ALL', cmmt1.Comments)) - CHARINDEX('ALL', cmmt1.Comments) BETWEEN 4
																		AND 5
																	THEN 'Bulk'	
																WHEN cmmt1.CommitmentTypCd = 'BULK'
																	THEN 'Bulk'	
																ELSE 'Mand Flow'
																END) else null end
							/*Kanan Field adds */
							,la.InitCap
							,la.LifeCap
							------,la.UWProgramSetNm
							------,ala.FrmEnhRef
							,LRIL.CreateDTM
							/*Kanan Field adds 20200214 */
							,CL.[CEMAFlag] 
							,LRIL.ClientID
							,B.CompNm
							,CL.FHA203kFlag
							,LRIL.LoanPurpose
							,LRIL.[LockOccType]
							,LRIL.[LockPropType]
							,LRIL.NonDelInd
							,LRIL.AppraisedValue
			,LRIL.BaseLoanCLTV
			,LRIL.BaseLoanLTV
			,LRIL.BorrFICO
			,LRIL.BorrLstNm
			,LRIL.CoBorrFICO
			,LRIL.Comments
			,LRIL.ConfirmationNum
			,LRIL.EscrowWaivedInd
			,LRIL.GuaranteeFeeFinancedInd
			,LRIL.HomeOneInd
			,LRIL.HomePossibleAdvInd
			,LRIL.HomePossibleInd
			,LRIL.HomeReadyInd
			,LRIL.LifeFloor
			,LRIL.LoanType
			,LRIL.LockStsDtm
			,LRIL.ModDtm
			,LRIL.PeriodicCap
			,LRIL.PrepaymentTypCd
			,LRIL.TotalLoanCLTV
			,LRIL.TotalLoanLTV
			,LRIL.UNDWMethodTyp
			,[RowCreateDTM] = GETDATE()
			, TestLoanFlag = case when LRIL.clientid in('700123') then 'Y' 
									when LRIL.loannum in('80000038','80000041','8000016126') then 'Y' 
										else 'N' end
			,LRIL.Legacy_Loanprogram
			,initpenddate_ddf = cast (null as datetime)
			,lastpenddate_ddf = cast (null as datetime)

iNTO DBO.LOS_PCG_LockDetails_Staging


FROM #xx_Temp_LS_Tables_LockRqstInfoLoc1 LRIL 	 WITH(NOLOCK)  ----alter to be base temp table 20200121 jleyba

LEFT JOIN #xx_Temp_LS_Tables_LoanAppLoc1 AS [LAL]

ON LAL.loannum = LRIL.loannum --------updated for kanan changes during downstream cert 20200517 jleyba

LEFT JOIN #xx_Temp_LS_Tables_AddnLoanAppLoc1 ALAL 
ON LRIL.loanappid = ALAL.loanappid

LEFT JOIN #xx_Temp_LS_Tables_CLGBELocks CL
ON CL.LoanNum = LRIL.loannum

LEFT JOIN #xx_Temp_LS_Tables_CMMTinfo cmmt1
ON cmmt1.PoolNum = ALAL.CommitmentNumber

LEFT JOIN #xx_Temp_LS_Tables_CMMTDetail cmmt2
ON cmmt1.cmmtinfoid = cmmt2.cmmtinfoid and cmmt2.refid = alal.loanappid

LEFT JOIN #xx_Temp_LS_Tables_PartyCompDtl AS b  WITH(NOLOCK)  
ON b.CompDtlId = LRIL.SourceId

LEFT JOIN #xx_Temp_LS_Tables_LoanStsAction AS d   WITH(NOLOCK) 
ON d .ActionCd = [LAL].LstStsDtCd

LEFT JOIN #LoanApp		AS [la]	WITH(NOLOCK) ---------updated as part of kanan testing for edward. Needs to be updated in dev and stage as well
ON la.loannum = LRIL.loannum

LEFT JOIN #AddnLoanApp		AS [ala]	WITH(NOLOCK) 
ON ala.loanappid = LAL.loanappid



--Removed PK for Dev Env *KANAN*
------------------------------------------Populate Hubs----------------------------------------------------
----ALTER TABLE dbo.LOS_PCG_LockDetails_Staging DROP CONSTRAINT [PK_LOS_PCG_LockDetails_Staging_LoanNum];
-----------------------------------------------------------------------------------------------------------

IF @PopFlag = 'ALL'
	BEGIN
		IF OBJECT_ID('dbo.LOS_PCG_LockDetails_All') IS NOT NULL DROP TABLE  dbo.LOS_PCG_LockDetails_All;
		EXECUTE SP_RENAME 'dbo.LOS_PCG_LockDetails_Staging', 'LOS_PCG_LockDetails_All';

		CREATE CLUSTERED INDEX IX_LOS_PCG_LockDetails_LoanNum
			ON  dbo.LOS_PCG_LockDetails_All
			(LoanNum);

		IF OBJECT_ID('dbo.LOS_PCG_LockDetails_Last18') IS NOT NULL DROP TABLE  dbo.LOS_PCG_LockDetails_Last18;

		SELECT A.* INTO  dbo.LOS_PCG_LockDetails_Last18 
		
		FROM  dbo.LOS_PCG_LockDetails_All A ---JOIN  PROD_STRATEGY.dbo.LOS_PCG_LoanDetails_Last18 B 
		
		where A.InitialLockDt >= @StartDt
						
		
		-----on A.LoanNum = B.LoanNum
		;

		CREATE CLUSTERED INDEX IX_LOS_PCG_LockDetails_LoanNum
			ON  dbo.LOS_PCG_LockDetails_Last18
			(LoanNum);
		
		IF OBJECT_ID('dbo.LOS_PCG_LockDetails_Active') IS NOT NULL DROP TABLE  dbo.LOS_PCG_LockDetails_Active;

		SELECT A.* INTO  dbo.LOS_PCG_LockDetails_Active FROM  dbo.LOS_PCG_LockDetails_All A --replaced20200529-----JOIN  PROD_STRATEGY.dbo.LOS_PCG_LoanDetails_Active B on A.LoanNum = B.LoanNum;
		where A.CreateDtm >= @StartDt_ActiveRun
		


		CREATE CLUSTERED INDEX IX_LOS_PCG_LockDetails_LoanNum
			ON  dbo.LOS_PCG_LockDetails_Active
			(LoanNum);
	END;

-- if Last 18 then: 1. drop and rename to Last18; 2: copy Active to Active
IF @PopFlag = 'Last18'
	BEGIN
		IF OBJECT_ID('dbo.LOS_PCG_LockDetails_Last18') IS NOT NULL DROP TABLE dbo.LOS_PCG_LockDetails_Last18;
				EXECUTE dbo.SP_RENAME 'dbo.LOS_PCG_LockDetails_Staging', 'LOS_PCG_LockDetails_Last18';

		CREATE CLUSTERED INDEX IX_LOS_PCG_LockDetails_LoanNum
			ON dbo.LOS_PCG_LockDetails_Last18
			(LoanNum);

		IF OBJECT_ID('dbo.LOS_PCG_LockDetails_Active') IS NOT NULL DROP TABLE dbo.LOS_PCG_LockDetails_Active;
		SELECT A.* INTO dbo.LOS_PCG_LockDetails_Active FROM dbo.LOS_PCG_LockDetails_Last18 A -----JOIN PROD_STRATEGY.dbo.LOS_PCG_LoanDetails_Active B on A.LoanNum = B.LoanNum;
		where A.CreateDtm >= @StartDt_ActiveRun
		CREATE CLUSTERED INDEX IX_LOS_PCG_LockDetails_LoanNum
			ON dbo.LOS_PCG_LockDetails_Active
			(LoanNum);
	END;

-- if Active then: 1. drop and rename to Active

IF @PopFlag = 'Active'
	BEGIN
		IF OBJECT_ID('dbo.LOS_PCG_LockDetails_Active') IS NOT NULL DROP TABLE dbo.LOS_PCG_LockDetails_Active;
				EXECUTE dbo.SP_RENAME 'dbo.LOS_PCG_LockDetails_Staging', 'LOS_PCG_LockDetails_Active';

		CREATE CLUSTERED INDEX IX_LOS_PCG_LockDetails_LoanNum
			ON dbo.LOS_PCG_LockDetails_Active
			(LoanNum);
	END;

	/*ADDED FOR KANAN */
If @PopFlag = 'All'
BEGIN
execute [clg_strategy].[dbo].[sp_async_execute] 'exec clg_reporting.dbo.usp_merge_LOS_PCG_LockDetails ''All'';'
END

If @PopFlag = 'Last18'
BEGIN
execute [clg_strategy].[dbo].[sp_async_execute] 'exec clg_reporting.dbo.usp_merge_LOS_PCG_LockDetails ''Last18'';'
END

If @PopFlag = 'Active'
BEGIN
execute [clg_strategy].[dbo].[sp_async_execute] 'exec clg_reporting.dbo.usp_merge_LOS_PCG_LockDetails ''Active'';'
END


-- TABLE CLEANUP

If OBJECT_ID('DBO.LOS_PCG_LockDetails_Staging') Is Not Null drop table DBO.LOS_PCG_LockDetails_Staging;

-- BEGIN END WRAPPER CODE	

		EXEC PCG_BusSpprt_DC.dbo.sp_SP_End
			@dbname,
			@schema,
			@spname

---- END END WRAPPER CODE

END TRY

BEGIN CATCH
-- BEGIN ERROR WRAPPER CODE	
	set @ERRORLINE		= ERROR_LINE();
	set	@ERRORMESSAGE	= ERROR_MESSAGE();
	set @ERRORNUMBER    = ERROR_NUMBER();
	select @errorline, @errormessage, @errorNumber 
	EXEC PCG_BusSpprt_DC.dbo.sp_SP_End_Error
		@dbname,
		@schema,
		@spname,
		@ErrorLine,
		@ErrorMessage,
		@ErrorNumber
-- END ERROR WRAPPER CODE

END CATCH



