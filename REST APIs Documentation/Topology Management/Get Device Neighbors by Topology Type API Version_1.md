
# Topology API Design

## ***GET*** /V1/CMDB/Topology/Devices/Neighbors
Call this API to get the neighbor device hostname and connection interface names of interface pair from any devices in current working domain if without the input hostname and topotype.<br>**Note: The API follows the privilege control of NB system. If there is restriction set by Access Control Policy for the target querying resources, the response will not return queried data.**

## Detail Information

> **Title** : Device Neighbors with Topology Type API<br>

> **Version** : 08/22/2019.

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
If customer insert both and there is no corresponding topology interface exist in some devices, then return "Device XXXXX don't have XXXXX interface." If customer only insert one input then only need to consider one filter. e.g. only ["US-BOS-R1"] then return all topology type of this device.|
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
|hostdevice | list of object | List of object content detail information of neighbor base on this device. |
|hostdevice.interface | string | Interface name of the interface which belongs to hostdevice. |
|hostdevice.connected_device | object | Detail information of neighbor device which connect to the hostdevice |
|hostdevice.connected_device.nbr_device| string | The host name of neighbor device which connect to the hostdevice.|
|hostdevice.connected_device.inteface_name| string | The interface name belongs to neighbor device which connect with the hostdevice interface.|
|hostdevice.topology | string | The topology name which this neighbor device belongs to, such as "L2_Topo_Type", "L3_Topo_Type", "Ipv6_L3_Topo_Type" or "VPN_Topo_Type". |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***



```python
{
    "topology":
    [
        {   
            "hostname": "device_1",
            "neighbors":
            [
                {
                    "interface": "intf_1",
                    "connected_device":
                    {
                        "nbr_device": "device_2",
                        "nbr_intf": "intf_3"
                    },
                    "topology": "L2"
                }
				{
                    "interface": "intf_2",
                    "connected_device":
                    {
                        "nbr_device": "device_3",
                        "nbr_intf": "intf_4"
                    },
                    "topology": "L2"
                }
            ]
        }
		{   
            "hostname": "device_4",
            "neighbors":
            [
                {
                    "interface": "intf_5",
                    "connected_device":
                    {
                        "nbr_device": "device_5",
                        "nbr_intf": "intf_6"
                    },
                    "topology": "L3"
                }
        }
    ]
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
token = "e9c7af7c-eedd-40fb-8b4b-356974a12b91"
nb_url = "http://192.168.28.143"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Topology/Devices/Neighbors"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

hostnames = ["BJ_Acc_Sw4"]
topoTypes = [1]

data = {
        "hostname" : hostnames,
        "topoType" : topoTypes,
        "version": "1"
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
  'http://192.168.28.143/ServicesAPI/API/V1/CMDB/Topology/Devices/Neighbors%0A?hostname=%5B%22BJ_Acc_SW1%22%5D&topoType=%5B1%5D&version=%221%22' \
  -H 'Postman-Token: d43de85c-8de9-4bcf-be28-9bc16ce7b329' \
  -H 'cache-control: no-cache' \
  -H 'token: 3d0f475d-dbae-4c44-9080-7b08ded7d35b'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
        
        hostname = [""] # Cannot be null.
        topoType = [] # Cannot be null.

Response:
    
    "Get neighbors by topology failed! - 
        {'topology': [], 'statusCode': 790200, 'statusDescription': 'Success.'}"
        
###################################################################################################################    

"""Error 2: wrong inputs"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
        
        hostname = "dummy" # No device with a hostname called "dummy"
        topoType = []

Response:
    
    "Get neighbors by topology failed! - 
        {'topology': [], 'statusCode': 790200, 'statusDescription': 'Success.'}"

#--------------------------------------------------------------------------------------------------------------------        
    
Input:
        
        hostname = "R1" 
        topoType = [7] # No topology code for 7.

Response:
    
    "Get neighbors by topology failed! - 
        {'statusCode': 791001, 'statusDescription': "Parameter 'TopoType' value must be greater than 0 and less than 4"}"
```
