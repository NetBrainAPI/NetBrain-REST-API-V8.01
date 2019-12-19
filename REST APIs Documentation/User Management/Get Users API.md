# User API Design

GET /V1/CMDB/Users{?username}&{?authenticationServer}
-----------------------------------------------------

Calling this API to get user information. If input username, API return just
this one user information. If no specific user name is input, API return all
user information.

Detail Information
------------------

>   **Title** : Get User(s) information API

>   **Version** : 02/06/2019.

>   **API Server URL** : http(s):// IP address of your NetBrain Web API Server
>   /ServicesAPI/API/V1/CMDB/Users

>   **Authentication** :

| **Type**              | **In**     | **Name**             |
|-----------------------|------------|----------------------|
|                       |            |                      |
| Bearer Authentication | Parameters | Authentication token |

Request body(\*\*\*\*required\*\*\*)
------------------------------------

>   No request body.

Query Parameters(\*\*\*\*required\*\*\*)
----------------------------------------

| **Name**             | **Type** | **Description**                                                                                                                                                           |
|----------------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                      |          |                                                                                                                                                                           |
| username             | string   | The name of Netbrain system user. This field is the key to get the user information. if set "username" = null or "username" == "", API will returns all users information |
| authenticationServer | string   | The corresponding name of the authentication server.                                                                                                                      |

**Note:** the "authenticationServer" is an optional attribute, to prevent
mis-retrieving if there are same user account names exist in different servers.
Check the detail in the following example.

Headers
-------

>   **Data Format Headers**

| **Name**     | **Type** | **Description**            |
|--------------|----------|----------------------------|
|              |          |                            |
| Content-Type | string   | support "application/json" |
| Accept       | string   | support "application/json" |

>   **Authorization Headers**

| **Name** | **Type** | **Description**                           |
|----------|----------|-------------------------------------------|
|          |          |                                           |
| token\*  | string   | Authentication token, get from login API. |

Response
--------

| **Name**                     | **Type**                     | **Description**                                                                                                                                                                                                                                                                                                                       |
|------------------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                              |                              |                                                                                                                                                                                                                                                                                                                                       |
| UserData                     | list of object               | List of users info.                                                                                                                                                                                                                                                                                                                   |
| UserData.username            | string                       | The user name, this filed is the key to update the user information.                                                                                                                                                                                                                                                                  |
| UserData.email               | string                       | The email address of the user.                                                                                                                                                                                                                                                                                                        |
| UserData.firstName           | string                       | The first name of the user.                                                                                                                                                                                                                                                                                                           |
| UserData.lastName            | string                       | The last name of the user.                                                                                                                                                                                                                                                                                                            |
| UserData.authenticationType  | int                          | The authentication type for the user account.                                                                                                                                                                                                                                                                                         |
|                              |                              | ▪ 1 - Local                                                                                                                                                                                                                                                                                                                           |
|                              |                              | ▪ 2 - External                                                                                                                                                                                                                                                                                                                        |
| UserData.phoneNumber         | string                       | The phone number of the user.                                                                                                                                                                                                                                                                                                         |
| UserData.department          | string                       | The department that the user belongs to.                                                                                                                                                                                                                                                                                              |
| UserData.description         | string                       | Any description about the user.                                                                                                                                                                                                                                                                                                       |
| UserData.allowChangePassword | bool                         | Decide whether to allow the user to change his/her password independently.                                                                                                                                                                                                                                                            |
| UserData.deactivatedTime     | string                       | Specify the time when the user account is expired.                                                                                                                                                                                                                                                                                    |
| UserData.isSystemAdmin       | string                       | Decide whether to allocate the system administrator role to the user.                                                                                                                                                                                                                                                                 |
| UserData.TenantAndRole       | list of TenantAndRole object | Specify Tenant And Role for the user.                                                                                                                                                                                                                                                                                                 |
|                              |                              | ▪ tenantId (string) - the tenant that the user can access.                                                                                                                                                                                                                                                                            |
|                              |                              | ▪ isAdmin(bool) - decide whether to allocate the tenant administrator role to the user. If it is false, you need to specify a domain for the user to access.                                                                                                                                                                          |
|                              |                              | ▪ canAddDomain(bool) - decide whether to allow the user to create domains.                                                                                                                                                                                                                                                            |
| users                        | list of object               | The list contains the dupilcate account information in different server.                                                                                                                                                                                                                                                              |
| users.authenticationServer   | string                       | The name of authentication server.                                                                                                                                                                                                                                                                                                    |
| users.userName               | string                       | The name of the user account.                                                                                                                                                                                                                                                                                                         |
| statusCode                   | integer                      | Code issued by NetBrain server indicating the execution result.                                                                                                                                                                                                                                                                       |
| statusDescription            | bool                         | The explanation of the status code.                                                                                                                                                                                                                                                                                                   |

>   **Example**

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Normal Response:

{
    "UserData": [
        {
            "username": "Suneet45",
            "email": "suneet.tatikonda@netbraintech.com",
            "firstName": "Suneet",
            "lastName": "Tatikonda",
            "allowChangePassword": true,
            "isSystemAdmin": true,
            "isUserManager": true,
            "isSystemManager": true
        },
        {
            "username": "admin",
            "email": "lin.zhu@netbraintech.com",
            "firstName": "Lin",
            "lastName": "Zhu",
            "phoneNumber": "",
            "description": "description",
            "allowChangePassword": true,
            "isSystemAdmin": true,
            "isUserManager": true,
            "isSystemManager": true
        },
    "statusCode": 790200,
    "statusDescription": "Success."
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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Full Example:
=============

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "9eaef30e-3a21-44b7-8600-d21625a2198e"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Users"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

username = ""

data = {
        "username":username,
        "authenticationServer":"NetBrain"
    }

try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get Users Information failed! - " + str(response.text))
    
except Exception as e:
    print (str(e))  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{'UserData': [{'username': 'Suneet45', 'email': 'suneet.tatikonda@netbraintech.com', 'firstName': 'Suneet', 'lastName': 'Tatikonda', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiYzg4OTNiNDAxNTVkN2JhMmMzZmRjNTE0ODgzOGE2NzExMjBiMmQ4OTAwOTk4ZTc5NDJhNjg2Yjk4YTg2OGIyODc1NTA2NWE5ZGRkMzM0MzE5OGE2M2Q2YzhlM2MzODgwYmRlNWUzYTA2ZmIwMzk1MWIyZmZmYjVmNDA0MDc5NWEiLCJkYXRhIjoiMjQ4ZGE2MDc1OGE3N2JkMmM5NWYyOGM3ZDM4MzFiZTRkYjkwMzVmOTg5Y2ViMzllZGZiYWUxNmE1M2VkYjk3OCJ9', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'admin', 'email': 'lin.zhu@netbraintech.com', 'firstName': 'Lin', 'lastName': 'Zhu', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiMGY0YWZlNmZkYTBjNzA5YTcxYjBlYzI4NWRiZmY1NWVhN2NlMGU0NDcyZTk0NGNhMDM3NDRjNWE2NjZhMmI3YjE3ZGM0ZGY4ZTQ4ZDRlNWEyNWExN2ZlMGYwYWJiN2RmYWFmMTkyMmI4ODQ5Y2U0ZjAxZWRkOWVjNzVhZTk1Y2QiLCJkYXRhIjoiN2RlMTllNDNlMzU5ZTViMzg2ZDZkYzhkNzhhMmIyNmU4MDc0OGZmZDVlZDA0M2Q5ZTgzOGJjZjc5MGIxZWZkNyJ9', 'phoneNumber': '', 'description': 'description', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'atin.tandon', 'email': 'atin.tandon@netbraintech.com', 'firstName': 'atin', 'lastName': 'tandon', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiM2YwZjRiYmYwNmZiNGVhMWU1MjVjNWZmZTQ0MTcxODIwMmQ3OTAyYWJiNzA3ZGQ0OGI1OWE0NTRkNGE3OTFiMzhkOTczNDMxOWYwOTMzOWJhMDg5YTQ3YzYyMTQ4NDg3ZTJiNmZkYjExNGIwYzhiOTJjNTE2ZGRkNThjZWE2ZGYiLCJkYXRhIjoiM2RhNmQyZDQwM2Q1ZjNkYWFjMDIwZTM0YTBhNmU5MmMxMzE3N2M4ODdjODQxN2FiZDRkYTMwNDFhZjQwMWI3ZiJ9', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'gdluserTest', 'email': 'liugongdai@163.com', 'firstName': 'gd', 'lastName': 'liu', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiNDNjNDM4MzRjOWNkYzdkZWM0Y2QwYWQ2MDU1NDJkMjAxMTdlM2M3YzAxNWNmN2MxN2NmMGM0ZTI3Y2Q1MDkzNmE3NGQ5NDIyNWZmZDI4ZmQ5OGNjNTRiMDYwMmYxZWI4MWRiMjY4MDg0MzA3MzQyY2RiMmQ1ZmVmNzIwZWRhNDYiLCJkYXRhIjoiNmE3NzRjZWU1YjNiY2QyODBjMzEwY2EyMDJjY2I4YjI0NDExZTAyZmNhMjdhM2VjYTFhMDllMGRkM2M3OTYxZSJ9', 'allowChangePassword': True, 'isSystemAdmin': False, 'isUserManager': True, 'isSystemManager': False}, {'username': 'georgej', 'email': 'george.jiang@netbraintech.com', 'firstName': 'George', 'lastName': 'Jiang', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiOWNjZGU3YjQxMzFkMGVlNjVmY2U2MzQwMzI5ZmVmYzU2NmQxYjE2NDE2ZDE1YjkyYThjZjZlZjA0YmQ5MDJlZWU4MmQ3ZTJiZDkxNTA5MDE0YzEwMmQ3Y2RmMjgxOWQ3MTk0ZjVjNThkODNkYzkxNWUxM2M1NTBiNzBlYjU1MDkiLCJkYXRhIjoiZjEwODAyOTBlMWFkNDJkNTA5YzE0Y2VlYzZlOTRmNGI2MDdhZjQzYTVhNTA5OGJhZmQ4NzllZGNjMzhiMDg3YyJ9', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'gongdaiAdmin', 'email': 'Gongdai.Liu@netbraintech.com', 'firstName': 'Gongdai', 'lastName': 'Liu', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiMzZjM2NmYTY5ODQ0ZjA0OWQxYTU5NmY1MDMxYWU4ZWRhOGFjMDZjZThjZGUwNjc4ZjYyNmI2YjFlYzAwNzNlZDM4NDBkODc2MzgxNzg0YzM2ZWFmZTkyN2YxMGUwMDVmNDVkZWFjOGQ4ZWNkNzM2ZDI1NzAwMWQzMzI4YmI3OTIiLCJkYXRhIjoiYjlmMjkwOGQ2MTUxYWQ4NDc3Y2E4MDliM2IyZWIzZGY4ZTU2ZGY1YzA4Njg4NzhmMjg0YjIwMDkwYjU0ZDYzMCJ9', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'gongdailiu', 'email': 'liugongdai@gmail.com', 'firstName': 'Gongdai', 'lastName': 'Liu', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiZTMwZDIxOTI4YThiYzQxOTM3MDAyNTc1YTBiOTg3MTM2MzJiNTljMDZlOTNjYjU1ZGMzZjU0NmRiNmFmNjk4ZWZlZTI1MTU3MTU5ODhkOWJmZWQ0NWJhMDFkNDM4ZjA5NzNlMjA4OGY3OGI0YWY0MjZlZTM1NzcwYTRlZTI5ZjAiLCJkYXRhIjoiNTFjN2M1MzUwN2Y1NzAwYTNjMWY3OTA0NDFiNmVmMDViZWVjNmE0NDVjYWIzZjZiZTdhODNkZjU0MDY1ZWMwYiJ9', 'allowChangePassword': True, 'isSystemAdmin': False, 'isUserManager': False, 'isSystemManager': False}, {'username': 'haoran.song', 'email': 'haoran.song@netbraintech.com', 'firstName': 'Haoran', 'lastName': 'Song', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiMzBiOTI1OGExNGJiZTcxOGIxYTgzZWJlNDhiMGJlNTBlNzViOWQzM2JkYTc0YzE5YTY4MWJiMGY0NzM4ZmE3YTI5NDNhN2FmYjljOTVhOTJiMzFiY2VlMTYwZjE2ODQ3OWJhZDU1Mjc0MWQ4MzM1OTU3NDNiZjdkZGMxM2Y1ZDciLCJkYXRhIjoiYzNlYmYxN2UyYzNjZjA2YjNkNTdjNzYwZTg3MDA5NzljZTg4YzU4YmE1YjA3OGNmOWM2YzI2MDNmY2E1NGZhZSJ9', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'haoran.test', 'email': 'test@netbraintech.com', 'firstName': 'haoran', 'lastName': 'test', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiMjAyNTBiODFlYzY1MGQ5Y2RhZDgyMzBhZmM3ZjQ0YTQ4OTI2MjQwMDkzM2UwOWI4N2U0YzAxOGQ3MWZlOTgyMDFiY2JiNzgzMDFjMDhmNDIzMjVmNTdlM2UxZjY0Yzc5MTkwY2UyOGFlNGMyOTkxMTkxYjYyYTdiZDE2OWEwNGIiLCJkYXRhIjoiNjhkYmJmNTZmMTg3YTFkNjA0N2FjZGI5MWEyNmE1MWU2YjI5NGI4MDJjNWYwYmFkN2NiNDQxNjJjMjQ4YzNmNSJ9', 'allowChangePassword': True, 'isSystemAdmin': False, 'isUserManager': False, 'isSystemManager': False}, {'username': 'henryshen', 'email': 'haoyun.shen@netbraintech.com', 'firstName': 'Haoyun', 'lastName': 'Shen', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiOWVlNWEzNjgyOTQwYTE0MzBhYTJmMTNjYTMzM2RiNzRhYzYxMWIwNTU1MDdhYjkyZDk0YjFlNGZiMGUxNzU4MzQyZDE2NzQ1MWQwYWNjMzRmMmRmMmMyYTQ5NjM5NWMxZWUxZTRmZDI4ZTliOTAzOGM4MjA4NTMxNzQ3Mzc5NDQiLCJkYXRhIjoiYmUzM2M1YjBjYTAwNjVjYTE3Y2I1YTRhNDU4Y2Y5MDVkYTIwYWJmNjY0ZjkxODBhMmJiMGNlOGVmMDg5NmQ4NCJ9', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'lin.zhu', 'email': 'lin.zhu@netbrain.com', 'firstName': 'Lin', 'lastName': 'Zhu', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiMjhlZTk4OGJiMDBkODA3NTE1N2UxOTkyMzRmZmM5YjZmNTAzOGYyNjRjMDE5ZDkxNGVjNWVkNTU0ZGQ4N2QyMWFjZTFmNDliMTlkODYzOWExMjZmYTk5MzIwNjM1MTZiMmQwYzUzZDE5MjVkMWIzNDRiMDc0ZmNjMmQ3OTJmZjMiLCJkYXRhIjoiYWJlNzQ4MDFjNGI5YWQ1MWNhMWUyN2Q1ODJiYWU2Yzk1MzMyM2ZkNGI5OWI0NzdiMTFjODhmNDEzMzQ1MWI2OSJ9', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'nliu', 'email': 'nicky.liu@netbraintech.com', 'firstName': 'Nick', 'lastName': 'Liu', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiYjQzNTg3NTM3Njg1MjcxOTFjZmQ4ZTcyMWZkYzBjMmE0ZmE3Y2JiZDI0YjZmNzNmYmM5MGYxZGE1YjQyMGExYmM4ODlhOWMzZGNjZmFkNmQ0MzI0ZGQ4ODZjYWExNDdkZDg2ODVhMDIxYjEwMzE3ZTg1YzI0ZjQxNDBjMmQ1NzkiLCJkYXRhIjoiODgzYjg4NmQ0NmRlMDE0NTMzNWJjZmFjNmI3M2Q2OGFlOTE4NTBjMWEyNjNjZmZiYzE3MTNjMWRkNjBiZmRjZCJ9', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}, {'username': 'weiwei', 'email': 'chris.ju@netbraintech.com', 'firstName': 'weiwei', 'lastName': 'Ju', 'password': 'eyJhbGciOiJzaGEyNTYiLCJuYnZlciI6IjcuMS4xLjEiLCJzYWx0IjoiZWUzMjYyNTM1NzZlMmVhMmM2ZmUwYjlhNzYxMTJkOGMxMGQwZTlmODVhNWE5ZmI3YjdmMjM2YmNmMGY1NTY2ZjFmMTk1MTNmM2IwNjFhMDNmZWQxNzE3NjIwZGYxOGI1Y2NjYmU0OTUyMTYzNTdmMDZiNTFmMjBlYzNhY2ZiYzgiLCJkYXRhIjoiNzI2NjU2Y2M1YzlkOGVjYjk2NmI5NjlkMjAzYTdmOTE5ZmJhMDA1NzFmMDMxNzY0MzAzN2VhNzZjY2FmZTNmNiJ9', 'phoneNumber': '6478750888', 'allowChangePassword': True, 'isSystemAdmin': True, 'isUserManager': True, 'isSystemManager': True}], 'statusCode': 790200, 'statusDescription': 'Success.'}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cURL Code from Postman:
=======================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
curl -X GET \
  'http://192.168.28.173/ServicesAPI/API/V1/CMDB/Users?username=&authenticationServer=NetBrain' \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 192.168.28.173' \
  -H 'Postman-Token: 3cd9a344-50f6-4ae9-8c79-41a01f90ca41,e008e5f9-4fd7-4f2e-8e39-fd77d54d0651' \
  -H 'User-Agent: PostmanRuntime/7.15.2' \
  -H 'cache-control: no-cache' \
  -H 'token: b2cd935b-51ad-4f5d-a713-b195d041fa48'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Error Examples:
===============

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###################################################################################################################    

"""Error 1: wrong inputs"""

Input:
    
        username = "kakakakaakak" # No user with a name called "kakakakaakak".
    
Response:
    
    "Get Users Information failed! - 
        {
            "statusCode":791006,
            "statusDescription":"user kakakakaakak does not exist."
        }"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
