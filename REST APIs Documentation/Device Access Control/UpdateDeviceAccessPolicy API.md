
# UpdateDeviceAccessPolicy 

## ***PUT*** /V1/CMDB/DeviceAccessPolicy
Call this API to modify a new device access policy <br>
***Note:*** customer needs to have **Domain Management** privilege at least.

## Detail Information

> **Title** : Update Device Access Policy API<br>

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
| newName | string  | The new name of the policy which customer want to modify.|
| description | string  | A brief explanation of new access policy.|
| privileges* | list of integer  | The privilege inclueded in this policy.<br> 1: View data.<br> 2: Execute Network Change.|
| scope* | object  | The device scope of this new policy.|
| scope.type* | integer | The type of current scope.<br> 0: base on all devices. <br> 1: base on device site. |
| scope.items | list of object | Only needed when customer set the scope.type = 1 to specify the identification of device sites|
| scope.items.siteId | list of string | A string list to specify the sites with site ID.|
| scope.items.sitePath | list of string | A string list to specify the sites with site path. |
>***Note:*** customer can only select one method between siteId and sitePath for specify device sites. If customer provide both then system will choose siteId as primary parameter automatically.

***Example:*** 


```python
{
    "name": "DeviceAccessPolicy_GL",
    "newName":"DeviceAccessPolicy_GL_Update",
    "description": "a device access policy",
    "privileges": [
        1,
        2
    ],
    "scope": {
        "type": 1,
        "items": [
            {"sitePath":"My Network/site1/site1"}
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
    "name": "DeviceAccessPolicy_GL",
    "newName":"DeviceAccessPolicy_GL_Update",
    "description": "a device access policy",
    "privileges": [
        1,
        2
    ],
    "scope": {
        "type": 1,
        "items": [
            {"sitePath":"My Network"}
        ]
    }
}

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

def updateDevicesAccessPolicy(headers, body, nb_url):
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy"
    try:
        response = requests.put(full_url, data = json.dumps(body), headers=headers, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Modify existing access policy Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
        
result = updateDevicesAccessPolicy(headers, body, nb_url)
result
```




    {'statusCode': 790200, 'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X PUT \
  https://10.10.7.209/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 1bcd8232-8c82-40e0-8586-ba37d779cdeb' \
  -H 'cache-control: no-cache' \
  -H 'token: 9dbd05fa-2630-4c2f-bfd2-86973e886bf2' \
  -d '{
    "name": "DeviceAccessPolicy_GL",
    "newName":"DeviceAccessPolicy_GL_Update",
    "description": "a device access policy",
    "privileges": [
        1,
        2
    ],
    "scope": {
        "type": 1,
        "items": [
            {"sitePath":"My Network"}
        ]
    }
}'
```
