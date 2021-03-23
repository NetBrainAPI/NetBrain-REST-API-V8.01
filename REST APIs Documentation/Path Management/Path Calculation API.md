
# Path Calculation Design

***Note:*** the sequence of steps must be followed if customer want to use Path Calculation API.

# Step 1 - Resolve device gateway
=======================================================================================================================

## ***GET*** /V1/CMDB/Path/Gateways
Call this API to retrieve the gateways for a device used as path source.

## Detail Information

> **Title** : Resolve Device Gateway API<br>

> **Version** : 06/27/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Path/Gateways

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No request body.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| ipOrHost* | string  | Device mgmIp or hostname, used as the source in path calculation. |

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
|gatewayList| List of Object | Gateway list.  |
|gatewayList.gatewayName| string | The name of gateway.  |
|gatewayList.type| string | The type of gateway.  |
|gatewayList.payload| dict | Internal data structure, customer don't need to considered.  |
|transip| string | Ip address of gateway.  |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |


```python
{
    "gatewayList": [
        {
            "gatewayName": "BJ_L2_test_1.Vlan10(172.24.33.10)",
            "type": "Device Interface",
            "payload": "{\"ip\": \"172.24.33.10\", \"endPointInfo\": {\"deviceId\": \"101deae6-8d11-47d2-b87f-b69cbe7ba2ce\", \"interfaceId\": \"9a40c2e8-12ba-4556-bb2f-9545f776afb7\"}, \"device\": \"BJ_L2_test_1\", \"deviceId\": \"101deae6-8d11-47d2-b87f-b69cbe7ba2ce\", \"interface\": \"Vlan10\", \"interfaceId\": \"9a40c2e8-12ba-4556-bb2f-9545f776afb7\", \"prefixLen\": 26}"
        }
    ],
    "transip": "172.24.33.10",
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

## Full Example


```python
# import python modules 
import requests
import time
import urllib3
import pprint
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

nb_url = "http://192.168.28.173"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'} 
token = "76f95ffa-fc1b-4eb6-a503-75760185f2a5"
source_device = "172.24.33.10"
destination_device = "172.24.33.135"
```


```python
Resolve_Device_Gateway_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Gateways"

def resolve_device_gateway(Resolve_Device_Gateway_url, token, ipOrHost, headers):
    headers["Token"] = token
    data = {"ipOrHost":ipOrHost}
    try:
        response = requests.get(Resolve_Device_Gateway_url, params = data, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return ("Create module attribute failed! - " + str(response.text))

    except Exception as e:
        print (str(e))

source_gateway = resolve_device_gateway(Resolve_Device_Gateway_url, token, source_device, headers)
source_gateway
```




    {'gatewayList': [{'gatewayName': 'BJ_L2_test_1.Vlan10(172.24.33.10)',
       'type': 'Device Interface',
       'payload': '{"ip": "172.24.33.10", "endPointInfo": {"deviceId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce", "interfaceId": "9a40c2e8-12ba-4556-bb2f-9545f776afb7"}, "device": "BJ_L2_test_1", "deviceId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce", "interface": "Vlan10", "interfaceId": "9a40c2e8-12ba-4556-bb2f-9545f776afb7", "prefixLen": 26}'}],
     'transip': '172.24.33.10',
     'statusCode': 790200,
     'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X GET \
  'http://192.168.28.173/ServicesAPI/API/V1/CMDB/Path/Gateways?ipOrHost=172.24.33.10' \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 192.168.28.173' \
  -H 'Postman-Token: e03fba73-b667-49d4-badb-7c166ef88a94,a062a3f7-6186-4ef4-98ca-2afae1c17f7f' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'token: 76f95ffa-fc1b-4eb6-a503-75760185f2a5'
```

# Step 2 - Path Calculation
=======================================================================================================================

## ***POST*** /V1/CMDB/Path/Calculation
Call this API to calculate the path from endpoint A (source) to endpoint B (destination). It returns the result of the calculated path in the form of a path ID (a string), and you can use the path ID in the GetPath API as the input parameter to get each hop information of the path.

## Detail Information

> **Title** : Calculate Path API<br>

> **Version** : 06/27/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Path/Calculation

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|sourceIP* | string  | Input the IP address of the source device.  |
|sourcePort | integer  | Specify the source protocol port If TCP/UDP is selected such as 23 for telnet. This parameter can be null.  |
|sourceGateway* | Object  | Source gateway resolve result, end user **MUST** use gateway resolve result.  |
|sourceGateway.type* | string | Result rely on Step 1, customer don't need to consider.|
|sourceGateway.gatewayName* | string  | The name of the gateway. Result from Step 1.  |
|gatewayList.payload*| dict | Internal data structure, customer don't need to considered.  |
|destIP* | string  | Input the IP address of the destination device.  |
|destPort* | integer  | Specify the destination protocol port If TCP/UDP is selected, such as 23 for telnet. This parameter can be null.  |
|protocol* | integer  | Specify the application protocol. see list_of_ip_protocol_numbers, such as 4 for IPv4.  |
|isLive* | bool  | ▪ False - Use data From current Baseline<br>▪ True - Use data via live access |
|advanced |object	|advance setting.|
|advanced.debugMode | bool	|The debug mode of trigger API.|
|advanced.calcWhenDeniedByACL| bool	| Whether to keep calculate when the process been denied by ACL.|
|advanced.calcWhenDeniedByPolicy |bool	|Whether to keep calculate when the process been denied by policy.|
|advanced.calcL3ActivePath| bool	|Whether to calculate L3 active path.|
|advanced.useCommandsWithArguments| bool	|Whether to use the commands with arguments inside.|
|advanced.enablePathFixup	|bool	|Whether to enable the path fixup feature.|

## Parameters(****required***)

>No parameters required.

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
|taskID| string | The task ID of the calculated path. You can call the hop information of the path with the taskID in the GetPath API. |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
{
    'taskID': 'dcf25655-81a9-4cfe-82ca-aef80a698971',
    'statusCode': 790200,
    'statusDescription': 'Success.'
}
```

## Full Example:


```python
# call calculate_path API

Calculate_Path_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation"

gwName = source_gateway["gatewayList"][0]["gatewayName"]
gwType = source_gateway["gatewayList"][0]["type"]
gw = source_gateway["gatewayList"][0]["payload"]

sourceIP = source_device
sourcePort = None #can be 8080
destIP = destination_device
destPort = 0
pathAnalysisSet = 2
protocol = 4
isLive = True

body = {
    "sourceIP" : sourceIP,                # IP address of the source device.
    "sourcePort" : sourcePort,
    "sourceGateway" : {
        "type" : gwType,
        "gatewayName" : gwName,
        "payload" : gw
    },    
    "destIP" : destIP,                    # IP address of the destination device.
    "destPort" : destPort,
    "protocol" : protocol,                # Specify the application protocol, check online help, such as 4 for IPv4.
    "isLive" : isLive                     # False: Current Baseline; True: Live access
} 


def calculate_path(Calculate_Path_url, body, headers, token):
    headers["Token"] = token
    
    try:
        response = requests.post(Calculate_Path_url, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return ("Create module attribute failed! - " + str(response.text))

    except Exception as e:
        return (str(e)) 

res = calculate_path(Calculate_Path_url, body, headers, token)
res
```




    {'taskID': 'dcf25655-81a9-4cfe-82ca-aef80a698971',
     'statusCode': 790200,
     'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X POST \
  http://192.168.28.173/ServicesAPI/API/V1/CMDB/Path/Calculation \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Host: 192.168.28.173' \
  -H 'Postman-Token: 8e0bc75f-58c8-48fe-869a-0535f6385590,b98e9443-bf6d-4b12-be03-bf580231fa38' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'content-length: 581' \
  -H 'token: 76f95ffa-fc1b-4eb6-a503-75760185f2a5' \
  -d '{
"sourceIP": "172.24.33.10",
 "sourcePort": None,
 "sourceGateway": {
 	"type": "Device Interface",
    "gatewayName": "BJ_L2_test_1.Vlan10(172.24.33.10)",
    "payload": "{"ip": "172.24.33.10", "endPointInfo": {"deviceId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce", "interfaceId": "9a40c2e8-12ba-4556-bb2f-9545f776afb7"}, "device": "BJ_L2_test_1", "deviceId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce", "interface": "Vlan10", "interfaceId": "9a40c2e8-12ba-4556-bb2f-9545f776afb7", "prefixLen": 26}"},
 "destIP": "172.24.33.135",
 "destPort": 0,
 "protocol": 4,
 "isLive": True	
}'
```

# Step 3 - Get Path Calculation OverView
=======================================================================================================================

## ***GET*** /V1/CMDB/Path/Calculation/{taskID}/OverView	
Call this API to get the hop information of a path calculated through the CalcPath API. 

If the Calculation Path task is not finished yet or failed, user will get an error with messsage reminding.which means you don't need to wait anymore before trying to query the result.

All directed links in the result consists of a directed path grapth, which contains all possible reachable paths from the original source to the destination specified in path calculation

## Detail Information

> **Title** : Get Path Calculation OverView API<br>

> **Version** : 06/27/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Path/Calculation/{taskID}/OverView	

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
|taskID* | string  | Input the task ID returned by the CalcPath API. |

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
| path_overview | list of Object | A list of path_list.|
| path_list | list of Object | A list of path.|
| branch_list | list of Object | A list of branch.|
| hop_detail_list | list of Object | A list of hop with hop detail information.|
| fromDev | Object | Detail information of source device. |
| devId | string | ID of source device. |
| devName | string | Hostname of source device. |
| devType | integer | Type of source device. |
| fromIntf | Object | The detail information of source device interface. |
| hopId | string | The ID of current hop. |
| failure_reason | string | Explanation of the failure path. |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
{
    "path_overview": [
        {
            "path_list": [
                {
                    "branch_list": [
                        {
                            "hop_detail_list": [
                                {
                                    "fromDev": {
                                        "devId": "101deae6-8d11-47d2-b87f-b69cbe7ba2ce",
                                        "devName": "BJ_L2_test_1",
                                        "devType": 2001,
                                        "domainId": ""
                                    },
                                    "fromIntf": {
                                        "intfKeyObj": {
                                            "schema": "",
                                            "value": ""
                                        },
                                        "intfDisplaySchemaObj": {
                                            "schema": "",
                                            "value": ""
                                        },
                                        "PhysicalInftName": ""
                                    },
                                    "hopId": "66ca008f-eb89-4f92-a5c2-d2d6e545ba10",
                                    "isComplete": false,
                                    "isP2P": false,
                                    "mediaId": "",
                                    "mediaInfo": {
                                        "mediaName": "",
                                        "mediaType": "",
                                        "neat": false,
                                        "topoType": ""
                                    },
                                    "preHopId": "00000000-0000-0000-0000-000000000000",
                                    "sequnce": 0,
                                    "toIntf": {
                                        "intfKeyObj": {
                                            "schema": "",
                                            "value": ""
                                        },
                                        "intfDisplaySchemaObj": {
                                            "schema": "",
                                            "value": ""
                                        },
                                        "PhysicalInftName": ""
                                    },
                                    "toDev": {
                                        "devId": "",
                                        "devName": "",
                                        "devType": 0,
                                        "domainId": ""
                                    },
                                    "topoType": "",
                                    "trafficState": {
                                        "acl": "",
                                        "alg": -1,
                                        "dev_name": "BJ_L2_test_1",
                                        "dev_type": 2001,
                                        "in_intf": "Vlan10",
                                        "in_intf_schema": "intfs",
                                        "in_intf_topo_type": "L3_Topo_Type",
                                        "next_dev_in_intf": "",
                                        "next_dev_in_intf_schema": "",
                                        "next_dev_in_intf_topo_type": "L3_Topo_Type",
                                        "next_dev_name": "",
                                        "next_dev_type": 0,
                                        "next_hop_ip": "",
                                        "next_hop_mac": "",
                                        "out_intf": "",
                                        "out_intf_schema": "",
                                        "out_intf_topo_type": "L3_Topo_Type",
                                        "pbr": "",
                                        "vrf": ""
                                    },
                                    "parentHopId": ""
                                }
                            ],
                            "failure_reason": "No next hop IP and output interface were found",
                            "status": "Failed"
                        }
                    ],
                    "failure_reasons": [],
                    "path_name": "L3 Path",
                    "description": "10.4.40.21 -> 10.4.40.213",
                    "status": "Failed"
                }
            ],
            "failure_reasons": [],
            "status": "Failed"
        }
    ],
    "statusCode": 794008,
    "statusDescription": "Task '09e2acd2-d684-44b0-b035-3563d14e8150' is failed"
}
```

## Full Example:


```python
Get_Path_Calulation_Result_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation/" + str(res["taskID"]) + "/OverView"

def get_patth_result(Get_Path_Calulation_Result_url, headers, token):
    headers["Token"] = token
    try:
        response = requests.get(Get_Path_Calulation_Result_url, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return (response)

    except Exception as e:
        return (str(e)) 

final = get_patth_result(Get_Path_Calulation_Result_url, headers, token)
final
```




    {'path_overview': [{'path_list': [{'branch_list': [{'hop_detail_list': [{'fromDev': {'devId': '101deae6-8d11-47d2-b87f-b69cbe7ba2ce',
              'devName': 'BJ_L2_test_1',
              'devType': 2001,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': 'ipIntfs._id',
               'value': '3c8adda5-c8ca-41c6-92fd-81218df0e273'},
              'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
               'value': 'Vlan10 172.24.33.10/26'},
              'PhysicalInftName': 'Vlan10'},
             'hopId': 'abbd9aa7-a22f-4a5a-b1c3-a7b7a2f5838d',
             'isComplete': False,
             'isP2P': False,
             'mediaId': 'a9e00aa8-1c64-4339-b0a7-1554032826fb',
             'mediaInfo': {'mediaName': '172.24.33.0/26',
              'mediaType': 'Lan',
              'neat': True,
              'topoType': 'L3_Topo_Type'},
             'preHopId': '00000000-0000-0000-0000-000000000000',
             'sequnce': 0,
             'toIntf': {'intfKeyObj': {'schema': 'ipIntfs._id',
               'value': 'da224866-5457-4b8b-82ee-4aceda586439'},
              'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
               'value': 'FastEthernet0/1 172.24.33.1/26'},
              'PhysicalInftName': 'FastEthernet0/1'},
             'toDev': {'devId': '51cdcf63-1cee-4e14-b5cd-e4698e7ccca8',
              'devName': 'LA.DIS,1',
              'devType': 2,
              'domainId': ''},
             'topoType': 'L3_Topo_Type',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'BJ_L2_test_1',
              'dev_type': 2001,
              'in_intf': 'Vlan10',
              'in_intf_schema': 'intfs',
              'in_intf_topo_type': 'L3_Topo_Type',
              'next_dev_in_intf': 'FastEthernet0/1 172.24.33.1/26',
              'next_dev_in_intf_schema': 'ipIntfs',
              'next_dev_in_intf_topo_type': 'L3_Topo_Type',
              'next_dev_name': 'LA.DIS,1',
              'next_dev_type': 2,
              'next_hop_ip': '172.24.33.1',
              'next_hop_mac': '',
              'out_intf': 'Vlan10 172.24.33.10/26',
              'out_intf_schema': 'ipIntfs',
              'out_intf_topo_type': 'L3_Topo_Type',
              'pbr': '',
              'vrf': ''},
             'parentHopId': ''},
            {'fromDev': {'devId': '51cdcf63-1cee-4e14-b5cd-e4698e7ccca8',
              'devName': 'LA.DIS,1',
              'devType': 2,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': 'ipIntfs._id',
               'value': '2d5152f7-49f1-485a-9e2f-df52d2b09f2b'},
              'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
               'value': 'FastEthernet0/0 172.24.32.66/26'},
              'PhysicalInftName': 'FastEthernet0/0'},
             'hopId': '399f9956-b2aa-4369-8721-5d39b1e8c515',
             'isComplete': False,
             'isP2P': False,
             'mediaId': '918e7d9a-6c19-45c5-8b8c-aaca3771b326',
             'mediaInfo': {'mediaName': '172.24.32.64/26',
              'mediaType': 'Lan',
              'neat': True,
              'topoType': 'L3_Topo_Type'},
             'preHopId': 'abbd9aa7-a22f-4a5a-b1c3-a7b7a2f5838d',
             'sequnce': 1,
             'toIntf': {'intfKeyObj': {'schema': 'ipIntfs._id',
               'value': '03d429e3-0dd7-4023-9b41-8e78f74ba0fb'},
              'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
               'value': 'Ethernet1/2 172.24.32.65/26'},
              'PhysicalInftName': 'Ethernet1/2'},
             'toDev': {'devId': '89fccb2d-c833-4c76-a995-2aa429932a47',
              'devName': 'LA_POP',
              'devType': 2,
              'domainId': ''},
             'topoType': 'L3_Topo_Type',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'LA.DIS,1',
              'dev_type': 2,
              'in_intf': 'FastEthernet0/1 172.24.33.1/26',
              'in_intf_schema': 'ipIntfs',
              'in_intf_topo_type': 'L3_Topo_Type',
              'next_dev_in_intf': 'Ethernet1/2 172.24.32.65/26',
              'next_dev_in_intf_schema': 'ipIntfs',
              'next_dev_in_intf_topo_type': 'L3_Topo_Type',
              'next_dev_name': 'LA_POP',
              'next_dev_type': 2,
              'next_hop_ip': '172.24.32.65',
              'next_hop_mac': '',
              'out_intf': 'FastEthernet0/0 172.24.32.66/26',
              'out_intf_schema': 'ipIntfs',
              'out_intf_topo_type': 'L3_Topo_Type',
              'pbr': '',
              'vrf': ''},
             'parentHopId': ''},
            {'fromDev': {'devId': '89fccb2d-c833-4c76-a995-2aa429932a47',
              'devName': 'LA_POP',
              'devType': 2,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': 'ipIntfs._id',
               'value': '3d8e2c36-0485-4af5-82df-dadffe8f9fbc'},
              'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
               'value': 'Ethernet1/3 172.24.32.6/30'},
              'PhysicalInftName': 'Ethernet1/3'},
             'hopId': '7bc8cdd5-a6ad-4c32-9a1b-50da70750c50',
             'isComplete': False,
             'isP2P': False,
             'mediaId': '84ab7215-24a6-42e5-8277-03bb2a0756e3',
             'mediaInfo': {'mediaName': '172.24.32.4/30',
              'mediaType': 'Lan',
              'neat': True,
              'topoType': 'L3_Topo_Type'},
             'preHopId': '399f9956-b2aa-4369-8721-5d39b1e8c515',
             'sequnce': 2,
             'toIntf': {'intfKeyObj': {'schema': 'ipIntfs._id',
               'value': '5f1a7df0-fdae-487a-986a-41ba064745a3'},
              'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
               'value': 'Ethernet1 172.24.32.5/30'},
              'PhysicalInftName': 'Ethernet1'},
             'toDev': {'devId': '15c3ed98-38ea-44a7-8002-db6a58653fa2',
              'devName': 'BST,POP1',
              'devType': 2,
              'domainId': ''},
             'topoType': 'L3_Topo_Type',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'LA_POP',
              'dev_type': 2,
              'in_intf': 'Ethernet1/2 172.24.32.65/26',
              'in_intf_schema': 'ipIntfs',
              'in_intf_topo_type': 'L3_Topo_Type',
              'next_dev_in_intf': 'Ethernet1 172.24.32.5/30',
              'next_dev_in_intf_schema': 'ipIntfs',
              'next_dev_in_intf_topo_type': 'L3_Topo_Type',
              'next_dev_name': 'BST,POP1',
              'next_dev_type': 2,
              'next_hop_ip': '172.24.32.5',
              'next_hop_mac': '',
              'out_intf': 'Ethernet1/3 172.24.32.6/30',
              'out_intf_schema': 'ipIntfs',
              'out_intf_topo_type': 'L3_Topo_Type',
              'pbr': '',
              'vrf': ''},
             'parentHopId': ''},
            {'fromDev': {'devId': '15c3ed98-38ea-44a7-8002-db6a58653fa2',
              'devName': 'BST,POP1',
              'devType': 2,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': '', 'value': ''},
              'intfDisplaySchemaObj': {'schema': '', 'value': ''},
              'PhysicalInftName': ''},
             'hopId': 'f28a67e6-6703-4d1c-9e07-34bb2015935b',
             'isComplete': False,
             'isP2P': False,
             'mediaId': '',
             'mediaInfo': {'mediaName': '',
              'mediaType': '',
              'neat': False,
              'topoType': ''},
             'preHopId': '7bc8cdd5-a6ad-4c32-9a1b-50da70750c50',
             'sequnce': 3,
             'toIntf': {'intfKeyObj': {'schema': '', 'value': ''},
              'intfDisplaySchemaObj': {'schema': '', 'value': ''},
              'PhysicalInftName': ''},
             'toDev': {'devId': '', 'devName': '', 'devType': 0, 'domainId': ''},
             'topoType': '',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'BST,POP1',
              'dev_type': 2,
              'in_intf': 'Ethernet1 172.24.32.5/30',
              'in_intf_schema': 'ipIntfs',
              'in_intf_topo_type': 'L3_Topo_Type',
              'next_dev_in_intf': '',
              'next_dev_in_intf_schema': '',
              'next_dev_in_intf_topo_type': '',
              'next_dev_name': '',
              'next_dev_type': 0,
              'next_hop_ip': '',
              'next_hop_mac': '',
              'out_intf': '',
              'out_intf_schema': '',
              'out_intf_topo_type': '',
              'pbr': '',
              'vrf': ''},
             'parentHopId': ''}],
           'failure_reason': '',
           'status': 'Success'}],
         'failure_reasons': [],
         'path_name': 'L3 Path',
         'description': '172.24.33.10 -> 172.24.33.135',
         'status': 'Success'},
        {'branch_list': [{'hop_detail_list': [{'fromDev': {'devId': '101deae6-8d11-47d2-b87f-b69cbe7ba2ce',
              'devName': 'BJ_L2_test_1',
              'devType': 2001,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': 'intfs._id',
               'value': 'fd63e0b2-4c6d-4f85-8808-b8380c7de60a'},
              'intfDisplaySchemaObj': {'schema': 'intfs.name',
               'value': 'FastEthernet1/0/2'},
              'PhysicalInftName': 'FastEthernet1/0/2'},
             'hopId': '154aa600-b590-46d2-ab17-7a47d5527cba',
             'isComplete': False,
             'isP2P': True,
             'mediaId': '',
             'mediaInfo': {'mediaName': '',
              'mediaType': '',
              'neat': False,
              'topoType': ''},
             'preHopId': '00000000-0000-0000-0000-000000000000',
             'sequnce': 0,
             'toIntf': {'intfKeyObj': {'schema': 'intfs._id',
               'value': '159dbd17-4dbf-4666-b903-bfae6dc40937'},
              'intfDisplaySchemaObj': {'schema': 'intfs.name',
               'value': 'FastEthernet0/1'},
              'PhysicalInftName': 'FastEthernet0/1'},
             'toDev': {'devId': '51cdcf63-1cee-4e14-b5cd-e4698e7ccca8',
              'devName': 'LA.DIS,1',
              'devType': 2,
              'domainId': ''},
             'topoType': 'L2_Topo_Type',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'BJ_L2_test_1',
              'dev_type': 2001,
              'in_intf': '',
              'in_intf_schema': '',
              'in_intf_topo_type': '',
              'next_dev_in_intf': 'FastEthernet0/1',
              'next_dev_in_intf_schema': 'intfs',
              'next_dev_in_intf_topo_type': 'L2_Topo_Type',
              'next_dev_name': 'LA.DIS,1',
              'next_dev_type': 2,
              'next_hop_ip': '',
              'next_hop_mac': '',
              'out_intf': 'FastEthernet1/0/2',
              'out_intf_schema': 'intfs',
              'out_intf_topo_type': 'L2_Topo_Type',
              'pbr': '',
              'vrf': ''},
             'parentHopId': 'abbd9aa7-a22f-4a5a-b1c3-a7b7a2f5838d'},
            {'fromDev': {'devId': '51cdcf63-1cee-4e14-b5cd-e4698e7ccca8',
              'devName': 'LA.DIS,1',
              'devType': 2,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': '', 'value': ''},
              'intfDisplaySchemaObj': {'schema': '', 'value': ''},
              'PhysicalInftName': ''},
             'hopId': '7b79630e-88e3-420e-97ec-1c27053db1e6',
             'isComplete': False,
             'isP2P': False,
             'mediaId': '',
             'mediaInfo': {'mediaName': '',
              'mediaType': '',
              'neat': False,
              'topoType': ''},
             'preHopId': '154aa600-b590-46d2-ab17-7a47d5527cba',
             'sequnce': 1,
             'toIntf': {'intfKeyObj': {'schema': '', 'value': ''},
              'intfDisplaySchemaObj': {'schema': '', 'value': ''},
              'PhysicalInftName': ''},
             'toDev': {'devId': '', 'devName': '', 'devType': 0, 'domainId': ''},
             'topoType': '',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'LA.DIS,1',
              'dev_type': 2,
              'in_intf': 'FastEthernet0/1',
              'in_intf_schema': 'intfs',
              'in_intf_topo_type': 'L2_Topo_Type',
              'next_dev_in_intf': '',
              'next_dev_in_intf_schema': '',
              'next_dev_in_intf_topo_type': '',
              'next_dev_name': '',
              'next_dev_type': 0,
              'next_hop_ip': '',
              'next_hop_mac': '',
              'out_intf': '',
              'out_intf_schema': '',
              'out_intf_topo_type': '',
              'pbr': '',
              'vrf': ''},
             'parentHopId': 'abbd9aa7-a22f-4a5a-b1c3-a7b7a2f5838d'}],
           'failure_reason': '',
           'status': 'Success'}],
         'failure_reasons': [],
         'path_name': 'L2 Path',
         'description': '172.24.33.10 -> 172.24.33.1',
         'status': 'Success'},
        {'branch_list': [{'hop_detail_list': [{'fromDev': {'devId': '51cdcf63-1cee-4e14-b5cd-e4698e7ccca8',
              'devName': 'LA.DIS,1',
              'devType': 2,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': 'intfs._id',
               'value': 'e68afa28-40ca-496d-a7e3-785bf07f689a'},
              'intfDisplaySchemaObj': {'schema': 'intfs.name',
               'value': 'FastEthernet0/0'},
              'PhysicalInftName': 'FastEthernet0/0'},
             'hopId': '927e9bd0-dbef-4850-81bb-3ceec7a7fc61',
             'isComplete': False,
             'isP2P': True,
             'mediaId': '',
             'mediaInfo': {'mediaName': '',
              'mediaType': '',
              'neat': False,
              'topoType': ''},
             'preHopId': '00000000-0000-0000-0000-000000000000',
             'sequnce': 0,
             'toIntf': {'intfKeyObj': {'schema': 'intfs._id',
               'value': '44bc0c0f-3e12-47a8-b53a-9dc1e59d5f17'},
              'intfDisplaySchemaObj': {'schema': 'intfs.name',
               'value': 'Ethernet1/2'},
              'PhysicalInftName': 'Ethernet1/2'},
             'toDev': {'devId': '89fccb2d-c833-4c76-a995-2aa429932a47',
              'devName': 'LA_POP',
              'devType': 2,
              'domainId': ''},
             'topoType': 'L2_Topo_Type',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'LA.DIS,1',
              'dev_type': 2,
              'in_intf': '',
              'in_intf_schema': '',
              'in_intf_topo_type': '',
              'next_dev_in_intf': 'Ethernet1/2',
              'next_dev_in_intf_schema': 'intfs',
              'next_dev_in_intf_topo_type': 'L2_Topo_Type',
              'next_dev_name': 'LA_POP',
              'next_dev_type': 2,
              'next_hop_ip': '',
              'next_hop_mac': '',
              'out_intf': 'FastEthernet0/0',
              'out_intf_schema': 'intfs',
              'out_intf_topo_type': 'L2_Topo_Type',
              'pbr': '',
              'vrf': ''},
             'parentHopId': '399f9956-b2aa-4369-8721-5d39b1e8c515'},
            {'fromDev': {'devId': '89fccb2d-c833-4c76-a995-2aa429932a47',
              'devName': 'LA_POP',
              'devType': 2,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': '', 'value': ''},
              'intfDisplaySchemaObj': {'schema': '', 'value': ''},
              'PhysicalInftName': ''},
             'hopId': '2562a33f-12b3-4a1d-b3ba-5104ae2bffa2',
             'isComplete': False,
             'isP2P': False,
             'mediaId': '',
             'mediaInfo': {'mediaName': '',
              'mediaType': '',
              'neat': False,
              'topoType': ''},
             'preHopId': '927e9bd0-dbef-4850-81bb-3ceec7a7fc61',
             'sequnce': 1,
             'toIntf': {'intfKeyObj': {'schema': '', 'value': ''},
              'intfDisplaySchemaObj': {'schema': '', 'value': ''},
              'PhysicalInftName': ''},
             'toDev': {'devId': '', 'devName': '', 'devType': 0, 'domainId': ''},
             'topoType': '',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'LA_POP',
              'dev_type': 2,
              'in_intf': 'Ethernet1/2',
              'in_intf_schema': 'intfs',
              'in_intf_topo_type': 'L2_Topo_Type',
              'next_dev_in_intf': '',
              'next_dev_in_intf_schema': '',
              'next_dev_in_intf_topo_type': '',
              'next_dev_name': '',
              'next_dev_type': 0,
              'next_hop_ip': '',
              'next_hop_mac': '',
              'out_intf': '',
              'out_intf_schema': '',
              'out_intf_topo_type': '',
              'pbr': '',
              'vrf': ''},
             'parentHopId': '399f9956-b2aa-4369-8721-5d39b1e8c515'}],
           'failure_reason': '',
           'status': 'Success'}],
         'failure_reasons': [],
         'path_name': 'L2 Path',
         'description': '172.24.32.66 -> 172.24.32.65',
         'status': 'Success'},
        {'branch_list': [{'hop_detail_list': [{'fromDev': {'devId': '89fccb2d-c833-4c76-a995-2aa429932a47',
              'devName': 'LA_POP',
              'devType': 2,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': 'intfs._id',
               'value': '12a49a85-6ee6-46cd-94fc-21db1951d647'},
              'intfDisplaySchemaObj': {'schema': 'intfs.name',
               'value': 'Ethernet1/3'},
              'PhysicalInftName': 'Ethernet1/3'},
             'hopId': '503c354b-49cc-4351-bb04-df9b03efe2b7',
             'isComplete': False,
             'isP2P': True,
             'mediaId': '',
             'mediaInfo': {'mediaName': '',
              'mediaType': '',
              'neat': False,
              'topoType': ''},
             'preHopId': '00000000-0000-0000-0000-000000000000',
             'sequnce': 0,
             'toIntf': {'intfKeyObj': {'schema': 'intfs._id',
               'value': '955c2be9-8924-4cd5-9e99-857869815099'},
              'intfDisplaySchemaObj': {'schema': 'intfs.name',
               'value': 'Ethernet1'},
              'PhysicalInftName': 'Ethernet1'},
             'toDev': {'devId': '15c3ed98-38ea-44a7-8002-db6a58653fa2',
              'devName': 'BST,POP1',
              'devType': 2,
              'domainId': ''},
             'topoType': 'L2_Topo_Type',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'LA_POP',
              'dev_type': 2,
              'in_intf': '',
              'in_intf_schema': '',
              'in_intf_topo_type': '',
              'next_dev_in_intf': 'Ethernet1',
              'next_dev_in_intf_schema': 'intfs',
              'next_dev_in_intf_topo_type': 'L2_Topo_Type',
              'next_dev_name': 'BST,POP1',
              'next_dev_type': 2,
              'next_hop_ip': '',
              'next_hop_mac': '',
              'out_intf': 'Ethernet1/3',
              'out_intf_schema': 'intfs',
              'out_intf_topo_type': 'L2_Topo_Type',
              'pbr': '',
              'vrf': ''},
             'parentHopId': '7bc8cdd5-a6ad-4c32-9a1b-50da70750c50'},
            {'fromDev': {'devId': '15c3ed98-38ea-44a7-8002-db6a58653fa2',
              'devName': 'BST,POP1',
              'devType': 2,
              'domainId': ''},
             'fromIntf': {'intfKeyObj': {'schema': '', 'value': ''},
              'intfDisplaySchemaObj': {'schema': '', 'value': ''},
              'PhysicalInftName': ''},
             'hopId': 'eade8bd5-6bee-48ff-99ac-1274306e9d37',
             'isComplete': False,
             'isP2P': False,
             'mediaId': '',
             'mediaInfo': {'mediaName': '',
              'mediaType': '',
              'neat': False,
              'topoType': ''},
             'preHopId': '503c354b-49cc-4351-bb04-df9b03efe2b7',
             'sequnce': 1,
             'toIntf': {'intfKeyObj': {'schema': '', 'value': ''},
              'intfDisplaySchemaObj': {'schema': '', 'value': ''},
              'PhysicalInftName': ''},
             'toDev': {'devId': '', 'devName': '', 'devType': 0, 'domainId': ''},
             'topoType': '',
             'trafficState': {'acl': '',
              'alg': -1,
              'dev_name': 'BST,POP1',
              'dev_type': 2,
              'in_intf': 'Ethernet1',
              'in_intf_schema': 'intfs',
              'in_intf_topo_type': 'L2_Topo_Type',
              'next_dev_in_intf': '',
              'next_dev_in_intf_schema': '',
              'next_dev_in_intf_topo_type': '',
              'next_dev_name': '',
              'next_dev_type': 0,
              'next_hop_ip': '',
              'next_hop_mac': '',
              'out_intf': '',
              'out_intf_schema': '',
              'out_intf_topo_type': '',
              'pbr': '',
              'vrf': ''},
             'parentHopId': '7bc8cdd5-a6ad-4c32-9a1b-50da70750c50'}],
           'failure_reason': '',
           'status': 'Success'}],
         'failure_reasons': [],
         'path_name': 'L2 Path',
         'description': '172.24.32.6 -> 172.24.32.5',
         'status': 'Success'}],
       'failure_reasons': [],
       'status': 'Success'}],
     'statusCode': 790200,
     'statusDescription': 'Success.'}



## cURL Code from Postman


```python
curl -X GET \
  http://192.168.28.173/ServicesAPI/API/V1/CMDB/Path/Calculation/dcf25655-81a9-4cfe-82ca-aef80a698971/OverView \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 192.168.28.173' \
  -H 'Postman-Token: b0cd60b6-d29d-4665-9469-8969c925ee92,c4d2df42-2573-402b-8327-174c45ee1356' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'token: db5757cb-aaa6-4efb-ad25-ce4918def0ce'
```
