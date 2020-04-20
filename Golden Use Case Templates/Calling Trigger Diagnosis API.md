
# Retrive multiple dynamic map by calling trigger diagnosis API
In this use case,  we will totally focus on trigger diagnosis API to trigger multiple dynamic map as diagnosis referances. At the beginning, we must clarify that the trigger diagnosis API is one of the most important API in Netbrain's API library. Obviously it can trigger a few dynamic maps from Netbrain to help engineers diagnose the real time issuses of network, actually the most significant value of this API is that it is the bridge for 3rd party data integration with Netbrain. Thus, if users eager to intergration with NetBrain's function and data from other software, this API is the only and the easist way so far. 

**[Step 1: Use case preparation](Step-1:-Use-case-preparation)**
>> 1a. import all useful modules and create global variables<br>
>> 1b. call login API<br>
>> 1c. call specify_a_working_domain API<br>

**[Step 2: Calling trigger_diagnosis API](Step-2:-Calling-trigger_diagnosis-API)**
>> 2a. Call API to Default Neighbor Map<br>
>> 2b. Call API to Open Site Map of The Device<br>
>> 2c. Call API to Trigger An Existing Map<br>
>> 2d. Call API to Map A Path<br>

## Step 1: Use case preparation.
***1a. import the corresponding modules in python and some fixed input parameters.***<br>
> Note: If users try to use this code. please remember to change the "nb_url" to users' own working url.

***1b. login API.***<br>
>Same with use case 2, we calling the login API with "username" and "password" as inputs in the first step. As response we can get the authentication token as one fixed input in following APIs calling. If users get errors when calling this API please check the API documentation on [Github_login](https://github.com/NetBrainAPI/North-Bound-API/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Login%20API.md).

***1c. specify_a_working_domain API.***<br>
>After we running this step successfully, we directly complete the full login processes which means we totally join in Netbrain System by calling APIs(because we have record our tenantId and domainId，if users don't know the ID of corresponding tenant and domain please fully follow step 1 to step 4 in use case 1). Next step, we will start to use Netbrain functions formally. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_domain](https://github.com/NetBrainAPI/North-Bound-API/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Specify%20A%20Working%20Domain%20API.md).



```python
# import python modules 
import requests
import time
import urllib3
import pprint
#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import json

nb_url = "http://192.168.28.79"
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'} 
TenantName = "Initial Tenant"
DomainName = "Support and Service"
username = "gdluserTest"
password = "123456"
tenant_id = "fb24f3f0-81a7-1929-4b8f-99106c23fa5b"
domain_id = "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
trigger_url = nb_url + "/ServicesAPI/API/V1/Triggers/Run"
```


```python
# Calling Login API.

body = {
    "username" : username,      
    "password" : password  
}

login_URL = nb_url + "/ServicesAPI/API/V1/Session"

def login(login_URL, body, headers):
    try:
        # Do the HTTP request
        response = requests.post(login_URL, headers=headers, data = json.dumps(body), verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            js = response.json()
            return (js["token"])
        else:
            return ("Get token failed! - " + str(response.text))
    except Exception as e:
        return (str(e))
    
token = login(login_URL, body, headers)
print(token) # print out the authentication token.
```

API Response:     e85a53f1-5741-4d3d-9200-e1473c5453a4
    


```python
# Calling Specify A Working Domain API

Specify_a_working_domain_url = nb_url + "/ServicesAPI/API/V1/Session/CurrentDomain"

def specify_a_working_domain(tenantId, domainId, Specify_a_working_domain_url, headers, token):
    headers["Token"] = token
    body = {
        "tenantId": tenant_id,
        "domainId": domain_id
    }
    
    try:
        # Do the HTTP request
        response = requests.put(Specify_a_working_domain_url, data=json.dumps(body), headers=headers, verify=False)
        # Check for HTTP codes other than 200
        if response.status_code == 200:
            # Decode the JSON response into a dictionary and use the data
            result = response.json()
            return ("Working Domain Specified Successfully, with domainId: " + domainId)
            
        elif response.status_code != 200:
            return ("Login failed! - " + str(response.text))

    except Exception as e: print (str(e))

res =  specify_a_working_domain(tenantId, domainId, Specify_a_working_domain_url, headers, token)
print (res)
```

API Response:     Working Domain Specified Successfully, with domainId: 850ff5e9-c639-404d-85a3-d920dbee509c
    

## Step 2: Calling Trigger Diagnosis API 
After we finished all preparations, we are going to start to calling this API in step. One of the most significant characteristic of trigger diagnosis API is the gigantic input body (as a post function the body input is reasonable). There are more than 100 attributes in the entire body parameter. The body including 6 sub-sections, each section provide different input informations.See detail explanation in [Github_trigger_diagnosis](https://github.com/NetBrainAPI/NetBrain-REST-API-V8.01/blob/master/REST%20APIs%20Documentation/Trigger%20Diagnosis%20API/Trigger%20Diagnosis%20API%20V8.md)<br>

>***Note:*** before calling this API, users must create a stub in Netbrain GUI system first: click desktop menu button -> System Automation Task Manager -> API Stub Manager -> Add Stub.

***2a. Calling API to Create Default Neighbor Map***<br>
>Note: 

>1) if the input value of map_setting.device is empty,
then the API response will return the map about basic_setting.device defaulty.<br>

>2) if the input value of map_setting.include_neighbor is empty,
the API response map will return all neighbors of map_setting.device defaultly.<br>

>3) if the input value of map_setting.device set as an un-exist device name,
an error will occured : {'error': 'Failed to find the designated device SW40'}.<br>

***2b. Calling API to Open Site Map of The Device.***<br>
***2c. Calling API to Trigger An Existing Map.***<br>
>When user willing to use this feature please follow the input format in code cell respectively and if user provide the map_id then the value of duplicate_map also must be provided. Or there would be an error occured: {'error': 'The duplicate_map flag is not set in the map-open parameters.'}.

***2d. Calling API to Map A Path.***<br>
>When user willing to use this feature please follow the input format and some input Parameters must be provided or an error will occoured: {'error': 'Source device or destination device is not provided.'}.

>Til now we have fully called trigger diagnosis API and got four different type of maps. Users can copy the "mapUrl" in API response and open it in any browsers to check the map detail directly. 

>If users want to get more details about this API or get errors when calling this API please check the API documentation on[Github_trigger_diagnosis](https://github.com/NetBrainAPI/North-Bound-API/blob/master/REST%20APIs%20Documentation/Trigger%20Diagnosis%20API/Trigger%20Diagnosis%20API.md)


```python
# Calling API to Create Default Neighbor Map.

API_Body = {
               "domain_setting": {
                    "tenant_id": tenant_id,
                    "domain_id": domain_id
                },
                "basic_setting": {
                    "triggered_by": "Netbrain",
                    "user": "gdluserTest",
                    "device": "R20",
                    "stub_name": "stubTest1"
                },
                "map_setting": {
                        "map_create_mode": 0,
                        "map_device_para": {
                        "device": "SW4",
                        "include_neighbor": "",
                        "interfaces": [""],
                        "neighbor_type": ""
                        }
                }
            }  

def trigger_default_map(trigger_url, headers, API_Body, token):
    headers["Token"] = token
    api_result = requests.post(trigger_url, data=json.dumps(API_Body), headers=headers, verify=False)
    if api_result.status_code == 200:
        return api_result.json()
    else:
        return api_result.json()
    
result = trigger_default_map(trigger_url, headers, API_Body, token)
result
```


API Response: 

    {'mapId': 'e7343091-c01a-40c9-9e33-bb066bb9d7f8',
     'mapName': 'stubTest1-20190222154255',
     'mapType': 1,
     'mapUrl': 'http://192.168.28.79/map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=e7343091-c01a-40c9-9e33-bb066bb9d7f8&maptype=1'}




```python
# Calling API to Open Site Map of The Device.
# Please follow the input format 

API_Body1 = {
        "domain_setting": {
        "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
        "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
        },
        "basic_setting": {
            "triggered_by": "Netbrain",
            "user": "gdluserTest",
            "device": "R20",
            "stub_name": "stubTest1"
        },
        "map_setting": {
                "map_create_mode": 1,
                "map_device_sitemap_para": {
                "device": "R10", # can not be null.
                "duplicate_map": False # can not be null.
            }
        }  
}

result1 = trigger_default_map(trigger_url, headers, API_Body1, token)
result1
```

API Response: 


    {'mapId': 'e762eaa7-507f-4c02-9d40-c616f6d64702',
     'mapName': 'AM-ARG-BA-BEN-1621-KM375RAM1618',
     'mapType': 3,
     'mapUrl': 'http://192.168.28.79/map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=e762eaa7-507f-4c02-9d40-c616f6d64702&maptype=3'}




```python
# Calling API to Trigger An Existing Map.
# Please follow the input format 

API_Body2 = {
                "domain_setting": {
                "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
                "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
                },
                "basic_setting": {
                    "triggered_by": "Netbrain",
                    "user": "gdluserTest",
                    "device": "R20",
                    "stub_name": "stubTest1"
                },
                "map_setting": {
                        "map_create_mode": 2,
                        "map_open_para": {
                        "map_id": "e762eaa7-507f-4c02-9d40-c616f6d64702", # can not be null.
                        "site_id": "", 
                            # Please change to the correct input value before using, or an error will occured
                        "device_group_id": "", 
                            # Please change to the correct input value before using, or an error will occured
                        "duplicate_map": True # can not be null.
                        }
                }  
        }

result2 = trigger_default_map(trigger_url, headers, API_Body2, token)
result2
```

API Response: 


    {'mapId': 'f881543a-a631-45cb-8778-840f33a9341c',
     'mapName': 'stubTest1-20190222155811',
     'mapType': 1,
     'mapUrl': 'http://192.168.28.79/map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=f881543a-a631-45cb-8778-840f33a9341c&maptype=1'}




```python
# Calling API to Map A Path.
# Please follow the input format 

API_Body3 = {
                "domain_setting": {
                "tenant_id": "fb24f3f0-81a7-1929-4b8f-99106c23fa5b",
                "domain_id": "0201adc4-ae96-46f0-ae3d-01cdba9e41d6"
                },
                "basic_setting": {
                    "triggered_by": "Netbrain",
                    "user": "gdluserTest",
                    "device": "R20",
                    "stub_name": "stubTest1"
                },
                "map_setting": {
                        "map_create_mode": 3,
                        "map_path_para": {
                        "source": "R3", # Can not be null
                        "source_gateway": "10.120.15.5",
                        "source_gateway_dev": "R3",
                        "source_gateway_intf": "Ethernet0/3.15",
                        "source_port": "",
                        "destination": "R2",# Can not be null
                        "destination_gateway": "10.120.13.1",
                        "destination_port": "",
                        "destination_gateway_dev": "R2",
                        "destination_gateway_intf": "Ethernet0/3.13",
                        "direction": 1, # Can not be null
                        "protocol": 28, # Can not be null
                        "protocol_name": "",
                        "path_analysis_set_name": "",
                        "path_analysis_set": "L3 Path", # Can not be null
                        "dataSource": {
                            "type": 1,
                            "recent": {
                                "unit": 2,
                                "duration": 5
                            },
                            "range": {
                                "start": "",
                                "end": ""
                            },
                            "around": {
                                "time": ""
                            }
                        }
                    }
                }  
        }

result3 = trigger_default_map(trigger_url, headers, API_Body3, token)
result3
```

API Response: 


    {'mapId': '2a46013a-f913-4865-9f6c-bf8a77636f54',
     'mapName': 'stubTest1-20190222160345',
     'mapType': 1,
     'mapUrl': 'http://192.168.28.79/map.html?t=fb24f3f0-81a7-1929-4b8f-99106c23fa5b&d=0201adc4-ae96-46f0-ae3d-01cdba9e41d6&id=2a46013a-f913-4865-9f6c-bf8a77636f54&maptype=1',
     'taskId': 'ccd770be-2c7f-427a-921b-03b37b447cc0'}



## Step 3: Calling Logout API


```python
Logout_url = nb_url + "/ServicesAPI/API/V1/Session"

def logout(Logout_url, token, headers):
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

logout = logout(Logout_url, token, headers)
logout
```


API Response: 

    {'statusCode': 790200, 'statusDescription': 'Success.'}



# Referance:

> 1) login API:<br>

>https://github.com/NetBrainAPI/North-Bound-API/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Login%20API.md

> 2) specify_a_working_domain API: <br>

>https://github.com/NetBrainAPI/North-Bound-API/blob/master/REST%20APIs%20Documentation/Authentication%20and%20Authorization/Specify%20A%20Working%20Domain%20API.md

> 3) trigger_diagnosis API:<br>

>https://github.com/NetBrainAPI/North-Bound-API/blob/master/REST%20APIs%20Documentation/Trigger%20Diagnosis%20API/Trigger%20Diagnosis%20API.md



```python

```
