
# Device Group API Design

## ***GET*** /V1/CMDB/DeviceGroups/{deviceGroupID}/devices
This API call returns devices in a device group.

## Detail Information

> **Title** : Get devices of Device Group API<br>

> **Version** : 10/08/2019.

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/API/V1//CMDB/DeviceGroups/{deviceGroupID}/devices

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| deviceGroupID | string  | The unique ID of specified device group. |


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
|<img width=100/>|<img width=100/>|<img width=500/>|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code. |
|devices| string[] | Device name list |

> ***Example***


```python
{
    "statusCode": 790200,
    "statusDescription": "Success.",
    "devices":["bjretrahc001234","bjretrahc003465","bjta007616","bjta000408"]
}
```

# Full Example :


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "ad3c616e-5f3d-45e9-9ba1-bb71f003a098"
deviceGroupID = '9732dca7-9709-4c49-91e1-a2310b8364d9'
nb_url = "http://192.168.28.143"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/DeviceGroups/"+deviceGroupID+"/devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

try:
    response = requests.get(full_url, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get devices from group failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 

```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X GET \
  http://192.168.28.143/ServicesAPI/API/V1/CMDB/DeviceGroups/9732dca7-9709-4c49-91e1-a2310b8364d9/devices \
  -H 'accept: application/json' \
  -H 'content-type: application/json' \
  -H 'token: ad3c616e-5f3d-45e9-9ba1-bb71f003a098' \
}'
```

# Error Examples


```python
###################################################################################################################    


"""Error 1: Null parameter: the parameter '{}' cannot be null."""

Input:
    
    "name": "",
    "type": "policy"
    
Response:
    
    "Parameter cannot be null - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter '{}' cannot be null."
        }"

###################################################################################################################    

"""Error 2: device group: {}, type: {} already exists."""

Input:
    
    "name": "Device Group 1",
    "type": "policy"
    
Response:        
    
    "Device Group already exists! - 
        {
            "statusCode":791007,
            "statusDescription":"device group: {}, type: {} already exists."
        }"

###################################################################################################################    

"""Error 3: You are not allowed to perform the operation."""

Input:
    
    "User has no privilege to make change to device groups"
    
Response:
    
    "You are not allowed to perform the operation. Failed! - 
        {
            "statusCode":791000,
            "statusDescription":"You are not allowed to perform the operation."
        }"
        
