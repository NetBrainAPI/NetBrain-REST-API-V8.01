
# Cisco SNTC Qapps User Guide

## Use Case Introduction

This Qapp will retrieve **Cisco** device maintenance information from Cisco cloud SNTC service and display it on NetBrain map as Data View (Cisco SNTC Qapp.xapp) or generate an overview report (Cisco SNTC Report.xapp).<br>
**The Data View includes:**
1. EOLProductID
2. EndOfSaleDate
3. EndOfServiceContractRenewal
4. LastDateOfSupport
5. ProductIDDescription
6. EOX_Migration_Details<br>
    a. MigrationInformation<br>
    b. MigrationOptions<br>
    c. MigrationProductId<br>
    d. MigrationProductInfoURL<br>
    e. MigrationProductName<br>
    f. MigrationStrategy<br>
    g. PIDActiveFlag<br>

**The report includes:**
1. EOLProductID
2. EndOfSaleDate
3. EndOfServiceContractRenewal
4. LastDateOfSupport
5. ProductIDDescription<br>

**Note: If there is no issue data available from the SNTC service, the Data View and report will display No Date/No Description/No Data, etc.**

## Setup Guide

### Create API Plugin

1.	Go to the System Management page.
2.	Click on the API Plugin Manager tab.
3.	Click on Add to add a new API Plugin.<br>
    a.	Set the name of the plugin as “Cisco SNTC API Plugin”.<br>
    b.	Copy and paste the following code into the Script field.<br>



```python
import requests
import requests.packages.urllib3 as urllib3
import json
import pythonutil
 
urllib3.disable_warnings()
 
def GetTokenClient(params, full_url, header, payload_id, payload_secret):
    apiServerId = params['apiServerId']
    servInfo = pythonutil.GetApiServerInfo(apiServerId)
    client_id = servInfo['username']
    client_secret = servInfo['password']
    payload=payload_id+client_id+payload_secret+client_secret
    try:
        response = requests.post(full_url, data=payload, headers=header, verify=False)
        if response.status_code == 200:
            result = response.json()
            token = result["token_type"] + " " + result["access_token"]
            return token
        else:
            print(response.text)
    except Exception as e: print(str(e))

def GetWarrantyByID(token, sn, params):
    header = {'Authorization': token, 'Accept':'application/json'}
    apiServerId = params['apiServerId']
    servInfo = pythonutil.GetApiServerInfo(apiServerId)
    base_url = servInfo['endpoint']
    full_url = base_url + sn
 
    try:
        response = requests.get(full_url, headers=header, verify=False)
        if response.status_code == 200:
            result = response.json()
            return result["EOXRecord"]
        else:
            print(response.text)
    except Exception as e: print(str(e))        

```

### Configure API Server Instance

1.	Go to the domain management page.
2.	Click on “Operations” and select API Server Manager.
3.	Press “Add” to add a new API server.<br>
    a.	Name the server “Cisco SNTC”.<br>
    b.	API Source Type should be “Cisco SNTC API Plugin” (previously created API Plugin).<br>
    c.	Put https://api.cisco.com/supporttools/eox/rest/5/EOXBySerialNumber/1/ into the Endpoint field. <br>
    d.	Put the Client ID and Client secret of your Cisco account in the “Username” and “Password” fields, respectively.<br>
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
    d.	Check off the box next to “Cisco SNTC API Plugin”, and in the drop down select “Cisco SNTC API Plugin”.<br>
    e.	Click “Submit”.<br>

## How to Run The Qapp

**Cisco SNTC Qapp**<br>

1.	Open a NetBrain map.
2.	In the Runbook tab, press the “+” icon and select the “Cisco SNTC Qapp”. Make sure that the correct devices are in the queue by clicking on the top left of the Qapp tab. 
3.	For Data Source, select “Pull live data once”.
4.	Press Run.<br>

**Cisco SNTC Report**<br>

1. Navigate to Inventory Report.
2. Click on Go To Manage Reports Page>>.
3. Click on +New Inventory Report.
4. Fill out the forms, on Step 2 of 4, select Qapp Report.
5. Choose Cisco SNTC Report Qapp and pick "Pull live data once" as Data Source.
6. Click Finish.
7. Navigate back to Inventory Report and select Cisco SNTC Report.
8. Click on Run to upadte report with live data.
