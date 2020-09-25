Remove-Item c:\kanan142\LoadXML\*.*
# C:\"Program Files"\Amazon\AWSCLI\bin\aws # s3 cp s3://pnmaciicswindowsagentdev/DesktopUnderwritter/ C:\Users\informatica\lmp_support\DesktopUnderwritter --exclude "*" --include "*.json" --recursive
aws s3 cp s3://pnmaciicswindowsagentdev/DesktopUnderwritter/ C:\Users\informatica\lmp_support\DesktopUnderwritter --exclude "*" --include "*.json" --recursive
if (!(Test-Path "C:\Users\informatica\lmp_support\DesktopUnderwritter\samplepath.txt"))
{
   New-Item -path C:\Users\informatica\lmp_support\DesktopUnderwritter -name samplepath.txt -type "file" -value '"PATH"'
   Add-Content -path C:\Users\informatica\lmp_support\DesktopUnderwritter\samplepath.txt -value ''
}
$files = Get-ChildItem "C:\Users\informatica\lmp_support\DesktopUnderwritter" -Filter *.json
foreach ($f in $files){

    $filename = '"' + $f.FullName + '"'
    Add-Content -path C:\Users\informatica\lmp_support\DesktopUnderwritter\samplepath.txt -value $filename
}