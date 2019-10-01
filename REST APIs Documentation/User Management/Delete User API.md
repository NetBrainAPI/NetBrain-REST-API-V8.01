
# User API Design

## ***DELETE*** /V1/CMDB/Users/{userName}/{authenticationserver}
Call this API to delete a user account from NetBrain system.

## Detail Information

> **Title** : Delete User API<br>

> **Version** : 02/01/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Users

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
|username* | string  | The user name of one user account which going to be deleted. |
|authenticationServer | string | The corresponding name of the authentication server. |
***Note:*** the "authenticationServer" is an optional attribute, to prevent mis-deletion if there are same user account names exist in different servers. Check the detail in the following example.

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
|users|list of object| The list contains the dupilcate account information in different server.|
|users.authenticationServer|string|The name of authentication server.|
|users.userName|string|The name of the user account.|
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |

> ***Example***


```python
#normal response:
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

username = "NetBrain1"
authenticationServer = "NetBrain"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Users/" + str(username) + "/" + str(authenticationServer)
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

try:
    response = requests.delete(full_url, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Delete user account failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X DELETE \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Users/Netbrain1/NetBrain \
  -H 'Postman-Token: f303ba1f-55ab-43d8-9d39-d00e936a5ef5' \
  -H 'cache-control: no-cache' \
  -H 'token: 005fd6cc-cf08-4742-985b-902503dad2a4'
```
