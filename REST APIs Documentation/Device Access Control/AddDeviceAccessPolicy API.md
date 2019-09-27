
## ***POST*** /V1/CMDB/DeviceAccessPolicy
Call this API to create a new device access policy

## Detail Information

> **Title** : Add Device Access Policy API<br>

> **Version** : 08/15/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| name* | string  | The name of the policy which customer want to create.|
| description | string  | A brief explanation of new access policy.|
| privileges* | list of integer  | The privilege inclueded in this policy.<br> 1: View data.<br> 2: Execute Network Change.|
| scope* | object  | The device scope of this new policy.|
| scope.type* | integer | The type of current scope.<br> 0: base on all devices. <br> 1: base on device site. |
| scope.items | list of object | This would be a required input if customer set the scope.type = 1, to specify the identification of device sites|
| scope.items.siteId | list of string | A string list to specify the sites with site ID. <br> ***Note:*** Working for unassign site also.|
| scope.items.sitePath | list of string | A string list to specify the sites with site path. <br> ***Note:*** Working for unassign site also.|
>***Note:*** customer can only select one method between siteId and sitePath for specify device sites. If customer provide both then system will choose siteId as primary parameter automatically.

***Example:*** 


```python
{
    "name": "DeviceAccessPolicy1",
    "description": "a device access policy",
    "privileges": [1, 2],
    "scope": {
        "type": 1,
        "items": [
            {"siteId":"5419d222-f499-4e0e-8306-aaaaaaaaaaaa"},
            {"siteId":"5419d222-f499-4e0e-8306-bbbbbbbbbbbb"},
            .
            .
            .
        ]
    }
}

## OR ##

{
    "name": "DeviceAccessPolicy1",
    "description": "a device access policy",
    "privileges": [1, 2],
    "scope": {
        "type": 1,
        "items": [
            {"sitePath":"My Network/Site1"},
            {"sitePath":"My Network/Site2"},
            .
            .
            .
        ]
    }
}

## OR ##

{
    "name": "DeviceAccessPolicy1",
    "description": "a device access policy",
    "privileges": [1, 2],
    "scope": {
        "type": 1,
        "items": [
            {"siteId":"5419d222-f499-4e0e-8306-aaaaaaaaaaaa", "sitePath":"My Network/Site1"},
            {"siteId":"5419d222-f499-4e0e-8306-bbbbbbbbbbbb", "sitePath":"My Network/Site2"},
            .
            .
            .
        ]
    }
}
```

## Parameters(****required***)

> No required parameter.

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

body = {
    "name": "DeviceAccessPolicy_GL1",
    "description": "a device access policy",
    "privileges": [1, 2],
    "scope": {
        "type": 0
    }
}

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

def addDevicesAccessPolicy(headers, body, nb_url):
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy"
    try:
        response = requests.post(full_url, data = json.dumps(body), headers=headers, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Create new device access policy Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
        
result = addDevicesAccessPolicy(headers, body, nb_url)
result
```




    {'statusCode': 790200, 'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X POST \
  https://10.10.7.209/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 1c6aab8e-44ba-4ec7-b9ea-ec2c02813a93' \
  -H 'cache-control: no-cache' \
  -H 'token: 9dbd05fa-2630-4c2f-bfd2-86973e886bf2' \
  -d '{
    "name": "DeviceAccessPolicy_GL2",
    "description": "a device access policy",
    "privileges": [
        "1",
        "2"
    ],
    "scope": {
        "type": 0
    }
}'
```
