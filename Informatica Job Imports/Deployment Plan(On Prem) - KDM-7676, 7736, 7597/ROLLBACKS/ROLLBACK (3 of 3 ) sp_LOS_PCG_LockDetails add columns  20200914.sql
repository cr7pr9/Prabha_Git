
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [FulfilledOn] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [FulfilledOn] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [FulfilledOn] 

alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [FulfilledOn] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [FulfilledOn] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [FulfilledOn] 

alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [FulfilledOn] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [FulfilledOn] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [FulfilledOn] 

/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [AVMRunDate] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [AVMRunDate] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [AVMRunDate] 
													
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [AVMRunDate] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [AVMRunDate] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [AVMRunDate] 
													
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [AVMRunDate] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [AVMRunDate] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [AVMRunDate] 
															

/*EXECUTE 1 BY 1 IN ORDER */
alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [AgencyCaseAssignmentDate] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [AgencyCaseAssignmentDate] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [AgencyCaseAssignmentDate] 
							
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [AgencyCaseAssignmentDate] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [AgencyCaseAssignmentDate] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [AgencyCaseAssignmentDate] 
													
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [AgencyCaseAssignmentDate] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [AgencyCaseAssignmentDate] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [AgencyCaseAssignmentDate] 

/*EXECUTE 1 BY 1 IN ORDER */
alter table clg_reporting.dbo.LOS_PCG_LockDetails_All			 drop column [CumulativeExtensionDays] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active		 drop column [CumulativeExtensionDays] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18		 drop column [CumulativeExtensionDays] 
												
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All			 drop column [CumulativeExtensionDays] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active		 drop column [CumulativeExtensionDays] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18		 drop column [CumulativeExtensionDays] 
												
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All			 drop column [CumulativeExtensionDays] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active			 drop column [CumulativeExtensionDays] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18			 drop column [CumulativeExtensionDays] 
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [OriginalCreatorFlag] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [OriginalCreatorFlag] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [OriginalCreatorFlag] 
											
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [OriginalCreatorFlag] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [OriginalCreatorFlag] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [OriginalCreatorFlag] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [OriginalCreatorFlag] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [OriginalCreatorFlag] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [OriginalCreatorFlag] 
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [TexasA6Ind] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [TexasA6Ind] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [TexasA6Ind] 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [TexasA6Ind] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [TexasA6Ind] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [TexasA6Ind] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [TexasA6Ind] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [TexasA6Ind] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [TexasA6Ind] 
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [AppraisalWaiverInd] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [AppraisalWaiverInd] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [AppraisalWaiverInd] 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [AppraisalWaiverInd] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [AppraisalWaiverInd] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [AppraisalWaiverInd] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [AppraisalWaiverInd] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [AppraisalWaiverInd] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [AppraisalWaiverInd] 
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [CustomMiniMI] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [CustomMiniMI] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [CustomMiniMI] 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [CustomMiniMI] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [CustomMiniMI] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [CustomMiniMI] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [CustomMiniMI] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [CustomMiniMI] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [CustomMiniMI] 
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [AVMFSD] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [AVMFSD] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [AVMFSD] 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [AVMFSD] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [AVMFSD] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [AVMFSD] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [AVMFSD] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [AVMFSD] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [AVMFSD] 
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [HELOCActualBalance] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [HELOCActualBalance] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [HELOCActualBalance] 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [HELOCActualBalance] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [HELOCActualBalance] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [HELOCActualBalance] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [HELOCActualBalance] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [HELOCActualBalance] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [HELOCActualBalance] 
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [HELOCCreditLimit] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [HELOCCreditLimit] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [HELOCCreditLimit] 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [HELOCCreditLimit] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [HELOCCreditLimit] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [HELOCCreditLimit] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [HELOCCreditLimit] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [HELOCCreditLimit] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [HELOCCreditLimit] 
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [SingleClose_OTCInd] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [SingleClose_OTCInd] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [SingleClose_OTCInd] 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [SingleClose_OTCInd] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [SingleClose_OTCInd] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [SingleClose_OTCInd] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [SingleClose_OTCInd] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [SingleClose_OTCInd] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [SingleClose_OTCInd] 
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		drop column [VARenovationInd] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	drop column [VARenovationInd] 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	drop column [VARenovationInd] 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		drop column [VARenovationInd] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	drop column [VARenovationInd] 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	drop column [VARenovationInd] 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		drop column [VARenovationInd] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		drop column [VARenovationInd] 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		drop column [VARenovationInd] 
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		 drop column Recommendation
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	 drop column Recommendation
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	 drop column Recommendation
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		 drop column Recommendation
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	 drop column Recommendation
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	 drop column Recommendation
															 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		 drop column Recommendation
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		 drop column Recommendation
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		 drop column Recommendation
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		alter column	 LockPropType varchar(25) 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	alter column	 LockPropType varchar(25) 
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	alter column	 LockPropType varchar(25) 
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		alter column	 LockPropType varchar(25) 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	alter column	 LockPropType varchar(25) 
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	alter column	 LockPropType varchar(25) 
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		alter column	 LockPropType varchar(20) 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		alter column	 LockPropType varchar(20) 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		alter column	 LockPropType varchar(20) 