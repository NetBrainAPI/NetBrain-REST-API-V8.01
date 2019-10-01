
# Device API Design

## ***PUT*** /V1/CMDB/Devices/Attributes	
Call this API to set a value for the specified attriute of a device.

## Detail Information

> **Title** : Set Device Attribute API<br>

> **Version** : 01/25/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices/Attributes

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|attributeName* | string  | The name of the attribute that you want to set a value for. Please note that some properties, such as Hostname and Device Type cannot be set. |
|attributeValue* | string  | The value for the attribute.  |
|hostname* | string  | The hostname of the device.  |

>**Note:** Applicable Device Attributes

|**Property/Attribute Name**|**Display Name in Device Details Pane**|**Description**|
|------|------|------|
|<img width=50/>|<img width=50/>|<img width=300/>|
|vendor | Vendor  | The vendor information of a device. |
|model | Model  | The model information of a device. |
|ver | Software Version  | The version of a device. |
|sn | Serial Number  | The serial number of a device. |
|loc | Location  | The location of a device. |
|contact | Contact  | The contact person of a device. |
|mem | System Memory Size  | The system memory size of a device. |
|assetTag | Asset Tag  | The asset tag of a device. |
|layer | Hierarchy Layer  | The network layer that a device belongs to. |
|descr | Description  | The description of a device. |

> ***Example***


```python
attributeName = "vendor"
attributeValue = "New Attribute"
hostname = "R20"

body = {
        "hostname": hostname,
        "attributeName": attributeName,
        "attributeValue": attributeValue
       }
```

## Parameters(****required***)

> No Parameters Required.

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
token = "6e1f5fdd-247c-4710-91bb-2cbd3f737489"
nb_url = "http://192.168.28.79"

attributeName = "vendor"
attributeValue = "New Attribute"
hostname = "R20"

body = {
            "hostname": hostname,
            "attributeName": attributeName,
            "attributeValue": attributeValue
        }

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices/Attributes"
    
try:
    response = requests.put(full_url, data=json.dumps(body), headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Set device attribute failed! - " + str(response.text))

except Exception as e:
        print (str(e)) 
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X PUT \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices/Attributes \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: d0022cb0-109e-491c-bba4-b3e99e7ec1dd' \
  -H 'cache-control: no-cache' \
  -H 'token: 6e1f5fdd-247c-4710-91bb-2cbd3f737489' \
  -d '{
    "hostname": "R20",
    "attributeName": "newAttribute",
    "attributeValue": "20"
	}'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty hostname or sttribute name"""

Input:
    
        attributeName = ""
        attributeValue = ""
        hostname = "R20"
        
        ##OR##
        
        attributeName = "newAttribute"
        attributeValue = ""
        hostname = ""

Response:
    
    "Set device attribute failed! - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter 'attributeName' cannot be null." 
                         ## OR  "Null parameter: the parameter 'hostname' cannot be null."
        }"
        
#Note: attributeValue can be null.

###################################################################################################################    

"""Error 2: device not exist"""

Input:
    
        attributeName = "newAttribute"
        attributeValue = "20"
        hostname = "R201" # There is no device named as "R201"

Response:
    
    "Set device attribute failed! - 
        {
            "statusCode":791006,
            "statusDescription":"device R201 does not exist."
        }"
        
###################################################################################################################    

"""Error 2: attribute not exist"""

Input:
    
        attributeName = "blahblahblah" # There is no device attribute named as "blahblahblah"
        attributeValue = "20"
        hostname = "R20" 

Response:
    
    "Set device attribute failed! - 
        {
            "statusCode":791006,
            "statusDescription":"attribute blahblahblah does not exist."
        }"
```
