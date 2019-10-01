
# Role API Design

## ***POST*** /V1/CMDB/Roles
Call this API to add a new role into Netbrain system and grant privileges to this role.

## Detail Information

> **Title** : Add Role API<br>

> **Version** : 02/01/2019.

> **API Server URL** : http(s)://IP address of NetBrain Web API Server/ServicesAPI/API/V1/CMDB/Roles

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Headers | Authentication token | 

## Request body(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|roleName* | string  | The name of the created role. length between 0 and 128. The following special characters are not allowed in roleName: '/', ':', '*', '?', '"', '<', '>', '|', '$'  |
|description | string  | The description of the role. This field is optional.  |
|privileges | list of integer  | The privileges that the role owns. See roles and privileges for more details. this field is optional. |

> ***Example***


```python
{
      "roleName": "Role Name",
      "description": "string",
      "privileges": [2,5...]
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
    'statusCode': 790200,
    'statusDescription': 'Success.'
}
```




    {'statusCode': 790200, 'statusDescription': 'Success.'}



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
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Roles"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

roleName = "testRole11"
description = "string"
privileges = [2]

body = {
        "roleName": roleName, 
        "description": description, 
        "privileges": privileges
    }

try:
    response = requests.post(full_url, data = json.dumps(body), headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Update Role failed! - " + str(response.text))
    
except Exception as e:
    print (str(e)) 
```

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X POST \
  http://192.168.28.79/ServicesAPI/API/V1/CMDB/Roles \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: 8cad3c96-5b2a-4281-8ffc-4fd67e4b27dc' \
  -H 'cache-control: no-cache' \
  -H 'token: 005fd6cc-cf08-4742-985b-902503dad2a4' \
  -d '{
          "roleName": "testRole1",
          "description": "string",
          "privileges": "string"
    }'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
        
        roleName = "" # Can not be null.
        description = ""
        privileges = []

Response:
    
    "Add Role failed! - 
        {
            "statusCode":791000,
            "statusDescription":"Null parameter: the parameter 'roleName' cannot be null."
        }"
        
###################################################################################################################    

"""Error 2: wrong inputs"""

Input:
        
        roleName = "/" # Can not be "\\, /, :, *, ?, \", <, >, |, $".
        description = ""
        privileges = []

Response:
    
    "Add Role failed! - 
        {
            "statusCode":792007,
            "statusDescription":"Invalid roleName,"
                                "the roleName can't contain any of the following characters \\, /, :, *, ?, \", <, >, |, $."
        }"
    
###################################################################################################################    

"""Error 3: duplicate inputs"""

Input:
        
        roleName = "testRole11" # Role named as "testRole11" is already exist.
        description = ""
        privileges = []

Response:
    
    "Add Role failed! - 
        {
            "statusCode":791007,
            "statusDescription":"roleName already exists."
        }"
     
###################################################################################################################    

"""Error 4: wrong inputs value type"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""''

Input:
        
        roleName = 11111111 # Shouldn't be integer
        description = 11 # Shouldn't be integer
        privileges = "[2]" # Shouldn't be string


Response:
    
        "{ 
            'statusCode': 790200, 
            'statusDescription': 'Success.'
        }"
     
```


```python
'''
Some Issues:
        
        1) Success response too simple, a message is needed, return the new role body information would be the best.
        
        2) The duplicate "roleName" response can be improved, shows which name is duplicated.
        
        3) In the body table, it requires "roleName" and "description" should be string, "privileges" should be a list of integer,
           But when I set "roleName" and "description" as integer and "privileges" as a string, the role also can be 
           created successfully. That is not resonable, a wrong type alert should be provided.
           
        4) According the input of "privileges" should be a list of integer to spicified the corresponding privilege 
           for the new created role, users neet a table to clarify the number for each privilege, and when I check the table in 
           online help, there is no corresponding number for each privilege. That would be confused to users.
''' 
```

# Roles and Privileges Table
The system provides the following pre-defined roles and the default privileges of each role are listed as follows:
> **Note:** "Domain Admin", "Power User", "Engineer", "Guest", "Network Change Creator" and "Network Change Excutor" are defaultly setted roles by Netbrain, users can selest them in "System Management"->"User Accounts"->"Roles" and without setting 
custumized role privilege.

|**Privilege Number**|**Privilege**|**Description**|**Domain Admin**|**Power User**|**Engineer**|**Guest**|**Network Change Creator**|**Network Change Excutor**|
|------|------|------|------|------|------|------|------|------|
|<img width=20/>|<img width=100/>|<img width=400/>|<img width=20/>|<img width=20/>|<img width=20/>|<img width=20/>|<img width=20/>|<img width=20/>|
|2|Domain Management|Log in to the Domain Management page and do the following domain management tasks:<br>▪View, export, and delete discovery report in the Domain Manager<br>▪Add network definition<br>▪Resolve unknown end systems in the Unknown End System Manager<br>▪View created snapshots in the Snapshot Manager<br>▪View and export global Data Folders in Global Data Folder Manager<br>▪View, add, modify, delete, disable topology links in the Topology Link Manager<br>▪Resolve duplicated IPs and subnets in the Duplicated IP and Subnet Manager<br>▪Add checkpoint OPSEC tasks in the Checkpoint OPSEC Manager<br>▪Configure network security settings and minimum subnet mask in L2 topology building<br>▪Configure desktop profile for all users under a domain|√|√|no|no|√|√|
|5|Share Policy Management|▪Configure share policy (assign domain access and privileges to other users in this domain)|	√|no|no|no|no|no|
|6|Device Management|▪Add, modify, and remove MPLS cloud<br>▪Remove devices from a domain|√|√|no|no|√|√|
|7|Shared Device Group Management|▪Add devices into a device group from Map Data Folder Manager, Global Data Folder Manager, Data Folder Manager<br>▪Create a shared device group or set a private device group as public in the Device Group pane<br>▪Save discovered devices into a device group from on-demand discovery results<br>▪Add devices into a device group from the Domain Manager|√|√|no|no|√|√|
|8|Site Management|▪Add MPLS clouds and unclassified network devices from the Domain Manager into a site<br>▪Open the Site Manager to do site management, such as creating, editing, deleting, importing, committing, rebuilding sites, and so on|√|√|no|no|√|√|
|9|Discover/Tune Network Device|▪Create a do-not-scan list<br>▪Add discovery tasks from the Start Page or the Schedule Task page<br>▪Rediscover selected IPs and devices in the Domain Manager<br>▪Tune live access<br>▪Run on-demand discoveries|√|√|no|no|√|√|
|11|Schedule Benchmark|▪Add benchmark tasks from the Start Page or the Schedule Task page|√|√|no|no|√|√|
|15|Access to Live Network|Download the shared network settings or device settings data from the server and use these data to retrieve live device data from the network, which includes:<br>▪Run CLI commands and Qapps on a map page or in a runbook<br>▪Re-run CLI commands in the Map Data Folder Manager, Data Folder Manager, and Global Data Folder Manager<br>▪Run monitor (Qapp-based) widgets and retrieve live data in static widgets in a dashboard<br>▪Run Data View Template using the live network as the data source<br>▪Retrieve variables once or monitor variables periodically from the live network in Instant Qapp<br>▪Calculate live paths (use live network as the data source)<br>▪Configure SNMP, CLI timeout, SNMP hostname trim rules, management interface selection order, and live access method polling order (SNMP/Telnet/SSH/Jumpbox)<br>▪Browse live access logs in the Domain Manager|√|√|√|√|√|√|
|20|Manage Device Settings|▪Configure and manage shared device settings for each device in a domain from the following entries:<br>----Site pane<br>----Map<br>----Domain Manager<br>----Discover<br>----Tune Live Access|√|√|√|no|√|√|
|21|Manage Network Settings|Configure and manage shared network settings|√|√|no|no|√|√|
|23|Create Network Change|Create network change tasks.|√|√|no|no|√|no|
|24|Execute Network Change|Execute network change tasks.|√|√|no|no|no|√|



```python

```
