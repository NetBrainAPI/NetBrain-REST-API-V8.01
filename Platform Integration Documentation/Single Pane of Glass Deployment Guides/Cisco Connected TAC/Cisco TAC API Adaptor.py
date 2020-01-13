import requests
import requests.packages.urllib3 as urllib3
import json
import pythonutil
 
urllib3.disable_warnings()

def getToken(cred_params):
    apiServerId = cred_params['apiServerId']
    servInfo = pythonutil.GetApiServerInfo(apiServerId)
    username = servInfo['username']
    password = servInfo['password']
    host_url = servInfo['endpoint'] + '/api'
    
    header = {"Content-Type": "application/x-www-form-urlencoded", 'Accept':'application/json'}
    full_url = host_url + "/token"
    payload = "username="+username+"&password="+password+"&grant_type=password"
    try:
        response = requests.post(full_url, data=payload, headers=header, verify=False)
        if response.status_code == 200:
            result = response.json()
            #{'access_token': 'Kqpa99145ZHXMjYlcmf6Ht38SAhe', 'token_type': 'Bearer', 'expires_in': 3599}
            token = result["token_type"] + " " + result["access_token"]
            return token
        else:
            print(response.text)
    except Exception as e: print(str(e))
#Bearer IIzXqNxI5typPtHHuEIsnBMmPFGL
 
def getIssuesByDevice(cred_params, token, hostname):
    apiServerId = cred_params['apiServerId']
    servInfo = pythonutil.GetApiServerInfo(apiServerId)
    host_url = servInfo['endpoint'] + '/api'
    
    header = {'Authorization': token, 'Accept':'application/json'}
    full_url = host_url + "/Devices/" + hostname + "/Issues"
    querystring = {"isHostname":"true",
    "includeOccurences":"false",
    "includeLastAlert":"true",
    "includeRemediations":"false",
    "includeAppliedRemediations":"false",
    "includeExternalTextInSearch":"true",
    "page":"1",
    "pageSize":"100"
    }  
    try:
        response = requests.get(full_url, headers=header, params=querystring, verify=False)
        if response.status_code == 200:
            result = response.json()
            # return result
            return response.text
        else:
            print(response.text)
    except Exception as e: print(str(e))
    
def _test(param):
    #fp = open(r'C:\Program Files\NetBrain\Front Server\log\frontsvr\log.ext', 'w+')
    #fp.write(param)
    #p.close()
    param_temp = json.loads(param)
    #apiServerId = param_temp['apiServerId']
    #servInfo = pythonutil.GetApiServerInfo(apiServerId)
    username = param_temp['username']
    password = param_temp['password']
    host_url = param_temp['endpoint'] + '/api'
    
    header = {"Content-Type": "application/x-www-form-urlencoded", 'Accept':'application/json'}
    full_url = host_url + "/token"
    payload = "username="+username+"&password="+password+"&grant_type=password"
    try:
        response = requests.post(full_url, data=payload, headers=header, verify=False)
        if response.status_code == 200:
            result = response.json()
            #{'access_token': 'Kqpa99145ZHXMjYlcmf6Ht38SAhe', 'token_type': 'Bearer', 'expires_in': 3599}
            #token = result["token_type"] + " " + result["access_token"]
            #token = result['access_token']
            #rtn = {"isFailed":False, "msg":"Connection Works!"+ "Token ID: "+ token}
            rtn = {"isFailed":False, "msg":"Connection Works!"}
            return json.dumps(rtn)
        elif response.status_code == 400:
            json_response = response.json()
            rtn = {'isFailed':True, 'msg':json_response['error_description']}
            return json.dumps(rtn)
    except Exception as e:
        rtn = {'isFailed':True, 'msg':'Invalid endpoint'}
        return rtn