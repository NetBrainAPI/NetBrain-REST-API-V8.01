
# Device API Design

## ***GET*** /V1/CMDB/Devices/decive/FrontServer{?hostname}
Call this API to set a value for the specified attriute of a device.

* ## Detail Information

> **Title** : Get Front Server of a device API<br>

> **Version** : 04/05/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Devices/device/FrontServer

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

* ## Request body(****required***)

>No request body.

* ## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|hostname* | string  | The hostname of the target device. |

* ## Headers

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

* ## Response

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|alias | string | the alias of the front server  |
|ipOrHostname| string | the ip or hostname of the front server  |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***


```python
{
    "statusCode": 793404,
    "statusDescription": "No resource"
}

# If customer don't have enough privilige:
{
    "statusCode":795003,
    "statusDescription":"Insufficient permissions: the current user has insufficient permissions to perform the requested operation. The user has no tenant or domain access permission.sharePolicyManagement"
}
```

* # Full Example:


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "6b56c382-5577-49fa-a9a4-444e80831562"
nb_url = "http://192.168.28.79"
hostname = "R10"

data = {
    "hostname":hostname
}

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Devices/device/FrontServer"
try:
    response = requests.get(full_url, headers=headers, params = data, verify=False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get front server failed! - " + str(response.text))

except Exception as e:
    print (str(e))   
```

    {'alias': 'NetBrainServer', 'ipOrHostname': '192.168.28.79', 'statusCode': 790200, 'statusDescription': 'Success.'}
    

* # cURL Code from Postman


```python
curl -X GET \
  'http://192.168.28.79/ServicesAPI/API/V1/CMDB/Devices/device/FrontServer?hostname=R10' \
  -H 'Postman-Token: 4a9bba1f-85ff-4f36-9eee-a1abd1cceec3' \
  -H 'cache-control: no-cache' \
  -H 'token: 6b56c382-5577-49fa-a9a4-444e80831562'
```
