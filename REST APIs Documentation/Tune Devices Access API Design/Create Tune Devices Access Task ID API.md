
# Tune Devices Access REST API Design

## POST /V1/CMDB/TuneDevices

This API call is used to start a tune devies task.

## Detail Information

>**Title:** Create Tune Devices Access Task ID API

>**Version:** 01/07/2020

>**API Server URL:** http(s)://IP Address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/TuneDevices

>**Authentication:**

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication|Headers|Authentication token|

## Query Parameters (*required)

>No request query parameter.

## Request Body (*required)

|**Name**|**Type**|**Description**|
|------|------|------|
|IsCheckPing|	bool|	if ping the IP when tuning a device|
|IsCheckSnmp| bool| if do snmp on the device when tuning a device|
|IsCheckCliLogin|	bool| if check cli login when tuning a device|
|IsCheckCliEnable|	bool|	if check enable priority when tuning a device|
|hostnames|	list of string	|list all devices that need to be tuned, no value means all devices|

>***Example***


```python
{
    "isCheckPing" : True,
    "isCheckSnmp" : True,
    "isCheckCliLogin" : True,
    "isCheckCliEnable" : True,
    "hostnames": ["US-BOS-SW3", "US-BOS-SW1"]
}
```

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
|taskId|string|tune device task ID, which can be use to query task status later on.|
|status|bool|Status code. true for success.|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

>***Example***


```python
{
    'taskId': '8bf5fc21-911b-4e63-8acf-e3fe0be72fc4', 
    'status': True, 
    'statusCode': 790200, 'statusDescription': 'Success.'
}
```

# Full Example：


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

full_url = nb_url + "/ServicesAPI/API/V1/CMDB/TuneDevices"
tunedata = {
    "isCheckPing" : True,
    "isCheckSnmp" : True,
    "isCheckCliLogin" : True,
    "isCheckCliEnable" : True,
    "hostnames": ["US-BOS-SW3", "US-BOS-SW1"]
}


try:
    response = requests.post(full_url, data = json.dumps(tunedata), headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Add devices to group failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'taskId': '7669f629-3465-4c3b-9909-8dea4d1257ab', 'status': True, 'statusCode': 790200, 'statusDescription': 'Success.'}
    

    D:\Anaconda\lib\site-packages\urllib3\connectionpool.py:847: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
      InsecureRequestWarning)
    

# cURL Code from Postman:


```python
curl -X POST \
  https://integrationlab.netbraintech.com/ServicesAPI/API/V1/CMDB/TuneDevices \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 176' \
  -H 'Content-Type: application/json' \
  -H 'Host: integrationlab.netbraintech.com' \
  -H 'Postman-Token: 0874d561-a2ee-4f7c-8c3b-49c8f48ae09d,f59b389d-7e7f-471f-be82-898f05093d45' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'token: 7962f853-2fb7-4b5f-98e1-4fd98dc2dc33' \
  -d '{
    "isCheckPing" : "True",
    "isCheckSnmp" : "True",
    "isCheckCliLogin" : "True",
    "isCheckCliEnable" : "True",
    "hostnames": ["US-BOS-SW3", "US-BOS-SW1"]
}'
```
