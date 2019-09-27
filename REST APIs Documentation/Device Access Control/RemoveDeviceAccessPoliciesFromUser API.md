
# RemoveDeviceAccessPoliciesFromUser

## ***DELETE*** /V1/CMDB/UserDeviceAccessPolicy
Call this API to remove device access policies from user

## Detail Information

> **Title** : Remove Device Access Policies from User API<br>

> **Version** : 08/12/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| userName* | string  | The name of the user account.|
| policies* | list of string | The list of policy name. <br> ***Note:*** policy list can not be empty.|

***Example:***


```python
{
    "userName":"user1",
    "policies" : ["policyName1", "policyName2"]               
}
```

## Parameters(****required***)

> No required paramenters.

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
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

***Example:***


```python
{
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

## Full Example


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

body = {
  "userName":"deviceAPAPI",
  "policies" : ["DeviceAccessPolicy_GL1"]              
 
}

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

def RemoveDeviceAccessPoliciesFromUser(headers, body, nb_url):
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy"
    try:
        response = requests.delete(full_url, data = json.dumps(body), headers=headers, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Assign user to device access policy Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
        
result = RemoveDeviceAccessPoliciesFromUser(headers, body, nb_url)
result
```




    {'statusCode': 790200, 'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X DELETE \
  https://10.10.7.209/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 40957ce1-cd88-47a4-a5ae-2aa308afd6cc' \
  -H 'cache-control: no-cache' \
  -H 'token: 6bf756e4-18dd-49ec-b63e-cad4a1129c95' \
  -d '{
  "userName":"deviceAPAPI",
  "policies" : ["DeviceAccessPolicy_GL1"]              
 
}'
```
