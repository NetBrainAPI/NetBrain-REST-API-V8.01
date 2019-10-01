
# DataEngine API Design

## ***GET*** /V1/CMDB/DataEngine/DeviceData/Configuration/{?hostname}
Calling this API to get the configuration of a device.

## Detail Information

> **Title** : Get Device Configuration API<br>

> **Version** : 02/06/2019.

> **API Server URL** : http(s):// IP address of your NetBrain Web API Server /ServicesAPI/API/V1/CMDB/DataEngine/DeviceData/Configuration

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
| hostname* | string  | The name of a device. |

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
|configuration| string | Full configuration context of the device.  |
|time| DataTime | The last update time of the device configuration. |
|statusCode| integer | Code issued by NetBrain server indicating the execution result.  |
|statusDescription| string | The explanation of the status code. |

> ***Example***


```python
{
    "configuration": "! Info via SNMP: sysoid=1.3.6.1.4.1.9.1.1,vendor=Cisco,model=DEVELOPMENT TEST SOFTWARE,hostname=R1\r\nR1#show run\r\nBuilding configuration...\r\n\r\nCurrent configuration : 2313 bytes\r\n!\r\nversion 15.4\r\nservice timestamps debug datetime msec\r\nservice timestamps log datetime msec\r\nno service password-encryption\r\n!\r\nhostname R1\r\n!\r\nboot-start-marker\r\nboot-end-marker\r\n!\r\naqm-register-fnf\r\n!\r\nno logging on\r\n!enable secret ********\r\n!\r\nno aaa new-model\r\nclock timezone CET 1 0\r\nmmi polling-interval 60\r\nno mmi auto-configure\r\nno mmi pvc\r\nmmi snmp-timeout 180\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n\r\n\r\n!\r\n!\r\n!\r\n!\r\nno ip domain lookup\r\nip domain name netbraintech.com\r\nip cef\r\nno ipv6 cef\r\nipv6 multicast rpf use-bgp\r\n!\r\nmultilink bundle-name authenticated\r\nmpls label protocol ldp\r\nno mpls ip propagate-ttl \r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!username ********\r\n!\r\nredundancy\r\n!\r\n!\r\nip ssh version 2\r\n! \r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\ninterface Loopback0\r\n ip address 123.1.1.1 255.255.255.255\r\n!\r\ninterface Ethernet0/0\r\n no ip address\r\n!\r\ninterface Ethernet0/1\r\n ip address 123.10.1.5 255.255.255.252\r\n!\r\ninterface Ethernet0/2\r\n ip address 123.10.1.2 255.255.255.252\r\n!\r\ninterface Ethernet0/3\r\n no ip address\r\n!\r\nrouter ospf 12345\r\n mpls ldp autoconfig\r\n router-id 123.1.1.1\r\n network 123.0.0.0 0.255.255.255 area 0\r\n!\r\nrouter bgp 12345\r\n bgp router-id 123.1.1.1\r\n bgp log-neighbor-changes\r\n no bgp default ipv4-unicast\r\n neighbor iBGP peer-group\r\n neighbor iBGP remote-as 12345\r\n neighbor iBGP update-source Loopback0\r\n neighbor PEER peer-group\r\n neighbor PEER remote-as 12345\r\n neighbor PEER update-source Loopback0\r\n neighbor 123.2.2.2 peer-group iBGP\r\n neighbor 123.3.3.3 peer-group iBGP\r\n neighbor 123.6.6.6 peer-group iBGP\r\n neighbor 123.7.7.7 peer-group iBGP\r\n !\r\n address-family ipv4\r\n  neighbor iBGP route-reflector-client\r\n  neighbor 123.2.2.2 activate\r\n  neighbor 123.3.3.3 activate\r\n  neighbor 123.6.6.6 activate\r\n  neighbor 123.7.7.7 activate\r\n exit-address-family\r\n !\r\n address-family vpnv4\r\n  neighbor iBGP send-community extended\r\n  neighbor iBGP route-reflector-client\r\n  neighbor PEER send-community extended\r\n  neighbor PEER route-reflector-client\r\n  neighbor 123.2.2.2 activate\r\n  neighbor 123.3.3.3 activate\r\n  neighbor 123.6.6.6 activate\r\n  neighbor 123.7.7.7 activate\r\n exit-address-family\r\n!\r\nip forward-protocol nd\r\n!\r\n!\r\nno ip http server\r\nno ip http secure-server\r\n!\r\n!\r\n!snmp-server community ********\r\n!\r\nmpls ldp router-id Loopback0\r\n!\r\ncontrol-plane\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\nline con 0\r\n exec-timeout 0 0\r\n logging synchronous\r\nline aux 0\r\nline vty 0 4\r\n login local\r\n transport input all\r\n!\r\n!\r\nend\r\n\r\n\n",
    "time": "2019-01-29T17:08:57Z",
    "statusCode": 790200,
    "statusDescription": "Success."
}

# If customer don't have enough privilige:
{
    "statusCode":795003,
    "statusDescription":"Insufficient permissions: the current user has insufficient permissions to perform the requested operation. The user has no tenant or domain access permission.sharePolicyManagement"
}
```

## Full Example : 


```python
# import python modules 
import requests
import time
import urllib3
import pprint
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Set the request inputs
token = "c7e8707f-3dab-4ddf-b7da-b19186f2c0f0"
nb_url = "http://192.168.28.79"
full_url = nb_url + "/ServicesAPI/API/V1/CMDB/DataEngine/DeviceData/Configuration"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

hostname = "R3"

data = {
        "hostname":hostname
    }

try:
    response = requests.get(full_url, params = data, headers = headers, verify = False)
    if response.status_code == 200:
        result = response.text
        print (result)
    else:
        print ("Get Device Configuration failed! - " + str(response.text))
    
except Exception as e:
    print (str(e))  

```

    {"configuration":"! Info via SNMP: sysoid=1.3.6.1.4.1.9.1.1,vendor=Cisco,model=DEVELOPMENT TEST SOFTWARE,hostname=R3\r\nR3#show run\r\nBuilding configuration...\r\n\r\nCurrent configuration : 4492 bytes\r\n!\r\n! Last configuration change at 22:05:01 CET Fri Jan 25 2019\r\n!\r\nversion 15.4\r\nservice timestamps debug datetime msec\r\nservice timestamps log datetime msec\r\nno service password-encryption\r\n!\r\nhostname R3\r\n!\r\nboot-start-marker\r\nboot-end-marker\r\n!\r\naqm-register-fnf\r\n!\r\nno logging on\r\n!enable secret ********\r\n!\r\nno aaa new-model\r\nclock timezone CET 1 0\r\nmmi polling-interval 60\r\nno mmi auto-configure\r\nno mmi pvc\r\nmmi snmp-timeout 180\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n\r\n\r\n!\r\nip vrf BLUE\r\n rd 65111:13\r\n route-target export 13:13\r\n route-target import 13:13\r\n!\r\nip vrf GREEN\r\n rd 65111:12\r\n route-target export 12:12\r\n route-target import 12:12\r\n!\r\nip vrf INET\r\n rd 30000:99\r\n route-target export 99:99\r\n route-target import 99:99\r\n!\r\nip vrf RED\r\n rd 65111:14\r\n route-target export 14:14\r\n route-target import 14:14\r\n!\r\nip vrf YELLOW\r\n rd 45678:15\r\n route-target export 15:15\r\n route-target import 15:15\r\n!\r\n!\r\n!\r\n!\r\nno ip domain lookup\r\nip domain name netbraintech.com\r\nip cef\r\nno ipv6 cef\r\nipv6 multicast rpf use-bgp\r\n!\r\nmultilink bundle-name authenticated\r\nmpls label protocol ldp\r\nno mpls ip propagate-ttl \r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!username ********\r\n!\r\nredundancy\r\n!\r\n!\r\nip ssh version 2\r\n! \r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\ninterface Loopback0\r\n ip address 123.3.3.3 255.255.255.255\r\n!\r\ninterface Ethernet0/0\r\n no ip address\r\n!\r\ninterface Ethernet0/0.12\r\n encapsulation dot1Q 12\r\n ip vrf forwarding GREEN\r\n ip address 102.2.123.2 255.255.255.252\r\n!\r\ninterface Ethernet0/0.13\r\n encapsulation dot1Q 13\r\n ip vrf forwarding BLUE\r\n ip address 102.2.123.2 255.255.255.252\r\n!\r\ninterface Ethernet0/0.14\r\n encapsulation dot1Q 14\r\n ip vrf forwarding RED\r\n ip address 102.2.123.2 255.255.255.252\r\n!\r\ninterface Ethernet0/0.15\r\n encapsulation dot1Q 15\r\n ip vrf forwarding YELLOW\r\n ip address 102.2.123.2 255.255.255.252\r\n!\r\ninterface Ethernet0/0.99\r\n encapsulation dot1Q 99\r\n ip vrf forwarding INET\r\n ip address 102.2.123.2 255.255.255.252\r\n!\r\ninterface Ethernet0/1\r\n ip address 123.10.1.10 255.255.255.252\r\n mpls ip\r\n!\r\ninterface Ethernet0/2\r\n ip address 123.10.1.13 255.255.255.252\r\n mpls ip\r\n!\r\ninterface Ethernet0/3\r\n no ip address\r\n!\r\ninterface Ethernet0/3.12\r\n encapsulation dot1Q 21\r\n ip vrf forwarding GREEN\r\n ip address 10.120.12.5 255.255.255.252\r\n!\r\ninterface Ethernet0/3.13\r\n encapsulation dot1Q 31\r\n ip vrf forwarding BLUE\r\n ip address 10.120.13.5 255.255.255.252\r\n!\r\ninterface Ethernet0/3.14\r\n encapsulation dot1Q 41\r\n ip vrf forwarding RED\r\n ip address 10.120.14.5 255.255.255.252\r\n!\r\ninterface Ethernet0/3.15\r\n encapsulation dot1Q 51\r\n ip vrf forwarding YELLOW\r\n ip address 10.120.15.5 255.255.255.252\r\n!\r\ninterface Ethernet0/3.99\r\n encapsulation dot1Q 999\r\n ip vrf forwarding INET\r\n ip address 10.120.99.5 255.255.255.252\r\n!\r\nrouter ospf 12345\r\n router-id 123.3.3.3\r\n network 123.0.0.0 0.255.255.255 area 0\r\n!\r\nrouter bgp 12345\r\n bgp router-id 123.3.3.3\r\n bgp log-neighbor-changes\r\n no bgp default ipv4-unicast\r\n neighbor 123.1.1.1 remote-as 12345\r\n neighbor 123.1.1.1 update-source Loopback0\r\n !\r\n address-family ipv4\r\n  neighbor 123.1.1.1 activate\r\n exit-address-family\r\n !\r\n address-family vpnv4\r\n  neighbor 123.1.1.1 activate\r\n  neighbor 123.1.1.1 send-community extended\r\n exit-address-family\r\n !\r\n address-family ipv4 vrf BLUE\r\n  neighbor 10.120.13.6 remote-as 65112\r\n  neighbor 10.120.13.6 activate\r\n  neighbor 102.2.123.1 remote-as 10002\r\n  neighbor 102.2.123.1 activate\r\n exit-address-family\r\n !\r\n address-family ipv4 vrf GREEN\r\n  neighbor 10.120.12.6 remote-as 65112\r\n  neighbor 10.120.12.6 activate\r\n  neighbor 102.2.123.1 remote-as 10002\r\n  neighbor 102.2.123.1 activate\r\n exit-address-family\r\n !\r\n address-family ipv4 vrf INET\r\n  neighbor 10.120.99.6 remote-as 65112\r\n  neighbor 10.120.99.6 activate\r\n  neighbor 102.2.123.1 remote-as 10002\r\n  neighbor 102.2.123.1 activate\r\n  neighbor 102.2.123.1 prefix-list PERMIT123 out\r\n exit-address-family\r\n !\r\n address-family ipv4 vrf RED\r\n  neighbor 10.120.14.6 remote-as 65112\r\n  neighbor 10.120.14.6 activate\r\n  neighbor 102.2.123.1 remote-as 10002\r\n  neighbor 102.2.123.1 activate\r\n exit-address-family\r\n !\r\n address-family ipv4 vrf YELLOW\r\n  neighbor 10.120.15.6 remote-as 65112\r\n  neighbor 10.120.15.6 activate\r\n  neighbor 102.2.123.1 remote-as 10002\r\n  neighbor 102.2.123.1 activate\r\n exit-address-family\r\n!\r\nip forward-protocol nd\r\n!\r\n!\r\nno ip http server\r\nno ip http secure-server\r\n!\r\n!\r\nip prefix-list PERMIT123 seq 5 permit 123.0.0.0/8 le 32\r\nip prefix-list PERMIT123 seq 10 permit 192.168.28.0/24\r\n!\r\n!snmp-server community ********\r\n!\r\nmpls ldp router-id Loopback0\r\n!\r\ncontrol-plane\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\n!\r\nline con 0\r\n exec-timeout 0 0\r\n logging synchronous\r\nline aux 0\r\nline vty 0 4\r\n login local\r\n transport input all\r\n!\r\n!\r\nend\r\n\r\n\n","time":"2019-01-29T16:11:38Z","statusCode":790200,"statusDescription":"Success."}
    


```python
text = "{configuration: Info via SNMP: sysoid=1.3.6.1.4.1.9.1.1,vendor=Cisco,model=DEVELOPMENT TEST SOFTWARE,hostname=R1,R1#show run,Building configuration...,,Current configuration : 2313 bytes,,version 15.4,service timestamps debug datetime msec,service timestamps log datetime msec,no service password-encryption,,hostname R1,,boot-start-marker,boot-end-marker,,aqm-register-fnf,,no logging on,enable secret ********,,no aaa new-model,clock timezone CET 1 0,mmi polling-interval 60,no mmi auto-configure,no mmi pvc,mmi snmp-timeout 180,,,,,,,,,,,,,,,no ip domain lookup,ip domain name netbraintech.com,ip cef,no ipv6 cef,ipv6 multicast rpf use-bgp,,multilink bundle-name authenticated,mpls label protocol ldp,no mpls ip propagate-ttl ,,,,,,,,,username ********,,redundancy,,,ip ssh version 2, ,,,,,,,,,,,,,interface Loopback0, ip address 123.1.1.1 255.255.255.255,,interface Ethernet0/0, no ip address,,interface Ethernet0/1, ip address 123.10.1.5 255.255.255.252,,interface Ethernet0/2, ip address 123.10.1.2 255.255.255.252,,interface Ethernet0/3, no ip address,,router ospf 12345, mpls ldp autoconfig, router-id 123.1.1.1, network 123.0.0.0 0.255.255.255 area 0,,router bgp 12345, bgp router-id 123.1.1.1, bgp log-neighbor-changes, no bgp default ipv4-unicast, neighbor iBGP peer-group, neighbor iBGP remote-as 12345, neighbor iBGP update-source Loopback0, neighbor PEER peer-group, neighbor PEER remote-as 12345, neighbor PEER update-source Loopback0, neighbor 123.2.2.2 peer-group iBGP, neighbor 123.3.3.3 peer-group iBGP, neighbor 123.6.6.6 peer-group iBGP, neighbor 123.7.7.7 peer-group iBGP, , address-family ipv4,  neighbor iBGP route-reflector-client,  neighbor 123.2.2.2 activate,  neighbor 123.3.3.3 activate,  neighbor 123.6.6.6 activate,  neighbor 123.7.7.7 activate, exit-address-family, , address-family vpnv4,  neighbor iBGP send-community extended,  neighbor iBGP route-reflector-client,  neighbor PEER send-community extended,  neighbor PEER route-reflector-client,  neighbor 123.2.2.2 activate,  neighbor 123.3.3.3 activate,  neighbor 123.6.6.6 activate,  neighbor 123.7.7.7 activate, exit-address-family,,ip forward-protocol nd,,,no ip http server,no ip http secure-server,,,snmp-server community ********,,mpls ldp router-id Loopback0,,control-plane,,,,,,,,,line con 0, exec-timeout 0 0, logging synchronous,line aux 0,line vty 0 4, login local, transport input all,,,end,,,time:2019-01-29T17:08:57Z,statusCode:790200,statusDescription:Success.}"
words = text.split(",") 
list(set(words))
```




    ['',
     'hostname=R1',
     ' neighbor 123.3.3.3 peer-group iBGP',
     ' neighbor PEER remote-as 12345',
     'time:2019-01-29T17:08:57Z',
     'interface Ethernet0/2',
     ' neighbor 123.2.2.2 peer-group iBGP',
     ' transport input all',
     'no ip http secure-server',
     ' exit-address-family',
     'mpls label protocol ldp',
     '  neighbor iBGP send-community extended',
     '  neighbor 123.7.7.7 activate',
     'line vty 0 4',
     'line aux 0',
     'aqm-register-fnf',
     ' no bgp default ipv4-unicast',
     'boot-start-marker',
     'no ip domain lookup',
     ' logging synchronous',
     'service timestamps debug datetime msec',
     'mpls ldp router-id Loopback0',
     '  neighbor 123.6.6.6 activate',
     ' neighbor iBGP update-source Loopback0',
     'service timestamps log datetime msec',
     'no ip http server',
     'no mpls ip propagate-ttl ',
     'interface Ethernet0/0',
     ' neighbor 123.6.6.6 peer-group iBGP',
     ' address-family ipv4',
     '{configuration: Info via SNMP: sysoid=1.3.6.1.4.1.9.1.1',
     'Building configuration...',
     'mmi polling-interval 60',
     ' neighbor 123.7.7.7 peer-group iBGP',
     'router ospf 12345',
     ' neighbor iBGP remote-as 12345',
     'mmi snmp-timeout 180',
     'multilink bundle-name authenticated',
     'redundancy',
     'boot-end-marker',
     'version 15.4',
     'no mmi pvc',
     'R1#show run',
     'snmp-server community ********',
     'interface Ethernet0/3',
     ' router-id 123.1.1.1',
     ' address-family vpnv4',
     'no logging on',
     'line con 0',
     'no aaa new-model',
     'vendor=Cisco',
     'ipv6 multicast rpf use-bgp',
     'model=DEVELOPMENT TEST SOFTWARE',
     '  neighbor 123.2.2.2 activate',
     ' ip address 123.10.1.5 255.255.255.252',
     ' bgp log-neighbor-changes',
     ' network 123.0.0.0 0.255.255.255 area 0',
     'statusDescription:Success.}',
     'interface Ethernet0/1',
     ' ip address 123.10.1.2 255.255.255.252',
     ' neighbor PEER peer-group',
     ' exec-timeout 0 0',
     ' neighbor PEER update-source Loopback0',
     '  neighbor PEER send-community extended',
     'ip cef',
     ' login local',
     'Current configuration : 2313 bytes',
     'username ********',
     'statusCode:790200',
     'hostname R1',
     'no service password-encryption',
     '  neighbor iBGP route-reflector-client',
     ' bgp router-id 123.1.1.1',
     '  neighbor 123.3.3.3 activate',
     'interface Loopback0',
     'ip domain name netbraintech.com',
     ' mpls ldp autoconfig',
     'no mmi auto-configure',
     ' no ip address',
     ' ip address 123.1.1.1 255.255.255.255',
     'router bgp 12345',
     ' ',
     'ip forward-protocol nd',
     'end',
     'no ipv6 cef',
     'control-plane',
     'clock timezone CET 1 0',
     'ip ssh version 2',
     '  neighbor PEER route-reflector-client',
     ' neighbor iBGP peer-group',
     'enable secret ********']



# cURL Code from Postman:


```python
curl -X GET \
  'http://192.168.28.79/ServicesAPI/API/V1/CMDB/DataEngine/DeviceData/Configuration?hostname=R1' \
  -H 'Postman-Token: 9d3502a2-6587-4be6-9d57-3d0e411dcb22' \
  -H 'cache-control: no-cache' \
  -H 'token: 220d6462-ba64-4058-83cb-affb2d55de78'
```

# Error Examples:


```python
###################################################################################################################    

"""Error 1: empty inputs"""

Input:
    
        hostname = "" # Can not be null.
    
Response:
    
    "Get Device Configuration failed! - 
    {
        "statusCode":791000,
        "statusDescription":"Null parameter: the parameter 'hostname' cannot be null."
    }"

###################################################################################################################    

"""Error 1: empty inputs"""

Input:
    
        hostname = "hahahaah" # On device called "hahahaah"
    
Response:
    
    "Get Device Configuration failed! - 
        {
            "statusCode":791006,
            "statusDescription":" Device Name is not in domain: hahahaah does not exist. 
                                " Device Name is not in domain: hahahaah"
        }"
```
