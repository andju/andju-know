---
published: true
---
# Test callouts
The following mock classes help testing Apex code that makes (asynchronous) callouts, by tracking the requests that have been sent during the test. They allow you to assert that the request content is as expected.

> [!important] Test setup
> The `reset` method needs to be called before each test (can be included in the `@testSetup`)
> 
> Calling the `Test.setMock` method during the `@testSetup` will not correctly track the calls resp. responses.
 
## REST Callout
Each request is stored in the list `requests`. The testing basics are described on [developer.salesforce.com](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_classes_restful_http_testing_httpcalloutmock.htm).

```java
public class AndjusHttpCalloutMock implements HttpCalloutMock {
    public static HttpResponse mockResponse;

    // Keeps track of all executed calls.
    public static List<HTTPRequest> requests = new List<HTTPRequest>();

    /**
     * Reset the mockResponse and the calledEndpoints.
     * 
     * @param  newMockResponse Response that will be sent by a web service call.
     */
    public static void reset(HttpResponse httpResponse) {
        mockResponse = httpResponse;
        requests.clear();
    }

    /**
     * Get all requests against a specific endpoint.
     *
     * @param  endpoint URL of the endpoint
     * @return          List of requests
     */
    public static List<HTTPRequest> getRequests(String endpoint) {
        List<HTTPRequest> endpointReqs = new List<HTTPRequest>();
        for (HTTPRequest req : requests) {
            if (endpoint == call.getEndpoint()) {
                endpointReqs.add(req);
            }
        }
        return endpointReqs;
    }
   
    global HTTPResponse respond(HTTPRequest req) {
        requests.add(req);
        return mockResponse;
    }
}
```

Example test class:

```java
@isTest
private class SomeObjectTriggerHandler_Test {
    @testSetup
    static void setup() {
        HttpResponse mockResponse = new HttpResponse();
        mockResponse.setHeader('Content-Type', 'application/json');
        mockResponse.setBody('{"example":"test"}');
        mockResponse.setStatusCode(200);
		AndjusHttpCalloutMock.reset(mockResponse);
    }

    /**
     * If something is done, GET request should be sent to REST.
     */
    @isTest
    public static void dtagBaseline() {
        Test.setMock(HttpCalloutMock.class, new AndjusHttpCalloutMock());
        Test.startTest();
        // run your test
        Test.stopTest();

        List<HTTPRequest> reqs = AndjusHttpCalloutMock.getRequests('https://www.example.com');
        Assert.areEqual(1, reqs.size(), 'REST was not called once');

        HTTPRequest req = reqs.get(0);
        Assert.areEqual('GET', req.getMethod(), 'Incorrect http method was used');
    }
}
```

## SOAP Callout
Each call is stored as a key-value-map in the list `calls`. The testing basics are described on [developer.salesforce.com](https://developer.salesforce.com/docs/atlas.en-us.apexcode.meta/apexcode/apex_callouts_wsdl2apex_testing.htm).

```java
public class AndjusWebServiceMock implements WebServiceMock {
    public static Object mockResponse;

    // Keeps track of all executed calls.
    public static List<Map<String, Object>> calls = new List<Map<String, Object>>();

    /**
     * Reset the mockResponse and the calledEndpoints.
     * 
     * @param  newMockResponse Response that will be sent by a web service call.
     */
    public static void reset(Object responseX) {
        mockResponse = responseX;
        calls.clear();
    }

    /**
     * Get all calls against a specific endpoint.
     *
     * @param  endpoint URL of the endpoint
     * @return          List of calls
     */
    public static List<Map<String, Object>> getCalls(String endpoint) {
        List<Map<String, Object>> endpointCalls = new List<Map<String, Object>>();
        for (Map<String, Object> call : calls) {
            if (endpoint == call.get('endpoint')) {
                endpointCalls.add(call);
            }
        }
        return endpointCalls;
    }

    public void doInvoke(
        Object stub,
        Object request,
        Map<String, Object> response,
        String endpoint,
        String soapAction,
        String requestName,
        String responseNS,
        String responseName,
        String responseType
    ) {
        calls.add(
            new Map<String, Object>{
                'request' => request,
                'endpoint' => endpoint,
                'soapAction' => soapAction,
                'requestName' => requestName,
                'responseNS' => responseNS,
                'responseName' => responseName,
                'responseType' => responseType
            }
        );
        response.put('response_x', mockResponse);
    }
}
```

Example test class (assuming the request is the class `CustomRequest_element` and the response is the class `CustomResponse_element`):

```java
@isTest
private class SomeObjectTriggerHandler_Test {
    @testSetup
    static void setup() {
        CustomResponse_element mockResponse = new CustomResponse_element();
        mockResponse.ResponseMessage = 'success';
        AndjusWebServiceMock.reset(mockResponse);
    }

    /**
     * If something is done, the Name 'Smith' should be sent to the web service.
     */
    @isTest
    public static void dtagBaseline() {
        Test.setMock(WebServiceMock.class, new AndjusWebServiceMock());
        String testName = 'Smith';
        Test.startTest();
        // run your test
        Test.stopTest();

        List<Map<String, Object>> wsCalls = AndjusWebServiceMock.getCalls('https://www.example.com');
        Assert.areEqual(1, wsCalls.size(), 'WS was not called once');

        CustomRequest_element wsReq = (CustomRequest_element) wsCalls.get(0).get('request');
        Assert.areEqual(testName, wsReq.Name, 'Incorrect Name was sent');
    }
}
```
