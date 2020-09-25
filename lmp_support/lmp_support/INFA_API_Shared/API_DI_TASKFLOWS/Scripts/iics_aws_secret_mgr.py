# -------------------------------------------------------------------------------------------------------------
# Developer         : RaghuRama Krishna
# CreatedDate       : 06/02/2020
# Description       : Script used to retrieve the credencials using Secrets Manager
# ModifiedDate      : 
# Modified By       :
# Version comments  :
# -------------------------------------------------------------------------------------------------------------

import os
import logging
import boto3
import json


try:

    ### Method to retrieve credentials from Secrets Manager
    def get_credentials(secret_name):
        session = boto3.session.Session()
        client = session.client(
            service_name='secretsmanager',
            region_name="us-west-2",
        )
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        res=json.loads(get_secret_value_response["SecretString"])
        return res
except Exception as error:
    print('This is outer block %s', str(error))
    raise

