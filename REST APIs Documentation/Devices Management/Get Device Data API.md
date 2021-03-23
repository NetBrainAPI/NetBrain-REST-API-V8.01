
# Device API Design

## ***GET*** /V1/CMDB/Devices/DeviceRawData
Call this API to get the raw data for specified devices by device hostname or mgmIp. Currently we only support the data from current baseline.

## Detail Information

> **Title** : Get Device Raw Data API<br>

> **Version** : 06/25/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices/DeviceRawData

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Query parameter(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|hostname* | string  | The hostname of the device.  |
|IP* | string  | The management IP of  the device.  |
|dataType*| integer | candidates:<br> 0: configFile<br> 1: dataTable<br> 2: cli_cmd_result
|tableName | string  | 0, if user set dataType==1, then "tableName" field cannot be empty<br> 1, for system table, we have some constant value<br> 2, for nct table, just use the real table name<br> 3, Candidates:<br> routeTable<br> arpTable<br> macTable<br> cdpTable<br> stpTable<br> bgpNbrTable<br> for nct table, just use the real table name |
|vrf | string| 1, optional -- only needed for some table<br> 2, candidates can ref to what we see from IE UI|
|cmd | string  |  0, if user set dataType==2, then "cmd" field cannot be empty<br> 1, optional -- only needed for cli command<br>2, only support exact match, e.g. "sh ver" is different with "show version"  |

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
|content| string | Data content. |
|retrievalTime| string | The time of users retrieved data. |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***


```python
{
    "content" : "",
    "retrievalTime" : "", #formal DateTime Format in UTC, e.g. 2019-04-16T14:53:29Z
    "statusCode" : xx, # ref to https://www.netbraintech.com/docs/ie71/help/error-code-list.htm
    "statusDescription" : "" # note: only applicable
}
```

# Full Example:


```python
# import python modules 
import requests
import time
import urllib3
import pprint
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

nb_url = "https://ie80.netbraintech.com"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'} 
token = "6cb4a2bf-178d-4b63-bc21-26f6b4a8bf68"
headers["Token"] = token
# call login API

get_device_raw_data_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices/DeviceRawData"

def get_device_raw_data(get_device_raw_data_url, token, hostname, headers):
    
    headers["Token"] = token
    
    data = {
        "hostname" : hostname,
        "dataType" : 2,
        "tableName" : "",
        "vrf" : "",
        "cmd" : "show log"
    }
    
    try:
        response = requests.get(get_device_raw_data_url, params = data, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return ("Create module attribute failed! - " + str(response.text))

    except Exception as e:
        return (str(e))
    
# for i in range(10):
res = get_device_raw_data(get_device_raw_data_url, token, "GW2Lab", headers)
print(res)

```

    {'content': 'GW2Lab#show log\r\nSyslog logging: enabled (0 messages dropped, 32 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)\r\n\r\nNo Active Message Discriminator.\r\n\r\n\r\n\r\nNo Inactive Message Discriminator.\r\n\r\n\r\n    Console logging: level debugging, 48 messages logged, xml disabled,\r\n                     filtering disabled\r\n    Monitor logging: level debugging, 0 messages logged, xml disabled,\r\n                     filtering disabled\r\n    Buffer logging:  level debugging, 48 messages logged, xml disabled,\r\n                    filtering disabled\r\n    Exception Logging: size (8192 bytes)\r\n    Count and timestamp logging messages: disabled\r\n    Persistent logging: disabled\r\n\r\nNo active filter modules.\r\n\r\n    Trap logging: level informational, 52 message lines logged\r\n        Logging Source-Interface:       VRF Name:\r\n\r\nLog Buffer (8192 bytes):\r\n\r\n*Jan  2 00:00:01.395: %IOS_LICENSE_IMAGE_APPLICATION-6-LICENSE_LEVEL: Module name = c3900e Next reboot level = ipbasek9 and License = ipbasek9\r\n*May 26 05:49:11.123: %LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to down\r\n*May 26 05:49:11.123: %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down\r\n*May 26 05:49:11.123: %LINK-3-UPDOWN: Interface GigabitEthernet0/2, changed state to down\r\n*May 26 05:49:11.123: %LINK-3-UPDOWN: Interface GigabitEthernet0/3, changed state to down\r\n*May 26 05:49:13.497: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to down\r\n*May 26 05:49:13.497: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to down\r\n*May 26 05:49:13.497: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/2, changed state to down\r\n*May 26 05:49:13.497: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/3, changed state to down\r\n*May 26 05:49:17.365: %SYS-5-CONFIG_I: Configured from memory by console\r\n*May 26 05:49:17.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback0, changed state to up\r\n*May 26 05:49:17.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback3, changed state to up\r\n*May 26 05:49:17.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback4, changed state to up\r\n*May 26 05:49:17.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback5, changed state to up\r\n*May 26 05:49:17.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback6, changed state to up\r\n*May 26 05:49:17.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback7, changed state to up\r\n*May 26 05:49:17.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback8, changed state to up\r\n*May 26 05:49:17.713: %LINEPROTO-5-UPDOWN: Line protocol on Interface Loopback9, changed state to up\r\n*May 26 05:49:17.945: %LINEPROTO-5-UPDOWN: Line protocol on Interface NVI0, changed state to up\r\n*May 26 05:49:18.699: %LINK-5-CHANGED: Interface Loopback1, changed state to administratively down\r\n*May 26 05:49:18.699: %LINK-5-CHANGED: Interface Loopback2, changed state to administratively down\r\n*May 26 05:49:18.699: %LINK-5-CHANGED: Interface Loopback10, changed state to administratively down\r\n*May 26 05:49:18.911: %LINK-5-CHANGED: Interface GigabitEthernet0/2, changed state to administratively down\r\n*May 26 05:49:18.911: %LINK-5-CHANGED: Interface GigabitEthernet0/3, changed state to administratively down\r\n*May 26 05:49:25.189: %SYS-5-RESTART: System restarted --\r\nCisco IOS Software, C3900e Software (C3900e-UNIVERSALK9-M), Version 15.2(4)M6a, RELEASE SOFTWARE (fc1)\r\nTechnical Support: http://www.cisco.com/techsupport\r\nCopyright (c) 1986-2014 by Cisco Systems, Inc.\r\nCompiled Tue 15-Apr-14 06:10 by prod_rel_team\r\n*May 26 05:49:25.387: %SSH-5-ENABLED: SSH 2.0 has been enabled\r\n*May 26 05:49:25.471: %SNMP-5-COLDSTART: SNMP agent on host GW2Lab is undergoing a cold start\r\n*May 26 05:50:12.387: %PIM-5-DRCHG: DR change from neighbor 0.0.0.0 to 172.24.30.1 on interface GigabitEthernet0/1\r\n*May 26 05:50:13.943: %LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to up\r\n*May 26 05:50:14.943: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/1, changed state to up\r\n*May 26 05:50:57.307: %OSPF-5-ADJCHG: Process 10, Nbr 172.24.255.20 on GigabitEthernet0/1 from LOADING to FULL, Loading Done\r\n*May 26 06:08:49.071: %LINK-3-UPDOWN: Interface GigabitEthernet0/0, changed state to up\r\n*May 26 06:08:50.071: %LINEPROTO-5-UPDOWN: Line protocol on Interface GigabitEthernet0/0, changed state to up\r\n*May 26 06:09:32.269: %OSPF-5-ADJCHG: Process 200, Nbr 172.24.255.51 on GigabitEthernet0/0.5 from LOADING to FULL, Loading Done\r\n*Jun 15 03:57:49.693: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 192.168.32.44\r\n*Jun 18 06:16:13.958: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.0.237\r\n*Jun 18 07:17:44.668: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.0.237\r\n*Jun 18 10:07:49.627: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.0.237\r\n*Jun 19 17:43:54.236: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.32.133\r\n*Jun 19 21:44:54.925: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.32.133\r\n*Jun 20 00:44:50.590: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.32.133\r\n*Jun 20 02:44:46.263: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.32.133\r\n*Jun 20 05:43:47.115: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.32.133\r\n*Jun 20 05:44:52.361: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.32.133\r\n*Jun 20 06:44:42.558: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.32.133\r\n*Jun 20 08:44:38.574: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.32.133\r\n*Jun 25 06:15:44.869: %SSH-4-SSH2_UNEXPECTED_MSG: Unexpected message type has arrived. Terminating the connection from 10.10.0.237\r\n*Jul  2 02:15:40.300: %SYS-5-CONFIG_I: Configured from console by admin on vty3 (10.10.4.5)\r\n', 'retrievalTime': '0001-01-01T00:00:00', 'statusCode': 790200, 'statusDescription': 'Success.'}


```python
# If customer face the response "{"statusCode":791006,"statusDescription":"Device Data Not Found"}", 
# that means customer didn't run a benchmark to collect the corresponding device data table or CLI information.
```

# cURL Code From Postman


```python
curl -X GET \
  'https://ie80.netbraintech.com/ServicesAPI/API/V1/CMDB/Devices/DeviceRawData?hostname=US-BOS-SW3&dataType=1&tableName=routeTable' \
  -H 'Accept: */*' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Host: ie80.netbraintech.com' \
  -H 'Postman-Token: 81733a42-965c-40b2-8c31-dbf5d6d7cd46,28e92296-2b9d-4f26-82d3-8dccddf44787' \
  -H 'User-Agent: PostmanRuntime/7.13.0' \
  -H 'accept-encoding: gzip, deflate' \
  -H 'cache-control: no-cache' \
  -H 'content-length: 80' \
  -H 'token: 1b6d0451-c598-497d-91b2-1a28db1ac089' \
  -d '{
	"hostname" : "BJ_L2_Core_5",
    "dataType" : 2,
    "cmd" : "show version"
}'
```
