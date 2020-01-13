
# Trigger NetBrain Dynamic Map in ServiceNow

## Content

1) [Requirements for both sides setup.](#Requirements)
2) [Purpose of integration.](#Purpose) 
3) [Configuration of trigger map.](#Configuration) 
4) [Deploying the setup.](#Deploying) <br>
a. [Define an API-triggered diagnosis task in NetBrain (Add Stub).](#Define) <br>
b. [Add custom field (NetBrainMapURL) to ServiceNow.](#Add) <br>
c. [Call API-triggered diagnosis task in your third-party systems (Add Business Rule in ServiceNow).](#Call) <br>
d. [View triggered tasks and results (Testing) Manually add incident to demo the trigger diagnosis.](#View) 
5) [Customizing existing use case.](#Customizing) <br>
a) [Customizing map in the Stub.](#Stub) <br>
b) [Customizing Runbooks in the stub.](#Runbooks) <br>
c) [Customizing type of Incident to trigger stub.](#type) <br>
d) [Update Business Rule in ServiceNow.](#Business)
6) [Appendix](#Appendix)

## Requirements for both sides setup <a name="Requirements"></a>

1. NetBrain requirements<br>
a. NetBrain Tenant and Domain access.<br>
b. Netbrain Web Server should be reached by ServiceNow instance via http/https.

2. ServiceNow requirements<br>
a. ServiceNow admin access, which need to define "Business Rule".<br>
b. ServiceNow Business Rule should be defined follow predefined "Business Rule" as a reference in NetBrain.

## Purpose of integration<a name="Purpose"></a>
Whenever an incident is created in ServiceNow, it triggers NetBrain to build a map and perform diagnosis.<br>
a. Attach a NetBrain URL in the Incident, which open dynamic map of the device (Configuration Item)<br>
b. Specified runbook output is saved in map

<img src="images\worddav4a5303f12c9797f1f2a1e70ccb99de60.png" /><br>

## Configuration of trigger map<a name="Configuration"></a>

1) The trigger condition is set on the "incident" table – trigger is executed whenever a new incident is added to the table.<br>
2) Script is executed when the trigger is executed – this is implemented in ServiceNow using "Business Rules". Within a business rule, "Advanced" option is checked to enable script<br>
3) The script performs the following logical steps:<br>
a. Performs authentication with NetBrain server<br>
b. Gather source device detail information(hostname, gateway) and destination device hostname from ServiceNow custom field.<br>
c. Trigger NetBrain Stub to generate the map<br>
d. Receives the map URL as a response to the API call
4) NetBrain credentials are placed in the script


## Deploying the setup<a name="Deploying"></a>
The following major steps describe a general flow to define and use API-triggered diagnosis task:

a) Define an API-triggered diagnosis task in NetBrain. (Add Stub)<br>
b) Add custom field (NetBrainMapURL) to ServiceNow.<br>
c) Call API-triggered diagnosis task in your third-party systems. (Add Business Rule in ServiceNow)<br>
d) View triggered tasks and results. (Troubleshooting)

### a) Define an API-triggered diagnosis task in NetBrain. (Add Stub)<a name="Define"></a>
1. Navigate to < your netbrain serverIP >/desktop.html<br>
2. Click on the menu button and select "System Automation Manager"Note: If you don't have admin privilege you will not see the "System Automation Manager" <br>
<img src="images\worddavdbd2682c0faaec1fe567a6f2fe46390e.png"  /><br>

3. Navigate to the "API Stub Manager" and select "Add Stub"<br>
<img src="images\image2018-2-9%2016_25_5.png"  /><br>

4. Enter the following details in the stub:Stub name, Map setting, Runbook. <br>
<img src="images\image2018-2-9%2016_25_45.png" /><br>

### b) Add custom column (NetBrainMapURL) to ServiceNow. (Add Stub)<a name="Add"></a>
To add a new field to a table please follow the step in the link below:<br>
https://developer.servicenow.com/app.do#!/lp/new_to_servicenow/app_store_learnv2_buildneedit_jakarta_adding_fields_to_a_table?v=jakarta

### c) Call API-triggered diagnosis task in your third-party systems. (Add Business Rule in ServiceNow)<a name="Call"></a>
1. In ServiceNow, navigate to "Business Rule", and add a new rule to the page.<br>
<img src="images\image2018-2-9%2016_27_20.png" /><br>

2. Set the following settings on the Business Rule Page.<br>
<img src="images\image2018-2-9%2016_30_0.png" /><br>

3. Paste the script under advanced. (Please update Netbrain Server URL and NetBrain credential.)<br>
During this script, we totally follow the workflow of trigger a netbrain daynamic map by calling trigger diagnosis API. More information please check [here](https://github.com/Gongdai/REST_API_with_Markdown/blob/master/Golden%20Use%20Case%20Templates/Calling%20Trigger%20Diagnosis%20API.md). A little differnt is we have to use Javascript in ServiceNow. Thus, we provide a Js script for ServiceNow integration.
Same with reference in Github, we define all global variables at beginning then calling all rest APIs Js functions to get the triggered map URL, the last part is all functions we provide for Netbrain API calling.  

   
(function executeRule(current, previous /*null when async*/) {

    //Update the values of the following attributes to your specific API base URL, login credentials, and tenant/domain names
    var NetBrainPrefix = 'http://unity.netbraintech.com/ServicesAPI/API/';
    var Username = 'admin';
    var Password = 'admin';
    var TenantName = 'Initial Tenant';
    var DomainName = 'Experience Lab';
 
    //Get login token
    function requestloginApiToken(usr, pwd, authId) {
        var authdata = {
            username: usr,
            password: pwd,
            authentication_id: authId
        };
        var r = new sn_ws.RESTMessageV2();
        r.setEndpoint(NetBrainPrefix + 'V1/Session');
        r.setHttpMethod('POST');
        r.setRequestBody(JSON.stringify(authdata));
        r.setHttpTimeout(100000);
        try {
            var response = r.execute();
            var responseBody = response.getBody();
            var obj = new JSON.parse(responseBody);
            var token = obj.token;
            return token;
        } catch (ex) {
            return "ERROR : requestloginApiToken";
        }
    }
 
    //Get working tenant ID from the user accessible tenant list
    function getTenantID(tenantName, tokenStr) {
        var r = new sn_ws.RESTMessageV2();
        r.setEndpoint(NetBrainPrefix + 'V1/CMDB/Tenants');
        r.setHttpMethod('GET');
        r.setRequestHeader('Token', tokenStr);
        r.setHttpTimeout(100000);
        try {
            var response = r.execute();
            var responseBody = response.getBody();
            var obj = new JSON.parse(responseBody);
            for (var i=0; i < obj.tenants.length; i++) {
                if (obj.tenants[i].tenantName == tenantName) {
                    return obj.tenants[i].tenantId;
                } else {
                    return "You cannot access the specified tenant.";
                }
            }
        } catch (ex) {
            return "ERROR: getTenantID";
        }
    }
 
    //Get working domain ID from the user accessible domain list of a specific accessible tenant
    function getDomainID(domainName, tenantId, tokenStr) {
        var r = new sn_ws.RESTMessageV2();
        r.setEndpoint(NetBrainPrefix + 'V1/CMDB/Domains');
        r.setHttpMethod('GET');
        r.setRequestHeader('Token', tokenStr);
        r.setRequestHeader('tenantId', tenantId);
        r.setHttpTimeout(100000);
        try {
            var response = r.execute();
            var responseBody = response.getBody();
            var obj = new JSON.parse(responseBody);
            for (var i=0; i < obj.domains.length; i++) {
                if (obj.domains[i].domainName == domainName) {
                    return obj.domains[i].domainId;
                } else {
                    return "You cannot access the specified domain.";
                }
            }
        } catch (ex) {
            return "ERROR: getDomainID";
        }
    }
 
    //Logout token
    function logoutApiToken(tokenStr) {
        var r = new sn_ws.RESTMessageV2();
        r.setEndpoint(NetBrainPrefix + 'V1/Session');
        r.setHttpMethod('DELETE');
        r.setRequestHeader('Token', tokenStr);
        r.setHttpTimeout(10000);
        try {
            var response = r.execute();
            var responseBody = response.getBody();
            var obj = new JSON.parse(responseBody);
            var token = obj.token;
            return token;
        } catch (ex) {
            return "ERROR : logoutApiToken";
        }
    }
    
    //Trigger NetBrain to draw path map
    function drawPathTrigger(serviceLoginToken, tenant_id, domain_id, nbuser, StubName, source, sourceGateway, destination, destinationPort, direction, protocol, pathAnalysisSetName) {
        var r = new sn_ws.RESTMessageV2();
        r.setEndpoint(NetBrainPrefix + 'V1/Triggers/Run');
        r.setHttpMethod('POST');
        var data = {
            domain_setting: {
                tenant_id: tenant_id,
                domain_id: domain_id
            },
            basic_setting: {
                triggered_by: 'haoran',
                user: nbuser,
                stub_name: StubName
            },
            map_setting: {
                map_create_mode: 3,
                map_path_para: {
                    source: source,
                    source_gateway: sourceGateway,
                    destination: destination,
                    destination_port: destinationPort,
                    direction: direction,
                    protocol_name: protocol,
                    path_analysis_set_name: pathAnalysisSetName
                }
            }
        };
        r.setRequestHeader('Token', serviceLoginToken);
        r.setRequestHeader('Content-Type', 'application/json');
        r.setRequestBody(JSON.stringify(data));
        r.setHttpTimeout(10000);
        try {
            var response = r.execute();
            var responseBody = response.getBody();
            var responseStatusCode = response.getStatusCode();
            var obj = new JSON.parse(responseBody);
            return obj.mapUrl;
        } catch (ex) {
            gs.log(ex.getMessage());
            gs.log('Netbrain drawPathTrigger()');
        }
    }
    
    //Set value to ServiceNow field
    function setRrdValue(grName, srcPrName, srcPrV, dstPrName, dstPrValue) {
        var gr = new GlideRecord(grName);
        gr.addQuery(srcPrName, srcPrV);
        gr.query();
        if (gr.next()) {
            gr.setValue(dstPrName, dstPrValue);
            gr.update();
        }
    }
 
    //Get token
    token = requestloginApiToken(Username, Password);
    current.work_notes = "Token: " + token;
    current.update();
    //Get tenant ID
    tenantId = getTenantID(TenantName, token);
    //Get domain ID
    domainId = getDomainID(DomainName, tenantId, token);
    current.work_notes = "Tenant ID: " + tenantId + "\n" + "Domain ID: " + domainId;
    current.update();
    //Get path source IP from ServiceNow "u_source_ip_new" field
    source = current.getDisplayValue('u_source_ip_new');
    //Get path destination IP from ServiceNow "u_destination_ip_new" field
    destination = current.getDisplayValue('u_destination_ip_new');
    sourceGateway = current.getDisplayValue('u_source_gateway');
    destinationPort = current.getDisplayValue('u_destination_port');
    direction = current.getDisplayValue('u_path_direction');
    pathAnalysisSetName = current.getDisplayValue('u_path_analysis_set');
    protocol = current.getDisplayValue('u_protocol');
    current.work_notes = "source: " + source + "\n" + "destination: " + destination;
    current.work_notes = "sourceGateway: " + sourceGateway;
    current.update();
    //Update the 5th parameter to the specific API Stub you defined in NetBrain. Get NetBrain path map URL from NetBrain Trigger API response
    netbrainurl = drawPathTrigger(token, tenantId, domainId, Username, 'TestStub', source, sourceGateway, destination, destinationPort, direction, protocol, pathAnalysisSetName);
    //Set NetBrain path map URL to "u_netbrainmapurl" field
    if (netbrainurl.length > 0) {
        gs.log('NetBrain Map Url ' + netbrainurl);
        setRrdValue('incident', 'sys_id', current.getValue('sys_id'), 'u_netbrainmapurl', netbrainurl);       
    }
    logoutApiToken(apiTokenStr);
    
})(current, previous);


### d) View triggered tasks and results. (Manually add incident to demo the trigger diagnosis)<a name="View"></a>
1. Navigate to incident page and add new incident, and make sure the "Configuration Item" is filled.<br>
2. To see troubleshooting logs, right click on the grey panel on top and click "Save". This helps display logs in the next page which is loaded. <br>
3. A map URL would appear in the case when integration is successful. When user click into the URL, there is a dynamic map exist.<br>
<img src="images\image2018-2-9%2016_26_43.png" /><br>
<img src="images\image2018-2-9%2016_39_33.png" /><br>

4. The list of all the maps generated after each "trigger diagnostic" task is displayed in the System Automation Task Manager.<br>
<img src="images\image2018-2-9%2016_37_43.png" /><br>

## Customizing existing use case<a name="Customizing"></a>
We are willing to provide a simple use case sample at here to help customer understand the workflow more directly. In this use case we totally consider four sections, listed as following. Then we will provide a brief explanation for each section.<br>
a) Customizing map in the Stub. <br>
b) Customizing Runbooks in the stub. <br>
c) Customizing type of Incident to trigger stub. <br>
d) Update Business Rule in ServiceNow.<br>

### a) Customizing map in the Stub. <a name="Stub"></a>
<img src="images\worddavdac55ddc321cc435666ee41213215dce.png" /><br>

The following types of maps can be defined in the stub:<br>
* Map Devices and its neighbors<br>
---* Topology options: IPv4 L3, IPv6 L3, L2.<br>
---* All interfaces or 1 specific interface (just specify long/short form name).<br>
* Open Site Map of the Device<br>
---* Existing site map, or duplicate of site map.<br>
* Open existing Qmap<br>
---* Existing map, or duplicate of site map.<br>
* Map a Path<br>
---* Path type: L3, L3 Active, L2<br>
---* Date Source: Live Network, Baseline, historical data<br>
---* Protocol<br>
---* Gateway device<br>
---* One way or bidirectional
* Open Context Map <br>
* Use Qapp to Create a Map<br>

### b) Customizing Runbooks in the Stub. <a name="Runbooks"></a>
<img src="images\worddav713ca71772831400453eeb9247bea908.png" /><br>

<img src="images\image2018-2-12%2010_17_7.png" /><br>

After a runbook is specified, the following execution settings are be changed:
1. Frequency of a Monitor Qapp.<br>
2. Data Source: Live Network<br>
3. Maximum runtime allowed

***Note:*** When customizing the stub, ensure the stub name is not changed. If the stub name is changed, the advanced script needs to be updated.

### c) Customizing type of Incident to trigger stub. <a name="type"></a>
Current business rule runs on the incident type "Link Status is down…". <br>
If the wordings of the incident's short description changes, the following changes are to be made

### d) Update Business Rule in ServiceNow.<a name="Business"></a>
1. In ServiceNow, navigate to "Business Rule", and open the rule you wish to edit.<br>
<img src="images\worddav54c9188ba18992f0e2e33249fcc080ad.png" /><br>

2. Edit the filter setting to match the requirement. <br>
<img src="images\worddavf3db4fa118177bd1dc93fd8ff11ce6d0.png" /><br>

3.In the advanced script, update the following lines of code to adjust the regex.
<img src="images\worddavc927803dfa5ba84ab896bdd9f55543a3.png" /><br>

Click "update" to save the Business Rule.

## Appendix <a name="Appendix"></a>
If your requirement is different from the case stated above, please contact NetBrain Support for customization.
