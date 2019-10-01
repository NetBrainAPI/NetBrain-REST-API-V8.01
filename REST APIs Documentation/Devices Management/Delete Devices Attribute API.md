
# Device API Design

## ***DELETE*** /V1/CMDB/Devices/Attributes/{attributeName}
Call this API to delete a device attribute (property) from schema.

## Detail Information

> **Title** : Delete Device Attribute API<br>

> **Version** : 01/28/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices/Attributes/{attributeName}

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

>No request body.

## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|attributeName* | string  | Name of the attribute which user decide to delete from schema,case sensitive. |

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

> ***Example***


```python
{
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
token = "13c7ed6e-781d-4b22-83e7-b1722de4e31d"
nb_url = "http://192.168.28.79"

attributeName = "newAttribute1"
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices/Attributes/"+str(attributeName)

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
    
try:
    response = requests.delete(full_url, headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Delete device attribute failed! - " + str(response.text))
    
except Exception as e:
    print (str(e))  
```

    Delete device attribute failed! - {"statusCode":795005,"statusDescription":"Invalid token."}
    


```python
# Call Get Device Attribute API first before call delete API.

hostname = "Client1"
attributeName = ""

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

    {'hostname': 'Client1', 'attributes': {'name': 'Client1', 'mgmtIP': '10.1.12.2', 'mgmtIntf': 'Ethernet0/0', 'subTypeName': 'Cisco Router', 'vendor': 'Cisco', 'model': 'DEVELOPMENT TEST SOFTWARE', 'ver': '15.4(2)T4', 'sn': '71374883', 'site': 'My Network\\Unassigned', 'loc': '', 'contact': '', 'mem': '100787876', 'assetTag': '', 'layer': '', 'descr': '', 'oid': '1.3.6.1.4.1.9.1.1', 'driverName': 'Cisco Router', 'fDiscoveryTime': {'$date': 1547572714000}, 'lDiscoveryTime': {'$date': 1547572714000}, 'assignTags': '', 'hasBGPConfig': False, 'hasOSPFConfig': False, 'hasEIGRPConfig': False, 'hasISISConfig': False, 'hasMulticastConfig': False, 'TestTable': '', 'newAttribute': '', 'attributeName': '', 'newAttribute1': '', 'newAttribute11': '', 'newAttribute111': ''}, 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X DELETE \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices/Attributes/newAttribute1 \
  -H 'Postman-Token: fe203534-a0f5-4597-9874-321d1f335d75' \
  -H 'cache-control: no-cache' \
  -H 'token: 13c7ed6e-781d-4b22-83e7-b1722de4e31d'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: set attributeName as empty"""

Input:
    
        attributeName = ""

Response:
    
    "Delete device attribute failed! - 
        {
            "statusCode":793405,
            "statusDescription":"Method is not supported"
        }"
        
###################################################################################################################    

"""Error 1: the attribute not exist or has been deleted already"""

Input:
    
        attributeName = "newAttribute1" #this attribute has already been deleted.

Response:
    
    "Delete device attribute failed! - 
        {
            "statusCode":791006,
            "statusDescription":"attribute newAttribute1 does not exist."
        }"

###################################################################################################################    

"""Error 1: the attribute exists in other devices"""

Input:
    
        attributeName = "newAttribute" #this attribute exist in device "R20" not in "Client 1".

Response:
    
    "Delete device attribute failed! - 
        {
            "statusCode":793001,
            "statusDescription":"Inner exception. Property (ID=\"newAttribute\") is using by other devices"
        }"
        
###################################################################################################################    

```
