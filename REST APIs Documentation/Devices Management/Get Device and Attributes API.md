
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
|||If only provide skip value, return the rest of the full device list. If only provide limit value, return from the first device in DB. If provided both skip and limit, return as required. Error exceptions follow each parameter's description.<br>Skip and limit parameters are based on the search result from DB.|
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
    response = requests.get(full_url, params = json.dumps(data), headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 
```
    {'devices': [{'id': 'ad53a0f6-644a-400b-9216-8df746baed3b', 'mgmtIP': '10.1.12.2', 'hostname': 'Client1', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'cd97d9ce-1d39-421d-a56d-e8da3aaa08c7', 'mgmtIP': '10.1.13.2', 'hostname': 'Client2', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '612a963c-e6cd-4ed1-8742-67b664dd214c', 'mgmtIP': '10.2.18.2', 'hostname': 'Client4', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '1a5d49f5-3755-4aad-b27d-cb5760aa494d', 'mgmtIP': '10.1.20.130', 'hostname': 'Client7', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '77242378-e865-449e-adeb-c4eeaf361853', 'mgmtIP': '10.1.14.2', 'hostname': 'Client3', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'fb1c1785-66a7-45cf-8cc6-98f637e8ad39', 'mgmtIP': '10.2.19.2', 'hostname': 'Client5', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '575fd214-acdf-427c-914a-2acd2aedb6af', 'mgmtIP': '123.12.12.12', 'hostname': 'R12', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '4b814621-05d0-4dd2-98e0-59d79b1ec410', 'mgmtIP': '123.11.11.11', 'hostname': 'R11', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '432d39b7-9729-4313-af18-3cbbf8473663', 'mgmtIP': '123.20.1.3', 'hostname': 'SW5', 'deviceTypeName': 'Cisco IOS Switch', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '1d8c841f-a9bc-4288-aab2-6322bbb1ab1b', 'mgmtIP': '10.18.19.19', 'hostname': 'R19', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'bbfbc73f-3425-4286-9402-fda3bc4e7661', 'mgmtIP': '123.14.14.14', 'hostname': 'R14', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'de62bda7-b285-4750-97bc-419570b58439', 'mgmtIP': '123.204.4.4', 'hostname': 'SW4', 'deviceTypeName': 'Cisco IOS Switch', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'c61cde7b-7ddf-41de-bc2f-dafae6c7c7ef', 'mgmtIP': '123.203.3.3', 'hostname': 'SW3', 'deviceTypeName': 'Cisco IOS Switch', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '5074459d-1435-4f65-a323-94c7dffcd3a9', 'mgmtIP': '123.13.13.13', 'hostname': 'R13', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'ff8b6bbc-4348-4f60-a202-2616ab37af9d', 'mgmtIP': '10.1.20.2', 'hostname': 'Client6', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'eb31a451-3236-4681-b46e-9084e7e01765', 'mgmtIP': '10.120.15.1', 'hostname': 'R2', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '64a80717-49a3-4f61-829b-926d1dabde79', 'mgmtIP': '123.1.1.1', 'hostname': 'R1', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'c1f0d040-7b93-4ddf-a1df-04e8ce276107', 'mgmtIP': '123.10.1.14', 'hostname': 'R5', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '1e8029be-a858-48bd-b532-54b694edc529', 'mgmtIP': '10.120.14.5', 'hostname': 'R3', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '98c00148-016f-43fc-9c1d-926fc728551e', 'mgmtIP': '123.15.15.15', 'hostname': 'R15', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '183b658c-c8d8-4623-bb76-1f670f0e09a3', 'mgmtIP': '123.8.8.8', 'hostname': 'R8', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '0d2c8440-307b-46a1-8c72-12fd670ad86c', 'mgmtIP': '123.6.6.6', 'hostname': 'R6', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'b95dbda8-64a0-44cb-a12e-79478a2e1f3b', 'mgmtIP': '123.20.1.10', 'hostname': 'R17', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '4fcaf03f-8d26-47c9-9dba-37d41e09d741', 'mgmtIP': '123.7.7.7', 'hostname': 'R7', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '2f410fd9-8b43-4bba-ab0f-54922951739d', 'mgmtIP': '123.20.1.11', 'hostname': 'SW6', 'deviceTypeName': 'Cisco IOS Switch', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '4222a806-6646-40fc-bd19-11294940434e', 'mgmtIP': '123.10.1.18', 'hostname': 'R4', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '1b558e72-6671-48f8-849e-7f7df473e3aa', 'mgmtIP': '123.20.20.20', 'hostname': 'R20', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'fc1e0e19-83a9-4f84-8e46-9ef7ae767b6e', 'mgmtIP': '123.9.9.9', 'hostname': 'R9', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'f7eec066-c9b0-4e08-8ada-aad8f5e35a16', 'mgmtIP': '123.10.10.10', 'hostname': 'R10', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'f51f6e8e-d4ef-47af-9139-74a18691c052', 'mgmtIP': '123.20.1.2', 'hostname': 'R16', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '2ef50fff-eb73-49da-8599-45c68b876275', 'mgmtIP': '10.18.19.18', 'hostname': 'R18', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}], 'statusCode': 790200, 'statusDescription': 'Success.'}

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
