
# DeleteDeviceAccessPolicy 

## ***DELETE*** /V1/CMDB/DeviceAccessPolicy/{policyName}
Call this API to delete a device access policy.

## Detail Information

> **Title** : Delete Device Access Policies API<br>

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
| policyName* | string  | The policy name which customer want to delete.|

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
policyName = "DeviceAccessPolicy_GL2"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

def deleteDeviceAccessPolicy(headers, policyName):
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy/" + policyName
    try:
        response = requests.delete(full_url, headers=headers, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Delete device policy access Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
        
result = deleteDeviceAccessPolicy(headers, policyName)
result
```




    {'statusCode': 790200, 'statusDescription': 'Success.'}



## cURL Code fromPostman


```python
curl -X DELETE \
  https://10.10.7.209/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy/DeviceAccessPolicy_GL2 \
  -H 'Postman-Token: 4e7f346d-8cb6-46c6-9507-976c6132b1eb' \
  -H 'cache-control: no-cache' \
  -H 'token: 6bf756e4-18dd-49ec-b63e-cad4a1129c95'
```
