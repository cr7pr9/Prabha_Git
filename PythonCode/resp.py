import json
x={"Response":{"code":"1","message":"\r\nC:-Users-informatica-lmp_support-INFA_API_Shared-API_LoanLogics-Scripts>python C:-Users-informatica-lmp_support-INFA_API_Shared-API_LoanLogics-Scripts-downloadLoanLogicsxml.py 3396757d-5f04-424b-8fea-a734bd62b1eb kanan-tpi-object-store archive/3396757d-5f04-424b-8fea-a734bd62b1eb/loantools/8000083225_20190107130939948_Loandata.xml archive/3396757d-5f04-424b-8fea-a734bd62b1eb/loantools/8000083225_20190107130939948_LoanDocMetaData.xml \r\nTraceback (most recent call last):\r\n  File 'C:-Users-informatica-lmp_support-INFA_API_Shared-API_LoanLogics-Scripts-downloadLoanLogicsxml.py', line 67, in \r\n    DownloadXmlFiles(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])\r\n  File 'C:-Users-informatica-lmp_support-INFA_API_Shared-API_LoanLogics-Scripts-downloadLoanLogicsxml.py', line 37, in DownloadXmlFiles\r\n    s3.Bucket(bucket).download_file(xml_key,dest_file_path+loan_file[3])\r\n  File 'C:-Python38-lib-site-packages-boto3-s3-inject.py', line 244, in bucket_download_file\r\n    return self.meta.client.download_file(\r\n  File 'C:-Python38-lib-site-packages-boto3-s3-inject.py', line 170, in download_file\r\n    return transfer.download_file(\r\n  File 'C:-Python38-lib-site-packages-boto3-s3-transfer.py', line 307, in download_file\r\n    future.result()\r\n  File 'C:-Python38-lib-site-packages-s3transfer-futures.py', line 106, in result\r\n    return self._coordinator.result()\r\n  File 'C:-Python38-lib-site-packages-s3transfer-futures.py', line 265, in result\r\n    raise self._exception\r\n  File 'C:-Python38-lib-site-packages-s3transfer-tasks.py', line 255, in _main\r\n    self._submit(transfer_future=transfer_future, **kwargs)\r\n  File 'C:-Python38-lib-site-packages-s3transfer-download.py', line 340, in _submit\r\n    response = client.head_object(\r\n  File 'C:-Python38-lib-site-packages-botocore-client.py', line 316, in _api_call\r\n    return self._make_api_call(operation_name, kwargs)\r\n  File 'C:-Python38-lib-site-packages-botocore-client.py', line 626, in _make_api_call\r\n    raise error_class(parsed_response, operation_name)\r\nbotocore.exceptions.ClientError: An error occurred (404) when calling the HeadObject operation: Not Found\r\n","isSuccess":"False"}}
a=x['error']['detail']['code']

b=x['error']['detail']['code']

c=b.replace('{"Response":','')

d=c[:-1]
e=json.loads(d)
#print(e)
#print(e['code'],e['message'],e['iSuccess'])
print(e['isSuccess'])
print(e['code'])
print(e['message'])
