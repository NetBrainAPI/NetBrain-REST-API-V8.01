
# Site API Design

## ***GET*** /V1/CMDB/Sites{?sitePath}|{?siteId}
Calling this API to get all devices belong to the site specified by site name.

NOTE:  must be a leaf site, error would return if the parameter is root site or a container site.

## Detail Information

> **Title** : Get Site Devices API<br>

> **Version** : 02/04/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Sites/Devices

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

>No request body.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|sitePath^ | string  | Full path name of a site. For example, 'My Network/Site1/Boston/Dev'. |
|siteId^ | string  |  The unique id of specified site. |
>>**Note :** ^ required if the other parameter is null.

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
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |
|devices | list of object | A list of all devices.  |
|devices.id| string | Device id.  |
|devices.mgmtIP| string | Management ip of this device. |
|devices.hostname| string | Hostname of this device. |
|devices.deviceTypeName| string | Hostname of this device. |

> ***Example***


```python
{
    "devices": [],
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

# Full Exmaple:


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "1cde0ef4-4956-43ce-9e24-96d9a471e4fd"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/Devices"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

sitePath = "testSite1/testSiteLeaf"
##OR##
#sitId = "37965f93-377c-46b9-852c-193870bb5933"

data = {
           "sitePath" : sitePath
            # "sitId" : sitId
    }         

try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get Site Devices Failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'devices': [], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X GET \
  'http://192.168.28.79/ServicesAPI/API/V1/CMDB/Sites/Devices?sitePath=testSite1/testSiteLeaf' \
  -H 'Postman-Token: a870e233-6976-4c3a-a018-d2585da1a0c6' \
  -H 'cache-control: no-cache' \
  -H 'token: 1cde0ef4-4956-43ce-9e24-96d9a471e4fd'
```

# Error Examples:
Same with "delete a site API"
