import requests
import json
import pythonutil
  
def extract_param(param):
    # The NetBrain initial parameters with customized fields.
    if isinstance(param, str):
        param = json.loads(param)  
    #username, password, endpoint are build-in keywords in initial param.
    username = ''
    password = ''
    endpoint = ''
    #callParam is customized fields.
    api_param = {}
    apiServerId = ''
    servInfo = {}
    if 'apiServerId' in param:
        apiServerId = param['apiServerId']
        servInfo = pythonutil.GetApiServerInfo(apiServerId)
        username = servInfo['username']
        password = servInfo['password']
        endpoint = servInfo['endpoint']
        api_params = param['api_params']
    else:
        username = param["username"]
        password = param["password"]
        endpoint = param["endpoint"]
        api_params = param['api_params']
    return (endpoint, username, password, api_params)

def get_data(param):
    # headers = {"Content-Type": "application/json", "Accept": "application/json"}
    headers = {}
    endpoint, username, password, api_params = extract_param(param)
    full_url = endpoint + api_params['api_uri']
    url_params = {}
    if 'url_params' in param['api_params']:
        url_params = api_params['url_params']
    url_params['username'] = username
    url_params['password'] = password
    try:            
        response = requests.get(full_url, headers=headers, params=url_params, verify=False)
        if response.status_code == 200:
            json_response = response.json()
            return json_response
        else:
            return response.text
    except Exception as e:
        return str(e)

# API Domain Manager Test function definition.
def _test(param):
    test_param = json.loads(param)
    test_param["api_params"] = {'api_uri':'/api/table.json?content=groups&output=json'}
    result = json.dumps(get_data(test_param))
        #"isFailed" and "msg" key fileds are the required.
    if "prtg-version" in result:
        rtn = {"isFailed":False, "msg":"Endpoint and crendentials are verified"}
        return json.dumps(rtn)
    elif "Unauthorized" in result:
        rtn = {"isFailed":True, "msg":"Invalid username/password"}
        return json.dumps(rtn)
    else:
        rtn = {'isFailed':True, 'msg':'Endpoint is not reachable.'}
        return rtn
