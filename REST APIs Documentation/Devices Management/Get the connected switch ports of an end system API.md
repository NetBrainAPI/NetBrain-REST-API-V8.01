
# Device API Design

## ***GET*** /V1/CMDB/Topology/Devices/{ip}/ConnectedSwitchPort
Use this API to get the connected layer 2 switch ports of an end system.

## Detail Information

> **Title** : Get the connected switch ports of an end system<br>

> **Version** : 06/05/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API//V1/CMDB/Topology/Devices/{ip}/ConnectedSwitchPort

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 


## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|ip* | string  | The IP address of an end system.  |

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
|hostname| string | The hostname of the device that the end system connects to. |
|interface| string | The interface that the end system connects to. |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***



```python
{
    "statusCode": 790200,
    "statusDescription": "success",
    "hostname": "Bos-SW",
    "interface": "Ethernet 0/1"
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
token = "ba6b63c6-5703-4549-9145-XXXXXXXXXXXX"
nb_url = "http://unity.netbraintech.com"
ip = "10.8.3.130"

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Topology/Devices/" + str(ip) + "/ConnectedSwitchPort"

try:
    response = requests.get(full_url, headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get connected switch ports failed! - " + str(response.text))

except Exception as e:
    print (str(e))   
```

    {'hostname': 'CA-TOR-SW1', 'interface': 'Ethernet0', 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X GET \
  http://unity.netbraintech.com/ServicesAPI/API/V1/CMDB/Topology/Devices/10.8.3.130/ConnectedSwitchPort \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: unity.netbraintech.com' \
  -H 'Postman-Token: e0ac94df-e9d9-416e-8061-bd26b364b7b4,7174ad61-31d7-4050-b697-0ec7fec43195' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'token: ba6b63c6-5703-4549-9145-baefc22183de'
```
