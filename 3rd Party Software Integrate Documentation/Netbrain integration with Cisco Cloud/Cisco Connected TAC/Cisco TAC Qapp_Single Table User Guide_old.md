
# Cisco TAC Qapp_Single Table User Guide

## Use Case Introduction

This Qapp will retrieve **Cisco** device issue data from Cisco Connected TAC bridge server and display it on NetBrain map as Data View.<br>
**The Data View includes:**
1. Issue Count
2. Severity
3. Severity_Int
4. Name
5. External_Title
6. External_Text<br>

**Note: If there is no issue data available from the bridge server, the Data View only displays the Issue Count as 0 (zero) without any other data.**

## Setup Guide

### Create API Plugin

1.	Go to the System Management page.
2.	Click on the API Plugin Manager tab.
3.	Click on Add to add a new API Plugin.<br>
    a.	Set the name of the plugin as “Cisco TAC API Plugin”.<br>
    b.	Copy and paste the following code into the Script field.<br>


```python
import requests
import requests.packages.urllib3 as urllib3
import json
import pythonutil
 
urllib3.disable_warnings()

def getToken(cred_params):
    apiServerId = cred_params['apiServerId']
    servInfo = pythonutil.GetApiServerInfo(apiServerId)
    username = servInfo['username']
    password = servInfo['password']
    host_url = servInfo['endpoint'] + '/api'
    
    header = {"Content-Type": "application/x-www-form-urlencoded", 'Accept':'application/json'}
    full_url = host_url + "/token"
    payload = "username="+username+"&password="+password+"&grant_type=password"
    try:
        response = requests.post(full_url, data=payload, headers=header, verify=False)
        if response.status_code == 200:
            result = response.json()
            token = result["token_type"] + " " + result["access_token"]
            return token
        else:
            print(response.text)
    except Exception as e: print(str(e))

def getIssuesByDevice(cred_params, token, hostname):
    apiServerId = cred_params['apiServerId']
    servInfo = pythonutil.GetApiServerInfo(apiServerId)
    host_url = servInfo['endpoint'] + '/api'
    
    header = {'Authorization': token, 'Accept':'application/json'}
    full_url = host_url + "/Devices/" + hostname + "/Issues"
    querystring = {"isHostname":"true",
    "includeOccurences":"false",
    "includeLastAlert":"true",
    "includeRemediations":"false",
    "includeAppliedRemediations":"false",
    "includeExternalTextInSearch":"true",
    "page":"1",
    "pageSize":"100"
    }  
    try:
        response = requests.get(full_url, headers=header, params=querystring, verify=False)
        if response.status_code == 200:
            result = response.json()
            return response.text
        else:
            print(response.text)
    except Exception as e: print(str(e))
```

### Configure API Server Instance

1.	Go to the domain management page.
2.	Click on “Operations” and select API Server Manager.
3.	Press “Add” to add a new API server.<br>
    a.	Name the server “Cisco TAC”.<br>
    b.	API Source Type should be “Cisco TAC API Plugin” (previously created API Plugin).<br>
    c.	Put https://api.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/1/ into the Endpoint field.<br>
    d.	Put the Username and Password in the “Username” and “Password” fields, respectively.<br>
    e.	Select an available Front Server.<br>
        **Note: If you have multiple Front Servers managing different group of devices, please repeat all steps to create API Server instance for each Front Server.**<br>
    f.	Press “OK” to finish creating the API Server.<br>
4.	Create a Device Group<br>
    a.	Go back to your NetBrain Desktop.<br>
    b.	Open the menu from the button in the top left corner.<br>
    c.	Click on “Device Group”.<br>
    d.	From the drop down from the folder “My Device Groups”, select “New Device Group”.<br>
    e.	Name your device group.<br>
    f.	Add the necessary devices through manual adding or Dynamic Search (these should be the devices that the Qapp is being used on).<br>
    g.	Select “OK” to finish the process.<br>
5.	Add API settings to device group.<br>
    a.	Open a map with one of the devices in the device group.<br>
    b.	Right click on the device and select “Shared Device Settings”.<br>
    c.	Click on the “API” tab and check the box for “Apply above Settings to device group”. In the drop down, select your device group.<br>
    d.	Check off the box next to “Cisco TAC API Plugin”, and in the drop down select “Cisco TAC API Plugin”.<br>
    e.	Click “Submit”.<br>


## How to Run The Qapp

1.	Open a NetBrain map.
2.	In the Runbook tab, press the “+” icon and select the “Cisco TAC Qapp”. Make sure that the correct devices are in the queue by clicking on the top left of the Qapp tab. 
3.	For Data Source, select “Pull live data once”.
4.	Press Run.
