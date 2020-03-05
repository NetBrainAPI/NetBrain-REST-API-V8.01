
# Sites and  devices in sites modification
During this use case, we are going to focus on Site API. We will create multiple sites with different types and add some devices into one site, in the end we will delete all sites we have created.

In this use case, we totally concern 11 APIs, as shown below:

**[Step 1: Use case preparation](Step-1:-Use-case-preparation)**
>> 1a. import all useful modules and create global variables<br>
>> 1b. call login API<br>
>> 1c. call specify_a_working_domain API<br>

**[Step 2: Create one transaction for site modification](Step-2:-Create-one-transaction-for-site-modification)**
>> 2a. call create_site_transaction API<br>
>> 2b. call site_transaction_heartbeat API <br>

**[Step 3: Create site for devices modification](Step-3:-Create-site-for-devices-modification)**
>> 3a. call create_site API<br>
>> 3b. call create_a_leaf_site API <br>

**[Step 4: Modify devices in site](Step-4:-Modify-devices-in-site)**
>> 4a. call add_site_device API<br>
>> 4b. call get_site_devices API <br>
>> 4c. call replace_site_devices API <br>

**[Step 5: Implement all modifications to system](Step-5:-Implement-all-modifications-to-system)**
>> 5a. call commit_Site_Transaction API

## Step 1: Use case preparation
***1a. import all useful modules and create global variables***
> Note: If users try to use this code. please remember to change the "nb_url" to users' own working url.

***1b. call login API***
>In step 1, we calling the login API with "username" and "password" as inputs. As response we can get the authentication token as one fixed input in following APIs calling. If users get errors when calling this API please check the API documentation on [Github_login](https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/STANDARD_formate_TEST1_LOGIN_API.ipynb) 

***1c. call specify_a_working_domain API***
>After we running this step successfully, we directly complete the full login processes which means we totally join in Netbrain System by calling APIs(because we have record our tenantId and domainId，if users don't know the ID of corresponding tenant and domain please fully follow step 1 to step 4 in use case 1). Next step, we will start to use Netbrain functions formally. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_domain](https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/STANDARD_formate_Specify_a_domain_to_work_on_API_Test1%20.ipynb) 


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
tenantId = "fb24f3f0-81a7-1929-4b8f-99106c23fa5b"
domainId = "850ff5e9-c639-404d-85a3-d920dbee509c"
```


```python
# call login API

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
API Response: 

    639afa4a-0fb1-4005-b540-ad037ed131d9
    


```python
# call specify_a_working_domain API

Specify_a_working_domain_url = nb_url + "/ServicesAPI/API/V1/Session/CurrentDomain"

def specify_a_working_domain(tenantId, domainId, Specify_a_working_domain_url, headers, token):
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
            return ("Working Domain Specified Successfully, with domainId: " + domainId)
            
        elif response.status_code != 200:
            return ("Login failed! - " + str(response.text))

    except Exception as e: print (str(e))

res =  specify_a_working_domain(tenantId, domainId, Specify_a_working_domain_url, headers, token)
print (res)
```
API Response: 

    Working Domain Specified Successfully, with domainId: 850ff5e9-c639-404d-85a3-d920dbee509c
    

## Step 2: Create one transaction for site modification
***2a. call create_site_transaction API***
>All site modification operations must be executed in a transaction. In another word, the user should create a transaction before starting any other site changes for example, create site, move devices.

>And also, after change site, the user should explicitly commit the operations .

>Note that a site transaction will lock the entire NetBrain system for site change operations. To prevent a system-wide dead lock due to client exception or negligence, if no follow-up operations or heartbeat sent within a 30 seconds time frame, another could invalidate this transaction, and create a new transaction which cannot used by the current session.

>Deleting a transaction could let the user to discard any site change operations since the beginning of a transaction, or called rollback.

>If users want to get more details about this API or get errors when calling this API please check the API documentation on[Github_site_transaction](https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Create_a_Site_Transaction_API_Test.ipynb)

***2b. call site_transaction_heartbeat API***
>This API send a hearbeat signal to the server to keep a transaction alive.

>Failed to do so will cause transaction being disgarded by the system if no other site change operations sent to the server via the current session with the next 30 seconds.If users want to get more details about this API or get errors when calling this API please check the API documentation on[Github_site_transaction_heartbeat](https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Site_Transaction_Heartbeat_API_Test.ipynb)


```python
# call create_site_transaction API

create_a_transaction_URL = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/Transactions"

def create_a_transaction(create_a_transaction_URL, headers, token):
    try:
        response = requests.post(create_a_transaction_URL, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            print (result)
        else:
            print ("Get User Report failed! - " + str(response.text))

    except Exception as e:
        print (str(e)) 

result = create_a_transaction(create_a_transaction_URL, headers, token)
result
```
API Response: 

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    


```python
# call site_transaction_heartbeat API

site_transaction_heartbeat_URL = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/Transactions/Heartbeat"

def site_transaction_heartbeat(headers, token):
    headers["Token"] = token

    try:
        response = requests.post(site_transaction_heartbeat_URL, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            print (result)
        else:
            print ("Get User Report failed! - " + str(response.text))

    except Exception as e:
        print (str(e))
        
result = site_transaction_heartbeat(headers, token)
result
```
API Response: 

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

## Step 3: Create site for devices modification
***3a. call create_site API***
>After we create the transaction for sites modification, we are going to create a site as beginning using create site API. If users want to get more details about this API or get errors when calling this API please check the API documentation on Github_create_site
>>Note that<br>
>>a) a new site will be created as a parent site if a site doesn't have its parent site in current system.<br>
>>b) this API will replace the ImportSiteTree in 7.0b.<br>
>>c) this API call needs to be invoked in a site transaction.

***3b. call create_a_leaf_site API***
>As shown in previous step, we have created two sites which as parent sites. Now we calling this API to create a container site. If one parent site doesn't exist in current system, create it before create its child site. If users want to get more details about this API or get errors when calling this API please check the API documentation on Github_create_leaf_site


```python
create_site_URL = nb_url + "/ServicesAPI/API/V1/CMDB/Sites"

sitePath1 = "My Network/America"
isContainer1 = True

sitePath2 = "My Network/America/Burlington"
isContainer2 = False

body = {
   "sites": [
                {
                    "sitePath" : sitePath1,
                    "isContainer": isContainer1
                },
                {
                    "sitePath" : sitePath2,
                    "isContainer": isContainer2
                }
            ]
        }

def create_site(create_site_URL, headers, token, body):
    headers["Token"] = token
    try:
        response = requests.post(create_site_URL, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            print (result)
        else:
            print ("Site Created Failed! - " + str(response.text))

    except Exception as e:
        print (str(e))
        
result = create_site(create_site_URL, headers, token, body)
result
```
API Response: 

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    


```python
create_a_leaf_site_URL = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/Leaf"

sitePath = "My Network/America/Burlington/Netbrain"

body = {
            "sitePath" : sitePath       
        }

def create_a_leaf_site(create_a_leaf_site_URL, headers, token, body):
    try:
        response = requests.post(create_a_leaf_site_URL, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            print (result)
        else:
            print ("Leaf Site Created Failed! - " + str(response.text))

    except Exception as e:
        print (str(e))
        
result = create_a_leaf_site(create_a_leaf_site_URL, headers, token, body)
result
```
API Response: 

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

## Step 4: Modify devices in site
***4a. call add_site_device API***
>After we completely created all sites we need, during this step we will start to import devices into our sites. To implete this feature by calling this API to add devices to the site which specified by site path or Id. All devices will be marked as manually added type. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_add_site_devices](https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Add_Site_Devices_API_Test.ipynb)  

>And we will add two devices lists to two created sites respectively. In this sub-step, we totally concern two parts, first part we add four devices in site with site path: "My Network/America/Burlington/Netbrain", second part we also add four devices (which are different with first part) to another site with site path: "My Network/America".

***4b. call get_site_devices API***
>After we running previous sub-step successfully, in order to confirm we added the devices correctly to each site, we wish to call this API to output the detail information of each site. Calling this API to get all devices belong to the site specified by site name. Note that the siteID must be a leaf site ID, error would return if the parameter is root site or a container site. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_get_site_devices](https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Get_Site_Devices_API_Test.ipynb)  

***4c. call replace_site_devices API***
>In this step we focus on change the devices group in one site, calling this API to remove all existing devices from the site which specified by site name or site Id and add new devices provided in the devices parameter at meanwhile. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_replace_site_devices](https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Replace_Site_Devices_API_Test.ipynb)  


```python
# call add_site_device API

add_site_device_URL = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/Devices"

sitePath = "My Network/America/Burlington/Netbrain"
devices = ["AS20001", "AS20002", "AS20003", "AS30000"]

body = {
           "sitePath" : sitePath,
           "Devices": devices
        } 

def add_site_device(add_site_device_URL, headers, token, body):
    headers["Token"] = token
    try:
        response = requests.post(add_site_device_URL, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            print (result)
        else:
            print ("Devices added Fail! - " + str(response.text))

    except Exception as e:
        print (str(e))
        
result = add_site_device(add_site_device_URL, headers, token, body)
result
```
API Response: 

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    


```python
sitePath1 = "My Network/America"
devices1 = ["R1", "R10", "R11", "R10"]

body1 = {
           "sitePath" : sitePath1,
           "Devices": devices1
        } 

result1 = add_site_device(add_site_device_URL, headers, token, body1)
result1
```
API Response: 

    Devices added Fail! - {"statusCode":791006,"statusDescription":"leaf site 6397dc66-429e-4e32-a5f1-0e3d3b72ba7e does not exist."}
    


```python
#call get_site_devices API

get_site_devices_URL = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/Devices"

sitePath = "My Network/ASIA"

data = {
           "sitePath" : sitePath
            # "sitId" : sitId
     }    

def get_site_devices(get_site_devices_URL, headers, token, data):
    headers["Token"] = token
    try:
        response = requests.get(get_site_devices_URL, params = data, headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()["devices"]
            print (result)
        else:
            print ("Get Site Devices Failed! - " + str(response.text))

    except Exception as e:
        print (str(e))
        
result = get_site_devices(get_site_devices_URL, headers, token, data)
result
```
API Response: 

    [{'id': '71e07730-1247-4f5f-acbc-2b3428f8d0cf', 'mgmtIP': '10.18.19.18', 'hostname': 'R18'}]
    


```python
sitePath1 = "My Network/MPLS Core"

data1 = {
           "sitePath" : sitePath1
            # "sitId" : sitId
     }

result1 = get_site_devices(get_site_devices_URL, headers, token, data1)
#print(str(len(result1)))
result1

```
API Response: 

    [{'id': '1d48d218-06cf-4657-af2c-39796946122b', 'mgmtIP': '123.10.1.1', 'hostname': 'R4'}, {'id': '497b25bd-1f8c-4bfa-80be-49ab692ce4d4', 'mgmtIP': '123.10.1.10', 'hostname': 'R3'}, {'id': '5c3d72d6-d0f2-41f4-8b1e-5762dff6e55a', 'mgmtIP': '123.10.1.22', 'hostname': 'R6'}, {'id': '6d62e420-af59-4ee3-948d-54df60fe05ca', 'mgmtIP': '123.10.1.6', 'hostname': 'R5'}, {'id': '81229708-571a-419a-a10d-9481661718a4', 'mgmtIP': '123.10.1.2', 'hostname': 'R1'}, {'id': 'a8652884-7701-5e84-b4d8-cc03652490e5', 'hostname': 'ISP'}, {'id': 'b98f107a-622e-4985-8f95-f5b541f699f3', 'mgmtIP': '123.7.7.7', 'hostname': 'R7'}, {'id': 'f190b385-676f-4579-ad6d-700122a21caf', 'mgmtIP': '123.10.1.17', 'hostname': 'R2'}]
    


```python
#call replace_site_devices API

replace_site_devices_URL = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/Devices"

sitePath = "My Network/MPLS Core"

devices = ["R1", "R10", "R11", "R12"]
#devicesOri = ["R4", "R3", "R6", "R5", "R1", "ISP", "R7", "R2"]

body = {
           "sitePath" : sitePath,
           "Devices": devices
    }   

def replace_site_devices(replace_site_devices_URL, headers, token, body):
    headers["Token"] = token
    try:
        response = requests.put(replace_site_devices_URL, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            print (result)
        else:
            print ("Devices added Fail! - " + str(response.text))

    except Exception as e:
        print (str(e))
        
result = replace_site_devices(replace_site_devices_URL, headers, token, body)
result
```
API Response: 

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

## Step 5: Implement all modifications to system
>Actually this step should be considered the final step of the whole use case. For all previous steps, we were modify system sites architecture but all can be seen as pending process. If we want to update all changing to whole structure, we have to commit site transactions. In other word, everytime users create a transaction to modify sites, in the end the commit site transaction API must be called to update the entire workflow. If users want to get more details about this API or get errors when calling this API please check the API documentation on [Github_commit_transaction](https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Commit_Site_Transaction_API_Test.ipynb)


```python
rebuildSite = False

body = {"rebuildSite" : rebuildSite}

commit_Site_Transaction_URL = nb_url + "/ServicesAPI/API/V1/CMDB/Sites/Transactions"

def commit_Site_Transaction(commit_Site_Transactio_URL, headers, token, rebuildSite):
    headers["Token"] = token
    try:
        response = requests.put(commit_Site_Transactio_URL, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            print (result)
        else:
            print ("Site commit Failed! - " + str(response.text))

    except Exception as e:
        print (str(e))
        
result = commit_Site_Transactio(commit_Site_Transactio_URL, headers, token, rebuildSite)
result
```
API Response: 

    {'statusCode': 790200, 'statusDescription': 'Success.'}
    

## Logout Netbrain System by calling logout API


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
> 1) login API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/STANDARD_formate_TEST1_LOGIN_API.ipynb<br> 

> 2) specify_a_working_domain API: 

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/STANDARD_formate_Specify_a_domain_to_work_on_API_Test1%20.ipynb<br>

>3) create_a_transaction API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Create_a_Site_Transaction_API_Test.ipynb<br>

>4) site_transaction_heartbeat API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Site_Transaction_Heartbeat_API_Test.ipynb<br>

>5) create_site API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Create_Site_API_Test.ipynb<br>

>6) create_a_leaf_site API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Create_A_Leaf_Site_API_Test.ipynb<br>

>7) add_site_device API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Add_Site_Devices_API_Test.ipynb<br>

>8) get_site_devices API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Get_Site_Devices_API_Test.ipynb<br>

>9) replace_site_devices API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Replace_Site_Devices_API_Test.ipynb<br>

>10) delete_a_site API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Delete_A_Site_API_Test.ipynb<br>

>11) commit_Site_Transaction API:

>https://github.com/Gongdai/Netbrain_REST_API_First_Regularization/blob/master/Netbrain_REST_API/API_test/Site%20API%20Design/STANDARD_formate_Commit_Site_Transaction_API_Test.ipynb


```python

```
