
# User API Design

## ***PUT*** /V1/CMDB/Users
Call this API to modify user information.

Note that, all optional fileds are only used to modify the value rather than to clear the value of this filed. so, if this filed is set to null or empty string, no change would be made for this field.

The only way to clear a field is delete a user and add this user back with new value.

## Detail Information

> **Title** : Update User API<br>

> **Version** : 02/01/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Users

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|username* | string  | The user name. This parameter is required.  |
|email* | string  | The email address of the user. This parameter is required. |
|firstName* | string  | The first name of the user. This parameter is required.  |
|lastName* | string  | The last name of the user. This parameter is required. |
|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|username* | string  | The user name. This parameter is required.  |
|email* | string  | The email address of the user. This parameter is required. |
|firstName* | string  | The first name of the user. This parameter is required.  |
|lastName* | string  | The last name of the user. This parameter is required. |
|password* | string  | The login password. The allowed length is 6-128 characters by default. This parameter is required.  |
|authenticationServer | string |The name of the authentication server for create an external account.|
|phoneNumber | string |The phone number of the user.|
|department | string |The department that the user belongs to.|
|description | string |Any description about the account.|
|allowChangePassword | bool |Specify whether to allow the user to change password independently. This parameter is required.|
|deactivatedTime | string |Specify the time when the account is expired.|
|isSystemAdmin | bool |Decide whether to allocate system administrator role to the user. This parameter is required.|
|tenants | list of tenant object |Specify a list of tenants for the user.<br>Only required if the parameter isSystemAdmin is false.<br>▪ tenantName (string) - the tenant that the user can access.<br>▪ isTenantAdmin (bool) - decide whether to allocate the tenant administrator role to the user. If false, you need to specify a domain for the user to access.<br>▪ allowCreateDomain (bool) - decide whether to allow the user to create domains.<br>▪ domains - required only if the parameter isTenantAdmin is false.<br>---domainName - the domain name.<br>---domainRoles - the role of the domain user.|

> ***Example***


```python
{
        "username": "user1",
        "authenticationServer":"Tacacs",
        "email": "user1@sso.com",
        "firstName": "user1",
        "lastName": "user1",
        "phoneNumber" : "",
        "department" : "",
        "description" : "",
        "deactivatedTime" : "",
        "isSystemAdmin":"true",
        "tenants" : [{
            "tenantName":"tenant_71a1",
            "isTenantAdmin":false,
            "allowCreateDomain":"false",
            "domains":[{
                "domainName":"domain_cyj",
                "domainRoles":["domainAdmin"]
            }]
        }]
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
# Normal Response:
{
    'statusCode': 790200,
    'statusDescription': 'Success.'
}

# response with duplicate user accounts in different server without aunthentication server provided in input.
{
    "users": [
        {
            "authenticationServer": "NetBrain",
            "userName": "user1"
        },
        {
            "authenticationServer": "AD",
            "userName": "user1"
        }
    ],
    "statusCode": 792032,
    "statusDescription": "There are users with the same name 'user1' in the system,You need to specify the authentication server."
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
token = "005fd6cc-cf08-4742-985b-902503dad2a4"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Users"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

body = {
        "username": "user1",
        "authenticationServer":"NetBrain",
        "email": "user1@sso.com",
        "firstName": "user1",
        "lastName": "user1",
        "phoneNumber" : "",
        "department" : "",
        "description" : "",
        "deactivatedTime" : "",
        "isSystemAdmin":"true",
        "tenants" : [{
            "tenantName":"tenant_71a1",
            "isTenantAdmin":false,
            "allowCreateDomain":"false",
            "domains":[{
                "domainName":"domain_cyj",
                "domainRoles":["domainAdmin"]
            }]
        }]
}


try:
    response = requests.put(full_url, data = json.dumps(body), headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Update User failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X PUT \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Users \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: bd33ab9d-7ce8-498d-a78d-c5b67186d998' \
  -H 'cache-control: no-cache' \
  -H 'token: 005fd6cc-cf08-4742-985b-902503dad2a4' \
  -d '{
        "username": "user1",
        "authenticationServer":"NetBrain",
        "email": "user1@sso.com",
        "firstName": "user1",
        "lastName": "user1",
        "phoneNumber" : "",
        "department" : "",
        "description" : "",
        "deactivatedTime" : "",
        "isSystemAdmin":"true",
        "tenants" : [{
            "tenantName":"tenant_71a1",
            "isTenantAdmin":false,
            "allowCreateDomain":"false",
            "domains":[{
                "domainName":"domain_cyj",
                "domainRoles":["domainAdmin"]
            }]
        }]
}'
```
