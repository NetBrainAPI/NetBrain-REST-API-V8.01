
## ***GET*** /V1/CMDB/UserDeviceAccessPolicy?{authenticationServer}&{userName}
Call this API to get all device access policy associated with one specified user account with account name.

## Detail Information

> **Title** : Get User Device Access Policy API<br>

> **Version** : 08/12/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No Request Body.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| authenticationServer | string  | The authentication server name.|
| userName* | string | The uer name of user account. |
>***Note:***<br> 1. The authentication server is optional.<br>2. The program will looks for users on all servers(including local  and external servers) when the authentication server name is null or empty.<br>3. The program will looks for users on local server when the authentication server name is "NetBrain", otherwise will looks for users on the specified server.

## Headers

> **Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| token | string  | Authentication token, get from login API. |

## Response
|**Name**|**Type**|**Description**|
|------|------|------|
| policies* | list of string | The list of policy name. |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

***Example:***


```python
{
    "policies": ["policyName1", "policyName2"],
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

## Full Example:


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "6bf756e4-18dd-49ec-b63e-cad4a1129c95"
nb_url = "https://10.10.7.209"
authenticationServer = "NetBrain"
userName = "gongdai.liu"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

def getUserDeviceAccessPolicy (headers, authenticationServer, userName):
    data = {
        "authenticationServer" : authenticationServer,
        "userName" : userName
    }
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy"
    try:
        response = requests.get(full_url, headers=headers, params = data, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Get users policies Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
        
result = getUserDeviceAccessPolicy(headers, authenticationServer, userName)
result
```




    {'policies': ['DeviceAccessPolicy_GL1', 'DeviceAccessPolicy_GL2'],
     'statusCode': 790200,
     'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X GET \
  'https://10.10.7.209/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy?authenticationServer=NetBrain&userName=gongdai.liu' \
  -H 'Postman-Token: 043a8e74-ddd9-4216-8f1a-85576fbfcc70' \
  -H 'cache-control: no-cache' \
  -H 'token: 6bf756e4-18dd-49ec-b63e-cad4a1129c95'
```
