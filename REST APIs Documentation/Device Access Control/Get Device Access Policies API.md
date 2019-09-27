
# Get Device Access Policies API

## ***GET*** /V1/CMDB/DeviceAccessPolicy?{name}
Call this API to get device access policy in current domain. If the input policy name is not none, API will return the corrsponding policy information of base one input name. Otherwise API will return all policy information.

## Detail Information

> **Title** : Get Device Access Policies API<br>

> **Version** : 08/12/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No Request Body.

## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| name | string  | The name of the policy which customer want to check.|

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
|policies|	list of object	|list of policy|
|policies.id|	string	|policy id|
|policies.name|	string	|policy name|
|policies.description|	string	|policy description|
|policies.privileges| list of int |The privileges which belong to this policy,<br> 1:View Data,<br> 2: Execute Network Change.|
|policies.scope| object	|Device Scope of current policy<br>▪type(int) -type of scope, 0: all Devices, 1: site<br>▪items(List) -0: no meaning，1: save the site id list.|
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |


***Example:***


```python
{
    "policies": [
        {
            "id": "fdd89e80-630c-44ff-97ea-07041b0cbbef",
            "name": "DeviceAccessPolicy2",
            "description": "a device access policy",
            "privileges": [
                1,
                2
            ],
            "scope": {
                "type": 1,
                "items": [
                    "eaedebea-9bba-4fad-9ff1-efddd55c58de"
                ]
            }                  
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

def getDeviceAccessPolicy(headers, taskName):
    data = {
        "name" : taskName
    }
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy"
    try:
        response = requests.get(full_url, headers=headers, params = data, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Get device policy access Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
        
result = getDeviceAccessPolicy(headers, taskName)
result
```




    {'policies': [{'id': '826ad918-8a4f-4a7c-8098-0ff93a4cad58',
       'name': 'DeviceAccessPolicy_GL2',
       'description': 'a device access policy',
       'privileges': [1, 2],
       'scope': {'type': 0, 'items': []}}],
     'statusCode': 790200,
     'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X GET \
  'https://10.10.7.209/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy?name=DeviceAccessPolicy_GL2' \
  -H 'Postman-Token: 9639788b-0500-4065-9947-94c95075808a' \
  -H 'cache-control: no-cache' \
  -H 'token: 9dbd05fa-2630-4c2f-bfd2-86973e886bf2'
```
