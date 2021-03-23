
# Return the devices path results


During current use case, the final goal is present the path result between two specified devices in current domain. There are totally 8 REST APIs we are going to concern to be a part of this use case, as shown in following:

1. Import python modules and global variables for sample code.
2. Call login API to get authentication token.
3. Call get_all_accessible_tenants API to get all accessible tenant IDs.
4. Call get_all_accessible_domains API to get all accessible domain IDs in specified tenant.
5. Call specify_a_working_domain API to specified which domain to work with.
6. Call resolve_device_gateway API to get devices gateway information. 
7. Call calculate_path API to get the task ID.
8. Call get_path_result API to get the result of calculation path.
9. Call logout API to log out from current account.

The sequencial of provided APIs is also the sequence of our workflow steps.

***Note***: if users want to find the path results of devices, then the step sequence must be followed. If users call these APIs with a different sequential then there would be no results or some errors would be occured.

## Step Explanation
***1. Import python modules and global variables for sample code.***<br>
> Note: If users try to use this code. please remember to change the "nb_url" to users' own working url.

***2. Call login API to get authentication token.***<br>
>Same with use case 2, we calling the login API with "username" and "password" as inputs in the first step. As response we can get the authentication token as one fixed input in following APIs calling. If users get errors when calling this API please check the API documentation on [Github_login](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Login%20API.md).

***3. call get_all_accessible_tenants API***
>After we got the token from previous section, we need to use this token as a key to find all tenants which we have the access authentication. During this step, the most important feature is to get the tenant id of the corresponding tenant which we decide to work inside. After running this API successfully, we will get the tenantId of the willing tenant which will be set as another input for next step API calling. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_tenant](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Get%20All%20Accessible%20Tenants%20API.md) 

***4. call get_all_accessible_domains API.***
>In this section, we are going to find all accessible domains in the corressponding tenant which we have got the tenantId from previous step. Similar with step 2, during current API call, we have to decide which domain we are going to work inside and get the domainId at meanwhile to prepare for next API calling. If users get errors when calling this API please check the API documentation on [Github_domain](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Get%20All%20Accessible%20Domains%20API.md) 

***5. call specify_a_working_domain API.***<br>
>After we running this step successfully, we directly complete the full login processes which means we totally join in Netbrain System by calling APIs(because we have record our tenantId and domainId，if users don't know the ID of corresponding tenant and domain please fully follow step 1 to step 4 in use case 1). Next step, we will start to use Netbrain functions formally. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_working_domain](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Specify%20A%20Working%20Domain%20API.md).

***6. call resolve_device_gateway API***
>Becasue we have specified the hostname of source device and destination device at beginning, we can calling resolve devices gateway API at here. Mention again, if users want to get path result by calling APIs then users must follow the sequencial of Step 2. In current section, we will input the Ips list we have got from previous section. After the API running successfully, we will get a gateway list with some device informations which is the required input for next section. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_Gateway](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Path%20Management/Path%20Calculation%20API.md)

***7. call calculate_path API***
>During this section, we are going to calling the Calculate Path API and set the gateway information list as one input(other inputs are shown in following code cell). When calling this API, users must input the required parameters correctly and follow the format of each inputs examples([Github_calPath](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Path%20Management/Path%20Calculation%20API.md)). After calling this API successfully, we will get the corresponding taskId of gateway information which has been put in. And the taskId is the only one required input for next section. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_calPath](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Path%20Management/Path%20Calculation%20API.md).

***8. call get_path_overview API***
>So far we attemp to the final functional step of this use case: to get the calculation result of the task which we have got the taskId in section 2c. After we running the following sample code successfully, we will finally get the path result in a json file. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_pathOverview](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Path%20Management/Path%20Calculation%20API.md). 

***9. call logout API***
>After we got all informations from this case, we have to logout from the Netbrain System.
If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_logout](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Logout%20API.md). 

## Sample Code

### import python modules, global variables 


```python
# import python modules
import requests
import json
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pprint

# Global Variables
nb_url = "http://customer NetBrain environment."
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'} 
TenantName = "tenant name"
DomainName = "domain name"
username = "user name"
password = "password"
source_device = "172.24.30.1"
destination_device = "172.24.101.2"
```

### Define calling Functions



```python
# call login API
def login(nb_url, username, password, headers):
    login_URL = nb_url + "/ServicesAPI/API/V1/Session"
    data = {
        "username" : username,      
        "password" : password  
    }
    try:
        # Do the HTTP request
        response = requests.post(login_URL, headers=headers, data = json.dumps(data), verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            js = response.json()
            return (js)
        else:
            return ("Get token failed! - " + str(response.text))
    except Exception as e:
        return (str(e))

# call get_all_accessible_tenants API
def get_all_accessible_tenants(nb_url, token, headers):
    Accessible_tenants_url = nb_url + "/ServicesAPI/API/V1/CMDB/Tenants"
    headers["Token"] = token
    try:
        # Do the HTTP request
        response = requests.get(Accessible_tenants_url, headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            result = response.json()
            tenants = result["tenants"]   
            return tenants
        else:
            return ("Get tenants failed! - " + str(response.text))
    except Exception as e: return (e)
    
# call get_all_accessible_domains API
def get_all_accessible_domains(nb_url, tenantId, token, headers):
    Accessible_domains_url = nb_url + "/ServicesAPI/API/V1/CMDB/Domains"
    headers["Token"] = token
    data = {"tenantId": tenantId}
    try:
        # Do the HTTP request
        response = requests.get(Accessible_domains_url, params = data, headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            result = response.json()
            domains = result["domains"]
            return domains
        else:
            return ("Get domains failed! - " + str(response.text))
    except Exception as e: print (str(e))
        
# call specify_a_working_domain API
def specify_a_working_domain(tenantId, domainId, nb_url, headers, token):
    Specify_a_working_domain_url = nb_url + "/ServicesAPI/API/V1/Session/CurrentDomain"
    headers["Token"] = token
    body = {
        "tenantId": tenantId,
        "domainId": domainId
    }
    
    try:
        # Do the HTTP request
        response = requests.put(Specify_a_working_domain_url, data=json.dumps(body), headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            result = response.json()
            return (domainId)
            
        elif response.status_code != 200:
            return ("Login failed! - " + str(response.text))

    except Exception as e: print (str(e))
        
# call resolve device gateway API
def resolve_device_gateway(token, ipOrHost, headers):
    Resolve_Device_Gateway_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Gateways"
    headers["Token"] = token
    data = {"ipOrHost":ipOrHost}
    try:
        response = requests.get(Resolve_Device_Gateway_url, params = data, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return ("Create module attribute failed! - " + str(response.text))

    except Exception as e:
        print (str(e))
        
# call calculate path API
def calculate_path(source_gateway, headers, token):
    Calculate_Path_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation"
    headers["Token"] = token
    
    gwName = source_gateway["gatewayName"]
    gwType = source_gateway["type"]
    gw = source_gateway["payload"]

    sourceIP = source_device
    sourcePort = None #can be 8080
    destIP = destination_device
    destPort = 0
    pathAnalysisSet = 2
    protocol = 4
    isLive = True

    body = {
        "sourceIP" : sourceIP,                # IP address of the source device.
        "sourcePort" : sourcePort,
        "sourceGateway" : {
            "type" : gwType,
            "gatewayName" : gwName,
            "payload" : gw
        },    
        "destIP" : destIP,                    # IP address of the destination device.
        "destPort" : destPort,
        "protocol" : protocol,                # Specify the application protocol, check online help, such as 4 for IPv4.
        "isLive" : isLive                     # False: Current Baseline; True: Live access
    } 
    
    
    try:
        response = requests.post(Calculate_Path_url, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            return (result)
        else:
            return ("Calculate path failed! - " + str(response.text))

    except Exception as e:
        return (str(e)) 

# call get path calculation overview API.
def get_path_result(taskID, headers, token):
    Get_Path_Calulation_Result_url = nb_url + "/ServicesAPI/API/V1/CMDB/Path/Calculation/" + str(taskID) + "/OverView"
    headers["Token"] = token
    try:
        response = requests.get(Get_Path_Calulation_Result_url, headers = headers, verify = False)
        result = response.json()
        code = result["statusCode"]
        print(".")
        if code != 790200:
            time.sleep(5)
            return get_path_result(taskID, headers, token)
        else:
            return (result["path_overview"])

    except Exception as e:
        return (str(e)) 

        
        
        
# call logout API
def logout(nb_url, token, headers):
    Logout_url = nb_url + "/ServicesAPI/API/V1/Session"
    headers["token"] = token
    
    try:
        # Do the HTTP request
        response = requests.delete(Logout_url, headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            js = response.json()
            return (js)
        else:
            return ("Session logout failed! - " + str(response.text))

    except Exception as e:
        return (str(e))

```

### Define main function


```python
def main(nb_url, headers, TenantName, DomainName, username, password, source_device_Ip, destination_device_Ip):
    # Calling login API
    print("Calling login API---------------------------------------------------------------------------------------")
    result = login(nb_url, username, password, headers)
    print(result) # print out the authentication token.
    token = result["token"]
    print(token)
    print("")
    
    # Calling get accessible tenant API
    print("Calling get accessible tenant API---------------------------------------------------------------------------------------")
    tenants = get_all_accessible_tenants(nb_url, token, headers)
    tenant =  [x for x in tenants if x["tenantName"] == TenantName] # Name of the tenant which we are going to work inside
    tenantId = tenant[0]["tenantId"]
    print("Tenant ID : " + tenantId) # print out the specified tenant id.
    print("")

    # Calling get accessible domain API
    print("Calling get accessible domain API---------------------------------------------------------------------------------------")
    domains = get_all_accessible_domains(nb_url, tenantId, token, headers)
    domain =  [x for x in domains if x["domainName"] == DomainName]# Name of the domain which we are going to work inside
    domainId = domain[0]["domainId"]
    print("Domain ID : " + domainId) # Print out the specified domain Id.
    print("")

    # Calling specify domain API
    print("Calling specify domain API---------------------------------------------------------------------------------------")
    res =  specify_a_working_domain(tenantId, domainId, nb_url, headers, token)
    print ("Domain ID of Specified Working Domain : " + res)
    print("")
    
    # Calling resolve device gateway API
    print("Calling resolve device gateway API---------------------------------------------------------------------------------------")
    res =  resolve_device_gateway(token, source_device, headers)
    gateway = res["gatewayList"][0]
    print ("Detail information of the first gateway in source device: ")
    pprint.pprint(gateway)
    print("")
    
    # Calling resolve device gateway API
    print("Calling calculate path API---------------------------------------------------------------------------------------")
    task =  calculate_path(gateway, headers, token)
    print ("Response of the calculate path API : ")
    pprint.pprint(task)
    print("")
    
    # Calling get path calculation overview API
    print("Calling get path calculation overview API---------------------------------------------------------------------------------------")
    print("########################################################################################################")
    taskID = task["taskID"]
    path =  get_path_result(taskID, headers, token)  
    print ("Detail information of path hops: ")
    pprint.pprint(path)
    print("########################################################################################################")
    print("")
    
    # Calling logout API
    print("Calling logout API---------------------------------------------------------------------------------------")
    Logout = logout(nb_url, token, headers)
    print(Logout)

main(nb_url, headers, TenantName, DomainName, username, password, source_device, destination_device)
```

    Calling login API---------------------------------------------------------------------------------------
    {'token': '2289e3fa-a64d-46bd-b150-a537f1437ef9', 'statusCode': 790200, 'statusDescription': 'Success.'}
    2289e3fa-a64d-46bd-b150-a537f1437ef9
    
    Calling get accessible tenant API---------------------------------------------------------------------------------------
    Tenant ID : 823e096b-093a-10f1-1471-21a9a5ff509c
    
    Calling get accessible domain API---------------------------------------------------------------------------------------
    Domain ID : af4581fd-a705-4ddf-a878-fd4c6f304b96
    
    Calling specify domain API---------------------------------------------------------------------------------------
    Domain ID of Specified Working Domain : af4581fd-a705-4ddf-a878-fd4c6f304b96
    
    Calling resolve device gateway API---------------------------------------------------------------------------------------
    Detail information of the first gateway in source device: 
    {'gatewayName': 'GW2Lab.GigabitEthernet0/1(172.24.30.1)',
     'payload': '{"ip": "172.24.30.1", "endPointInfo": {"deviceId": '
                '"100f18a9-ab16-499f-8ef4-e5ebce425319", "interfaceId": '
                '"2eac71ff-5743-4a39-ab3b-b0771ac7d356"}, "device": "GW2Lab", '
                '"deviceId": "100f18a9-ab16-499f-8ef4-e5ebce425319", "interface": '
                '"GigabitEthernet0/1", "interfaceId": '
                '"2eac71ff-5743-4a39-ab3b-b0771ac7d356", "prefixLen": 30}',
     'type': 'Device Interface'}
    
    Calling calculate path API---------------------------------------------------------------------------------------
    Response of the calculate path API : 
    {'statusCode': 790200,
     'statusDescription': 'Success.',
     'taskID': '075e35b0-71d1-490f-834d-7393a3291e08'}
    
    Calling get path calculation overview API---------------------------------------------------------------------------------------
    ########################################################################################################
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    .
    Detail information of path hops: 
    [{'failure_reasons': [],
      'path_list': [{'branch_list': [{'failure_reason': '',
                                      'hop_detail_list': [{'fromDev': {'devId': '100f18a9-ab16-499f-8ef4-e5ebce425319',
                                                                       'devName': 'GW2Lab',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': 'GigabitEthernet0/1',
                                                                        'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                                 'value': 'GigabitEthernet0/1 '
                                                                                                          '172.24.30.1/30'},
                                                                        'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                       'value': 'ec46fc9c-2bcf-4478-87c8-7abb41aede37'}},
                                                           'hopId': 'ed6b580c-48da-4772-993f-0fc5493811b3',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '51935453-4630-403b-acbf-e3debaa30082',
                                                           'mediaInfo': {'mediaName': '172.24.30.0/30',
                                                                         'mediaType': 'Lan',
                                                                         'neat': True,
                                                                         'topoType': 'L3_Topo_Type'},
                                                           'parentHopId': '',
                                                           'preHopId': '00000000-0000-0000-0000-000000000000',
                                                           'sequnce': 0,
                                                           'toDev': {'devId': '09f62415-44a2-45d5-9039-150c14936b2e',
                                                                     'devName': 'NY_Router',
                                                                     'devType': 2,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': 'FastEthernet0/0',
                                                                      'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                               'value': 'FastEthernet0/0 '
                                                                                                        '172.24.30.2/30'},
                                                                      'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                     'value': '8f195d7d-3b65-4757-878a-1cdfd223d119'}},
                                                           'topoType': 'L3_Topo_Type',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'GW2Lab',
                                                                            'dev_type': 2,
                                                                            'in_intf': 'GigabitEthernet0/1',
                                                                            'in_intf_schema': 'intfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'FastEthernet0/0 '
                                                                                                '172.24.30.2/30',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'NY_Router',
                                                                            'next_dev_type': 2,
                                                                            'next_hop_ip': '172.24.30.2',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'GigabitEthernet0/1 '
                                                                                        '172.24.30.1/30',
                                                                            'out_intf_schema': 'ipIntfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                          {'fromDev': {'devId': '09f62415-44a2-45d5-9039-150c14936b2e',
                                                                       'devName': 'NY_Router',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': 'Vlan100',
                                                                        'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                                 'value': 'Vlan100 '
                                                                                                          '172.24.30.5/30'},
                                                                        'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                       'value': '47e8e298-eb67-4bdc-968f-a940edb8262e'}},
                                                           'hopId': '814661b8-3a34-4332-8082-4695e0af72ea',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': 'b0492071-04fc-4d12-940d-6ee0ec202f40',
                                                           'mediaInfo': {'mediaName': '172.24.30.4/30',
                                                                         'mediaType': 'Lan',
                                                                         'neat': True,
                                                                         'topoType': 'L3_Topo_Type'},
                                                           'parentHopId': '',
                                                           'preHopId': 'ed6b580c-48da-4772-993f-0fc5493811b3',
                                                           'sequnce': 1,
                                                           'toDev': {'devId': '066da03d-50ea-4fe8-b9a6-f41095c8dd4f',
                                                                     'devName': 'NY_POPP',
                                                                     'devType': 2,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': 'Ethernet0/1',
                                                                      'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                               'value': 'Ethernet0/1 '
                                                                                                        '172.24.30.6/30'},
                                                                      'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                     'value': '3797846c-3308-4d84-b26d-4a9f87cae50e'}},
                                                           'topoType': 'L3_Topo_Type',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'NY_Router',
                                                                            'dev_type': 2,
                                                                            'in_intf': 'FastEthernet0/0 '
                                                                                       '172.24.30.2/30',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'Ethernet0/1 '
                                                                                                '172.24.30.6/30',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'NY_POPP',
                                                                            'next_dev_type': 2,
                                                                            'next_hop_ip': '172.24.30.6',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'Vlan100 '
                                                                                        '172.24.30.5/30',
                                                                            'out_intf_schema': 'ipIntfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                          {'fromDev': {'devId': '066da03d-50ea-4fe8-b9a6-f41095c8dd4f',
                                                                       'devName': 'NY_POPP',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': 'Ethernet0/0',
                                                                        'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                                 'value': 'Ethernet0/0 '
                                                                                                          '172.24.31.65/26'},
                                                                        'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                       'value': '7404c730-6930-445c-a801-687c9c31e42c'}},
                                                           'hopId': '0a3ce73b-ebf8-43c6-aa69-a7377e949a85',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': 'c555d2a2-5819-4276-ad53-dad4d870f407',
                                                           'mediaInfo': {'mediaName': '172.24.31.64/26',
                                                                         'mediaType': 'Lan',
                                                                         'neat': False,
                                                                         'topoType': 'L3_Topo_Type'},
                                                           'parentHopId': '',
                                                           'preHopId': '814661b8-3a34-4332-8082-4695e0af72ea',
                                                           'sequnce': 2,
                                                           'toDev': {'devId': 'fe2036f0-4cc3-469e-9df4-6479241392d5',
                                                                     'devName': 'NY-core-bak',
                                                                     'devType': 2,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': 'FastEthernet0/0',
                                                                      'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                               'value': 'FastEthernet0/0 '
                                                                                                        '172.24.31.125/26'},
                                                                      'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                     'value': '52ad6492-5b14-4c24-95f3-dc71cc24c619'}},
                                                           'topoType': 'L3_Topo_Type',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'NY_POPP',
                                                                            'dev_type': 2,
                                                                            'in_intf': 'Ethernet0/1 '
                                                                                       '172.24.30.6/30',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'FastEthernet0/0 '
                                                                                                '172.24.31.125/26',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'NY-core-bak',
                                                                            'next_dev_type': 2,
                                                                            'next_hop_ip': '172.24.31.125',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'Ethernet0/0 '
                                                                                        '172.24.31.65/26',
                                                                            'out_intf_schema': 'ipIntfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                          {'fromDev': {'devId': 'fe2036f0-4cc3-469e-9df4-6479241392d5',
                                                                       'devName': 'NY-core-bak',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': 'FastEthernet0/1.1',
                                                                        'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                                 'value': 'FastEthernet0/1.1 '
                                                                                                          '172.24.31.193/26'},
                                                                        'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                       'value': '5a94e073-8d9d-41f4-81a8-a64bcf1efbb7'}},
                                                           'hopId': '0e142a83-4b4f-4c5e-b450-c275104628b5',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '791b0426-2683-4c68-853c-822701f2474f',
                                                           'mediaInfo': {'mediaName': '172.24.31.192/26',
                                                                         'mediaType': 'Lan',
                                                                         'neat': True,
                                                                         'topoType': 'L3_Topo_Type'},
                                                           'parentHopId': '',
                                                           'preHopId': '0a3ce73b-ebf8-43c6-aa69-a7377e949a85',
                                                           'sequnce': 3,
                                                           'toDev': {'devId': '26e3e35d-4a4a-4fbd-9a40-17d65801b465',
                                                                     'devName': 'BJ*POP',
                                                                     'devType': 2,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': 'FastEthernet0/1',
                                                                      'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                               'value': 'FastEthernet0/1 '
                                                                                                        '172.24.31.195/26'},
                                                                      'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                     'value': '7bcaef5b-50b5-4594-96c7-7a8bab6267dc'}},
                                                           'topoType': 'L3_Topo_Type',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'NY-core-bak',
                                                                            'dev_type': 2,
                                                                            'in_intf': 'FastEthernet0/0 '
                                                                                       '172.24.31.125/26',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'FastEthernet0/1 '
                                                                                                '172.24.31.195/26',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'BJ*POP',
                                                                            'next_dev_type': 2,
                                                                            'next_hop_ip': '172.24.31.195',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'FastEthernet0/1.1 '
                                                                                        '172.24.31.193/26',
                                                                            'out_intf_schema': 'ipIntfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                          {'fromDev': {'devId': '26e3e35d-4a4a-4fbd-9a40-17d65801b465',
                                                                       'devName': 'BJ*POP',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': 'FastEthernet0/0',
                                                                        'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                                 'value': 'FastEthernet0/0 '
                                                                                                          '172.24.32.225/28'},
                                                                        'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                       'value': 'cd71ec6b-e6de-4c27-bf9a-b24e85604770'}},
                                                           'hopId': '04b1aba4-d93b-4ef1-871e-26665c41ea91',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '49f42014-4114-4427-8f78-fba8b3321597',
                                                           'mediaInfo': {'mediaName': '172.24.32.224/28',
                                                                         'mediaType': 'Lan',
                                                                         'neat': True,
                                                                         'topoType': 'L3_Topo_Type'},
                                                           'parentHopId': '',
                                                           'preHopId': '0e142a83-4b4f-4c5e-b450-c275104628b5',
                                                           'sequnce': 4,
                                                           'toDev': {'devId': '0c61fd0d-8dca-4b9e-80af-b000236e3c04',
                                                                     'devName': 'BJ_core_3550',
                                                                     'devType': 2001,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': 'FastEthernet0/1',
                                                                      'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                               'value': 'FastEthernet0/1 '
                                                                                                        '172.24.32.226/28'},
                                                                      'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                     'value': '10c98513-04e9-4b4f-bc2d-f23b36484b0d'}},
                                                           'topoType': 'L3_Topo_Type',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'BJ*POP',
                                                                            'dev_type': 2,
                                                                            'in_intf': 'FastEthernet0/1 '
                                                                                       '172.24.31.195/26',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'FastEthernet0/1 '
                                                                                                '172.24.32.226/28',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'BJ_core_3550',
                                                                            'next_dev_type': 2001,
                                                                            'next_hop_ip': '172.24.32.226',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'FastEthernet0/0 '
                                                                                        '172.24.32.225/28',
                                                                            'out_intf_schema': 'ipIntfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                          {'fromDev': {'devId': '0c61fd0d-8dca-4b9e-80af-b000236e3c04',
                                                                       'devName': 'BJ_core_3550',
                                                                       'devType': 2001,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': 'Port-channel10',
                                                                        'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                                 'value': 'Port-channel10 '
                                                                                                          '172.24.100.1/30'},
                                                                        'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                       'value': 'eb22ea5d-dcf4-4803-b974-2d80819ff283'}},
                                                           'hopId': '53ce2a5a-314e-4117-8431-b6975dc6b256',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '45e325a1-a7cd-4152-a4dc-2ad64e780422',
                                                           'mediaInfo': {'mediaName': '172.24.100.0/30',
                                                                         'mediaType': 'Lan',
                                                                         'neat': True,
                                                                         'topoType': 'L3_Topo_Type'},
                                                           'parentHopId': '',
                                                           'preHopId': '04b1aba4-d93b-4ef1-871e-26665c41ea91',
                                                           'sequnce': 5,
                                                           'toDev': {'devId': '93a1010e-7339-4276-9fcb-0d24b11e7c56',
                                                                     'devName': 'BJ-L2-Core-A',
                                                                     'devType': 2001,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': 'Port-channel10',
                                                                      'intfDisplaySchemaObj': {'schema': 'ipIntfs.name',
                                                                                               'value': 'Port-channel10 '
                                                                                                        '172.24.100.2/30'},
                                                                      'intfKeyObj': {'schema': 'ipIntfs._id',
                                                                                     'value': 'aac0d474-43c8-4d89-9d40-95730e83b73e'}},
                                                           'topoType': 'L3_Topo_Type',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'BJ_core_3550',
                                                                            'dev_type': 2001,
                                                                            'in_intf': 'FastEthernet0/1 '
                                                                                       '172.24.32.226/28',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': 'Port-channel10 '
                                                                                                '172.24.100.2/30',
                                                                            'next_dev_in_intf_schema': 'ipIntfs',
                                                                            'next_dev_in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_name': 'BJ-L2-Core-A',
                                                                            'next_dev_type': 2001,
                                                                            'next_hop_ip': '172.24.100.2',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'Port-channel10 '
                                                                                        '172.24.100.1/30',
                                                                            'out_intf_schema': 'ipIntfs',
                                                                            'out_intf_topo_type': 'L3_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}},
                                                          {'fromDev': {'devId': '93a1010e-7339-4276-9fcb-0d24b11e7c56',
                                                                       'devName': 'BJ-L2-Core-A',
                                                                       'devType': 2001,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                 'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                       'value': ''}},
                                                           'hopId': '5008ad89-dcb8-4b8a-89c4-68cf5341e2ad',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '',
                                                           'mediaInfo': {'mediaName': '',
                                                                         'mediaType': '',
                                                                         'neat': False,
                                                                         'topoType': ''},
                                                           'parentHopId': '',
                                                           'preHopId': '53ce2a5a-314e-4117-8431-b6975dc6b256',
                                                           'sequnce': 6,
                                                           'toDev': {'devId': '',
                                                                     'devName': '',
                                                                     'devType': 0,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': '',
                                                                      'intfDisplaySchemaObj': {'schema': '',
                                                                                               'value': ''},
                                                                      'intfKeyObj': {'schema': '',
                                                                                     'value': ''}},
                                                           'topoType': '',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'BJ-L2-Core-A',
                                                                            'dev_type': 2001,
                                                                            'in_intf': 'Port-channel10 '
                                                                                       '172.24.100.2/30',
                                                                            'in_intf_schema': 'ipIntfs',
                                                                            'in_intf_topo_type': 'L3_Topo_Type',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                      'status': 'Success'}],
                     'description': '172.24.30.1 -> 172.24.101.2',
                     'failure_reasons': [],
                     'path_name': 'L3 Path',
                     'status': 'Success'},
                    {'branch_list': [{'failure_reason': 'No L2 connections were '
                                                        'found',
                                      'hop_detail_list': [{'fromDev': {'devId': '09f62415-44a2-45d5-9039-150c14936b2e',
                                                                       'devName': 'NY_Router',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': 'intfs.name',
                                                                                                 'value': 'FastEthernet0/2/0'},
                                                                        'intfKeyObj': {'schema': 'intfs._id',
                                                                                       'value': ''}},
                                                           'hopId': 'fcf53857-42ac-490b-aa57-dedb8c682450',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '',
                                                           'mediaInfo': {'mediaName': '',
                                                                         'mediaType': '',
                                                                         'neat': False,
                                                                         'topoType': ''},
                                                           'parentHopId': '814661b8-3a34-4332-8082-4695e0af72ea',
                                                           'preHopId': '00000000-0000-0000-0000-000000000000',
                                                           'sequnce': 0,
                                                           'toDev': {'devId': '',
                                                                     'devName': '',
                                                                     'devType': 0,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': '',
                                                                      'intfDisplaySchemaObj': {'schema': '',
                                                                                               'value': ''},
                                                                      'intfKeyObj': {'schema': '',
                                                                                     'value': ''}},
                                                           'topoType': '',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'NY_Router',
                                                                            'dev_type': 2,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': 'FastEthernet0/2/0',
                                                                            'out_intf_schema': 'intfs',
                                                                            'out_intf_topo_type': 'L2_Topo_Type',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                      'status': 'Failed'}],
                     'description': '172.24.30.5 -> 172.24.30.6',
                     'failure_reasons': [],
                     'path_name': 'L2 Path',
                     'status': 'Failed'},
                    {'branch_list': [{'failure_reason': 'No L2 connections were '
                                                        'found',
                                      'hop_detail_list': [{'fromDev': {'devId': '066da03d-50ea-4fe8-b9a6-f41095c8dd4f',
                                                                       'devName': 'NY_POPP',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                 'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                       'value': ''}},
                                                           'hopId': 'dcfd6068-4f64-4004-967d-b11340df9fb2',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '',
                                                           'mediaInfo': {'mediaName': '',
                                                                         'mediaType': '',
                                                                         'neat': False,
                                                                         'topoType': ''},
                                                           'parentHopId': '0a3ce73b-ebf8-43c6-aa69-a7377e949a85',
                                                           'preHopId': '00000000-0000-0000-0000-000000000000',
                                                           'sequnce': 0,
                                                           'toDev': {'devId': '',
                                                                     'devName': '',
                                                                     'devType': 0,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': '',
                                                                      'intfDisplaySchemaObj': {'schema': '',
                                                                                               'value': ''},
                                                                      'intfKeyObj': {'schema': '',
                                                                                     'value': ''}},
                                                           'topoType': '',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'NY_POPP',
                                                                            'dev_type': 2,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                      'status': 'Failed'}],
                     'description': '172.24.31.65 -> 172.24.31.125',
                     'failure_reasons': [],
                     'path_name': 'L2 Path',
                     'status': 'Failed'},
                    {'branch_list': [{'failure_reason': 'No L2 connections were '
                                                        'found',
                                      'hop_detail_list': [{'fromDev': {'devId': 'fe2036f0-4cc3-469e-9df4-6479241392d5',
                                                                       'devName': 'NY-core-bak',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                 'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                       'value': ''}},
                                                           'hopId': 'a9e784b8-f1d6-4ccc-b94f-ba909c6a20a9',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '',
                                                           'mediaInfo': {'mediaName': '',
                                                                         'mediaType': '',
                                                                         'neat': False,
                                                                         'topoType': ''},
                                                           'parentHopId': '0e142a83-4b4f-4c5e-b450-c275104628b5',
                                                           'preHopId': '00000000-0000-0000-0000-000000000000',
                                                           'sequnce': 0,
                                                           'toDev': {'devId': '',
                                                                     'devName': '',
                                                                     'devType': 0,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': '',
                                                                      'intfDisplaySchemaObj': {'schema': '',
                                                                                               'value': ''},
                                                                      'intfKeyObj': {'schema': '',
                                                                                     'value': ''}},
                                                           'topoType': '',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'NY-core-bak',
                                                                            'dev_type': 2,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                      'status': 'Failed'}],
                     'description': '172.24.31.193 -> 172.24.31.195',
                     'failure_reasons': [],
                     'path_name': 'L2 Path',
                     'status': 'Failed'},
                    {'branch_list': [{'failure_reason': 'No L2 connections were '
                                                        'found',
                                      'hop_detail_list': [{'fromDev': {'devId': '26e3e35d-4a4a-4fbd-9a40-17d65801b465',
                                                                       'devName': 'BJ*POP',
                                                                       'devType': 2,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                 'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                       'value': ''}},
                                                           'hopId': '72d21630-b8c0-4fd5-b2dc-ae1e5e2256a8',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '',
                                                           'mediaInfo': {'mediaName': '',
                                                                         'mediaType': '',
                                                                         'neat': False,
                                                                         'topoType': ''},
                                                           'parentHopId': '04b1aba4-d93b-4ef1-871e-26665c41ea91',
                                                           'preHopId': '00000000-0000-0000-0000-000000000000',
                                                           'sequnce': 0,
                                                           'toDev': {'devId': '',
                                                                     'devName': '',
                                                                     'devType': 0,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': '',
                                                                      'intfDisplaySchemaObj': {'schema': '',
                                                                                               'value': ''},
                                                                      'intfKeyObj': {'schema': '',
                                                                                     'value': ''}},
                                                           'topoType': '',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'BJ*POP',
                                                                            'dev_type': 2,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                      'status': 'Failed'}],
                     'description': '172.24.32.225 -> 172.24.32.226',
                     'failure_reasons': [],
                     'path_name': 'L2 Path',
                     'status': 'Failed'},
                    {'branch_list': [{'failure_reason': 'No L2 connections were '
                                                        'found',
                                      'hop_detail_list': [{'fromDev': {'devId': '0c61fd0d-8dca-4b9e-80af-b000236e3c04',
                                                                       'devName': 'BJ_core_3550',
                                                                       'devType': 2001,
                                                                       'domainId': ''},
                                                           'fromIntf': {'PhysicalInftName': '',
                                                                        'intfDisplaySchemaObj': {'schema': '',
                                                                                                 'value': ''},
                                                                        'intfKeyObj': {'schema': '',
                                                                                       'value': ''}},
                                                           'hopId': '966ec229-0cd6-4940-a1b4-60f3c700042e',
                                                           'isComplete': False,
                                                           'isP2P': False,
                                                           'mediaId': '',
                                                           'mediaInfo': {'mediaName': '',
                                                                         'mediaType': '',
                                                                         'neat': False,
                                                                         'topoType': ''},
                                                           'parentHopId': '53ce2a5a-314e-4117-8431-b6975dc6b256',
                                                           'preHopId': '00000000-0000-0000-0000-000000000000',
                                                           'sequnce': 0,
                                                           'toDev': {'devId': '',
                                                                     'devName': '',
                                                                     'devType': 0,
                                                                     'domainId': ''},
                                                           'toIntf': {'PhysicalInftName': '',
                                                                      'intfDisplaySchemaObj': {'schema': '',
                                                                                               'value': ''},
                                                                      'intfKeyObj': {'schema': '',
                                                                                     'value': ''}},
                                                           'topoType': '',
                                                           'trafficState': {'acl': '',
                                                                            'alg': -1,
                                                                            'dev_name': 'BJ_core_3550',
                                                                            'dev_type': 2001,
                                                                            'in_intf': '',
                                                                            'in_intf_schema': '',
                                                                            'in_intf_topo_type': '',
                                                                            'next_dev_in_intf': '',
                                                                            'next_dev_in_intf_schema': '',
                                                                            'next_dev_in_intf_topo_type': '',
                                                                            'next_dev_name': '',
                                                                            'next_dev_type': 0,
                                                                            'next_hop_ip': '',
                                                                            'next_hop_mac': '',
                                                                            'out_intf': '',
                                                                            'out_intf_schema': '',
                                                                            'out_intf_topo_type': '',
                                                                            'pbr': '',
                                                                            'vrf': ''}}],
                                      'status': 'Failed'}],
                     'description': '172.24.100.1 -> 172.24.100.2',
                     'failure_reasons': [],
                     'path_name': 'L2 Path',
                     'status': 'Failed'}],
      'status': 'Success'}]
    ########################################################################################################
    
    Calling logout API---------------------------------------------------------------------------------------
    {'statusCode': 790200, 'statusDescription': 'Success.'}
    


```python

```
