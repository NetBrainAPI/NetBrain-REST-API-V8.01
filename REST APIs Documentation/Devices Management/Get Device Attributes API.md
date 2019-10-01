
# Device API Design

## ***GET*** /V1/CMDB/Devices/Attributes/{?hostname}/{?attributeName}
Call this API to get the value for an attribute of a device, get all attributes if attribute name is not specifed.

## Detail Information

> **Title** : Get Device Attribute API<br>

> **Version** : 01/28/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices/Attributes

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

>No request body.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|hostname* | string  | The hostname of the target device.  |
|attributeName | string  | Optionnal. The name of the attribute that you want to get its value, get all attributes if the attribute name is not specifed.<br>Please note that the attribute name here is case sensitive and not the name displayed in the Device Details pane of NetBrain IE system. See Applicable Device Attributes for system built-in device attributes. |

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
|attributes | object | attributes set  |
|attributeName| string | The name of the attribute.  |
|hostname| string | The hostname of returned device. |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***


```python
{
    "hostname": "R20",
    "attributes": {
        "name": "R20",
        "mgmtIP": "123.20.20.20",
        "mgmtIntf": "Loopback0",
        "subTypeName": "Cisco Router",
        "vendor": "Cisco",
        "model": "DEVELOPMENT TEST SOFTWARE",
        "ver": "15.4(2)T4",
        "sn": "71372834",
        "site": "My Network\\Unassigned",
        "loc": "",
        "contact": "",
        "mem": "356640420",
        "assetTag": "",
        "layer": "",
        "descr": "",
        "oid": "1.3.6.1.4.1.9.1.1",
        "driverName": "Cisco Router",
        "fDiscoveryTime": {
            "$date": 1547572719000
        },
        "lDiscoveryTime": {
            "$date": 1547572719000
        },
        "assignTags": "",
        "hasBGPConfig": true,
        "hasOSPFConfig": false,
        "hasEIGRPConfig": false,
        "hasISISConfig": false,
        "hasMulticastConfig": false,
        "TestTable": "",
        "newAttribute": "20",
        "attributeName": ""
    },
    "statusCode": 790200,
    "statusDescription": "Success."
}

# If customer don't have enough privilige:
{
    "statusCode":795003,
    "statusDescription":"Insufficient permissions: the current user has insufficient permissions to perform the requested operation. The user has no tenant or domain access permission.sharePolicyManagement"
}
```

# Full Example:


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "855b2da0-306b-4c29-b37f-be09e33e2d02"
nb_url = "http://192.168.28.79"

hostname = "R20"
attributeName = "kkkkk" # Set attributeName as null to present all attributes of device "R20"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices/Attributes"

body={
        "hostname":hostname, 
        "attributeName":attributeName
    }

try:
    response = requests.get(full_url, params=body, headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get device attributes failed! - " + str(response.text))

except Exception as e:
    print (str(e))   
```

    {'hostname': 'R20', 'attributes': {}, 'statusCode': 790200, 'statusDescription': 'Success.'}
    


```python
hostname = "R20"
attributeName = "mgmtIP" # Set attributeName as "mgmIP" to get the mgmIP value of device "R20"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices/Attributes"

body={
        "hostname":hostname, 
        "attributeName":attributeName
    }

try:
    response = requests.get(full_url, params=body, headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get device attributes failed! - " + str(response.text))

except Exception as e:
    print (str(e))   
```

    {'hostname': 'R20', 'attributes': {'mgmtIP': '123.20.20.20'}, 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X GET \
  'http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices/Attributes?hostname=R20&attributeName=' \
  -H 'Postman-Token: 3dbeaeff-9328-4154-814c-d2fbad2332a7' \
  -H 'cache-control: no-cache' \
  -H 'token: 13c7ed6e-781d-4b22-83e7-b1722de4e31d'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: set hostname as empty"""

Input:
    
        hostname = ""

Response:
    
    "Get device attributes failed! - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter 'hostname' cannot be null."
        }"
        
###################################################################################################################    

"""Error 1: hostname does not exist"""

Input:
    
        hostname = "blahblahblah"

Response:
    
    "Get device attributes failed! - 
        {
            "statusCode":791006,
            "statusDescription":"device does not exist."
        }"
        
###################################################################################################################    

"""Error 1: attributeName does not exist in specified device"""

Input:
    
        attributeName = "blahblahblah"

Response:
    
    "{
        'hostname': 'R20', 
        'attributes': {}, 
        'statusCode': 790200, 
        'statusDescription': 'Success.'
    }"
```
