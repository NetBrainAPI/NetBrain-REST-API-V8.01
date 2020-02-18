
# Trigger Map API Design

## ***POST*** /V1/Triggers/Run
Call this API to trigger a map built by Netbrain from third part software.

## Detail Information

> **Title** : Trigger Map And Path API<br>

> **Version** : 02/08/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/Triggers/Run

> **Authentication** : 

| Type | In | Name |
|---|---|---|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
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
|basic_setting.stub_setting.max_waiting_hours | int  | If wait time exceeds the int hours, then change task to On-demand mode.   |
|map_setting | object  | Map Setting Information  |
|map_setting.map_create_mode | int  | Create Map Mode.<br>0: Map Device and Its Neighbors.<br>1: Open Site Map of the Device.<br>2: Open Existing Map.<br>3: Map a Path.<br>4: Create an Empty Map.  |
|map_setting.map_open_para | object  | parameters of opening exist map  |
|map_setting.map_open_para.map_id| string  | map Id |
|map_setting.map_open_para.site_id | string  | Site Id  |
|map_setting.map_open_para.device_group_id | string  | Device Group Id  |
| map_setting.map_open_para.duplicate_map | bool | duplicate flag |
| map_setting.map_device_para | object | device parameters for creating map |
| map_setting.map_device_para.device | string | device name |
| map_setting.map_device_para.include_neighbor | bool | include neighbor flag |
| map_setting.map_device_para.interfaces | list | interface name list |
| map_setting.map_device_para.neighbor_type | string | topo Link type id |
| map_setting.map_device_sitemap_para | object | device site map |
| map_setting.map_device_sitemap_para.device | string | device name |
| map_setting.map_device_sitemap_para.duplicate_map | bool | duplicate map flag |
| map_setting.map_path_para | object | parameters of creating map by path |
| map_setting.map_path_para.source | string | source device name |
| map_setting.map_path_para.source_gateway | string | source gateway |
| map_setting.map_path_para.source_gateway_dev | string | source gateway device name |
| map_setting.map_path_para.source_gateway_intf | string | source gateway interface name |
| map_setting.map_path_para.source_port | string | source port |
| map_setting.map_path_para.destination | string | destination device name |
| map_setting.map_path_para.destination_gateway | string | destination gateway | 
| map_setting.map_path_para.destination_gateway_dev | string | destination gateway device name |
| map_setting.map_path_para.destination_gateway_intf | string | destination gateway interface name |
| map_setting.map_path_para.destination_port | string | destination port |
| map_setting.map_path_para.direction | int | path direction | 
| map_setting.map_path_para.protocol | string | protocol id |
| map_setting.map_path_para.protocol_name | string | protocol name |
| map_setting.map_path_para.isLiveUseBaseLineConfig | bool | whether to use live data or current baseline data during trigger API|
| map_setting.map_path_para.dataSource | object | path run data source |
| map_setting.map_path_para.dataSource.type | int | Run Type<br>1: Live<br>2: Baseline<br>3: Range<br>4: Around |
| map_setting.map_path_para.dataSource.recent | object | null |
| map_setting.map_path_para.dataSource.recent.duration | float | Run duration | 
| map_setting.map_path_para.dataSource.recent.unit | int | Time Unit<br> 1:Hour; 2:Minutes; 3:Second; 4:Day. |
| map_setting.map_path_para.dataSource.range | object | range information |
| map_setting.map_path_para.dataSource.range.start | datetime | start time of range |
| map_setting.map_path_para.dataSource.range.end | datetime | end time of range |
| map_setting.map_path_para.dataSource.around | object | around information |
| map_setting.map_path_para.dataSource.around.time | datetime | time |
| map_setting.map_path_para.dataSource.around.radius | object | radius information |
| map_setting.map_path_para.dataSource.around.radius.duration | float | Run duration |
| map_setting.map_path_para.dataSource.around.radius.unit | int | Time Unit<br> 1:Hour; 2:Minutes; 3:Second; 4:Day. |
|map_setting.map_path_para.advancedOption |object	|advance setting|
|map_setting.map_path_para.advancedOption.debugMode | bool	|The debug mode of trigger API|
|map_setting.map_path_para.advancedOption.calcWhenDeniedByACL| bool	| Whether to keep calculate when the process been denied by ACL|
|map_setting.map_path_para.advancedOption.calcWhenDeniedByPolicy |bool	|Whether to keep calculate when the process been denied by policy|
|map_setting.map_path_para.advancedOption.calcL3ActivePath| bool	||
|map_setting.map_path_para.advancedOption.useCommandsWithArguments| bool	|Whether to use the commands with arguments inside.|
|map_setting.map_path_para.advancedOption.enablePathFixup	|bool	|Whether to enable the path fixup feature.|
| runbook_setting | object | Runbook Setting information |
| runbook_setting.runbookPath | string | runbook path |
| runbook_setting.runbookNodes | list | all runbook nodes |
| runbook_setting.runbookNodes[].enabled | bool | runbook node enable flag |
| runbook_setting.runbookNodes[].runbookNodeId | string | runbook node Id |
| runbook_setting.runbookNodes[].runbookNodeType | int | runbook node type<br>0: Free Texe Node<br>1: Qapp Task Node<br>2: Monitor Task Node<br>4: Ping Task Node<br>5: Trace Task Node<br>7: Benchmark Task Node/Retrieve Live Data<br>13: CliCommand Node<br>17: Path Task Node<br>30: Gapp Task Node |
| runbook_setting.runbookNodes[].useDeviceOnMap | bool | use devices of map or not |
| runbook_setting.runbookNodes[].maxExecutingMins | int | max run minutes of the node |
| runbook_setting.runbookNodes[].runbookNodeSetting | object | setting information of node type |
| CLI_settings | list | CLI Command Node settings information by order |
| CLI_settings[].devices | list | cli command device for the node |
| CLI_settings[].devices[].deviceId | string | device Id |
| CLI_settings[].devices[].deviceName | string | device Name |
| CLI_settings[].retrieveData | object | retrieve setting for cli command of the node |
| CLI_settings[].retrieveData.showCommand | list | show command list |
| retrieve_settings | list | Retrieve Node settings information by order |
| retrieve_settings[].devices | list | retrieve device for the node |
| retrieve_settings[].devices[].deviceId | string | device Id |
| retrieve_settings[].devices[].deviceName | string | device Name |
| retrieve_settings[].retrieveData | object | retrieve setting for retrieve of the node |
| retrieve_settings[].retrieveData.deviceInfo | bool | retrieve device basic info flag |
| retrieve_settings[].retrieveData.interfaceInfo | bool | retrieve device interface info flag |
| retrieve_settings[].retrieveData.config | bool | retrieve config flag |
| retrieve_settings[].retrieveData.macTable | bool | retrieve mac table flag |
| retrieve_settings[].retrieveData.arpTable | bool | retrieve arp table flag |
| retrieve_settings[].retrieveData.nctTable | bool | retrieve nct table flag |
| retrieve_settings[].retrieveData.bgpNbr | bool | retrieve bgp table flag |
| retrieve_settings[].retrieveData.routeTable | bool | retrieve route table flag |
| retrieve_settings[].retrieveData.stpTable | bool | retrieve stp table flag |
| retrieve_settings[].retrieveData.cdpTable | bool | retrieve cdp table flag |
| retrieve_settings[].retrieveData.showCommand | list | show command list |
| ping_settings | list | Ping Node settings information by order |
| ping_settings[].source_type | int | Source Device Type<br>1: NetworkServer<br>2: Device<br>4: IP |
| ping_settings[].source | string | source device name |
| ping_settings[].source_interface | string | source interface name |
| ping_settings[].destination_type | int | destination Device Type<br>1: NetworkServer<br>2: Device<br>4: IP |
| ping_settings[].destination | string | destination device name |
| ping_settings[].destination_interface | string | destination interface name |
| ping_settings[].timeout_seconds | int | time out seconds |
| ping_settings[].packet_bytes | int | package size |
| ping_settings[].packet_count | int | package count |
| ping_settings[].fragment | bool | fragment flag in package |
| tracert_settings | list | Traceroute Node settings information by order |
| tracert_settings[].source_type | int | Source Device Type<br>1: NetworkServer<br>2: Device<br>4: IP |
| tracert_settings[].source | string | source device name |
| tracert_settings[].source_interface | string | sourece interface name |
| tracert_settings[].destination_type | int | destination Device Type<br>1: NetworkServer<br>2: Device<br>4: IP|
| tracert_settings[].destination | string | destination device name |
| tracert_settings[].destination_interface | string | destination interface name |
| tracert_settings[].timeout_seconds | int | time out seconds |
| tracert_settings[].max_hops | int | max hops |

> ***Example:***


```python
# In this cell we provide a full body input, including 6 sub-sections, each sub-section provide different input informations. 
# Although more than one hundred attributes in this body, but fortunately not all of them are required parameters. 

body = {
    
    # Section 1): so far we can consider the first section of input body and all required attributes are labeled. Users can only 
    # provide those six required parameters for calling this API. And if only these six inputs have been provided, the API will 
    # return a dynamic map about neighbors of "device".
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
    
    # Section 2): from the end of section 1) til here, we consider as section 2. If users familiar with Netbrain GUI, we can 
    # we can tottally create four kinds of dynamic maps. Same way, by input an integer value of "map_create_mode" 
    # (0: Map Device and Its Neighbors. 1: Open Site Map of the Device. 2: Open Existing Map. 3: Map a Path. 4: Create an 
    # Empty Map.). We can also provide different maps by calling API. But with different value of "map_create_mode" provided, 
    # different required attribute would be needed in rest of section 2). Check the detail in following steps.
    "map_setting": {
        "map_create_mode": 0,
        "map_open_para": {
            "map_id": "",
            "site_id": "",
            "device_group_id": "",
            "duplicate_map": ""
        },
        "map_device_para": {
            "device": "",
            "include_neighbor": False,
            "interfaces": [""],
            "neighbor_type": ""
        },
        "map_device_sitemap_para": {
            "device": "",
            "duplicate_map": False
        },
        "map_path_para": {
            "source": '',
            "source_gateway": '',
            "source_port": 80,
            "destination": '',
            "destination_gateway": '',
            "destination_port": 80,
            "direction": 1,
            "protocol": 4,
            "isLiveUseBaseLineConfig": True,
            "advancedOption": {
                "debugMode": False,
                "calcL3ActivePath": False,
                "useCommandsWithArguments": False,
                "calcWhenDeniedByACL": False,
                "calcWhenDeniedByPolicy": False,
                "enablePathFixup": True
                 }
            "dataSource": {
                "type": 1,
                "recent": {
                    "unit": 2,
                    "duration": 5
                },
                "range": {
                    "start": "",
                    "end": ""
                },
                "around": {
                    "time": ""
                }
            }
        }
    },
    
    # Section 3) runbook and CLI settings, this section is optional input. 
    "runbook_setting": {}, # Specify runbook template. 
    "CLI_settings": [{
            "retrieveData": {
            "showCommand": ["show version", "show interface"] # Specify out put values.
        }
    }],
    
    # Section 4) retrieve settings, decide what kinds of tables users need.
    "retrieve_settings": [{
        "retrieveData": {
            "macTable": False,
            "arpTable": False,
            "deviceInfo": True,
            "interfaceInfo": True,
            "config": True,
            "bgpNbr": False,
            "routeTable": False,
            "stpTable": False,
            "cdpTable": False,
            "nctTable": ["FabricPath Route Table", "MPLS LFIB"],
            "showCommand": ["show version", "show interface"]
        }
    }],
    
    # Section 5) ping settings, test the connection condition of source device and destination device. Also an optional setting.
    "ping_settings": [{
        "source_type": 2,
        "source": "",
        "source_interface": "",
        "destination": "",
        "destination_interface": "",
        "timeout_seconds": 50,
        "packet_bytes": 50,
        "packet_count": 50,
        "fragment": False
    }],
    
    # Section 6) tracert settings, optional settings.
    "tracert_settings": [{
        "source_type": 2,
        "source": "",
        "source_interface": "",
        "destination": "",
        "destination_interface": "",
        "max_hops": 50
    }]
    
}
```

## Path Parameters(****required***)

> No required parameters.

## Headers

> **Data Format Headers**

|**Name**|**Type**|**Description**|
|---|---|---|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

|**Name**|**Type**|**Description**|
|---|---|---|
| token | string  | Authentication token, get from login API. |

## Response

|**Name**|**Type**|**Description**|
|---|---|---|
|mapId| string | The ID of the map which users triggered from third party sofware.  |
|mapName| string | The name of the map. |
|mapType| string | Create Map Mode.<br>0: Map Device and Its Neighbors.<br>1: Open Site Map of the Device.<br>2: Open Existing Map.<br>3: Map a Path.<br>4: Create an Empty Map.  |
|mapUrl| string | The URL segment which navigates to the map file. This URL segment should be preceeded by the server name (Example "http://192.168.28.79/")  |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
{
    'mapId': '13304db4-6c28-401a-b546-5920b0db7750',
    'mapName': 'stubTest1-20190208211759',
    'mapType': 1,
    'mapUrl': 'map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=13304db4-6c28-401a-b546-5920b0db7750&maptype=1'
}
```

# Full Example:


```python
import requests
import json
import time
import requests.packages.urllib3 as urllib3
 
urllib3.disable_warnings()

token = "c814c66a-87e4-40e7-b85f-27550059b0fa"
host_url = "http://192.168.28.79"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

API_Body = {
    "domain_setting": {
        "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
        "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
    },
    "basic_setting": {
        "triggered_by": "Netbrain",
        "user_id": "admin",
        "user": "gdluserTest",
        "device": "R20",
        "interface": "Ethernet2/0.100",
        "stub_name": "stubTest1",
        "stub_setting": {
            "mode": 0,
            "max_waiting_hours": 1
        }
    },
    
    "CLI_settings": [{
            "retrieveData": {
            "showCommand": ["show version", "show interface"]
        }
    }],
    "retrieve_settings": [{
        "retrieveData": {
            "macTable": True,
            "arpTable": False,
            "deviceInfo": True,
            "interfaceInfo": True,
            "config": True,
            "bgpNbr": False,
            "routeTable": True,
            "stpTable": False,
            "cdpTable": False,
            "nctTable": ["FabricPath Route Table", "MPLS LFIB"],
            "showCommand": ["show version", "show interface"]
        }
    }],
    "ping_settings": [{
        "source_type": 2,
        "source": "R20",
        "source_interface": "Ethernet2/0.100",
        "destination": "123.10.1.6",
        "destination_interface": "Ethernet0/1",
        "timeout_seconds": 50,
        "packet_bytes": 50,
        "packet_count": 50,
        "fragment": False
    }],
    "tracert_settings": [{
        "source_type": 2,
        "source": "R20",
        "source_interface": "Ethernet2/0.100",
        "destination": "123.10.1.6",
        "destination_interface": "Ethernet0/1",
        "max_hops": 50
    }]
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




    {'mapId': '13304db4-6c28-401a-b546-5920b0db7750',
     'mapName': 'stubTest1-20190208211759',
     'mapType': 1,
     'mapUrl': 'map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=13304db4-6c28-401a-b546-5920b0db7750&maptype=1'}



# cURL Code from Postman:


```python
curl -X POST \
  http://192.168.28.79/ServicesAPI/API/V1/Triggers/Run \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 1f9f798a-a558-4a00-a9cc-63dbfc0db5fe' \
  -H 'cache-control: no-cache' \
  -H 'token: 80ef1e2f-5cbc-4b05-a497-b1848ad6740a' \
  -d '{
        "domain_setting": {
            "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
            "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
        },
        "basic_setting": {
            "triggered_by": "Netbrain",
            "user": "gdluserTest",
            "device": "R20",
            "stub_name": "stubTest1"

        }
    }'
```

# Error Examples and Notes:


```python
###################################################################################################################    

"""Error 1: empty and wrong inputs"""

Input: 
        # The minimum required inputs 
        API_Body = {
                        "domain_setting": {
                            "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
                            "domain_id": "0201adc4-ae96-46f0-ae3d"
                        },
                        "basic_setting": {
                            "triggered_by": "",
                            "user": "gdluserTest",
                            "device": "R20",
                            "stub_name": "stubTest1"

                        }
                    }
        
Response:
    
    # Set tenant or domain ID as ""
    {'error': 'tenant_id and domain_id is required.'} 
    # Set tenant or domain ID with a wrong formation or un-exist content.
    {
        'error': 'Tenant or domain id is not found in the system.' 
        'tenant with id: fb24f3f0-81a7-1929-4b8f-99106c23fa5b, domain with id: 0201adc4-ae96-46f0-ae3d'
    }
    
    # Set username as ""
    {'error': 'User name not found'}
    # Set username with an un-exist user account name.
    {'error': 'User name not found'}
    
    # Set device as ""
    {'error': 'The "device" parameter has no argument'}
    # Set device with an un-exist device name.
    {'error': 'Failed to find the designated device R200'}
    
    # Set stub as ""
    {'error': 'The designated stub () does not exist'}
    # Set stub as an un-exist stub name.
    {'error': 'The designated stub (hhahahahah) does not exist'}

###################################################################################################################    

"""Error 2: wrong format of input body"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input: 
        # The minimum required inputs 
        API_Body = {
                        "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
                        "domain_id": "0201adc4-ae96-46f0-ae3d"
                        "triggered_by": "",
                        "user": "gdluserTest",
                        "device": "R20",
                        "stub_name": "stubTest1"
                    }
        
Response:
    
        {'error': 'User name not found'}
        
###################################################################################################################  


###################################################################################################################
# For all notes, before users calling this API, users must input the value of map_create_mode correctly, or An error will 
# occoured : {'error': 'The map creation parameters are not provided.'}
###################################################################################################################


"""Note 1:  Map Device and Its Neighbors"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input: 
        # Please follow the input format 
        API_Body = {
                "domain_setting": {
                "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
                "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
                },
                "basic_setting": {
                    "triggered_by": "Netbrain",
                    "user": "gdluserTest",
                    "device": "R20",
                    "stub_name": "stubTest1"
                },
                "map_setting": {
                        "map_create_mode": 0,
                        "map_device_para": {
                        "device": "SW4",
                        "include_neighbor": "",
                        "interfaces": [""],
                        "neighbor_type": ""
                    }
                }  
        }
        
        # Note: 
        #     1) if the input value of map_setting.device is empty, 
        #        then the API response will return the map about basic_setting.device defaulty.
        
        #     2) if the input value of map_setting.include_neighbor is empty, 
        #        the API response map will return all neighbors of map_setting.device defaultly.
        
        #     3) if the input value of map_setting.device set as an un-exist device name,
        #        an error will occured : {'error': 'Failed to find the designated device SW40'}
        # 
        
Response:
    
        {
            'mapId': 'c34bd4ff-e260-4366-844c-9389ee77fcb1',
            'mapName': 'stubTest1-20190211144514',
            'mapType': 1,
            'mapUrl': 'map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=c34bd4ff-e260-4366-844c-9389ee77fcb1&maptype=1'
        }
        
###################################################################################################################    

"""Note 2:  Open Site Map of The Device"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input: 
        # Please follow the input format 
        API_Body = {
                "domain_setting": {
                "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
                "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
                },
                "basic_setting": {
                    "triggered_by": "Netbrain",
                    "user": "gdluserTest",
                    "device": "R20",
                    "stub_name": "stubTest1"
                },
                "map_setting": {
                        "map_create_mode": 1,
                        "map_device_sitemap_para": {
                        "device": "SW4",
                        "duplicate_map": False
                    }
                }  
        }
        
        # Note: if there is no site map for the input device, then an error will occoured:
        #       {'error': 'Site map does not exist for device SW4'}
        
Response:
    
        {
            'mapId': 'c34bd4ff-e260-4366-844c-f2eb6e6f94b3',
            'mapName': 'stubTest1-20190211144514',
            'mapType': 1,
            'mapUrl': 'map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=c34bd4ff-e260-5777-399c-7700ee77fcb1&maptype=1'
        }
        
        
###################################################################################################################    

"""Note 3: trigger an existing map"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input: 
        # Please follow the input format and if user provide the map_id then the value of duplicate_map also must be provided
        # Or there would be an error occured: {'error': 'The duplicate_map flag is not set in the map-open parameters.'}
        API_Body = {
                "domain_setting": {
                "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
                "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
                },
                "basic_setting": {
                    "triggered_by": "Netbrain",
                    "user": "gdluserTest",
                    "device": "R20",
                    "stub_name": "stubTest1"
                },
                "map_setting": {
                        "map_create_mode": 2,
                        "map_open_para": {
                        "map_id": "3379471c-1c06-19af-b030-8dc82245a7f1",
                        "site_id": "the Id of device site", # Please change to the correct input value before using, or an error will occured
                        "device_group_id": "the Id of group which device inside.", # Please change to the correct input value before using, or an error will occured
                        "duplicate_map": True
                        }
                }  
        }
        # Note: if the input of map_id is incorrect then an error will occoured:
        #       {'error': 'The designated map does not exist, mapType=1, mapId=3379471c-1c06-19af-b030-'}
        
Response:
    
        {
            'mapId': 'cf08cafc-a25f-4ba8-be92-f2eb6e6f94b3',
            'mapName': 'stubTest1-20190211142723',
            'mapType': 1,
            'mapUrl': 'map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=cf08cafc-a25f-4ba8-be92-f2eb6e6f94b3&maptype=1'
        }
        
###################################################################################################################    

"""Note 4:  Map a path"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input: 
        # Please follow the input format 
        API_Body = {
                "domain_setting": {
                "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
                "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
                },
                "basic_setting": {
                    "triggered_by": "Netbrain",
                    "user": "gdluserTest",
                    "device": "R20",
                    "stub_name": "stubTest1"
                },
                "map_setting": {
                        "map_create_mode": 3,
                        "map_path_para": {
                        "source": "R3", # Can not be null
                        "source_gateway": "10.120.15.5",
                        "source_gateway_dev": "R3",
                        "source_gateway_intf": "Ethernet0/3.15",
                        "source_port": "",
                        "destination": "R2",# Can not be null
                        "destination_gateway": "10.120.13.1",
                        "destination_port": "",
                        "destination_gateway_dev": "R2",
                        "destination_gateway_intf": "Ethernet0/3.13",
                        "direction": 1, # Can not be null
                        "protocol": 28, # Can not be null
                        "protocol_name": "",
                        "isLiveUseBaseLineConfig": True,
                        "advancedOption": {
                            "debugMode": False,
                            "calcL3ActivePath": False,
                            "useCommandsWithArguments": False,
                            "calcWhenDeniedByACL": False,
                            "calcWhenDeniedByPolicy": False,
                            "enablePathFixup": True
                        }
                        "dataSource": {
                            "type": 1,
                            "recent": {
                                "unit": 2,
                                "duration": 5
                            },
                            "range": {
                                "start": "",
                                "end": ""
                            },
                            "around": {
                                "time": ""
                            }
                        }
                    }
                }  
        }
        
        # Note: if users want to create the map of path, some input Parameters must be provided or an error will occoured:
        #       {'error': 'Source device or destination device is not provided.'}
        
Response:
    
        {
            'mapId': 'c7443ef6-bbe2-486f-a029-f0830d0f11b5',
            'mapName': 'stubTest1-20190211161535',
            'mapType': 1,
            'mapUrl': 'map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=c7443ef6-bbe2-486f-a029-f0830d0f11b5&maptype=1',
            'taskId': 'ef07f195-31ae-490b-9aa7-58533b889ea2'
        }
        
        
```


