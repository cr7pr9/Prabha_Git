
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [FulfilledOn]
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [AVMRunDate] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [AgencyCaseAssignmentDate] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [CumulativeExtensionDays] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [OriginalCreatorFlag] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [TexasA6Ind] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [AppraisalWaiverInd] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [CustomMiniMI] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [AVMFSD] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [HELOCActualBalance] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [HELOCCreditLimit] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [SingleClose_OTCInd] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[los_pcg_lockdetails] drop column [VARenovationInd] 
/*EXECUTE 1 BY 1 IN ORDER */
alter table [clg_reporting].[los_pcg_onprem].[LOS_PCG_lockDetails] drop column Recommendation 
/*EXECUTE 1 BY 1 IN ORDER */
alter table clg_reporting.los_pcg_onprem.LOS_PCG_LockDetails	alter column	 LockPropType varchar(20)