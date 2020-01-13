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
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    endpoint, username, password, api_params = extract_param(param)
    full_url = endpoint + api_params['api_uri']
    api_params['username'] = username
    api_params['password'] = password
    url_params = {}
    if 'url_params' in param['api_params']:
        url_params = api_params['url_params']
    try:            
        response = requests.get(full_url, auth=(username,password), headers=headers, params=url_params, verify=False)
        if response.status_code == 200:
            json_response = response.json()
            return json_response['result']
        else:
            return response.text
    except Exception as e:
        return str(e)

# Public function for API parser.
def post_data(param):
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    endpoint, username, password, api_params = extract_param(param)
    full_url = endpoint + api_params['api_uri']
    api_params['username'] = username
    api_params['password'] = password
    body_data = {}
    if 'body_data' in param['api_params']:
        body_data = json.dumps(api_params['body_data'])
    try:            
        response = requests.post(full_url, auth=(username,password), headers=headers, data=body_data, verify=False)
        if response.status_code == 200:
            json_response = response.json()
            return json_response['result']
        else:
            return response.text
    except Exception as e:
        return str(e)
        
def put_data(param):
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    endpoint, username, password, api_params = extract_param(param)
    full_url = endpoint + api_params['api_uri']
    api_params['username'] = username
    api_params['password'] = password
    body_data = {}
    if 'body_data' in param['api_params']:
        body_data = json.dumps(api_params['body_data'])
    try:            
        response = requests.put(full_url, auth=(username,password), headers=headers, data=body_data, verify=False)
        if response.status_code == 200:
            json_response = response.json()
            return json_response['result']
        else:
            return response.text
    except Exception as e:
        return str(e)

# API Domain Manager Test function definition.
def _test(param):
    param = json.loads(param)
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    username = param['username']
    password = param['password']
    full_url = param['endpoint'] + '/api/now/table/incident'
    url_params = {'sysparm_limit':1, 'sysparm_fields':'number'}
    try:
        response = requests.get(full_url, auth=(username,password), headers=headers, params=url_params, verify=False)
        if response.status_code == 200:
            rtn = {'isFailed':False, 'msg':'Endpoint and credentials are verified!'}
        elif response.status_code == 401:
            json_response = response.json()
            rtn = {'isFailed':True, 'msg':json_response['error']['message']}
        return json.dumps(rtn)
    except Exception as e:
        rtn = {'isFailed':True, 'msg':'Endpoint is not reachable!'}
        return rtn