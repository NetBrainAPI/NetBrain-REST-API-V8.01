import json
import requests
import urllib3
import pythonutil
urllib3.disable_warnings()

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
    headers = {"Content-Type": "application/json", "Accept": "*/*"}
    endpoint, username, password, api_params = extract_param(param)
    url_params = api_params['url_params']
    time = url_params["time"]
    typelog = url_params["type"]
    device = url_params["device"]
    full_url = str(endpoint + api_params['api_uri']+"?"+"password="+password+";time="+time+";type="+typelog+";device="+device+";")
    print(full_url)
    try:            
        response = requests.request("GET", full_url, headers=headers)        
        if response.status_code == 200:
            json_response = response.text
            print("200:"+json_response)
            return json_response
        else:
            print("not 200:"+response.text)
            return response.text
        
    except Exception as e:
        print("exception: "+str(e))
        return str(e)
        

# API Domain Manager Test function definition.
def _test(param):
    test_param = json.loads(param)    
    headers = {"Content-Type": "application/json", "Accept": "*/*"}
    password = test_param['password']
    full_url = test_param['endpoint']+"/api-msg?password="+password+";time=last30m;type=syslog;device=/^SAMPLE/;"
   
    try:
        response = requests.request("GET", full_url, headers=headers)
        #raise Exception("Checkpoint1!!!!!!!")
        if "api-msg invalid username/password" in response.text:
            rtn = {'isFailed':True, 'msg':'Invalid credentials. Please retry'}
        else:
            rtn = {'isFailed':False, 'msg':'Endpoint and credentials are verified'}
        return json.dumps(rtn)
    except Exception as e:
        rtn = {'isFailed':True, 'msg':'Endpoint is not reachable'+str(e)}
        return rtn

