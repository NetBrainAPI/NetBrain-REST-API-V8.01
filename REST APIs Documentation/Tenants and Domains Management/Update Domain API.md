
# Tenant Domain Management API Design

## ***PUT*** /V1/CMDB/Domains
Calling this API to update a domain specified by domain id(How to get ID? See Get All Domains of a Tenant.).

## Detail Information

> **Title** : Update Domain API<br>

> **Version** : 02/05/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Domains	

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|DomainId* | string | The domain ID.  |
|domainName | string | The name of current domain.  |
|maximumNodes | integer  | The maximum license nodes that the tenant owns. The number must be greater than 0.  |
|description | string  | The description about the tenant.  |


> ***Example***


```python
{
    "domainId": "5e75247a-309c-4231-96a5-823b6cb1e78d",
    "domainName": "TenantName",
    "description": "Description",
    "maximumNodes": "5"
}
```

## Parameters(****required***)

>No parameters required.

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
    "statusDescription": "success"
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
token = "855b2da0-306b-4c29-b37f-be09e33e2d02"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Domains"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

DomainId = "668489d7-54d9-41a9-a04e-0283f46e9135"
domainName = "testDomain"
maximumNodes = None

body = {
    "DomainId": DomainId,
    "domainName": domainName,
    "maximumNodes": maximumNodes
}

try:
    response = requests.put(full_url, data = json.dumps(body), headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Update domain failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X PUT \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Domains \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: d2cb2e99-c3d7-449a-be78-c7144cc88b10' \
  -H 'cache-control: no-cache' \
  -H 'token: 855b2da0-306b-4c29-b37f-be09e33e2d02' \
  -d '{
        "DomainId": "668489d7-54d9-41a9-a04e-0283f46e9135",
        "domainName": "testDomain",
        "maximumNodes": ""
    }'
```

# Error Examples:


```python
################################################################################################################### 

"""Basic errors similar with "Add Domain API" """

###################################################################################################################    

"""Error 1: munltiple update with same input values"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
        
        DomainId = "668489d7-54d9-41a9-a04e-0283f46e9135" # no new values in this update
        domainName = "testDomain"
        maximumNodes = None
        
Response:
    
        "{
            'statusCode': 790200, 
            'statusDescription': 'Success.'
        }"
            
###################################################################################################################    

"""Error 2: Id and name are not correspond """

Input:
        
        DomainId = "668489d7-54d9-41a9-a04e-0283f46e9135"
        domainName = "testDomain111"
        maximumNodes = None
        
Response:
    
        "{
            'statusCode': 790200, 
            'statusDescription': 'Success.'
        }"
            
        
```
