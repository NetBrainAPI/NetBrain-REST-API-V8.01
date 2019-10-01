
# User API Design

## ***GET*** /V1/CMDB/Users/UsageReport{?username}&{?tenantId}&{?domainId}&{?fromDate}&{?toDate}&{?authenticationServer}
Call this API to get the detail usage report of one user according to tenant/domain in a time specified time range .

## Detail Information

> **Title** : Get User Detail Usage Report API<br>

> **Version** : 02/01/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Users/DetailUsageReport

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

>No request body.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|username | string  | User name of the corresponding account.  |
|tenantId | string  | Tenant id, if not specified, check all tenants.  |
|domainId | string  | Domain id, if not specifed, check all domains on tenant specifed by tenantId.  |
|fromDate | string  | Start time, if not specified, from the beginning of the system installed. Format: yyyy-MM-ddThh:mm:ssZ, sample: "2018-03-07T04:59:59Z". Use default value 0001-01-01T00:00:00Z if value is null or of invalid format. |
|toDate | string  | End time, if not specified, use the current system time. Format: yyyy-MM-ddThh:mm:ssZ, sample: "2018-03-07T04:59:59Z". Use default value 0001-01-01T00:00:00Z if value is null or of invalid format.  |
|authenticationServer | string | The corresponding name of the authentication server. |
***Note:*** the "authenticationServer" is an optional attribute, to prevent mis-retrieving if there are same user account names exist in different servers. Check the detail in the following example.

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
|usageDetails| list |List of usage object.|
|usageDetails.tenantName| string | Name of working tenant.  |
|usageDetails.domainName| string | The name of user's working domain.  |
|usageDetails.machineName| string | Login machine name.  |
|usageDetails.IPAddress| string | The login machine ip.  |
|usageDetails.loginTime| string | The login time.  |
|usageDetails.logoutTime| string | The logout time.  |
|usageDetails.duration| string | The total online time.  |
|usageDetails.ofLoginFailureDueToSeatLicense| long | The total times of user login failure due to seat license.  |
|statusCode| integer | The returned status code of executing the API.  |
|statusDescription| string | The explanation of the status code.  |


> ***Example***


```python
# Normal response
{
    "usageDetails": [
        {
            "loginTime": "1/22/2019 7:02:30 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/22/2019 9:52:55 PM",
            "duration": "2h 50m 25s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/22/2019 9:53:06 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/23/2019 2:43:14 AM",
            "duration": "4h 50m 8s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/24/2019 3:05:22 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/25/2019 12:43:17 AM",
            "duration": "9h 37m 55s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/25/2019 10:13:45 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/26/2019 2:23:29 AM",
            "duration": "4h 09m 44s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/28/2019 1:51:50 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/28/2019 2:22:52 PM",
            "duration": "31m 2s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/28/2019 3:17:25 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/29/2019 2:38:35 AM",
            "duration": "11h 21m 10s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/29/2019 3:36:49 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/30/2019 2:53:37 AM",
            "duration": "11h 16m 48s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/29/2019 6:00:56 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/29/2019 6:11:07 PM",
            "duration": "10m 11s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/30/2019 12:28:05 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "1/30/2019 10:08:39 PM",
            "duration": "9h 40m 34s",
            "ofLoginFailureDueToSeatLicense": 0
        },
        {
            "loginTime": "1/31/2019 1:01:37 PM",
            "tenantName": "Initial Tenant",
            "domainName": "GE Test",
            "machineName": "",
            "IPAddress": "192.168.4.157",
            "logoutTime": "2/1/2019 1:38:42 AM",
            "duration": "12h 37m 5s",
            "ofLoginFailureDueToSeatLicense": 0
        }
    ],
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
token = "3d0f475d-dbae-4c44-9080-7b08ded7d35b"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Users/DetailUsageReport"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

username = "Netbrain"
tenantId = "fb24f3f0-81a7-1929-4b8f-99106c23fa5b"
domainId = "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
fromDate = ""
toDate = ""

data = {
        "username" : username,
        "tenantId" : tenantId,
        "domainId" : domainId,
        "fromDate" : fromDate,
        "toDate" : toDate
    }

try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get Detail User Report failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```
    
    "Get Detail User Report failed! - "
    {
        "users": [
            {
                "authenticationServer": "NetBrain",
                "userName": "API_Test"
            },
            {
                "authenticationServer": "AD",
                "userName": "API_Test"
            }
        ],
        "statusCode": 792032,
        "statusDescription": "There are users with the same name 'API_Test' in the system,You need to specify the authentication server."
    }

# cURL Code from Postman:


```python
curl -X GET \
  'http://192.168.28.79/ServicesAPI/API/V1/CMDB/Users/DetailUsageReport?username=gongdaiAdmin&tenantId=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&domainId=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&fromDate=&toDate=' \
  -H 'Postman-Token: 1be46915-3be8-4ab9-a30b-4d0fc50f3cd0' \
  -H 'cache-control: no-cache' \
  -H 'token: 3d0f475d-dbae-4c44-9080-7b08ded7d35b'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
        
        username = "" # Only one parameter can not set as null.
        tenantId = ""
        domainId = ""
        fromDate = ""
        toDate = ""

Response:
    
    "Get Detail User Report failed! - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter 'username' cannot be null."
        }"
        
# Note: If users only provide "username" and without anyother inputs, this API will run successfully. The reaponse will include
#       all informations of current user, include the report of all accessible tenants and domains.

###################################################################################################################    

"""Error 1: wrong username inputs"""

Input:
        
        username = "Brainnet" # No users called "Brainnet".
        tenantId = ""
        domainId = ""
        fromDate = ""
        toDate = ""

Response:
    
    "Get Detail User Report failed! - 
        {
            "statusCode":791006,
            "statusDescription":"username Brainnet does not exist."
        }"
        
###################################################################################################################  
   """Others same with "Get Usage Report of users API" """     
```
