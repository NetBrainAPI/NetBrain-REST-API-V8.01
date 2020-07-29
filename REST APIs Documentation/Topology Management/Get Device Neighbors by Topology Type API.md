
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
|hostname* | string  | The device name.  |
|topoType* | string  | Return the neighbors in a specified topology type, such as "L2_Topo_Type’, ‘L3_Topo_Type’, ‘Ipv6_L3_Topo_Type’ or ‘VPN_Topo_Type". |

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
