
# Topology API Design

## ***GET*** /V1/CMDB/Topology/Devices/Neighbors{?hostname}&{?topoType}
Use this API to get specific neighbors of a device according to the specified topology type.

## Detail Information

> **Title** : Get Device Neighbors by Topology Type API<br>

> **Version** : 02/01/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Topology/Devices/Neighbors


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
|hostname | list of string  | The devices name, such as ["US-BOS-R1"] or ["US-BOS-R2", "US-BOS-R3", "US-BOS-R4"]|
|topoType | list of int  | Return the neighbors in specified topology types<br> 1: L3_Topo_Type, <br>2: L2_Topo_Type, <br>3: Ipv6_L3_Topo_Type, <br>4: VPN_Topo_Type, <br>such as [1] or [2,3,4].<br> ***Note:*** Default value is 1. If customer insert the value outside of 1-4 return respones: "Please select the exist topology type."if customer insert the value with wrong value type: ["1", "2"], then return respone: "Topology type must be insert as Integer"|
|||If insert both "hostname" and "topoType" as filters and there is no corresponding topology interface exist in some devices, then return "Device XXXXX don't have XXXXX interface." If customer only insert one input then only need to consider one filter. e.g. only ["US-BOS-R1"] then return all topology type of this device.|
|version | string  | Value of this parameter is 1 for verison 8.01|
|skip|integer|The amount of records to be skipped. The value must not be negative.  If the value is negative, API throws exception {"statusCode":791001,"statusDescription":"Parameter 'skip' cannot be negative"}. No upper bound for this parameter.|
|limit|integer|The up limit amount of device records to return per API call. The value must not be negative.  If the value is negative, API throws exception {"statusCode":791001,"statusDescription":"Parameter 'limit' cannot be negative"}. The value of this parameter is in range of 10-100. If the parameter is not specified in API call, the default value 50 will be used.|
|||If only provide skip value, return the rest of the full device list. If only provide limit value, return from the first device in DB. If provided both skip and limit, return as required. Error exceptions follow each parameter's description.|
|||**Note:** The skip and limit parameters are based on device search result, not topology result record.|

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
|neighbors | list of object | List of neribor devices and interface.  |
|neighbors.hostname | string | The peer device name.  |
|neighbors.interface | string | The peer interface name. |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
{
    "neighbors": [
        {
            "hostname": "R4",
            "interface": "Ethernet0/1 123.10.1.1/30"
        },
        {
            "hostname": "R5",
            "interface": "Ethernet0/1 123.10.1.6/30"
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
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
token = "3d0f475d-dbae-4c44-9080-7b08ded7d35b"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Topology/Devices/Neighbors"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

hostname = "R1"
topoType = "L3_Topo_Type"

data = {
        "hostname" : hostname,
        "topoType" : topoType
    }

try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get neighbors by topology failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'neighbors': [{'hostname': 'R4', 'interface': 'Ethernet0/1 123.10.1.1/30'}, {'hostname': 'R5', 'interface': 'Ethernet0/1 123.10.1.6/30'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X GET \
  'http://192.168.28.79/ServicesAPI/API/V1/CMDB/Topology/Devices/Neighbors?hostname=R1&topoType=L3_Topo_Type' \
  -H 'Postman-Token: d43de85c-8de9-4bcf-be28-9bc16ce7b329' \
  -H 'cache-control: no-cache' \
  -H 'token: 3d0f475d-dbae-4c44-9080-7b08ded7d35b'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
        
        hostname = "" # Cannot be null.
        topoType = "" # Cannot be null.

Response:
    
    "Get neighbors by topology failed! - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter 'hostname' cannot be null."
        }"
        
    "Get neighbors by topology failed! - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter 'topoType' cannot be null."
        }"
        
###################################################################################################################    

"""Error 2: wrong inputs"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
        
        hostname = "hahahh" # No device with a hostname called "hahahh"
        topoType = "L3_Topo_Type"

Response:
    
    "Get neighbors by topology failed! - 
        {
            "statusCode":791006,
            "statusDescription":"hostname does not exist."
        }"

#--------------------------------------------------------------------------------------------------------------------        
    
Input:
        
        hostname = "R1" 
        topoType = "XXXX" # No topology type called "XXXX".

Response:
    
    "Get neighbors by topology failed! - 
        {
            "statusCode":791001,
            "statusDescription":"Invalid parameter: the parameter 'topoType' is invalid."
        }"
```
