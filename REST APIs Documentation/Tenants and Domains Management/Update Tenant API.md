
# Tenant Domain Management API Design

## ***PUT*** /V1/CMDB/Tenants
Calling this API to update a tenant specified by tenant id (how to get ID? see Get All Tenants).

## Detail Information

> **Title** : Update Tenant API<br>

> **Version** : 02/05/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Tenants	

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|tenantId* | string | The tenant ID.  |
|tenantName* | string  | The name of the created tenant.  |
|maximumNodes | integer  | The maximum license nodes that the tenant owns. The number must be greater than 0.  |
|description | string  | The description about the tenant.  |


> ***Example***


```python
{
    "tenantId": "4e75247a-309c-4231-96a5-823b6cb1e78d",
    "tenantName": "TenantName",
    "description": "Description",
    "maximumNodes": 5
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
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Tenants"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

tenantId = "2492adc4-6014-4c1f-b2d3-be4dadc4dd3e"
tenantName = "testTenantNewName"
maximumNodes = 10

body = {
    "tenantId" : tenantId,
    "tenantName" : tenantName,
    "maximumNodes" : maximumNodes
}

try:
    response = requests.put(full_url, data = json.dumps(body), headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Add tenant failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X PUT \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Tenants \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 9b324059-cd0d-45ac-926e-cc7fcfe0f9b8' \
  -H 'cache-control: no-cache' \
  -H 'token: 855b2da0-306b-4c29-b37f-be09e33e2d02' \
  -d '{
        "tenantId": "2492adc4-6014-4c1f-b2d3-be4dadc4dd3e",
        "tenantName": "testTenantNewName2",
        "description": "Description",
        "maximumNodes": 5
    }'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
        
        tenantId = "" # Can not be null.
        tenantName = ""
        maximumNodes = None
        
Response:
    
        # tenantId = "" 
        "Add tenant failed! - 
            {
                "statusCode":791000,
                "statusDescription":"Null parameter: the parameter 'tenantId' cannot be null."
            }"
          
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        # tenantName = "" 
        "{
            'statusCode': 790200, 
            'statusDescription': 'Success.'
        }"
          
        """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        # maximumNodes = None 
        "{
            'statusCode': 790200, 
            'statusDescription': 'Success.'
        }"
        
###################################################################################################################    

"""Error 1: wrong tenantId inputs"""

Input:
        
        tenantId = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # No tenant called "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        tenantName = "testTenantNewName5"
        maximumNodes = None

        
Response:
    
        "Add tenant failed! - 
            {
                "statusCode":791006,
                "statusDescription":"tenant with id XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX does not exist."
            }"
        
###################################################################################################################    

"""Error 1: duplicate update"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
        
        tenantId = "2492adc4-6014-4c1f-b2d3-be4dadc4dd3e" # No any new informations.
        tenantName = "testTenantNewName"
        maximumNodes = 10

        
Response:
    
            "{
                'statusCode': 790200, 
                'statusDescription': 'Success.'
            }"
        

```
