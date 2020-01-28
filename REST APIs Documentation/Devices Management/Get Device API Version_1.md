
# Devices REST API Design

## GET /V1/CMDB/Devices

This API is used to get devices and their attributes data in batch. The response of this API will return a list in JSON format.<br>**Note:<br>1. The API follows the privilege control of NB system. If there is restriction set by Access Control Policy for the target querying resources, the response will not return queried data.<br>2. This API doesn't support any GDR that is not set as displayed, except first discovery time and last discovery time.**

## Detail Information

>**Title:** Devices API

>**Version:** 08/22/2019

>**API Server URL:** http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices

>**Authentication:**

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication|Headers|Authentication token|

## Request body (*required)

>No request body.

## Query Parameters (*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|hostname|string OR list of string|A list of device hostnames|
|ip|string OR list of string|A list of device management IPs|
|||If provided both of hostname and ip, hostname has higher priority. If any of the devices are not found from the provided query parameter, return the found devices as a list in response and add another json key "deviceNotFound", the value is a mixed list of hostnames and IPs that are not found.|
|fullattr|integer|Default is 0.<br>0: return basic device attributes (device id, management IP, hostname, device type, first discover time, last discover time).<br>1: return all device attributes, including customized attributes|
|*version|string|Value of this parameter is 1 for verison 8.01|
|skip|integer|The amount of records to be skipped. The value must not be negative.  If the value is negative, API throws exception {"statusCode":791001,"statusDescription":"Parameter 'skip' cannot be negative"}. No upper bound for this parameter.|
|limit|integer|The up limit amount of device records to return per API call. The value must not be negative.  If the value is negative, API throws exception {"statusCode":791001,"statusDescription":"Parameter 'limit' cannot be negative"}. No upper bound for this parameter. If the parameter is not specified in API call, it means there is not limitation setting on the call.|
|||If only provide skip value, return the device list with 50 devices information start from the skip number. If only provide limit value, return from the first device in DB. If provided both skip and limit, return as required. Error exceptions follow each parameter's description.<br>Skip and limit parameters are based on the search result from DB. The "limit" value valid range is 10 - 100, if the assigned value exceeds the range, the server will respond error message: "Parameter 'limit' must be greater than or equal to 10 and less than or equal to 100."  |
|filter|json|If specified, return the matched device list with device attributes. Supported filtering attributes: name, assetTag, contact, descr, layer, loc, mgmtIP, model, site(complete site path， for example: "My Network\\Burlington"), sn, vendor, ver, hasBGPConfig, hasOSPFConfig, hasEIGRPConfig, hasISISConfig, hasMulticastConfig, hasOTVConfig, isHA, hasBPEConfig, isTransparent, isCluster, hasVXLANConfig, hasVPLSConfig|
|||Only support AND operator, when multiple filter attributes are specified in JSON.<br>If provide invalid data format, return error "invalid filter input".|

## Headers

>**Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|Content-Type|string|support "application/json"|
|Accept|string|support "application/json"|

>**Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
|token|string|Authentication token, get from login API.|

## Response

|**Name**|**Type**|**Description**|
|------|------|------|
|statusCode|integer|Code issued by NetBrain server indicating the execution result.|
|statusDescription|string|The explanation of the status code.|
|devices|string[]|A list of devices.|
|totalResultCount|integer|The total amount of the found records.|
|devices.devicesID|string|The device ID.|
|devices.deviceTypeName|string|The type of the returned device, such as Cisco Router.|
|devices.mgmtIP|string|The management IP address of the returned device.|
|devices.hostname|string|The hostname of returned device.|
|devices.customAttribute1|Refer to GDR data type|Customized Attribute 1.|
|devices.customAttribute2|Refer to GDR data type|Customized Attribute 2.|
|...|...|...|

>***Example***


```python
{
    "devices": [
        {
            "id": "ad53a0f6-644a-400b-9216-8df746baed3b",
            "name": "R20",
            "mgmtIP": "123.20.20.20",
            "mgmtIntf": "Loopback0",
            "subTypeName": "Cisco Router",
            "vendor": "Cisco",
            "model": "DEVELOPMENT TEST SOFTWARE",
            "ver": "15.4(2)T4",
            "sn": "71372834",
            "site": "My Network\\Unassigned",
            "loc": "",
            "contact": "",
            "mem": "356640420",
            "assetTag": "",
            "layer": "",
            "descr": "",
            "oid": "1.3.6.1.4.1.9.1.1",
            "driverName": "Cisco Router",
            "fDiscoveryTime": {
                "$date": 1547572719000
            },
            "lDiscoveryTime": {
                "$date": 1547572719000
            },
            "assignTags": "",
            "hasBGPConfig": true,
            "hasOSPFConfig": false,
            "hasEIGRPConfig": false,
            "hasISISConfig": false,
            "hasMulticastConfig": false,
            "customAttribute1": "string",
            "customAttribute2": true
        },
        {
            "id": "ad53a0f6-644a-400b-9216-8df746baed3c",
            "name": "R21",
            "mgmtIP": "123.20.20.21",
            "mgmtIntf": "Loopback0",
            "subTypeName": "Cisco Router",
            "vendor": "Cisco",
            "model": "DEVELOPMENT TEST SOFTWARE",
            "ver": "15.4(2)T4",
            "sn": "71372835",
            "site": "My Network\\Unassigned",
            "loc": "",
            "contact": "",
            "mem": "356640420",
            "assetTag": "",
            "layer": "",
            "descr": "",
            "oid": "1.3.6.1.4.1.9.1.1",
            "driverName": "Cisco Router",
            "fDiscoveryTime": {
                "$date": 1547572719000
            },
            "lDiscoveryTime": {
                "$date": 1547572719000
            },
            "assignTags": "",
            "hasBGPConfig": true,
            "hasOSPFConfig": false,
            "hasEIGRPConfig": false,
            "hasISISConfig": false,
            "hasMulticastConfig": false,
            "customAttribute1": "string",
            "customAttribute2": true
        }
    ],
    "deviceNotFound": ["R1","SW1","10.8.3.130","10.8.1.26"],
    "totalResultCount":2,
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
token = "13c7ed6e-781d-4b22-83e7-b1722de4e31d"
nb_url = "http://192.168.28.79"

full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token

data = {
    "version": 1
}


try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 
```
```python
{
  'devices': [
    {
      'name': 'CP-SW1',
      'mgmtIP': '192.168.0.58',
      'mgmtIntf': 'GigabitEthernet1/0/48',
      'subTypeName': 'Cisco IOS Switch',
      'vendor': 'Cisco',
      'model': 'WS-C3750X-48',
      'ver': '15.0(2)SE7',
      'sn': 'FDO1502R1Q3',
      'site': 'My Network\\NetBrain\\Asia\\Osaka',
      'mem': '175398456',
      'oid': '1.3.6.1.4.1.9.1.516',
      'driverName': 'Cisco IOS Switch',
      'fDiscoveryTime': '2019-12-11T18:00:19Z',
      'lDiscoveryTime': '2019-12-20T16:30:32Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'NB-IPN-02',
      'mgmtIP': '192.168.48.156',
      'mgmtIntf': 'mgmt0',
      'subTypeName': 'Cisco Nexus Switch',
      'vendor': 'Cisco',
      'model': 'N9K-C9372PX-E',
      'ver': '7.0(3)I4(1)',
      'sn': 'FDO222719KT',
      'site': 'My Network\\NetBrain\\Asia\\Seoul',
      'oid': '1.3.6.1.4.1.9.12.3.1.3.1712',
      'driverName': 'Cisco Nexus Switch',
      'fDiscoveryTime': '2019-12-11T18:00:26Z',
      'lDiscoveryTime': '2020-01-25T05:09:23Z',
      'assignTags': [
        'ipn'
      ],
      'hasBGPConfig': False,
      'hasOSPFConfig': True,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': True,
      'category': 'Unclassified'
    },
    {
      'name': 'US-NYC-PaloAlto',
      'mgmtIP': '192.168.28.18',
      'mgmtIntf': 'Management',
      'subTypeName': 'Palo Alto Firewall',
      'vendor': 'Palo Alto Networks',
      'model': 'PA-VM',
      'ver': '7.0.1',
      'sn': 'unknown',
      'site': 'My Network\\Unassigned',
      'loc': 'NYC',
      'contact': 'lin.zhu@netbraintech.com',
      'oid': '1.3.6.1.4.1.25461.2.3.29',
      'driverName': 'Palo Alto Firewall',
      'fDiscoveryTime': '2019-12-11T18:00:26Z',
      'lDiscoveryTime': '2019-12-20T16:30:32Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': True,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'isHA': False,
      'category': 'Unclassified'
    },
    {
      'name': 'NB-IPN-01',
      'mgmtIP': '192.168.48.155',
      'mgmtIntf': 'mgmt0',
      'subTypeName': 'Cisco Nexus Switch',
      'vendor': 'Cisco',
      'model': 'N9K-C9372PX-E',
      'ver': '7.0(3)I4(1)',
      'sn': 'FDO222719E4',
      'site': 'My Network\\NetBrain\\Asia\\Seoul',
      'oid': '1.3.6.1.4.1.9.12.3.1.3.1712',
      'driverName': 'Cisco Nexus Switch',
      'fDiscoveryTime': '2019-12-11T18:00:26Z',
      'lDiscoveryTime': '2020-01-25T05:09:22Z',
      'assignTags': [
        'ipn'
      ],
      'hasBGPConfig': False,
      'hasOSPFConfig': True,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': True,
      'category': 'Unclassified'
    },
    {
      'name': 'CP_GW2',
      'mgmtIP': '192.168.0.56',
      'mgmtIntf': 'Mgmt',
      'subTypeName': 'Checkpoint Firewall R80',
      'vendor': 'Checkpoint',
      'model': 'Check Point 3200',
      'ver': 'R80.10 - Build 170',
      'sn': '1832BA2346',
      'site': 'My Network\\NetBrain\\Asia\\Osaka',
      'loc': 'Unknown',
      'contact': 'nb',
      'mem': '3901972480',
      'oid': '1.3.6.1.4.1.2620.1.6.123.1.65',
      'driverName': 'Checkpoint Gaia R80',
      'fDiscoveryTime': '2019-12-11T18:00:27Z',
      'lDiscoveryTime': '2019-12-20T16:30:39Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'CP_GW1',
      'mgmtIP': '192.168.0.57',
      'mgmtIntf': 'Mgmt',
      'subTypeName': 'Checkpoint Firewall R80',
      'vendor': 'Checkpoint',
      'model': 'Check Point 3200',
      'ver': 'R80.10 - Build 170',
      'sn': '1832BA2305',
      'site': 'My Network\\NetBrain\\Asia\\Osaka',
      'loc': 'Unknown',
      'contact': 'nb',
      'mem': '3901972480',
      'oid': '1.3.6.1.4.1.2620.1.6.123.1.65',
      'driverName': 'Checkpoint Gaia R80',
      'fDiscoveryTime': '2019-12-11T18:00:28Z',
      'lDiscoveryTime': '2019-12-20T16:30:25Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'CP_HA1',
      'mgmtIP': '192.168.0.61',
      'mgmtIntf': 'Mgmt',
      'subTypeName': 'Checkpoint Firewall R80',
      'vendor': 'Checkpoint',
      'model': 'Check Point 3200',
      'ver': 'R80.10 - Build 170',
      'sn': '1832BA2323',
      'site': 'My Network\\NetBrain\\Asia\\Osaka',
      'loc': 'Unknown',
      'contact': 'nb',
      'mem': '3901972480',
      'oid': '1.3.6.1.4.1.2620.1.6.123.1.65',
      'driverName': 'Checkpoint Gaia R80',
      'fDiscoveryTime': '2019-12-11T18:00:28Z',
      'lDiscoveryTime': '2019-12-20T16:30:42Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'US-LAX-BIGIP',
      'mgmtIP': '192.168.28.9',
      'mgmtIntf': 'mgmt',
      'subTypeName': 'F5 Load Balancer',
      'vendor': 'F5',
      'model': 'bigipVirtualEdition',
      'ver': '13.0.0 0.0.1645 Final',
      'sn': 'e87bc037-6ac5-41cd-62871d40dd58\r',
      'site': 'My Network\\NetBrain\\North America\\LAX',
      'loc': 'Network Closet 1',
      'contact': 'Customer Name <admin@customer.com>',
      'oid': '1.3.6.1.4.1.3375.2.1.3.4.43',
      'driverName': 'F5 Load Balancer',
      'fDiscoveryTime': '2019-12-11T18:00:30Z',
      'lDiscoveryTime': '2019-12-20T16:30:29Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'CP_HA2',
      'mgmtIP': '192.168.0.62',
      'mgmtIntf': 'Mgmt',
      'subTypeName': 'Checkpoint Firewall R80',
      'vendor': 'Checkpoint',
      'model': 'Check Point 3200',
      'ver': 'R80.10 - Build 170',
      'sn': '1832BA2312',
      'site': 'My Network\\NetBrain\\Asia\\Osaka',
      'loc': 'Unknown',
      'contact': 'nb',
      'mem': '3901972480',
      'oid': '1.3.6.1.4.1.2620.1.6.123.1.65',
      'driverName': 'Checkpoint Gaia R80',
      'fDiscoveryTime': '2019-12-11T18:00:31Z',
      'lDiscoveryTime': '2019-12-20T16:30:25Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'ITE_EXTEND',
      'mgmtIP': '192.168.30.207',
      'mgmtIntf': 'GigabitEthernet0/47',
      'subTypeName': 'Cisco IOS Switch',
      'vendor': 'Cisco',
      'model': 'WS-C3560X-48P',
      'ver': '15.2(4)E7',
      'sn': 'FDO1518R0PK',
      'site': 'My Network\\Unassigned',
      'mem': '149241088',
      'oid': '1.3.6.1.4.1.9.1.1229',
      'driverName': 'Cisco IOS Switch',
      'fDiscoveryTime': '2019-12-11T18:00:31Z',
      'lDiscoveryTime': '2019-12-20T16:30:38Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'US-NYC-BIGIP',
      'mgmtIP': '192.168.29.35',
      'mgmtIntf': '',
      'subTypeName': 'F5 Load Balancer',
      'vendor': 'F5',
      'model': 'bigipVirtualEdition',
      'ver': '13.0.0 0.0.1645 Final',
      'sn': '4073a94b-ef81-4cea-89f660392532\r',
      'site': 'My Network\\Unassigned',
      'loc': 'CXL-EVE-NG',
      'contact': 'Lin Zhu <lin.zhu@netbraintech.com>',
      'oid': '1.3.6.1.4.1.3375.2.1.3.4.43',
      'driverName': 'F5 Load Balancer',
      'fDiscoveryTime': '2019-12-11T18:00:31Z',
      'lDiscoveryTime': '2019-12-20T16:30:30Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'CP-Mgmt',
      'mgmtIP': '192.168.0.55',
      'mgmtIntf': 'Mgmt',
      'subTypeName': 'Checkpoint Firewall R80',
      'vendor': 'Checkpoint',
      'model': 'Smart-1 405',
      'ver': 'R80.10 - Build 170',
      'sn': '1823BA2671',
      'site': 'My Network\\NetBrain\\Asia\\Osaka',
      'loc': 'Unknown',
      'contact': 'nb',
      'mem': '3694129152',
      'oid': '1.3.6.1.4.1.2620.1.6.123.1.73',
      'driverName': 'Checkpoint Gaia R80',
      'fDiscoveryTime': '2019-12-11T18:00:32Z',
      'lDiscoveryTime': '2019-12-20T16:30:24Z',
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'NBSPINE-5',
      'mgmtIP': '192.168.48.162',
      'mgmtIntf': 'Management0',
      'subTypeName': 'Cisco ACI Spine Switch',
      'vendor': 'Cisco Systems, Inc',
      'model': 'N9K-C9364C',
      'ver': 'n9000-14.1(2g)',
      'sn': 'FDO230300Q3',
      'site': '',
      'loc': '',
      'contact': '',
      'oid': '',
      'driverName': 'Cisco ACI Spine Switch',
      'fDiscoveryTime': '2020-01-22T20:25:35Z',
      'lDiscoveryTime': '2020-01-25T05:06:49Z',
      'assignTags': [
        'spine'
      ],
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'NBSPINE-6',
      'mgmtIP': '192.168.50.8',
      'mgmtIntf': 'Management0',
      'subTypeName': 'Cisco ACI Spine Switch',
      'vendor': 'Cisco Systems, Inc',
      'model': 'N9K-C9364C',
      'ver': 'n9000-14.1(2g)',
      'sn': 'FDO23230QBN',
      'site': '',
      'loc': '',
      'contact': '',
      'oid': '',
      'driverName': 'Cisco ACI Spine Switch',
      'fDiscoveryTime': '2020-01-22T20:25:32Z',
      'lDiscoveryTime': '2020-01-25T05:06:45Z',
      'assignTags': [
        'spine'
      ],
      'hasBGPConfig': False,
      'hasOSPFConfig': False,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    },
    {
      'name': 'BOS-N9K-L3OUT',
      'mgmtIP': '192.168.50.21',
      'mgmtIntf': 'mgmt0',
      'subTypeName': 'Cisco Nexus Switch',
      'vendor': 'Cisco',
      'model': 'NexusC9372TXE',
      'ver': '9.2(4)',
      'sn': 'SAL2023RCUH',
      'site': 'My Network\\Unassigned',
      'oid': '1.3.6.1.4.1.9.12.3.1.3.1713',
      'driverName': 'Cisco Nexus Switch',
      'fDiscoveryTime': '2019-12-11T18:00:46Z',
      'lDiscoveryTime': '2020-01-22T20:25:41Z',
      'assignTags': [
        'other'
      ],
      'hasBGPConfig': True,
      'hasOSPFConfig': True,
      'hasEIGRPConfig': False,
      'hasISISConfig': False,
      'hasMulticastConfig': False,
      'category': 'Unclassified'
    }
  ],
  'statusCode': 790200,
  'statusDescription': 'Success.'
}
```

# Example about get all devices by calling this API:

```python
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
skip = 0
count = 50
try:
    while count == 50:
        data = {
            "version": 1,
            "skip":skip,
            "fullattr":1
        }
        response = requests.get(full_url, params = data, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            count = len(result["devices"])
            skip = skip + count
            print (result)
        else:
            print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 
```
# cURL Code from Postman:


```python
curl -X GET \
  'https://integrationlab.netbraintech.com/ServicesAPI/API/V1/CMDB/Devices?ip=' \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -H 'Host: integrationlab.netbraintech.com' \
  -H 'Postman-Token: ec40d66c-7e51-46e2-90ee-421899414da9,4d41c70f-7d05-40fc-ae72-9064bf0b44bc' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'token: 7ac5b214-8844-43f6-b63b-c875a87ff1cf'
```
