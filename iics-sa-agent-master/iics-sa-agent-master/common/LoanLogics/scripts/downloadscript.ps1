Remove-Item C:\Users\informatica\lmp_support\LoanLogics\*.*
C:\"Program Files"\Amazon\AWSCLI\bin\aws s3 cp s3://pnmaciicswindowsagentdev/LoanLogics/LoadXML/ C:\Users\informatica\lmp_support\LoanLogics\ --exclude "*" --include "*.xml" --recursive
C:\"Program Files"\Amazon\AWSCLI\bin\aws s3 cp s3://pnmaciicswindowsagentdev/LoanLogics/MetadataXML/ C:\Users\informatica\lmp_support\LoanLogics\ --exclude "*" --include "*.xml" --recursive
if (!(Test-Path "C:\Users\informatica\lmp_support\LoanLogics\samplepath.txt"))
{
   New-Item -path C:\Users\informatica\lmp_support\LoanLogics -name samplexml.txt -type "file" -value ''
}
$files = Get-ChildItem "C:\Users\informatica\lmp_support\LoanLogics" -Filter *.xml
foreach ($f in $files){
	Add-Content $f.FullName "|"
	$content = (Get-Content -path $f.FullName -Raw)  -replace '\n','' -replace '\r',''
    if ([int]($f.FullName.length -lt 80)){
        $content = $content.remove(0,37).insert(0,'<?xml version="1.0"?>')
        $content = $content.insert(21,"`n")
    }
    else {
        $content = $content.remove(0,37).insert(0,'<?xml version="1.0"?>')
        $content = $content.insert(21,"`n")
    }
	
	$content | Set-Content -Path $f.FullName
    Add-Content -path C:\Users\informatica\lmp_support\LoanLogics\samplexml.txt -value $f.FullName
}