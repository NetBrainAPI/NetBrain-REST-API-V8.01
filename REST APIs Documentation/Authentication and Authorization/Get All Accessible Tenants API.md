
# Authentication and Authorization API

## ***GET*** /V1/CMDB/Tenants/
This method returns a list of accessible tenants (including tenant ID and names). The returned tenants list varies by the privileges of different user roles. To retrieve a full list of all available tenants, users must log in with admin role. 

## Detail Information

> **Title** : Get All Asseccible Tenants API<br>

> **Version** : 01/23/2019.

> **API Server URL** : http(s):// < NetBrain Web API Server Address > /ServicesAPI/API/V1/CMDB/Tenants

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication| Parameters | Authentication token | 

## Request body(****required***)

>No request body.

 ## Parameters(****required***)

> No parameters required

 ## Headers

> **Data Format Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| Content-Type | string  | support "application/json" |
| Accept | string  | support "application/json" |

> **Authorization Headers**

|**Name**|**Type**|**Description**|
|------|------|------|
| token* | string  | Authentication token, get from login API. |


 ## Response

|**Name**|**Type**|**Description**|
|------|------|------|
|tenants | array | A list of all accessible tenants.  |
|tenantId| string | The tenant ID.  |
|tenantName| string | The tenant name. |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

> ***Example*** :


```python
{
    'tenants': [
        {
            'tenantId': 'fb24f3f0-81a7-1929-4b8f-99106c23fa5b', 
            'tenantName': 'Initial Tenant'
        }
    ], 
    'statusCode': 790200, 
    'statusDescription': 'Success.'
}
```

## Full Example : 


```python
# import python modules 
import json
import requests
import time
import urllib3
import pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

token = "828a4561-5ee5-40ac-bf98-01788be48330" 
full_url = "http://192.168.28.79/ServicesAPI/API/V1/CMDB/Tenants"

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

try:
    # Do the HTTP request
    response = requests.get(full_url, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Get tenants failed! - " + str(response.text))
except Exception as e: return (str(e))

```




    {'tenants': [{'tenantId': 'fb24f3f0-81a7-1929-4b8f-99106c23fa5b',
       'tenantName': 'Initial Tenant'}],
     'statusCode': 790200,
     'statusDescription': 'Success.'}



# cURL Code from Postman


```python
curl --location --request GET 'https://integrationlab.netbraintech.com/ServicesAPI/API/V1/CMDB/Tenants' \
--header 'token: 6a2ad6ac-c048-4794-859a-321a407f3e3f'
```

## Error Example : 


```python
###################################################################################################################    

"""Error 1: empty url"""

Input:
    token = "828a4561-5ee5-40ac-bf98-01788be48330" 
    
    full_url = ""  

Response:
    "Invalid URL'': No schema supplied. Perhaps you meant http://"

###################################################################################################################    

"""Error 2: wrong url"""

Input:
    token = "828a4561-5ee5-40ac-bf98-01788be48330" 
    
    full_url = "http://192.1688.28.79/ServicesAPI/API/V1/CMDB/Tenants"  

Response:
    """HTTPConnectionPool(host='192.1688.28.79', port=80): 
       Max retries exceeded with url: /ServicesAPI/API/V1/Session (Caused by NewConnectionError(
           '<urllib3.connection.HTTPConnection object at 0x0000022F203C79B0>: 
           Failed to establish a new connection: [Errno 11001] getaddrinfo failed'))"""
    
###################################################################################################################    

"""Error 3: empty token"""

Input:
    token = "" 
    
    full_url = "http://192.168.28.79/ServicesAPI/API/V1/CMDB/Tenants"  

Response:
    { "statusCode": 795005, "statusDescription": "Invalid token. }
     
###################################################################################################################    

"""Error 4: wrong token"""

Input:
    token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" 
    
    full_url = "http://192.168.28.79/ServicesAPI/API/V1/CMDB/Tenants"  

Response:
    { "statusCode": 795005, "statusDescription": "Invalid token. }
```
