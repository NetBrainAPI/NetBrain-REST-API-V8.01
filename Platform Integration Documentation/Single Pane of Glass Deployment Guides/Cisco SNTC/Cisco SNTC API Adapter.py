import requests
import requests.packages.urllib3 as urllib3
import json
import pythonutil
 
urllib3.disable_warnings()

import time
import threading

# provide a Locks class to avoid multithread API calling conflict.
class Locks:
    __instance = None
    __lock = threading.Lock()
    @staticmethod
    def getInstance():
        """ Static access method. """
        instance = Locks.__instance
        if instance == None:
            Locks.__lock.acquire()
            instance = Locks.__instance
            if instance == None:
                Locks.__instance = instance = Locks()
        return instance
    def __init__(self):
        """ Virtually private constructor. """
        if Locks.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Locks.__instance = self
            self.endpoint2locks = {}
            self.lock = threading.Lock()
    def update_lock(self, endpoint):
        self.lock.acquire()
        if not endpoint in self.endpoint2locks:
            self.endpoint2locks[endpoint] = threading.Lock()
        self.lock.release()
    def request_access(self, endpoint):
        lock = self.endpoint2locks[endpoint]
        lock.acquire()
        time.sleep(0.3)
        lock.release()
 
# First API call to get token from SNTC server.
def GetTokenClient(params, full_url, header, payload_id, payload_secret):
    apiServerId = params['apiServerId']
    servInfo = pythonutil.GetApiServerInfo(apiServerId)
    client_id = servInfo['username']
    client_secret = servInfo['password']
    payload=payload_id+client_id+payload_secret+client_secret
    #predefine the status code for lock function.
    status_code = 403
    #define the initial value for re-call counter.
    counter = 1
    #initial the lock function
    locks = Locks.getInstance()
    #apply which url should be locked in current call.
    locks.update_lock(full_url)
    response = {}
    try:
        #provide a while loop when we face conflict and with three times re-call.
        while status_code == 403 and counter < 4:
            # apply the lock to token API call.
            locks.request_access(full_url)
            response = requests.post(full_url, data=payload, headers=header, verify=False)
            status_code = response.status_code
            counter += 1
        if status_code == 200:
            result = response.json()
            token = result["token_type"] + " " + result["access_token"]
            return token
        else:
            print("Get Token Failed with API Response: " + response.text + " -- And API Header: " + response.headers)
    except Exception as e: print(str(e))
 
def GetWarrantyByID(token, sn, params):
    header = {'Authorization': token, 'Accept':'application/json'}
    apiServerId = params['apiServerId']
    servInfo = pythonutil.GetApiServerInfo(apiServerId)
    base_url = servInfo['endpoint']
    full_url = base_url + sn
    status_code = 403
    counter = 1
    locks = Locks.getInstance()
    locks.update_lock(base_url)
    response = {}
 
    try:
        while status_code == 403 and counter < 4:
            locks.request_access(base_url)
            response = requests.get(full_url, headers=header, verify=False)
            status_code = response.status_code
            counter += 1
        if status_code == 200:
            result = response.json()
            return result["EOXRecord"]
        else:
            print("Get Token Failed with API Response: " + response.text + " -- And API Header: " + response.headers)
    except Exception as e: print(str(e))

def _test(param):
    get_param = json.loads(param)
    client_id = get_param['username']
    client_secret = get_param['password']
    endpoint  = get_param['endpoint']
    full_url = "https://cloudsso.cisco.com/as/token.oauth2"
    
    header = {"Content-Type": "application/x-www-form-urlencoded", 'Accept':'application/json'}
    payload_id = "grant_type=client_credentials&client_id="
    payload_secret = "&client_secret="
    payload=payload_id+client_id+payload_secret+client_secret
    if endpoint == "https://api.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/1/":
        try:
            response = requests.post(full_url, data=payload, headers=header, verify=False)
            if response.status_code == 200:
                result = response.json()
                token = result['access_token']
                rtn = {"isFailed":False, "msg":"Connection Works! "+ "Token ID: "+ token}
                return json.dumps(rtn)
            elif response.status_code == 401:
                json_response = response.json()
                rtn = {'isFailed':True, 'msg':json_response['error_description']}
                return json.dumps(rtn)
        except Exception as e: print(str(e))
    else:
        rtn = {"isFailed":True, "msg":"Please verify your endpoint"}
        return json.dumps(rtn)