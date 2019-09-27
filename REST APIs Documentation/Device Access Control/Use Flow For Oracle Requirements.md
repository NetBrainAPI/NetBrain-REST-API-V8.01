
## Use Flow For  Oracle Requirements 

1. Login to NetBrain System and Specify a Working Domain: <br> 
    a. Login API<br> 
    b. Get All Accessible Domains/Tenants.<br> 
    c. Specify a Working Domain API.<br> 
2. Create Sites /Add Devices to Sites. 
3. Create Device Access Policy / Add sites and access privilege. 
4. User Management <br> 
    a. Add SSO Users. 
5. Assign Role to SSO Users.
6. Assign Device Access Policy to Users. 

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
```

### Define Login Functions


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
```

### Create Sites /Add Devices to Sites.


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
        

# call create_a_leaf_site API        
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
```

### Create Device Access Policy / Add sites and access privilege.


```python
body = {
    "name": "DeviceAccessPolicy_GL1",
    "description": "a device access policy",
    "privileges": [1, 2],
    "scope": {
        "type": 0
    }
}

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

def addDevicesAccessPolicy(headers, body, nb_url):
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/DeviceAccessPolicy"
    try:
        response = requests.post(full_url, data = json.dumps(body), headers=headers, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Create new device access policy Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
```

### User Management / Add SSO Users.


```python
body = {
        "username": "externalAccount",
        "externalUserIdentity":"xxxx",
        "authenticationServer":"TACACS",
        "email": "user1@netbrain.com",
        "firstName": "user1",
        "lastName": "user1",
        "password": "user1",
        "phoneNumber" : "",
        "department" : "",
        "description" : "",
        "deactivatedTime" : "",
        "isSystemAdmin":"false",
        "tenants" : [{
            "tenantName":"tenant_71a1",
            "isTenantAdmin":false,
            "allowCreateDomain":"false",
            "domains":[{
                "domainName":"domain_cyj",
                "domainRoles":["domainAdmin"]
            }]
        }]
}

def add_SSO_user(body, token, nb_url):
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Users"
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    headers["Token"] = token
    try:
        response = requests.post(full_url, data = json.dumps(body), headers = headers, verify = False)
        if response.status_code == 200:
            result = response.json()
            print (result)
        else:
            print ("Add New User failed! - " + str(response.text))

    except Exception as e:
        print (str(e)) 
```

### Assign Role to SSO Users


```python
roleName = "testRole11"
description = "string"
privileges = [2]

body = {
        "roleName": roleName, 
        "description": description, 
        "privileges": privileges
    }

def add_role_to_user(nb_url, body, token):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    headers["Token"] = token
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/Roles"
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

### Assign Device Access Policy to Users.


```python
body = {
 
  "authenticationServer":"NetBrain",
  "userName":"deviceAPAPI",
  "policies" : ["New_DeviceAccessPolicy_GL1", "New_DeviceAccessPolicy_GL2"]              
 
}

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
headers["Token"] = token

def AssignDeviceAccessPoliciesToUser(headers, body, nb_url):
    full_url = nb_url + "/ServicesAPI/API/V1/CMDB/UserDeviceAccessPolicy/AssignDeviceAccessPolicies"
    try:
        response = requests.post(full_url, data = json.dumps(body), headers=headers, verify=False)
        if response.status_code == 200:
            res = response.json()
            return (res)
        else:
            return ("Assign user to device access policy Failed! - " + str(response.text))

    except Exception as e:
            return (str(e)) 
```

### Logout


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
```
