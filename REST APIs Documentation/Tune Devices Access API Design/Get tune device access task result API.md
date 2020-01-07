
# Tune Devices Access REST API Design

## GET /V1/CMDB/TuneDevices

This API call is used to get tune task status and result

## Detail Information

>**Title:** Get Tune Devices Access Task Result API

>**Version:** 01/07/2020

>**API Server URL:** http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/TuneDevices

>**Authentication:**

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication|Headers|Authentication token|

## Request Body (*required)

>No request body.

## Query Parameters (*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|taskId|bool| The tune task id. |
|begin| int | Begin index of data, API will return device tune result begin = "begin". |
|count|	int | Count of returned data, API will return device tune result, the total number = "count".|
|hostnames|	list of string	| List all devices that need to return tune result.<br> If Hostnames has value then Begin and Count are useless. <br>If Hostnmaes has no value then, we use Begin and Count to return tune results.|

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
|taskId	|string	|tune device task ID, which can be use to query task status later on.|
|status	|int	|Status code. 0 for success|
|devices|	list of object|	device tune results|
|devices.deviceName	|string|	device name|
|devices.log	|string	|device tune result|
|devices.TuneState|	list of object|	tune results of a device|
|devices.TuneState.Enable|	string	|cli enable result|
|devices.TuneState.Hostname|	string|	hostname|
|devices.TuneState.LiveHostname|	string	|live get hostname|
|devices.TuneState.Login|	string|	login result|
|devices.TuneState.MgrIntf|	string	|management interface|
|devices.TuneState.MgrIp|	string|	management IP|
|devices.TuneState.Model|	string	|model name|
|devices.TuneState.NetworkServer|	string	|networkserver name|
|devices.TuneState.Ping|	string	|ping result|
|devices.TuneState.SnmpRo|	string	|snmpRo information|
|devices.TuneState.TelnetSSH |	string	|telnet ssh result|
|devices.TuneState.Vendor|	string	|vendor name|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

>***Example***


```python
{
    "taskId": "8bf5fc21-911b-4e63-8acf-e3fe0be72fc4",
    "status": 3,
    "devices": [
        {
            "deviceName": "US-BOS-SW3",
            "log": "15:44:53 Begin tune process\r\n15:44:54 Ping [10.8.1.30] via FS2(192.168.28.194); Succeeded\r\n15:44:54 Send RO = [public][version:v2c] to [10.8.1.30] via FS2(192.168.28.194); Succeeded\r\n15:44:55 Retrieving [10.8.1.30]'s Hostname ,Vendor and Model via FS2(192.168.28.194); Succeeded\r\n15:44:55 Telnet to device 10.8.1.30 via FS2(192.168.28.194)\n15:44:55 Telnet to device 10.8.1.30 successfully via FS2(192.168.28.194)\n15:44:55 Return from Device:[Username:]\n15:44:55 Sending Username:netbrain\n15:44:55 Return from Device:[Password:]\n15:44:55 Sending Password:******\n15:44:57 Return from Device:[US-BOS-SW3>]\n15:44:57 Sending \"enable\" command\n15:44:57 Return from Device:[Password:]\n15:44:57 Sending Enable Password:******\n15:44:58 Return from Device:[US-BOS-SW3#]\n15:44:58 Sending \"enable\" command\n15:44:58 Return from Device:[US-BOS-SW3#]\n15:44:58 Sending \"exit\" command\n15:44:58 Telnet to device 10.8.1.30 disconnected.\n15:44:58 End tune process\r\n",
            "TuneState": {
                "ping": "Succeeded",
                "mgrIp": "10.8.1.30",
                "mgrIntf": "Vlan101",
                "telnetSSH": "Succeeded",
                "login": "Succeeded",
                "enable": "Succeeded",
                "snmpRo": "public",
                "hostname": "",
                "liveHostname": "Unchanged",
                "vendor": "Cisco",
                "model": "3560E",
                "networkServer": "FS2(192.168.28.194)"
            }
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
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

token = "7962f853-2fb7-4b5f-98e1-4fd98dc2dc33" 
nb_url = "https://integrationlab.netbraintech.com"
# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

taskId = '8bf5fc21-911b-4e63-8acf-e3fe0be72fc4'

full_url = nb_url + "/ServicesAPI/API/V1/CMDB/TuneDevices/" 
tuneRes = {
    "taskId" : taskId,
#     "Begin" : 0,
#     "Count" : 2
    "hostnames": ["US-BOS-SW3"]
}


try:
    response = requests.get(full_url, params = tuneRes, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Tune devices task failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'taskId': '8bf5fc21-911b-4e63-8acf-e3fe0be72fc4', 'status': 3, 'devices': [{'deviceName': 'US-BOS-SW3', 'log': '15:44:53 Begin tune process\r\n15:44:54 Ping [10.8.1.30] via FS2(192.168.28.194); Succeeded\r\n15:44:54 Send RO = [public][version:v2c] to [10.8.1.30] via FS2(192.168.28.194); Succeeded\r\n15:44:55 Retrieving [10.8.1.30]\'s Hostname ,Vendor and Model via FS2(192.168.28.194); Succeeded\r\n15:44:55 Telnet to device 10.8.1.30 via FS2(192.168.28.194)\n15:44:55 Telnet to device 10.8.1.30 successfully via FS2(192.168.28.194)\n15:44:55 Return from Device:[Username:]\n15:44:55 Sending Username:netbrain\n15:44:55 Return from Device:[Password:]\n15:44:55 Sending Password:******\n15:44:57 Return from Device:[US-BOS-SW3>]\n15:44:57 Sending "enable" command\n15:44:57 Return from Device:[Password:]\n15:44:57 Sending Enable Password:******\n15:44:58 Return from Device:[US-BOS-SW3#]\n15:44:58 Sending "enable" command\n15:44:58 Return from Device:[US-BOS-SW3#]\n15:44:58 Sending "exit" command\n15:44:58 Telnet to device 10.8.1.30 disconnected.\n15:44:58 End tune process\r\n', 'TuneState': {'ping': 'Succeeded', 'mgrIp': '10.8.1.30', 'mgrIntf': 'Vlan101', 'telnetSSH': 'Succeeded', 'login': 'Succeeded', 'enable': 'Succeeded', 'snmpRo': 'public', 'hostname': '', 'liveHostname': 'Unchanged', 'vendor': 'Cisco', 'model': '3560E', 'networkServer': 'FS2(192.168.28.194)'}}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

    D:\Anaconda\lib\site-packages\urllib3\connectionpool.py:847: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
      InsecureRequestWarning)
    

# cURL Code from Postman:


```python
curl -X GET \
  'https://integrationlab.netbraintech.com/ServicesAPI/API/V1/CMDB/TuneDevices?taskId=8bf5fc21-911b-4e63-8acf-e3fe0be72fc4&Begin=0&Count=1' \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: integrationlab.netbraintech.com' \
  -H 'Postman-Token: 0da5e0c3-a3c5-49a6-aa25-c04cd97cf612,ce1dba50-dd15-4912-96ee-3646651b7659' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'token: 7962f853-2fb7-4b5f-98e1-4fd98dc2dc33'
```
