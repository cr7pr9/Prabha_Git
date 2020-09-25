
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [FulfilledOn] [datetime] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [FulfilledOn] [datetime] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [FulfilledOn] [datetime] NULL

alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [FulfilledOn] [datetime] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [FulfilledOn] [datetime] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [FulfilledOn] [datetime] NULL

alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [FulfilledOn] [datetime] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [FulfilledOn] [datetime] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [FulfilledOn] [datetime] NULL

/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [AVMRunDate] [datetime] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [AVMRunDate] [datetime] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [AVMRunDate] [datetime] NULL
													
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [AVMRunDate] [datetime] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [AVMRunDate] [datetime] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [AVMRunDate] [datetime] NULL
													
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [AVMRunDate] [datetime] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [AVMRunDate] [datetime] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [AVMRunDate] [datetime] NULL
															

/*EXECUTE 1 BY 1 IN ORDER */
alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [AgencyCaseAssignmentDate] [datetime] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [AgencyCaseAssignmentDate] [datetime] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [AgencyCaseAssignmentDate] [datetime] NULL
							
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [AgencyCaseAssignmentDate] [datetime] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [AgencyCaseAssignmentDate] [datetime] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [AgencyCaseAssignmentDate] [datetime] NULL
													
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [AgencyCaseAssignmentDate] [datetime] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [AgencyCaseAssignmentDate] [datetime] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [AgencyCaseAssignmentDate] [datetime] NULL

/*EXECUTE 1 BY 1 IN ORDER */
alter table clg_reporting.dbo.LOS_PCG_LockDetails_All			 add [CumulativeExtensionDays] [int] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active		 add [CumulativeExtensionDays] [int] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18		 add [CumulativeExtensionDays] [int] NULL
												
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All			 add [CumulativeExtensionDays] [int] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active		 add [CumulativeExtensionDays] [int] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18		 add [CumulativeExtensionDays] [int] NULL
												
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All			 add [CumulativeExtensionDays] [int] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active			 add [CumulativeExtensionDays] [int] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18			 add [CumulativeExtensionDays] [int] NULL
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [OriginalCreatorFlag] [varchar](4) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [OriginalCreatorFlag] [varchar](4) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [OriginalCreatorFlag] [varchar](4) NULL
											
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [OriginalCreatorFlag] [varchar](4) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [OriginalCreatorFlag] [varchar](4) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [OriginalCreatorFlag] [varchar](4) NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [OriginalCreatorFlag] [varchar](4) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [OriginalCreatorFlag] [varchar](4) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [OriginalCreatorFlag] [varchar](4) NULL
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [TexasA6Ind] [char](1) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [TexasA6Ind] [char](1) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [TexasA6Ind] [char](1) NULL
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [TexasA6Ind] [char](1) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [TexasA6Ind] [char](1) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [TexasA6Ind] [char](1) NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [TexasA6Ind] [char](1) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [TexasA6Ind] [char](1) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [TexasA6Ind] [char](1) NULL
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [AppraisalWaiverInd] [char](1) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [AppraisalWaiverInd] [char](1) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [AppraisalWaiverInd] [char](1) NULL
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [AppraisalWaiverInd] [char](1) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [AppraisalWaiverInd] [char](1) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [AppraisalWaiverInd] [char](1) NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [AppraisalWaiverInd] [char](1) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [AppraisalWaiverInd] [char](1) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [AppraisalWaiverInd] [char](1) NULL
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [CustomMiniMI] [varchar](4) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [CustomMiniMI] [varchar](4) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [CustomMiniMI] [varchar](4) NULL
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [CustomMiniMI] [varchar](4) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [CustomMiniMI] [varchar](4) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [CustomMiniMI] [varchar](4) NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [CustomMiniMI] [varchar](4) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [CustomMiniMI] [varchar](4) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [CustomMiniMI] [varchar](4) NULL
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [AVMFSD] [float] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [AVMFSD] [float] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [AVMFSD] [float] NULL
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [AVMFSD] [float] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [AVMFSD] [float] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [AVMFSD] [float] NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [AVMFSD] [float] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [AVMFSD] [float] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [AVMFSD] [float] NULL
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [HELOCActualBalance] [float] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [HELOCActualBalance] [float] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [HELOCActualBalance] [float] NULL
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [HELOCActualBalance] [float] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [HELOCActualBalance] [float] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [HELOCActualBalance] [float] NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [HELOCActualBalance] [float] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [HELOCActualBalance] [float] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [HELOCActualBalance] [float] NULL
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [HELOCCreditLimit] [float] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [HELOCCreditLimit] [float] NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [HELOCCreditLimit] [float] NULL
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [HELOCCreditLimit] [float] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [HELOCCreditLimit] [float] NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [HELOCCreditLimit] [float] NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [HELOCCreditLimit] [float] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [HELOCCreditLimit] [float] NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [HELOCCreditLimit] [float] NULL
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [SingleClose_OTCInd] [varchar](4) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [SingleClose_OTCInd] [varchar](4) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [SingleClose_OTCInd] [varchar](4) NULL
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [SingleClose_OTCInd] [varchar](4) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [SingleClose_OTCInd] [varchar](4) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [SingleClose_OTCInd] [varchar](4) NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [SingleClose_OTCInd] [varchar](4) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [SingleClose_OTCInd] [varchar](4) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [SingleClose_OTCInd] [varchar](4) NULL
/*EXECUTE 1 BY 1 IN ORDER */


alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		add [VARenovationInd] [varchar](4) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	add [VARenovationInd] [varchar](4) NULL
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	add [VARenovationInd] [varchar](4) NULL
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		add [VARenovationInd] [varchar](4) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	add [VARenovationInd] [varchar](4) NULL
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	add [VARenovationInd] [varchar](4) NULL
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		add [VARenovationInd] [varchar](4) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		add [VARenovationInd] [varchar](4) NULL
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		add [VARenovationInd] [varchar](4) NULL
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		 Add Recommendation char(30)
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	 Add Recommendation char(30)
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	 Add Recommendation char(30)
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		 Add Recommendation char(30)
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	 Add Recommendation char(30)
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	 Add Recommendation char(30)
															 
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		 Add Recommendation char(30)
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		 Add Recommendation char(30)
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		 Add Recommendation char(30)
/*EXECUTE 1 BY 1 IN ORDER */

alter table clg_reporting.dbo.LOS_PCG_LockDetails_All		alter column	 LockPropType varchar(25)
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Active	alter column	 LockPropType varchar(25)
alter table clg_reporting.dbo.LOS_PCG_LockDetails_Last18	alter column	 LockPropType varchar(25)
															
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_All		alter column	 LockPropType varchar(25)
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Active	alter column	 LockPropType varchar(25)
alter table PCG_BusSpprt_DC.OTH.LOS_PCG_LockDetails_Last18	alter column	 LockPropType varchar(25)
															
alter table clg_strategy.dbo.LOS_PCG_LockDetails_All		alter column	 LockPropType varchar(25)
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Active		alter column	 LockPropType varchar(25)
alter table clg_strategy.dbo.LOS_PCG_LockDetails_Last18		alter column	 LockPropType varchar(25)