

CREATE TABLE clg_reporting.los_pcg.DI_Taskflow_Parameters (
	API_Name varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL,
	ServiceURL varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	FolderName varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	LogFilePath varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	LogFileName varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Subject varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	Body varchar(1000) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	TaskflowName varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	dev_failure_email varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	qa_failure_email varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	stg_failure_email varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	prod_failure_email varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	sender_email varchar(100) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
	CONSTRAINT PK__DI_Taskf__9217662BDAA00F65 PRIMARY KEY (API_Name)
) ;



CREATE TABLE clg_reporting.los_pcg.DI_Taskflows (
TaskflowName varchar(256) ,
FolderName varchar(256) ,
RunId bigint NULL,
StartTime datetime NULL,
EndTime datetime NULL,
Status varchar(20),
LoadDate datetime NULL
)

INSERT INTO clg_reporting.los_pcg.DI_Taskflow_Parameters Values('LoanLogics','https://na1.dm-us.informaticacloud.com/active-bpel/rt/tf_LoanLogics_MailRoom',
'DEP_PCG\DEP_PCG_ED_CORR_PROD_LOAN_LOGICS_MAILROOM',
'C:\Users\informatica\Kanan\API_LoanLogics\Logs\',
'log_LoanLogics_',
'LoanLogics DI Job In Progress..',
'Hi All,\n The LoanLogics taskflow instance is running: You cannot have multiple instances of taskflow running simultaneiously. \n Please find the attached logfiles for details.',
'tf_LoanLogics',
'enterprise_data_iics_support@pnmac.com',
'enterprise_data_iics_support@pnmac.com','enterprise_data_iics_support@pnmac.com','enterprisedba@pnmac.com','admin@pnmac.com')



INSERT INTO clg_reporting.los_pcg.DI_Taskflow_Parameters Values('TradeManagement','https://na1.dm-us.informaticacloud.com/active-bpel/rt/tf_trade_Pairoff_Mailroom',
'DEP_PCG\DEP_PCG_ED_CORR_PROD_TRADE_MANAGEMENT',
'C:\Users\informatica\Kanan\API_Trade_Management\Logs\',
'log_trade_',
'TradeManagement DI Job In Progress..',
'Hi All,\n The TradeManagement taskflow instance is running: You cannot have multiple instances of taskflow running simultaneiously. \n Please find the attached logfiles for details.',
'tf_trade_Pairoff_Mailroom',
'enterprise_data_iics_support@pnmac.com',
'enterprise_data_iics_support@pnmac.com',
'enterprise_data_iics_support@pnmac.com',
'enterprise_data_iics_support@pnmac.com,enterprisedba@pnmac.com',
'admin@pnmac.com')