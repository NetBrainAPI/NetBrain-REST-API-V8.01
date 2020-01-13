
# Discovery API Design

## ***GET*** /V1/CMDB/Devices/Discovery/Tasks/{task}/Results
Call this API to get the running result of specified ip addresses for a discovery task of the latest run.
> **Note**: users cannot put too many ip addresses in the query parameter, which will make the URLs over 2,000 characters and it will not work in some web browsers.<br> {task} means {taskId} or {taskName}

## Detail Information

> **Title** : Get Discovery Task Result API<br>

> **Version** : 01/28/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Discovery/Tasks/{task}/Results

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

>No request body.

## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|tasksId*| string | The ID of a discovery task.  |
|tasksName*| string | The name of a discovery task. |

>>**Note:** two parameters can only provide one to call this API and must provide one parameter.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|IPs| List of string | The list of IP for devices. Optional, returns results of all devices if not specified  |

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
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |
|devices| list | A list of discovered devices. |
|devices.mgmtIP| string | Management ip of the device. |
|devices.domainId| string | The ID of the domain that a device belongs to. |
|devices.source| string | The IP from which a device was discovered. |
|devices.hostname| string | The hostname of a device. |
|devices.frontServer| string | The Proxy Server used to discover a device. |
|devices.ping| string | The ping to a device succeeded or failed. |
|devices.SNMP| string | The SNMP community string of a device. |
|devices.vendor| string | The vendor of a device. |
|devices.oid| string | The OID of a device. |
|devices.type| string | The type of a device. |
|devices.config| string | Obtaining device configuration succeeded or failed. |
|devices.telenetSSH| string | Accessing a device via SSH or Telnet succeeded or failed. |

> ***Example***


```python
{
    "devices": [
        {
            "mgmtIP": "123.11.11.11",
            "source": "Scan 123.11.11.11/32",
            "hostname": "R11",
            "frontServerOrGroupId": "NetBrainServer",
            "ping": "Succeeded",
            "SNMP": "nb",
            "vendor": "Cisco",
            "oid": "1.3.6.1.4.1.9.1.1",
            "type": "Cisco Router",
            "config": "Succeeded",
            "telnetSSH": "Succeeded"
        },
        {
            "mgmtIP": "123.1.1.1",
            "source": "Scan 123.1.1.1/32",
            "hostname": "R1",
            "frontServerOrGroupId": "NetBrainServer",
            "ping": "Succeeded",
            "SNMP": "nb",
            "vendor": "Cisco",
            "oid": "1.3.6.1.4.1.9.1.1",
            "type": "Cisco Router",
            "config": "Succeeded",
            "telnetSSH": "Succeeded"
        },
        {
            "mgmtIP": "10.1.14.2",
            "source": "Scan 10.1.14.2/32",
            "hostname": "Client3",
            "frontServerOrGroupId": "NetBrainServer",
            "ping": "Succeeded",
            "SNMP": "nb",
            "vendor": "Cisco",
            "oid": "1.3.6.1.4.1.9.1.1",
            "type": "Cisco Router",
            "config": "Succeeded",
            "telnetSSH": "Succeeded"
        },
        {
            "mgmtIP": "123.15.15.15",
            "source": "Scan 123.15.15.15/32",
            "hostname": "R15",
            "frontServerOrGroupId": "NetBrainServer",
            "ping": "Succeeded",
            "SNMP": "nb",
            "vendor": "Cisco",
            "oid": "1.3.6.1.4.1.9.1.1",
            "type": "Cisco Router",
            "config": "Succeeded",
            "telnetSSH": "Succeeded"
        },
        {
            "mgmtIP": "10.1.13.2",
            "source": "Scan 10.1.13.2/32",
            "hostname": "Client2",
            "frontServerOrGroupId": "NetBrainServer",
            "ping": "Succeeded",
            "SNMP": "nb",
            "vendor": "Cisco",
            "oid": "1.3.6.1.4.1.9.1.1",
            "type": "Cisco Router",
            "config": "Succeeded",
            "telnetSSH": "Succeeded"
        },
        {
            "mgmtIP": "123.10.10.10",
            "source": "Scan 123.10.10.10/32",
            "hostname": "R10",
            "frontServerOrGroupId": "NetBrainServer",
            "ping": "Succeeded",
            "SNMP": "nb",
            "vendor": "Cisco",
            "oid": "1.3.6.1.4.1.9.1.1",
            "type": "Cisco Router",
            "config": "Succeeded",
            "telnetSSH": "Succeeded"
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
}
```


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

taskID = "34124e63-31d6-dfad-f5fa-05ae0ebb4b49"
##OR##
#taskName = "testGDL_DT1"
#data = {"ips" : ["10.1.13.2", "123.1.1.1", "10.1.14.2"]}

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Discovery/Tasks/"+str(taskID)+"/Results"
    
try:
    # Do the HTTP request
    #response = requests.get(full_url, headers=headers, params = data, verify=False)
    response = requests.get(full_url, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print("Get discovery results failed - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'devices': [{'mgmtIP': '123.20.1.3', 'source': 'Scan 123.20.1.3/32', 'hostname': 'SW5', 'frontServerOrGroupId': 'NetBrainServer', 'ping': 'Succeeded', 'SNMP': 'nb', 'vendor': 'Cisco', 'oid': '1.3.6.1.4.1.9.1.1227', 'type': 'Cisco IOS Switch', 'config': 'Succeeded', 'telnetSSH': 'Succeeded'}, {'mgmtIP': '123.1.1.1', 'source': 'Scan 123.1.1.1/32', 'hostname': 'R1', 'frontServerOrGroupId': 'NetBrainServer', 'ping': 'Succeeded', 'SNMP': 'nb', 'vendor': 'Cisco', 'oid': '1.3.6.1.4.1.9.1.1', 'type': 'Cisco Router', 'config': 'Succeeded', 'telnetSSH': 'Succeeded'}, {'mgmtIP': '10.1.14.2', 'source': 'Scan 10.1.14.2/32', 'hostname': 'Client3', 'frontServerOrGroupId': 'NetBrainServer', 'ping': 'Succeeded', 'SNMP': 'nb', 'vendor': 'Cisco', 'oid': '1.3.6.1.4.1.9.1.1', 'type': 'Cisco Router', 'config': 'Succeeded', 'telnetSSH': 'Succeeded'}, {'mgmtIP': '123.203.3.3', 'source': 'Scan 123.203.3.3/32', 'hostname': 'SW3', 'frontServerOrGroupId': 'NetBrainServer', 'ping': 'Succeeded', 'SNMP': 'nb', 'vendor': 'Cisco', 'oid': '1.3.6.1.4.1.9.1.1227', 'type': 'Cisco IOS Switch', 'config': 'Succeeded', 'telnetSSH': 'Succeeded'}, {'mgmtIP': '10.1.13.2', 'source': 'Scan 10.1.13.2/32', 'hostname': 'Client2', 'frontServerOrGroupId': 'NetBrainServer', 'ping': 'Succeeded', 'SNMP': 'nb', 'vendor': 'Cisco', 'oid': '1.3.6.1.4.1.9.1.1', 'type': 'Cisco Router', 'config': 'Succeeded', 'telnetSSH': 'Succeeded'}, {'mgmtIP': '123.204.4.4', 'source': 'Scan 123.204.4.4/32', 'hostname': 'SW4', 'frontServerOrGroupId': 'NetBrainServer', 'ping': 'Succeeded', 'SNMP': 'nb', 'vendor': 'Cisco', 'oid': '1.3.6.1.4.1.9.1.1227', 'type': 'Cisco IOS Switch', 'config': 'Succeeded', 'telnetSSH': 'Succeeded'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    


```python
# Provided a mgmIP address of one specified device. Or users can provide a list of mgmIP addresses to present multiple devices 

data = {"ips" : ["123.1.1.1"]}
#data = {"ips" : ["10.1.13.2", "123.1.1.1", "10.1.14.2"]}---a list of mgmIP addresses

try:
    # Do the HTTP request
    response = requests.get(full_url, headers=headers, params = data, verify=False)
    #response = requests.get(full_url, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print("Get discovery results failed - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'devices': [{'mgmtIP': '123.1.1.1', 'source': 'Scan 123.1.1.1/32', 'hostname': 'R1', 'frontServerOrGroupId': 'NetBrainServer', 'ping': 'Succeeded', 'SNMP': 'nb', 'vendor': 'Cisco', 'oid': '1.3.6.1.4.1.9.1.1', 'type': 'Cisco Router', 'config': 'Succeeded', 'telnetSSH': 'Succeeded'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X GET \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Discovery/Tasks/34124e63-31d6-dfad-f5fa-05ae0ebb4b49/Results \
  -H 'Postman-Token: 83feacb8-4ede-4d48-b2a5-d074c063acd6' \
  -H 'cache-control: no-cache' \
  -H 'token: fd8b3f95-adc6-406d-9c18-bdb155de2ced'
```

# Error Examples and Note


```python
###################################################################################################################    

"""Note 1: no devices shown"""

Input:
    
        taskID = "34124e63-31d6-dfad-f5fa-05ae0ebb4b49"
        ##OR##
        #taskName = "testGDL_DT1"

Response:
    
    "{
        'devices': [], 
        'statusCode': 790200, 
        'statusDescription': 'Success.'
    }"
        
Explanation:
    """Some times, users already created the discovery task and also added the IPs into task. But when users calling this API,
    the "devices" list is still empty. That is means the users haven't run this task. After user run this task successfully, 
    the "devices" list would shows the corresponding content as described in Response document. Thus, please calling the 
    "Run Discovery Task  Now API" before calling this API."""

###################################################################################################################    

"""Error 1: empty inputs"""

Input:
    
        taskID = ""

Response:
    
    "Get discovery results failed - 
        {
            "statusCode":793404,
            "statusDescription":"No resource"
        }"
        
###################################################################################################################    

"""Error 1: wrong mgmIP of device"""

Input:
    
        taskID = "34124e63-31d6-dfad-f5fa-05ae0ebb4b49"
        data = {"ips" : ["123.1.1.0"]} # there is no device in this discovery task has a mgmIP like this.

Response:
    
    "{
        'devices': [], 
        'statusCode': 790200,
        'statusDescription': 'Success."
    }"
```
