
# Tenant Domain Management API Design

## ***POST*** /V1/CMDB/Tenants
Calling this API to add a tenant to users Netbrain system.

## Detail Information

> **Title** : Add Tenant API<br>

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
|tenantName* | string  | The name of the created tenant.  |
|maximumNodes* | integer  | The maximum license nodes that the tenant owns. The number must be greater than 0.  |
|description | string  | The description about the tenant.  |


> ***Example***


```python
{
    "tenantName": "TenantName",
    "description": "Description",
    "maximumNodes": 5,

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
|tenantId| string | The tenant ID.  |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
{
    "statusCode": 790200,
    "statusDescription": "string",
    "tenantId": "3e75247a-309c-4231-96a5-823b6cb1e78d"
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

tenantName = "testTenant"
maximumNodes = 100

body = {
    "tenantName" : tenantName,
    "maximumNodes" : maximumNodes
}

try:
    response = requests.post(full_url, data = json.dumps(body), headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Add tenant failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'tenantId': '6f4e381a-1752-4b84-8a59-6ed6391614cf', 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X POST \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Tenants \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: b91448a7-608e-4aad-bfa7-6b1adf21b6fd' \
  -H 'cache-control: no-cache' \
  -H 'token: 855b2da0-306b-4c29-b37f-be09e33e2d02' \
  -d '{
        "tenantName" : "testTenant",
        "maximumNodes" : 100
    }'
```

 # Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
        
        tenantName = "" # Can not be null
        maximumNodes = None # Can not be null
        
Response:
    
        "Add tenant failed! - 
            {
                "statusCode":791000, 
                "statusDescription":"Null parameter: the parameter 'tenantName' cannot be null."
            }"
            
        
        "Add tenant failed! - 
            {
                "statusCode":791000,
                "statusDescription":"Null parameter: the parameter 'maximumNodes' cannot be null."
            }"

###################################################################################################################    

"""Error 1: wrong inputs""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
        
        tenantName = 12345
        maximumNodes = "1"
        
Response:
    
            "{
                'tenantId': '2492adc4-6014-4c1f-b2d3-be4dadc4dd3e', 
                'statusCode': 790200, 
                'statusDescription': 'Success.'
            }"

###################################################################################################################    

"""Error 1: input tenant name already exist"""

Input:
        
        tenantName = "testTenant" # tenant named as "testTenant" already exist.
        maximumNodes = 100
        
Response:
    
            "Add tenant failed! - 
                {
                    "statusCode":791007,
                    "statusDescription":"tenant testTenant already exists."
                }"

```
