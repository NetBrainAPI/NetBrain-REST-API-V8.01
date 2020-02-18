
# Trigger Map API Design

## ***POST*** /V1/Triggers/Run
Call this API to trigger a map built by Netbrain from third part software.

## Detail Information

> **Title** : Trigger Map And Path API<br>

> **Version** : 02/08/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/Triggers/Run

> **Authentication** : 

>| Type | In | Name |
|---|---|---|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

>|**Name**|**Type**|**Description**|
|---|---|---|
|domain_setting.tenant_id* | string  | Tenant Id  |
|domain_setting.domain_id* | string  | Domain Id  |
|basic_setting.triggered_by* | string  | Trigger user |
|basic_setting.user_id | string  | User Id，Not required |
|basic_setting.user* | string  | User Name |
|basic_setting.device* | string  | Device Name  |
|basic_setting.interface | string  | Interface Name，Not required  |
|basic_setting.stub_name* | string  | Stub Name  |
|basic_setting.stub_setting | object  | Stub Setting Information  |
|basic_setting.stub_setting.mode | int  | Triggered Type.<br> 0: Real-Time,<br> 1: On-Demand  |
|map_setting | object  | Map Setting Information  |
|map_setting.map_create_mode | int  | Create Map Mode.<br>0: Map Device and Its Neighbors.<br>1: Open Site Map of the Device.<br>2: Open Existing Map.<br>3: Map a Path.<br>4: Create an Empty Map.  |
|map_setting.map_open_para | object  | parameters of opening exist map  |
|map_setting.map_open_para.map_id| string  | map Id |
|map_setting.map_open_para.site_id | string  | Site Id  |
|map_setting.map_open_para.device_group_id | string  | Device Group Id  |
| map_setting.map_open_para.duplicate_map | bool | duplicate flag |


```python
body = {
    "domain_setting": {
        "tenant_id": "", # can not be null.
        "domain_id": ""  # can not be null.
    },
    "basic_setting": {
        "triggered_by": "", # can not be null.
        "user_id": "",
        "user": "", # can not be null.
        "device": "", # can not be null.
        "interface": "",
        "stub_name": "", # can not be null.
        "stub_setting": {
            "mode": 0,
            "max_waiting_hours": 1
        }
    },
    "map_setting": {
        "map_create_mode": 2, 
        "map_open_para": {
            "map_id": "XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX", #
            "site_id": "",
            "device_group_id": "",
            "duplicate_map": ""
        }
    }
}
```

## Path Parameters(****required***)

> No required parameters.

## Headers

> **Data Format Headers**

> |**Name**|**Type**|**Description**|
|---|---|---|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

> |**Name**|**Type**|**Description**|
|---|---|---|
| token | string  | Authentication token, get from login API. |

## Response

>|**Name**|**Type**|**Description**|
|---|---|---|
|mapId| string | The ID of the map which users triggered from third party sofware.  |
|mapName| string | The name of the map. |
|mapType| string | Create Map Mode.<br>0: Map Device and Its Neighbors.<br>1: Open Site Map of the Device.<br>2: Open Existing Map.<br>3: Map a Path.<br>4: Create an Empty Map.  |
|mapUrl| string | The URL link of the map triggered by users.  |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
{
    'mapId': '5edcf486-108c-63e8-5c30-a6d32941d576',
    'mapName': 'APIExisting',
    'mapType': 1,
    'mapUrl': 'map.html?t=40e0032e-14e7-4fea-7d00-8fe8bd65efae&d=b924c2f0-7210-43ba-9cdd-d1757ae23742&id=5edcf486-108c-63e8-5c30-a6d32941d576&maptype=1',
    'stubName': 'APITest'
}
```


```python
import requests
import json
import time
import requests.packages.urllib3 as urllib3
 
urllib3.disable_warnings()

token = "a2f45b2b-c7bf-43bf-9938-4d3d456b0264"
host_url = "https://integrationlab.netbraintech.com/"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

API_Body = {
    "domain_setting": {
        "tenant_id": "40e0032e-14e7-4fea-7d00-8fe8bd65efae",
        "domain_id": "b924c2f0-7210-43ba-9cdd-d1757ae23742"
    },
    "basic_setting": {
        "triggered_by": "Netbrain",
        "user_id": "admin",
        "user": "gongdai.liu",
#         "device": "R1",
#         "interface": "Ethernet2/0.100",
        "stub_name": "APITest",
#         "stub_setting": {
#             "mode": 0,
#             "max_waiting_hours": 1
#         }
    },
    "map_setting": {
        "map_create_mode": 2,
        "map_open_para": {
#             "map_id": "2ca17e26-e942-0147-85eb-e3652a71e19f",
#             "site_id": "",
#             "device_group_id": "",
#             "duplicate_map": ""
        }
    }
}
    
    
    
# Trigger API function
def TriggerTask(API_Body):
 
    # Trigger  API url
    API_URL = r"/ServicesAPI/API/V1/Triggers/Run"
    # Trigger API payload
 
    api_full_url = host_url + API_URL
    api_result = requests.post(api_full_url, data=json.dumps(
        API_Body), headers=headers, verify=False)
    if api_result.status_code == 200:
        return api_result.json()
    else:
        return api_result.json()
    
result = TriggerTask(API_Body)
result
```




    {'mapId': '2ca17e26-e942-0147-85eb-e3652a71e19f',
     'mapName': 'CXL Lab',
     'mapType': 1,
     'mapUrl': 'map.html?t=40e0032e-14e7-4fea-7d00-8fe8bd65efae&d=b924c2f0-7210-43ba-9cdd-d1757ae23742&id=2ca17e26-e942-0147-85eb-e3652a71e19f&maptype=1',
     'stubName': 'APITest'}



# cURL Code from Postman:


```python
curl --location --request POST 'https://integrationlab.netbraintech.com/ServicesAPI/API/V1/Triggers/Run' \
--header 'token: a2f45b2b-c7bf-43bf-9938-4d3d456b0264' \
--header 'Content-Type: application/json' \
--data-raw '{
    "domain_setting": {
        "tenant_id": "40e0032e-14e7-4fea-7d00-8fe8bd65efae",
        "domain_id": "b924c2f0-7210-43ba-9cdd-d1757ae23742"
    },
    "basic_setting": {
        "triggered_by": "Netbrain",
        "user_id": "admin",
        "user": "gongdai.liu",
        "device": "US-BOS-R1",
        "stub_name": "APITest",
        "stub_setting": {
            "mode": 0,
            "max_waiting_hours": 1
        }
    },
    "map_setting": {
        "map_create_mode": 2,
        "map_open_para": {
            "map_id": "",
            "site_id": "",
            "device_group_id": "",
            "duplicate_map": ""
        }
    }
}'
```
