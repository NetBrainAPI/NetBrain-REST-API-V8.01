
# Discovery API Design

## ***DELETE*** /V1/CMDB/Discovery/Tasks/{task}/Seeds
Call this API to remove specific IP addresses from  a discovery task, if list is empty, remove all.
> **Note**: {task} means {taskId} or {taskName}

## Detail Information

> **Title** : Add Seed IP(s) To Discovery API<br>

> **Version** : 01/28/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Discovery/Tasks/{taskId or taskName}/Seeds

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

> No request body.

## Path Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|tasks.id*| string | The ID of a discovery task.  |
|tasks.name*| string | The name of a discovery task. |
>>**Note:** two parameters can only provide one to call this API and must provide one parameter.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|ips| List of string | The list of device mgmIPs. Optional, remove all devices from this task if not specified.|

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

> ***Example***


```python
{
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
token = "fd8b3f95-adc6-406d-9c18-bdb155de2ced"
nb_url = "http://192.168.28.79"

mgmIP1 = "10.1.13.2"
mgmIP2 = "123.1.1.1"
mgmIP3 = "10.1.14.2"
#mgmIP4 = "123.203.3.3"
#mgmIP5 = "123.204.4.4"
#mgmIP6 = "123.20.1.3"

taskID = "34124e63-31d6-dfad-f5fa-05ae0ebb4b49"
##OR##
#taskName = "testGDL_DT1"

body = {
    "ips" : [mgmIP1, mgmIP2, mgmIP3]
    }
 
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"]=token
full_url= nb_url + "/ServicesAPI/API/V1/CMDB/Discovery/Tasks/"+str(taskID)+"/Seeds"

try:
    # Do the HTTP request
    response = requests.delete(full_url, params = body, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print("IP Add Failed - " + str(response.text))
    
except Exception as e:
    print (str(e)) 

```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl --location --request DELETE 'https://integrationlab.netbraintech.com/ServicesAPI/API/V1/CMDB/Discovery/Tasks/SNOW_CMDB_Test/Seeds?ips=10.1.13.2' \
--header 'token: d9d75950-8d49-48fd-b20b-0510602bef28'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty mgmIPs list """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
        mgmIP1 = ""
        mgmIP2 = ""
        mgmIP3 = ""
        taskID = "34124e63-31d6-dfad-f5fa-05ae0ebb4b49"
        ##OR##
        #taskName = "testGDL_DT1"

Response:
    
    "{
        "statusCode": 790200,
        "statusDescription": "Success."
    }"
    
################################################################################################################### 
    
"""Error 1: devices in mgmIPs list already deleted"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
        mgmIP1 = "10.1.13.2" #already not exist in DT
        mgmIP2 = "123.1.1.1" #already not exist in DT
        mgmIP3 = "10.1.14.2" #already not exist in DT
        taskID = "34124e63-31d6-dfad-f5fa-05ae0ebb4b49"
        ##OR##
        #taskName = "testGDL_DT1"

Response:
    
    "{
        "statusCode": 790200,
        "statusDescription": "Success."
    }"
    
```
