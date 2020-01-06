
# One Ip Table API Design

## ***GET*** /V1/CMDB/Topology/OneIPTable{?Ip}&{?beginIndex}&{?count}
Calling this API to get the One-IP Table.

If user provide an input value of "ip" attribute, then this API will return all items which have the same ip address in One-IP Table;

If user set "IP = null" or " IP = "" " but provide the input values of "beginIndex" and "count", API will return One-IP Table with items number equal to "count" values start from "beginIndex". But notice that the default maximum value of "count" is 1000. So if the input value of "count" greater than 1000, API will only return 1000 itmes. And if start from beginIndex to the end of table, there are no enough count items, API will return the rest of items.

>**Note:** The One-IP table records the physical connections for all IP addresses in your workspace. It is retrieved during the Layer 2 topology discovery. You can use the One-IP table to troubleshoot any Layer 2 connection issues.

## Detail Information

> **Title** : Get One-Ip Table API<br>

> **Version** : 02/06/2019.

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/API/V1/CMDB/Topology/OneIPTable

> **Authentication** : 

|**Type**|**In**|**Name**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|Bearer Authentication| Parameters | Authentication token | 

## Request body(****required***)

>No request body.

## Query Parameters(****required***)

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
| ip | string  | The ip address of current device.If user provide an input value of "ip" attribute, then this API will return all items which have the same ip address in One-IP Table; |
|lan|string|The LAN Segment of the IP address.If user provide an input value of “lan” attribute, then this API will return all items which have the same LAN segement in One-IP Table;|
|mac|string|The MAC address related to the IP address.If user provide an input value of “mac” attribute, then this API will return all items which have the same mac address in One-IP Table;|
|switch_name|string|The switch name connected to the end system.If user provide an input value of “switch_name” attribute, then this API will return all items which have the same switch name in One-IP Table;|
|switch_port|string|The [fullname](https://www.netbraintech.com/docs/ie71/help/index.html?interface-name-translation.htm) of switchport to connected to end system or the device interface configured with this IP address. This is not a independent attribute, to use this attribute, 'switch_name' is necessary.|
|dns|string|The resolved DNS name of the end system, or the combination of the device name and interface name. If the DNS name is not resolved, it is null.|
| beginIndex* | int  | Begin index of data, API will return OneIP Table items start from "beginIndex". |
| count* | int  | Count number of returned data, API will return OneIP Table items, the total number of items is the value of "count". Maximum "count" value is 10000. So API will only return 10000 itmes even users set the input value of "count" greater than 10000. If the total number of items which start from "beginIndex" to the end of table are less than "count" value, API will return the rest of items.<br> ***Note:*** If customer insert the beginindex as 1 and count as 10002 which meands the total number will greater than 10000. Then customer would get an error and without any result returned. |

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
| token* | string  | Authentication token, get from login API. |

## Response

|**Name**|**Type**|**Description**|
|------|------|------|
|<img width=100/>|<img width=100/>|<img width=500/>|
|OneIPList| list of object | list of OneIP item  |
|OneIPList.lanSegment| string | IP subnet |
|OneIPList.ip| string | IP Address |
|OneIPList.mac| string | Mac Address Of which the IP is on  |
|OneIPList.devName| string | Device Name Of which the IP is on  |
|OneIPList.interfaceName| string | Device Interface Name of the IP  |
|OneIPList.switchName| string | Switch Name that the IP connected to.  |
|OneIPList.portName| string | Switch Port Name that the IP connected to  |
|OneIPList.alias| string | device interface is HSRP/GLBP/VRRP |
|OneIPList.dns| string | DNS of the IP  |
|OneIPList.sourceDevice| string | from which device this One IP come  |
|OneIPList.serverType| int | device type |
|OneIPList.switchType| int | switch type |
|OneIPList.updateTime| DataTime | the update time of the One IP  |
|OneIPList.userFlag| int | one ip type<br>USERFLAG_AUTO = 0,<br>USERFLAG_MANUAL = 1,<br>OUTSIDE_ANOYMOUS_SOURCE = 2,<br>AUTO_CDPLLDP_TABLE = 5,<br>AUTO_MAC_TABLE = 6,<br>AUTO_ARP_TABLE = 7,<br>AUTO_CDPLLDP_MAC_TABLE = 8,<br>AUTO_DEVICE_INTERFACE = 9,<br>USERFLAG_DRIVER = 10,<br>USERFLAG_VALID_FLAGS_END,<br>USERFLAG_ABNORMAL_FLAGS_START = 0X7FFFFF00,<br>UNSIGNED_USERFLAG = USERFLAG_ABNORMAL_FLAGS_START+1,<br>ERR_USERFLAG ,<br>USERFLAG_ABNORMAL_FLAGS_END,|
|OneIPList.source| string | userFlag tos string<br><br> "Auto", //USERFLAG_AUTO<br>"Manual",//USERFLAG_MANUAL<br>"Provide Outside", //OUTSIDE_ANOYMOUS_SOURCE<br>"NDP Table", //AUTO_CDPLLDP_TABLE<br>"MAC Table",//AUTO_MAC_TABLE<br>"ARP Table", //AUTO_ARP_TABLE<br>"NDP & MAC table",//AUTO_CDPLLDP_MAC_TABLE<br>"Device Interface",//AUTO_DEVICE_INTERFACE<br>"Driver"//USERFLAG_DRIVER |
|OneIPList.vendor| string | device vendor |
|OneIPList.descr| string | description of the switch port  |
|time| DataTime | The last update time of the device configuration. |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***


```python
{
    "OneIPList": [
        {
            "lanSegment": "123.20.1.8/29",
            "ip": "123.20.1.11",
            "mac": "AABB.CC80.1300",
            "devName": "SW6",
            "interfaceName": "Vlan66",
            "switchName": "",
            "portName": "",
            "alias": "",
            "dns": "SW6.Vlan66",
            "sourceDevice": "SW6",
            "serverType": 2001,
            "switchType": 2001,
            "updateTime": "2019-02-01T19:13:05Z",
            "userFlag": 9,
            "source": "Device Interface",
            "vendor": "",
            "descr": ""
        }
    ],
    "statusCode": 790200,
    "statusDescription": "Success."
}
```

# Full Examples:


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "220d6462-ba64-4058-83cb-affb2d55de78"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Topology/OneIPTable"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

ip = "123.20.1.11"
beginIndex = 0
count = 5

data = {
    "ip" : ip,
    "beginIndex" : beginIndex,
    "count" : count
}

try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.json()
        print (result)
    else:
        print ("Get One-Ip Table failed! - " + str(response.text))
    
except Exception as e:
    print (str(e))  

```

    {'OneIPList': [{'lanSegment': '123.20.1.8/29', 'ip': '123.20.1.11', 'mac': 'AABB.CC80.1300', 'devName': 'SW6', 'interfaceName': 'Vlan66', 'switchName': '', 'portName': '', 'alias': '', 'dns': 'SW6.Vlan66', 'sourceDevice': 'SW6', 'serverType': 2001, 'switchType': 2001, 'updateTime': '2019-02-01T19:13:05Z', 'userFlag': 9, 'source': 'Device Interface', 'vendor': '', 'descr': ''}], 'statusCode': 790200, 'statusDescription': 'Success.'}
    

# cURL Code from Postman:


```python
curl -X GET \
  'http://192.168.28.79/ServicesAPI/API/V1/CMDB/Topology/OneIPTable?ip=123.20.1.11&beginIndex=0&count=5' \
  -H 'Postman-Token: ae0e4721-9d20-44ac-9b4d-4d73ccb8abcd' \
  -H 'cache-control: no-cache' \
  -H 'token: 220d6462-ba64-4058-83cb-affb2d55de78'
```

# Error Example：


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
    
        ip = ""
        count = None # Can not be null.
        beginIndex = None # Can not be null.
          
Response:
    
    "Get One-Ip Table failed! - 
    {"statusCode":791000,"statusDescription":"Null parameter: the parameter 'BeginIndex(int)' cannot be null."}

    "Get One-Ip Table failed! - 
    {"statusCode":791000,"statusDescription":"Null parameter: the parameter 'Count(int)' cannot be null."}"

###################################################################################################################    

"""Error 2: wrong input values type """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
        ip = ""
        count = "100" # Should be integer
        beginIndex = "50" # Should be integer
          
Response:
    
        "{
            'OneIPList': [...], 
            'statusCode': 790200,
            'statusDescription': 'Success.'
        }"  
    
###################################################################################################################    

"""Error 3: wrong input values type """

Input:
    
        ip = "hahahahaah" # There is no Ip address like this
        count = 100 
        beginIndex = 50 
          
Response:
    
        "Get One-Ip Table failed! - 
            {
                "statusCode":791001,
                "statusDescription":"Invalid parameter: the parameter 'IP' is invalid."
            }"  
    
###################################################################################################################    

"""Error 4: count > 1000 """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
        ip = "" 
        count = 10000 # Should be less or equal to 1000
        beginIndex = 50 
          
Response:
    
        "Get One-Ip Table failed! - 
            {
                "statusCode":791002,
                "statusDescription":"Invalid value"
            }"  
    
###################################################################################################################    

"""Error 5: "beginIndex" > size of One-Ip Table """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Input:
    
        ip = "" 
        count = 1 
        beginIndex = 500 # There are only 117 items in this table.
          
Response:
    
            "{
                'OneIPList': [], 
                'statusCode': 790200,
                'statusDescription': 'Success.'
            }"  
    
```
