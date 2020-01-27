
# Authentication and Authorization API

## ***GET*** /V1/CMDB/Domains/{?tenantId}
Use this function returns a list of accessible domains in a specific tenant. The returned accessible domains vary by the user privileges you use to log in. To retrieve a full list of domains in a specified tenant, you must log in with system admin or tenant admin permissions. 

## Detail Information

> **Title** : Get all accessible domains of a tenants API<br>

> **Version** : 01/23/2019.

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/API/V1/CMDB/Domains

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|Bearer Authentication| Parameters | Authentication token | 

 ## Request body(****required***)

>No request body.

 ## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
| tenantId* | string  | Unique identifier for the tenant from which you desire to retrieve the domain information. tenantId can be retrieved from get all accessible tenants.<br> **Note:** If user don't have the privilege to visit all tenants, specific tenantId is required for this API. |

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
|domains | array | A list of all accessible domains. |
|domainId| string | The domain ID.  |
|domainName| string | The domain name. |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***


```python
{
    'domains': [
        {
            'domainId': '850ff5e9-c639-404d-85a3-d920dbee509c', 
            'domainName': 'Support and Service'
        }, 
        {
            'domainId': '0201adc4-ae96-46f0-ae3d-01cdba9e41d6', 
            'domainName': 'GE Test'
        }
    ], 
    
    'statusCode': 790200, 
    'statusDescription': 'Success.'
}
```

 ## Full Example : 


```python
# import python modules 
import requests
import time
import urllib3
import pprint
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

# Set the request inputs
token = "4f257785-d5f9-42d4-b896-d21f0cb62e6f"
tenantId = "fb24f3f0-81a7-1929-4b8f-99106c23fa5b"
full_url = "http://192.168.28.79/ServicesAPI/API/V1/CMDB/Domains"

# Set proper headers
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

data = {"tenantId": tenantId}

try:
    # Do the HTTP request
    response = requests.get(full_url, params=data, headers=headers, verify=False)
    # Check for HTTP codes other than 200
    if response.status_code == 200:
        # Decode the JSON response into a dictionary and use the data
        result = response.json()
        print (result)
    else:
        print ("Get domains failed! - " + str(response.text))

except Exception as e: print (str(e))
```

    {'domains': [{'domainId': '850ff5e9-c639-404d-85a3-d920dbee509c', 'domainName': 'Support and Service'}, {'domainId': '0201adc4-ae96-46f0-ae3d-01cdba9e41d6', 'domainName': 'GE Test'}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman


```python
curl --location --request GET 'https://integrationLab.netbraintech.com/ServicesAPI/API/V1/CMDB/Domains?tenantId=40e0032e-14e7-4fea-7d00-8fe8bd65efae' \
--header 'token: 6a2ad6ac-c048-4794-859a-321a407f3e3f'
```

## Error Examples


```python
###################################################################################################################    

"""Error 1: empty tenantId"""

Input:
    token = "4f257785-d5f9-42d4-b896-d21f0cb62e6f"
    tenantId = ""
    full_url = "http://IP address of your NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Domains"

Response:
    "{'domains': [], 'statusCode': 790200, 'statusDescription': 'Success.'}"

###################################################################################################################    

"""Error 2: wrong tenantId"""

Input:
    token = "4f257785-d5f9-42d4-b896-d21f0cb62e6f"
    tenantId = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    full_url = "http://IP address of your NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Domains"

Response:
    """Get domains failed! - 
    {"statusCode":791006,
    "statusDescription":"tenant with id aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa does not exist."}"""
```
