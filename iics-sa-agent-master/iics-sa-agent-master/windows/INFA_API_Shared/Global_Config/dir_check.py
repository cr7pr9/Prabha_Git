import os
import yaml
with open(r"C:\Users\informatica\lmp_support\INFA_API_Shared\Global_Config\config.yaml") as stream:
    yaml_str = yaml.safe_load(stream)
    for api_name in yaml_str:
        if 'DB_ObjectNames' in api_name:
            pass
        else:
            for path in yaml_str[api_name]:
                try:
                    MYDIR = yaml_str[api_name][path]
                    CHECK_FOLDER = os.path.isdir(MYDIR)
                    if not CHECK_FOLDER:
                        os.makedirs(MYDIR)
                    else:
                        pass
                except Exception as error:
                    pass
