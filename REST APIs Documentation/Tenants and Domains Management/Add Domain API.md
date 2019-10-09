
# Tenant Domain Management API Design

## ***POST*** /V1/CMDB/Domains
Calling this API to create a new domain in current tenant.

## Detail Information

> **Title** : Add Domain API<br>

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
|tenantId* | string | The tenant ID.  |
|domainName* | string | The name of the created domain.  |
|maximumNodes | integer  | The maximum license nodes that the tenant owns. The number must be greater than 0.  |
|description | string  | The description about the tenant.  |


> ***Example***


```python
{
    "tenantId": "4e75247a-309c-4231-96a5-823b6cb1e78d",
    "domainName": "domainName",
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
|tenantId| string | The tenant ID.  |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
{
    "statusCode": 790200,
    "statusDescription": "string",
    "domainId": "3e75247a-309c-4231-96a5-823b6cb1e78d"
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

tenantId = "6f4e381a-1752-4b84-8a59-6ed6391614cf"
domainName = "testDomain"
maximumNodes = 5

body = {
    "tenantId" : tenantId,
    "domainName" : domainName,
    "maximumNodes" : maximumNodes
}

try:
    response = requests.post(full_url, data = json.dumps(body), headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Create a domain failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'domainId': '668489d7-54d9-41a9-a04e-0283f46e9135', 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X POST \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Domains \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 2d39e7fc-af8e-4295-a476-3544f288f85a' \
  -H 'cache-control: no-cache' \
  -H 'token: 855b2da0-306b-4c29-b37f-be09e33e2d02' \
  -d '{
        "tenantId" : "6f4e381a-1752-4b84-8a59-6ed6391614cf",
        "domainName" : "testDomain1",
        "maximumNodes" : 1
    }'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
        
        tenantId = "" # Can not be null
        domainName = "" # Can not be null
        maximumNodes = None # Can not be null
        
Response:
    
        "Create a domain failed! - 
            {
                "statusCode":791000,
                "statusDescription":"Null parameter: the parameter 'tenantId' cannot be null."
            }"
            
        
        "Create a domain failed! - 
            {
                "statusCode":791000,
                "statusDescription":"Null parameter: the parameter 'domainName' cannot be null."
            }"
            
            
        "Create a domain failed! - 
            {
                "statusCode":791000
                "statusDescription":"Null parameter: the parameter 'maximumNodes' cannot be null."
            }"

###################################################################################################################    

"""Error 2: wrong inputs"""

Input:
        
        tenantId = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" # No tenant have a ID like this.
        domainName = "testDomain2"
        maximumNodes = 1

        
Response:
    
            "Create a domain failed! - 
                {
                    "statusCode":791006,
                    "statusDescription":"tenant with id XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX does not exist."
                }"

#--------------------------------------------------------------------------------------------------------------------

Input:""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
        tenantId = "6f4e381a-1752-4b84-8a59-6ed6391614cf"
        domainName = 12345 # Shouldn't be integer
        maximumNodes = 1

        
Response:
    
            "{
                'domainId': 'c5ed26e6-c2ed-47b3-8b00-8aa4c016a5c3', 
                'statusCode': 790200, 
                'statusDescription': 'Success.'
            }"
            
#--------------------------------------------------------------------------------------------------------------------

Input:""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
        
        tenantId = "6f4e381a-1752-4b84-8a59-6ed6391614cf"
        domainName = 123456
        maximumNodes = "10" # Shouldn't be string

        
Response:
    
            "{
                'domainId': '9f43080f-d502-4ddb-9c76-006c3ef665ad', 
                'statusCode': 790200, 
                'statusDescription': 'Success.'
            }"
            
###################################################################################################################    

"""Error 3: domain maximumNodes greater than tenant maximumNodes"""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
        
        tenantId = "6f4e381a-1752-4b84-8a59-6ed6391614cf"
        domainName = "1234567"
        maximumNodes = 100 # the rest node in current domain is less than 100.

        
Response:
    
            "Create a domain failed! - 
                {
                    "statusCode":791002,
                    "statusDescription":"Invalid value , node size requested: 100, available: 83"
                }

###################################################################################################################    

"""Error 4: duplicate created"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
        
        tenantId = "6f4e381a-1752-4b84-8a59-6ed6391614cf"
        domainName = "testDomain" # domain named as "testDomain" in current domain is already exist.
        maximumNodes = 5


        
Response:
    
            "Create a domain failed! - 
                {
                    "statusCode":791007,
                    "statusDescription":"domain testDomain already exists."
                }"
```
