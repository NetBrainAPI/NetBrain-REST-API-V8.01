
# Device API Design

## ***GET*** /V1/CMDB/DeviceGroups/{groupname}
Call this API to get all device groups in current domain, include Public group, System group and Private group.

## Detail Information

> **Title** : Get Device Groups API<br>

> **Version** : 03/08/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/DeviceGroups

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No request body.

## Path Parameters(****required***)

> No parameters required.

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
|id| string | The ID of the device group. |
|name| string | The Name of the device group. |
|type | integer | The type of device group<br>0: Public group<br>1: Private group<br>2: System group<br>4: Policy device group|

> ***Example***



```python
{
    "deviceGroups": [
         {
            "id":"4ff2a25e-5614-43b0-8098-e981125773af",
            "name":"#BGP 64512",
            "type":2
         },
         {
            "id":"577ec510-cb92-46d3-83c6-f1e86c92158e",
            "name":"#BGP 65000",
            "type":2
         },
         {
            "id":"2270d9e7-8084-413c-9718-b0895d4a148d",
            "name":"lxj",
            "type":0
         }
    ],
    "statusCode":790200,
    "statusDescription":"Success."
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
token = "47cfe2f4-750d-4af2-ae83-afb50679a69b"
nb_url = "http://192.168.28.79"

full_url= nb_url + "/ServicesAPI/API/V1/CMDB/DeviceGroups"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token

try:
    response = requests.get(full_url, headers = headers, verify = False)
        #response = requests.delete(full_url, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()["deviceGroups"]
        print (result)
    else:
        print ("Get Device Groups Failed! - " + str(response.text))
except Exception as e:
    print (str(e))
```

    [{'id': 'a2576703-08f6-4a1e-bd38-c03f36e962d1', 'name': '#BGP 12345', 'type': 2}, {'id': '76c464a9-7fee-4ce6-ba05-c9962f206ed9', 'name': '#BGP 34567', 'type': 2}, {'id': '95efd71c-635b-44a0-ac6c-76d99f0f63fb', 'name': '#BGP 45678', 'type': 2}, {'id': 'fff9a03b-052c-4ece-b5db-8fb38ac4eada', 'name': '#BGP 65111', 'type': 2}, {'id': 'fa2273d4-6600-4870-8286-a258a3bb2b9f', 'name': '#BGP 65112', 'type': 2}, {'id': '3174bdc3-93a3-4fcb-b503-5d266c26bf3f', 'name': '#BGP 65222', 'type': 2}, {'id': '8395ef0c-2b99-4c83-84e2-a2e0b9e9c22f', 'name': '#EIGRP', 'type': 2}, {'id': 'd22885ac-e930-4ada-9c4c-f59b1611c3fa', 'name': '#EIGRP 34567', 'type': 2}, {'id': '649bc165-fe2d-485d-96a0-c4fa9ecf6282', 'name': '#EIGRP 45678', 'type': 2}, {'id': '40e37021-f94d-4a95-9aa2-216875d6b013', 'name': '#OSPF 12345', 'type': 2}, {'id': '08722b14-d70c-4293-b451-721b2c2a8e12', 'name': 'testG1', 'type': 1}]
    

# cURL Code from Postman


```python
curl -X GET \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/DeviceGroups \
  -H 'Postman-Token: ba1fc9ed-6a28-4f84-a0fe-f1a2de1d51ae' \
  -H 'cache-control: no-cache' \
  -H 'token: 47cfe2f4-750d-4af2-ae83-afb50679a69b'
```
