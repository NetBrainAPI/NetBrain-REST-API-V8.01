
# Device API Design

## ***DELETE*** /V1/CMDB/Devices
Call this API to delete a device in current domain.

## Detail Information

> **Title** : Delete Devices API<br>

> **Version** : 01/28/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Query Parameters(****required***)

>No query parameters.


## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|IPs* | list of string  | Management ip list of the target devices. Optional, IPs and hostnames must have at least one member. |
|hostnames* | list of string  | Hostname list of the target devices. Optional, IPs and hostnames must have at least one member. |

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
#mgmtIP = ["123.20.20.20", "10.1.12.2"]
mgmtIP = [""]
#hostname = ["R20", "Client1" ]
hostname = [""]

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices"
body={"hostnames" : hostname, "IPs": mgmtIP} # The inputs shouldn't been put in body parameters. 
    
try:
    response = requests.delete(full_url, headers=headers, data=json.dumps(body), verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Delete device Failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    Delete device Failed! - {"statusCode":791006,"statusDescription":"device does not exist."}
    

# cURL Code from Postman


```python
curl -X DELETE \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: f444c570-8f18-460e-9e58-2963b7fdbb91' \
  -H 'cache-control: no-cache' \
  -H 'token: 13c7ed6e-781d-4b22-83e7-b1722de4e31d' \
  -d '{
        "hostname" : ["R20", "Client1"],
        "IPs" : ["123.20.20.20", "10.1.12.2"]
    }' 
    # Again, they shouldn't be parse in as body parameters.
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: devices have deen deleted already"""

Input:
    
        mgmtIP = ["123.20.20.20", "10.1.12.2"]
        hostname = ["R20", "Client1"]

Response:
    
    "Delete device Failed! - 
        {
            "statusCode":791006,
            "statusDescription":"device does not exist."
        }"
        
###################################################################################################################    

"""Error 1: inputs not enough"""

Input:
        mgmtIP = ["123.20.20.20", "10.1.12.2"],
        hostname = []# hostname dose not provided
        ##OR##
        mgmtIP = []# management IP dose not provided
        hostname = ["R20", "Client1"]
        ##OR##
        mgmtIP = []
        hostname = [] # none if them has been provided

Response:
    
    "Delete device Failed! - 
        {
            "statusCode": 791000,
            "statusDescription": "Null parameter: the parameter 'IPs and hostnames' cannot be null."
        }"
        
###################################################################################################################    

"""Error 1: Wrong sequence of two lists"""

Input:
        hostname = ["Client1" , "R20"]
        mgmtIP = ["123.20.20.20", "10.1.12.2"] # "10.1.12.2" cprresponde to "Client1", "123.20.20.20" corresponde to "R20".
         
Response:
    
    "Delete device Failed! - 
        {
            "statusCode": 791000,
            "statusDescription": "device does not exist."
        }"
```
