
# Get Users of One Device Access Policy

## ***GET*** /V1/CMDB/UserDeviceAccessPolicy/UsersOfDeviceAccessPolicy?{name}
Call this API to get users which have the same device access policy in current domain.

## Detail Information

> **Title** : Get Users of One Device Access Policy API<br>

> **Version** : 08/12/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy/UsersOfDeviceAccessPolicy

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
| name* | string  | The name of the policy.|

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
|users|	list of object	|list of user brief information|
|users.authenticationServer|string|authentication server which using for login.|
|users.username|string|user name of user account.|
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

***Example:***


```python
{
    "users": [
        {
            "authenticationServer": "NetBrain",
            "username": "admin"
        }
    ],
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
token = "9dbd05fa-2630-4c2f-bfd2-86973e886bf2"
nb_url = "https://10.10.7.209"
taskName = "DeviceAccessPolicy_GL2"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

def getUsersofDeviceAccessPolicy(headers, taskName):
    data = {
        "name" : taskName
    }
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy/UsersOfDeviceAccessPolicy"
    try:
        response = requests.get(full_url, headers=headers, params = data, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Get users of one policy Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
        
result = getUsersofDeviceAccessPolicy(headers, taskName)
result
```




    {'users': [{'authenticationServer': 'NetBrain', 'username': 'deviceAPAPI'},
      {'authenticationServer': 'NetBrain', 'username': 'gongdai.liu'}],
     'statusCode': 790200,
     'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X GET \
  'https://10.10.7.209/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy/UsersOfDeviceAccessPolicy?name=DeviceAccessPolicy_GL2' \
  -H 'Postman-Token: 04d507d9-7c16-4570-be40-5fe8c649ce18' \
  -H 'cache-control: no-cache' \
  -H 'token: 9dbd05fa-2630-4c2f-bfd2-86973e886bf2'
```
