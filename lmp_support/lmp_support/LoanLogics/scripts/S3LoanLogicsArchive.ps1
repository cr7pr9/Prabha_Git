#C:\"Program Files"\Amazon\AWSCLI\aws s3 mv s3://pnmaciicsdwwindowsagentdev/LoanLogics/LoadXML/ s3://pnmaciicsdwwindowsagentdev/LoanLogics/Archive --exclude "*" --include "*.xml" --recursive
#C:\"Program Files"\Amazon\AWSCLI\aws s3 mv s3://pnmaciicsdwwindowsagentdev/LoanLogics/MetadataXML/ s3://pnmaciicsdwwindowsagentdev/LoanLogics/Archive --exclude "*" --include "*.xml" --recursive
Remove-Item C:\Users\informatica\lmp_support\LoanLogics\*.*
Remove-Item C:\Users\informatica\Kanan\LoanLogics\*.*