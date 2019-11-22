
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
