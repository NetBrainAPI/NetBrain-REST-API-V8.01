
# Device API Design

## ***GET*** /V1/CMDB/Devices/GroupDevices/{groupname}
Call this API to get all devices in the device group within the group name provided by user.

## Detail Information

> **Title** : Get Group Devices API<br>

> **Version** : 01/25/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices/GroupDevices/{groupName}

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No request body.

## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| groupName* | string  | The name of one device group which user want to present. |

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
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |
|devices| string[] | A list of devices. |
|devices.id | string | The device ID. |
|devices.mgmtIP| string | The management IP address of the returned device. |
|devices.hostname| string | The hostname of returned device. |


> ***Example***



```python
# Successful response with groupName = "testGroupGDL1"

{
    "devices": [
        {
            "id": "1b558e72-6671-48f8-849e-7f7df473e3aa",
            "mgmtIP": "123.20.20.20",
            "hostname": "R20"
        },
        {
            "id": "1d8c841f-a9bc-4288-aab2-6322bbb1ab1b",
            "mgmtIP": "10.18.19.19",
            "hostname": "R19"
        },
        {
            "id": "1e8029be-a858-48bd-b532-54b694edc529",
            "mgmtIP": "10.120.14.5",
            "hostname": "R3"
        },
        {
            "id": "2ef50fff-eb73-49da-8599-45c68b876275",
            "mgmtIP": "10.18.19.18",
            "hostname": "R18"
        },
        {
            "id": "b95dbda8-64a0-44cb-a12e-79478a2e1f3b",
            "mgmtIP": "123.20.1.10",
            "hostname": "R17"
        },
        {
            "id": "eb31a451-3236-4681-b46e-9084e7e01765",
            "mgmtIP": "10.120.15.1",
            "hostname": "R2"
        },
        {
            "id": "f51f6e8e-d4ef-47af-9139-74a18691c052",
            "mgmtIP": "123.20.1.2",
            "hostname": "R16"
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
}

# If customer don't have enough privilige:
{
    "statusCode":795003,
    "statusDescription":"Insufficient permissions: the current user has insufficient permissions to perform the requested operation. The user has no tenant or domain access permission.sharePolicyManagement"
}
```

# Full Example


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "e074d192-3f21-4ae8-b5f1-405d240b65ca"
nb_url = "http://192.168.28.79"
groupName = "testGroupGDL1"

full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices/GroupDevices/" + str(groupName)
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token

try:
    response = requests.get(full_url, headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get Group Devices Failed! - " + str(response.text))
except Exception as e:
    print (str(e))
```

    {'devices': [{'id': '1b558e72-6671-48f8-849e-7f7df473e3aa', 'mgmtIP': '123.20.20.20', 'hostname': 'R20'}, {'id': '1d8c841f-a9bc-4288-aab2-6322bbb1ab1b', 'mgmtIP': '10.18.19.19', 'hostname': 'R19'}, {'id': '1e8029be-a858-48bd-b532-54b694edc529', 'mgmtIP': '10.120.14.5', 'hostname': 'R3'}, {'id': '2ef50fff-eb73-49da-8599-45c68b876275', 'mgmtIP': '10.18.19.18', 'hostname': 'R18'}, {'id': 'b95dbda8-64a0-44cb-a12e-79478a2e1f3b', 'mgmtIP': '123.20.1.10', 'hostname': 'R17'}, {'id': 'eb31a451-3236-4681-b46e-9084e7e01765', 'mgmtIP': '10.120.15.1', 'hostname': 'R2'}, {'id': 'f51f6e8e-d4ef-47af-9139-74a18691c052', 'mgmtIP': '123.20.1.2', 'hostname': 'R16'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X GET \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices/GroupDevices/testGroupGDL1 \
  -H 'Postman-Token: 8ae37a86-5404-4e59-89d7-851fb44265a5' \
  -H 'Token: e074d192-3f21-4ae8-b5f1-405d240b65ca' \
  -H 'cache-control: no-cache'
```

# Error Examples and Note


```python
###################################################################################################################    

"""Error 1: empty group name"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
    groupName = "" #There is no device with a hostname called "blahblahblah" in users working domain.
    
Response:
    
    "Get Group Devices Failed! - 
        {
            "statusCode":793404,
            "statusDescription":"No resource"
        }"
        
###################################################################################################################    

"""Error 2: no input"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
    #There is no input which means only url and token
    
Response:
    
    "Get Group Devices Failed! - 
        {
            "statusCode":793404,
            "statusDescription":"No resource"
        }"
        
###################################################################################################################    

"""Error 2: no groups name as group name the user provided """

Input:
    
    groupName = "blahblahblah" #There is no group called "blahblahblah"
    
Response:
    
    "Get Group Devices Failed! - 
        {
            "statusCode":791006,
            "statusDescription":"Device group blahblahblah does not exist."
        }"
```
