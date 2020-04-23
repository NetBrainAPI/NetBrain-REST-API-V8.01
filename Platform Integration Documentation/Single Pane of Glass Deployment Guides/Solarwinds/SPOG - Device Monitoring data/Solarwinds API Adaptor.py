import requests
import json
import urllib3
import re
import pythonutil
urllib3.disable_warnings()

#verify import of solarwinds sdk 
importException = None
try:
    from orionsdk import SwisClient
except ModuleNotFoundError as e:
    importException ="Failed to import Solarwinds SDK: "+str(e)


class APIPlugin:
    _headers = {"Content-Type": "application/json",
                "Accept": "application/json"}
   
    def __init__(self, user, pwd, url):
        self._user = user
        self._pwd = pwd
        self.auth = (self._user, self._pwd)
 
        if re.search('http://(.+)', url):
            stripped = re.search('http://(.+)', url)
            url = stripped.group(1)
        if re.search('https://(.+)', url):
            stripped = re.search('https://(.+)', url)
            url = stripped.group(1)
        self._swis = SwisClient(url, user, pwd)
  
    def _query(self, query, deviceName):
        try:
            response = self._swis.query(query,id=deviceName)
            return response
        except Exception as e:
            return str(e)


def extract_param(param):
    if isinstance(param, str):
        param = json.loads(param)
  
    username = ''
    password = ''
    endpoint = ''
    callParam = {}
  
    apiServerId = ''
    servInfo = {}
    if 'apiServerId' in param:
        apiServerId = param['apiServerId']
        servInfo = pythonutil.GetApiServerInfo(apiServerId)
        username = servInfo['username']
        password = servInfo['password']
        endpoint = servInfo['endpoint']
    else:
        if 'username' in param:
            username = param['username']
        if 'password' in param:
            password = param['password']
        if 'endpoint' in param:
            endpoint = param['endpoint']

    if 'query' in param:
        query = param['query']
    if 'deviceName' in param:
        deviceName = param['deviceName']   
  
    return (username, password, endpoint, query, deviceName)
 
# API Domain Manager Test function definition.
def _test(param):
    if isinstance(param, str):
        param = json.loads(param)
    if importException is not None:
        return {'isFailed':True, 'msg':importException}

    username = param['username']
    password = param['password']
    endpoint = param['endpoint']

    api = APIPlugin(username, password, endpoint)
    deviceName='Network Performance Monitor'
    query='SELECT SettingName, SettingValue FROM Orion.WebSettings WHERE SettingValue LIKE @id'
    rtn = {}

    try:
        result = api._query(query, deviceName)
        if "403" in result:
            rtn = {'isFailed':True, 'msg':"Credentials entered are incorrect: "+result}
        elif "Network Performance Monitor" in result['results'][0]['SettingValue']:
            rtn = {'isFailed':False, 'msg':'Endpoint and credentials are verified!'}
        return json.dumps(rtn)
    except Exception as e:
        rtn = {'isFailed':True, 'msg':'Endpoint is not reachable.'}
        return rtn

# Public function for API parser.
def getData(param):
    username, password, endpoint, query , deviceName= extract_param(param)
    ap = APIPlugin(username, password, endpoint)
    rtn = ap._query(query, deviceName)
    return json.dumps(rtn)
 
 
#param = {'deviceName': 'NBUSMA-SW1', 'endpoint': 'http://192.168.31.99', 'password': 'Netbrain1', 'query': 'SELECT NodeID,IPAddress,CPULoad,PercentMemoryUsed,Uri FROM Orion.Nodes WHERE Caption LIKE @id', 'username': 'admin'}
#print(getData(param))
#print(_test(param))