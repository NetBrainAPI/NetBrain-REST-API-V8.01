
# Device API Design

## ***POST*** /V1/CMDB/Devices/Attributes	
Call this API to create a customized attribute for certain device types. 

User can use the SetDeviceAttribute API to set a value for the created attribute.

## Detail Information

> **Title** : Create Device Attribute API<br>

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
|attributeName* | string  | The name of the attribute.  |
|attributeDisplayName* | string  | The display name of the attribute in Device Details pane of NetBrain IE system. |
|deviceTypeNames | string[]  | Specify the device types that the created attribute applies to.  if set to null, it will apply to all device types. See Device Type Name and ID for available device types.  |
|dataType* | string/double/int/bool/list/table  | The supported data types of the attribute.  |
|subDataType | string  | Only available for list or table type property.<br>▪ The data type of each value in a list type property.<br>▪ If the data type is table, specify the sub properties of table type property as follows:<br>--name - the sub property name (displayed as a column header).<br>--displayName - the display name (alias) of the sub property (can be null).<br>--dataType - the data type of the sub property.<br>--isKey (bool) - control whether to use the sub property as the key when comparing the table type property. The default value is false.  |
|isFullSearch* | bool  | Set whether to use the property as an index in full scope search, including extended search and default search.  |

> ***Example***


```python
body = {
          "attributeName": "newAttribute",
          "attributeDisplayName": "New Attribute",
          "deviceTypeNames": "null",
          "dataType": "string",
          "subDataType": "null",
          "isFullSearch": True
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
token = "855b2da0-306b-4c29-b37f-be09e33e2d02"
nb_url = "http://192.168.28.79"

# Create device attribute
attributeName = "newAttribute05"
attributeDisplayName = "New Attribute05"
deviceTypeNames = "null"
dataType = "string"
subDataType = "null"
isFullSearch = True

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices/Attributes"

body={
        "attributeName": attributeName,
        "attributeDisplayName": attributeDisplayName,
        "deviceTypeNames": deviceTypeNames, 
        "dataType": dataType,
        "subDataType" : subDataType,
        "isFullSearch": isFullSearch
    }

try:
    response = requests.post(full_url, data=json.dumps(body), headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Create device attribute failed! - " + str(response.text))
    
except Exception as e:
    print (str(e))    

```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X POST \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices/Attributes \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: acd1f616-72f5-49a9-82be-3f1b7d2f82de' \
  -H 'cache-control: no-cache' \
  -H 'token: e074d192-3f21-4ae8-b5f1-405d240b65ca' \
  -d '{
        "attributeName": "attributeName",
        "attributeDisplayName": "attributeDisplayName",
        "deviceTypeNames": "null", 
        "dataType": "string",
        "subDataType" : "null",
        "isFullSearch": true
      }'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty one or some required body parameters"""

Input:
    
    attributeName = "" # empty required body parameters
    attributeDisplayName = "New Attribute"
    deviceTypeNames = "" # empty required body parameters
    dataType = "string"
    subDataType = "null"
    isFullSearch = True
    
Response:
    
    "Create device attribute failed! - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter 'attributeName' cannot be null."
        }"
 
###################################################################################################################    

"""Error 2: duplicate attribute name"""

Input:
    
    attributeName = "newAttribute" # attribute name as newAttribute already exist.
    attributeDisplayName = "New Attribute"
    deviceTypeNames = "null" 
    dataType = "string"
    subDataType = "null"
    isFullSearch = True
    
Response:
    
    "Create device attribute failed! - 
        {
            "statusCode":791007,
            "statusDescription":"attribute newAttribute already exists."
        }"
    
###################################################################################################################    

"""Error 2: two attributes, only different on name"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
    attributeName = "newAttribute1" # only name different from "newAttribute"
    attributeDisplayName = "New Attribute"
    deviceTypeNames = "null" 
    dataType = "string"
    subDataType = "null"
    isFullSearch = True
    
Response:
    
    "{
        "statusCode": 790200,
        "statusDescription": "Success."
    }"
        
```

