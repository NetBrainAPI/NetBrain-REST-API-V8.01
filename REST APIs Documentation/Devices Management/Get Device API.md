
# Device API Design

## ***GET*** /V1/CMDB/Devices
This API call is used to get the corresponding device by an IP address or device name. For duplicate IP addresses, this API returns a device list.

If none of hostname and ip provided, response will return all devices of current domain.<br>

***Note：Known-Issue*** 
> One of these two attributes: ***hostname*** and ***ip*** must be provided when calling this API. But value can be empty.

> ***Example***

```python
params = {
    "hostname": ""
    #or
    # "ip" : ""
    }
```

## Detail Information

> **Title** : Get Devices API<br>

> **Version** : 01/25/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices

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
| hostname | string  | The host name of device. |
| ip | string  | The management ip of device. |


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
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |
|devices| string[] | A list of devices. |
|devices.devicesID| string | The device ID. |
|devices.deviceTypeName| string | The type of the returned device, such as Cisco Router. |
|devices.mgmtIP| string | The management IP address of the returned device. |
|devices.hostname| string | The hostname of returned device. |

> ***Example***



```python
# Successful response weithout hostname or ip inputs value as ""
{
    "devices": [
        {
            "id": "ad53a0f6-644a-400b-9216-8df746baed3b",
            "mgmtIP": "10.1.12.2",
            "hostname": "Client1",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "cd97d9ce-1d39-421d-a56d-e8da3aaa08c7",
            "mgmtIP": "10.1.13.2",
            "hostname": "Client2",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "612a963c-e6cd-4ed1-8742-67b664dd214c",
            "mgmtIP": "10.2.18.2",
            "hostname": "Client4",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "1a5d49f5-3755-4aad-b27d-cb5760aa494d",
            "mgmtIP": "10.1.20.130",
            "hostname": "Client7",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "77242378-e865-449e-adeb-c4eeaf361853",
            "mgmtIP": "10.1.14.2",
            "hostname": "Client3",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "fb1c1785-66a7-45cf-8cc6-98f637e8ad39",
            "mgmtIP": "10.2.19.2",
            "hostname": "Client5",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "575fd214-acdf-427c-914a-2acd2aedb6af",
            "mgmtIP": "123.12.12.12",
            "hostname": "R12",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "4b814621-05d0-4dd2-98e0-59d79b1ec410",
            "mgmtIP": "123.11.11.11",
            "hostname": "R11",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "432d39b7-9729-4313-af18-3cbbf8473663",
            "mgmtIP": "123.20.1.3",
            "hostname": "SW5",
            "deviceTypeName": "Cisco IOS Switch",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "1d8c841f-a9bc-4288-aab2-6322bbb1ab1b",
            "mgmtIP": "10.18.19.19",
            "hostname": "R19",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "bbfbc73f-3425-4286-9402-fda3bc4e7661",
            "mgmtIP": "123.14.14.14",
            "hostname": "R14",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "de62bda7-b285-4750-97bc-419570b58439",
            "mgmtIP": "123.204.4.4",
            "hostname": "SW4",
            "deviceTypeName": "Cisco IOS Switch",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "c61cde7b-7ddf-41de-bc2f-dafae6c7c7ef",
            "mgmtIP": "123.203.3.3",
            "hostname": "SW3",
            "deviceTypeName": "Cisco IOS Switch",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "5074459d-1435-4f65-a323-94c7dffcd3a9",
            "mgmtIP": "123.13.13.13",
            "hostname": "R13",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "ff8b6bbc-4348-4f60-a202-2616ab37af9d",
            "mgmtIP": "10.1.20.2",
            "hostname": "Client6",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "eb31a451-3236-4681-b46e-9084e7e01765",
            "mgmtIP": "10.120.15.1",
            "hostname": "R2",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "64a80717-49a3-4f61-829b-926d1dabde79",
            "mgmtIP": "123.1.1.1",
            "hostname": "R1",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "c1f0d040-7b93-4ddf-a1df-04e8ce276107",
            "mgmtIP": "123.10.1.14",
            "hostname": "R5",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "1e8029be-a858-48bd-b532-54b694edc529",
            "mgmtIP": "10.120.14.5",
            "hostname": "R3",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "98c00148-016f-43fc-9c1d-926fc728551e",
            "mgmtIP": "123.15.15.15",
            "hostname": "R15",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "183b658c-c8d8-4623-bb76-1f670f0e09a3",
            "mgmtIP": "123.8.8.8",
            "hostname": "R8",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "0d2c8440-307b-46a1-8c72-12fd670ad86c",
            "mgmtIP": "123.6.6.6",
            "hostname": "R6",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "b95dbda8-64a0-44cb-a12e-79478a2e1f3b",
            "mgmtIP": "123.20.1.10",
            "hostname": "R17",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "4fcaf03f-8d26-47c9-9dba-37d41e09d741",
            "mgmtIP": "123.7.7.7",
            "hostname": "R7",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "2f410fd9-8b43-4bba-ab0f-54922951739d",
            "mgmtIP": "123.20.1.11",
            "hostname": "SW6",
            "deviceTypeName": "Cisco IOS Switch",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "4222a806-6646-40fc-bd19-11294940434e",
            "mgmtIP": "123.10.1.18",
            "hostname": "R4",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "1b558e72-6671-48f8-849e-7f7df473e3aa",
            "mgmtIP": "123.20.20.20",
            "hostname": "R20",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "fc1e0e19-83a9-4f84-8e46-9ef7ae767b6e",
            "mgmtIP": "123.9.9.9",
            "hostname": "R9",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "f7eec066-c9b0-4e08-8ada-aad8f5e35a16",
            "mgmtIP": "123.10.10.10",
            "hostname": "R10",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "f51f6e8e-d4ef-47af-9139-74a18691c052",
            "mgmtIP": "123.20.1.2",
            "hostname": "R16",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        },
        {
            "id": "2ef50fff-eb73-49da-8599-45c68b876275",
            "mgmtIP": "10.18.19.18",
            "hostname": "R18",
            "deviceTypeName": "Cisco Router",
            "firstDiscoverTime": "0001-01-01T00:00:00",
            "lastDiscoverTime": "0001-01-01T00:00:00"
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
}


# Successful response with hostname = "R3"
{
    "devices": [
        {
            "id": "1e8029be-a858-48bd-b532-54b694edc529",
            "mgmtIP": "10.120.14.5",
            "hostname": "R3",
            "deviceTypeName": "Cisco Router"
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
}


# Successful response with ip = "10.1.12.2"
{
    "devices": [
        {
            "id": "ad53a0f6-644a-400b-9216-8df746baed3b",
            "mgmtIP": "10.1.12.2",
            "hostname": "Client1",
            "deviceTypeName": "Cisco Router"
        }
    ],
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

try:
    response = requests.get(full_url, headers=headers, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 
```

    {'devices': [{'id': 'ad53a0f6-644a-400b-9216-8df746baed3b', 'mgmtIP': '10.1.12.2', 'hostname': 'Client1', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'cd97d9ce-1d39-421d-a56d-e8da3aaa08c7', 'mgmtIP': '10.1.13.2', 'hostname': 'Client2', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '612a963c-e6cd-4ed1-8742-67b664dd214c', 'mgmtIP': '10.2.18.2', 'hostname': 'Client4', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '1a5d49f5-3755-4aad-b27d-cb5760aa494d', 'mgmtIP': '10.1.20.130', 'hostname': 'Client7', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '77242378-e865-449e-adeb-c4eeaf361853', 'mgmtIP': '10.1.14.2', 'hostname': 'Client3', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'fb1c1785-66a7-45cf-8cc6-98f637e8ad39', 'mgmtIP': '10.2.19.2', 'hostname': 'Client5', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '575fd214-acdf-427c-914a-2acd2aedb6af', 'mgmtIP': '123.12.12.12', 'hostname': 'R12', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '4b814621-05d0-4dd2-98e0-59d79b1ec410', 'mgmtIP': '123.11.11.11', 'hostname': 'R11', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '432d39b7-9729-4313-af18-3cbbf8473663', 'mgmtIP': '123.20.1.3', 'hostname': 'SW5', 'deviceTypeName': 'Cisco IOS Switch', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '1d8c841f-a9bc-4288-aab2-6322bbb1ab1b', 'mgmtIP': '10.18.19.19', 'hostname': 'R19', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'bbfbc73f-3425-4286-9402-fda3bc4e7661', 'mgmtIP': '123.14.14.14', 'hostname': 'R14', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'de62bda7-b285-4750-97bc-419570b58439', 'mgmtIP': '123.204.4.4', 'hostname': 'SW4', 'deviceTypeName': 'Cisco IOS Switch', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'c61cde7b-7ddf-41de-bc2f-dafae6c7c7ef', 'mgmtIP': '123.203.3.3', 'hostname': 'SW3', 'deviceTypeName': 'Cisco IOS Switch', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '5074459d-1435-4f65-a323-94c7dffcd3a9', 'mgmtIP': '123.13.13.13', 'hostname': 'R13', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'ff8b6bbc-4348-4f60-a202-2616ab37af9d', 'mgmtIP': '10.1.20.2', 'hostname': 'Client6', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'eb31a451-3236-4681-b46e-9084e7e01765', 'mgmtIP': '10.120.15.1', 'hostname': 'R2', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '64a80717-49a3-4f61-829b-926d1dabde79', 'mgmtIP': '123.1.1.1', 'hostname': 'R1', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'c1f0d040-7b93-4ddf-a1df-04e8ce276107', 'mgmtIP': '123.10.1.14', 'hostname': 'R5', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '1e8029be-a858-48bd-b532-54b694edc529', 'mgmtIP': '10.120.14.5', 'hostname': 'R3', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '98c00148-016f-43fc-9c1d-926fc728551e', 'mgmtIP': '123.15.15.15', 'hostname': 'R15', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '183b658c-c8d8-4623-bb76-1f670f0e09a3', 'mgmtIP': '123.8.8.8', 'hostname': 'R8', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '0d2c8440-307b-46a1-8c72-12fd670ad86c', 'mgmtIP': '123.6.6.6', 'hostname': 'R6', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'b95dbda8-64a0-44cb-a12e-79478a2e1f3b', 'mgmtIP': '123.20.1.10', 'hostname': 'R17', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '4fcaf03f-8d26-47c9-9dba-37d41e09d741', 'mgmtIP': '123.7.7.7', 'hostname': 'R7', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '2f410fd9-8b43-4bba-ab0f-54922951739d', 'mgmtIP': '123.20.1.11', 'hostname': 'SW6', 'deviceTypeName': 'Cisco IOS Switch', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '4222a806-6646-40fc-bd19-11294940434e', 'mgmtIP': '123.10.1.18', 'hostname': 'R4', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '1b558e72-6671-48f8-849e-7f7df473e3aa', 'mgmtIP': '123.20.20.20', 'hostname': 'R20', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'fc1e0e19-83a9-4f84-8e46-9ef7ae767b6e', 'mgmtIP': '123.9.9.9', 'hostname': 'R9', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'f7eec066-c9b0-4e08-8ada-aad8f5e35a16', 'mgmtIP': '123.10.10.10', 'hostname': 'R10', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': 'f51f6e8e-d4ef-47af-9139-74a18691c052', 'mgmtIP': '123.20.1.2', 'hostname': 'R16', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}, {'id': '2ef50fff-eb73-49da-8599-45c68b876275', 'mgmtIP': '10.18.19.18', 'hostname': 'R18', 'deviceTypeName': 'Cisco Router', 'firstDiscoverTime': '0001-01-01T00:00:00', 'lastDiscoverTime': '0001-01-01T00:00:00'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    


```python
# within hostname or ip
hostname = "R3"
# ip = "10.1.12.2"

query = {"hostname" : hostname}
#query = {"ip" : ip}

try:
    response = requests.get(full_url, headers=headers, params = query, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print("Get Devices failed! - " + str(response.text))
except Exception as e:
    print (str(e)) 
```

    {'devices': [{'id': '1e8029be-a858-48bd-b532-54b694edc529', 'mgmtIP': '10.120.14.5', 'hostname': 'R3', 'deviceTypeName': 'Cisco Router'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl -X GET \
  'http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices?token=e074d192-3f21-4ae8-b5f1-405d240b65ca&ip=10.1.12.2' \
  -H 'Postman-Token: e0ba3bb8-aac1-4084-9e95-de424cbf7feb' \
  -H 'cache-control: no-cache'
```

# Error Examples and Note


```python
###################################################################################################################    

"""Error 1: the device with hostname does not exist"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
    hostname = "blahblahblah" #There is no device with a hostname called "blahblahblah" in users working domain.
    
Response:
    
    "{
        'devices': [], 
        'statusCode': 790200, 
        'statusDescription': 'Success.'
    }"

###################################################################################################################    

"""Error 2: wrong format ip"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
    ip = "101122" #the correct ip should be "10.1.12.2"
    
Response:
    
    "{
        'devices': [], 
        'statusCode': 790200, 
        'statusDescription': 'Success.'
    }"

###################################################################################################################    

"""Note 1 : If user provide hostname and ip together but not belongs to one device, 
            then the response device is correspond to the hostname"""
```
