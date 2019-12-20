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

def get_token(param):
    endpoint, username, password, api_params = extract_param(param)
    full_url = endpoint + ":8008/api/jwt/login"
    headers = {'content-type':'application/x-www-form-urlencoded'}
    data = "username="+username+"&password="+password
    token = ''
    try:            
        response = requests.post(full_url, data=data, headers=headers, verify=False)
    except Exception as e:
        return str(e)
    return response

def get_data(param):
    endpoint, username, password, api_params = extract_param(param)
    response = get_token(param)
    token = response.text
    full_url = endpoint + api_params['api_uri']
    headers = {'content-type':'application/json','authorization':'AR-JWT '+token}
    try:            
        response = requests.get(url=full_url, headers=headers, verify=False)
        if response.status_code == 200:
            json_response = response.json()
            return json_response
        else:
            return response.text
    except Exception as e:
        return str(e)

# API Domain Manager Test function definition.
def _test(param):
    if isinstance(param, str):
        param = json.loads(param)
    param['api_params'] = ''

    try:
        response = get_token(param)
        if response.status_code == 200:
            rtn = {"isFailed":False, "msg":"Login Successful."}
        elif response.status_code == 401:
            rtn = {"isFailed":True, "msg":"Authentication failed."}
        return json.dumps(rtn)
    except Exception as e:
        rtn = {'isFailed':True, 'msg':'Endpoint is not reachable.'+ str(e)}
        return rtn


#param = {'endpoint': 'http://192.168.31.94', 'password': 'Netbrain123', 'username': 'appadmin', 'api_params':{'api_uri':':8008/api/arsys/v1/entry/HPD:IncidentInterface'}}
#print(get_data(param))
#print(_test(param))    