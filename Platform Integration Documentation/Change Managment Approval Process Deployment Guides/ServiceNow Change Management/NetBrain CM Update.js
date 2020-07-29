/**
 * This call will only bind NetBrain CM ID with change request. Initial the request status.
 *
 */
(function executeRule(current, previous /*null when async*/) {

    var NB_API_PREFIX = 'https://integrationlab.netbraintech.com/ServicesAPI/API/V1/';

    // to login get token & logout
    var tokenEndPoint = NB_API_PREFIX + 'Session';
    var tenantDomainEndPoint = NB_API_PREFIX + 'Session/CurrentDomain';

    // credential to login into netbrain
    var credential = {
		username: 'siran.he',
        password: 'Netbrain1!'
    };
    var tenantDomain = { tenantId: '40e0032e-14e7-4fea-7d00-8fe8bd65efae', domainId: 'b924c2f0-7210-43ba-9cdd-d1757ae23742'};

    // api time out default is 10 seconds
    var API_TIME_OUT = 10 * 1000;

    // store the netbrain api token
    var nbToken = '';

    // **********************
    var vendor = 'ServiceNow';
    var stateMapping = {
        'not requested': 0, // planning
        'requested': 1, // pending
        'approved': 2,
        'rejected': 3
    };

    /**
     * Request the token
     * @return hasToken: bool
     *
     */
    function login() {
        var request = newRequest(tokenEndPoint, 'POST', credential);
        try {
            gs.info('send request to netbrain, get the token'); //
            var response = request.execute();
            var responseBody = response.getBody();
            var obj = new JSON.parse(responseBody);
            nbToken = obj.token;
            return nbToken.length > 0;
        } catch (ex) {
            // todo handle get token failed exception where to check this error msg
            gs.error('get netbrain token failed.');
            gs.error(ex.getMessage());
            return false;
        }
    }

    /**
     * logout netbrain, remove token
     * @return
     * @constructor
     */
    function logout() {
        var body = {
            token: nbToken
        };
        var request = newRequest(tokenEndPoint, 'DELETE', body);
        try {
            gs.info('logout netbrain.');
            request.execute();
            gs.info('logout netbrain success.');
        } catch (ex) {
            gs.error('get netbrain token failed.');
            gs.error(ex.getMessage()); // should retry?
        }
    }

    function addActivity(message) {
        current.work_notes = message;
        current.update();
    }

    /**
     * Request to set tenant & domain
     * @return success: bool
     *
     */
    function setTenantDomain() {
        var request = newRequest(tenantDomainEndPoint, 'PUT', tenantDomain);
        try {
            gs.info('set tenant & domain info.');
            var response = request.execute();
            var responseBody = response.getBody();
            var obj = new JSON.parse(responseBody);
            return true;
        } catch (ex) {
            gs.error('set tenant & domain failed.');
            gs.error(ex.getMessage()); // should retry?
            return false;
        }
    }

    /**
     * make a http call to netbrain to binding change request id to a cm runbook id
     * @return
     *
     */
    function apiCMBinding() {
        var ticketId = current.getValue('sys_id');
        var runbookId = current.getValue('u_netbrain_cm_id');// this might be different for different customer
        var ticketName = current.getValue('number'); // this might be different for different customer
        var endPoint = NB_API_PREFIX + 'CM/Binding';
        var postData = {
            runbookId: runbookId,
            ticketId: ticketId,
            vendor: vendor,
            ticketName: ticketName
        };
        var request = newRequest(endPoint, 'POST', postData);
        try {
            gs.info('send change management binding request.');
            var response = request.execute();
            var responseBody = response.getBody();
            var obj = new JSON.parse(responseBody);
            if (obj.statusCode == 790200) {
                gs.info('Change management binding to ' + runbookId + ' success.');
                addActivity('Change management binding to ' + runbookId + ' success.');
            } else {
                gs.info(obj.statusDescription);
                // please change it to a proper msg, and this message is going to display on service now page
                gs.addErrorMessage('Binding Failed: ' + obj.statusDescription);
                addActivity('Binding Failed: ' + obj.statusDescription);
            }

        } catch (ex) {
            gs.error('change management binding failed.');
            gs.error(ex.getMessage()); // should retry?
            gs.addErrorMessage('binding Failed: ' + ex.getMessage());
            addActivity('binding Failed: ' + ex.getMessage());
        }
    }

    /**
     * make a http call to netbrain to set cm runbook approval state
     */
    function apiUpdateCMApprovalState() {
        var ticketId = current.getValue('sys_id'); // this might be different for different customer
        var runbookId = current.getValue('u_netbrain_cm_id');// this might be different for different customer
        var endPoint = NB_API_PREFIX + 'CM/approval/state';
        var ticketName = current.getValue('number'); // this might be different for different customer
        var snState = current.getValue('approval');
        if (stateMapping[snState] == null) {
            gs.error('cannot find the correspond state from netbrain.');
            return;
        }
        var postData = {
            runbookId: runbookId,
            ticketId: ticketId,
            vendor: vendor,
            ticketName: ticketName,
            state: stateMapping[snState]
        };
        var request = newRequest(endPoint, 'POST', postData);
        try {
            gs.info('set change management state.');
            var response = request.execute();
            var responseBody = response.getBody();
            var obj = new JSON.parse(responseBody);
            if (obj.statusCode == 790200) {
                var msg = 'set change management(' + runbookId + ') to state ' + snState + ' success.';
                gs.info(msg);
                addActivity(msg);
            } else {
                gs.info(obj.statusDescription);
                gs.addErrorMessage('update approval failed: ' + obj.statusDescription);
                addActivity('update approval failed: ' + obj.statusDescription);
            }
        } catch (ex) {
            gs.error('set change management state failed.');
            gs.error(ex.getMessage());
            gs.addErrorMessage('Error: ' + ex.getMessage());
            addActivity('Error: ' + ex.getMessage());
        }
    }

    function newRequest(url, method, data) {
        var request = new sn_ws.RESTMessageV2();
        request.setEndpoint(url);
        request.setHttpMethod(method);
        request.setRequestBody(JSON.stringify(data));
        request.setRequestHeader('Accept', 'application/json');
        request.setRequestHeader('Content-Type', 'application/json');
        request.setRequestHeader('token', nbToken);
        request.setHttpTimeout(API_TIME_OUT);
        return request;
    }

    /**
     * update a value of service now
     */
    function updateColumnValue(table, primaryKey, primaryVal, targetColumn, targetVal) {
        var gr = new GlideRecord(table);
        gr.addQuery(primaryKey, primaryVal);
        gr.query();
        if (gr.next()) {
            gr.setValue(targetColumn, targetVal);
            gr.update();
        }
    }

    /**
     * make a http call to netbrain to binding change request id to a cm runbook id
     */
    function main() {
		gs.info('-----current change status is: ' + current.getValue('approval'));
        var hasToken = login();
        if (hasToken) {
            gs.debug('----- bind login success.');
            if (setTenantDomain()) {
                // business logic
//                 apiCMBinding();
// 				gs.info('-----after binding, current change status is: ' + current.getValue('approval'));
				apiUpdateCMApprovalState();
				gs.info('-----updateing is triggerd. after update in updating, current change status is: ' + current.getValue('approval'));
            }
            logout();
        } else {
            gs.info('-----login failed, quit now...');
        }
    }

    main(); // run
})(current, previous);