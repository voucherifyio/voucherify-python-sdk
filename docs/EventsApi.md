# voucherify.EventsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**track_custom_event**](EventsApi.md#track_custom_event) | **POST** /v1/events | Track Custom Event


# **track_custom_event**
> EventsCreateResponseBody track_custom_event(events_create_request_body=events_create_request_body)

Track Custom Event

To track a custom event, you create an event object.   The event object must be linked to the customer who performs the action. If a customer doesnt exist in Voucherify, the customer will be created.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.events_create_request_body import EventsCreateRequestBody
from voucherify.models.events_create_response_body import EventsCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.EventsApi(api_client)
    events_create_request_body = {"event":"event-name","customer":{"source_id":"referee-source_id"},"referral":{"code":"voucher-code","referrer_id":"referrer-source_id"}} # EventsCreateRequestBody | Specify the details of the custom event. (optional)

    try:
        # Track Custom Event
        api_response = api_instance.track_custom_event(events_create_request_body=events_create_request_body)
        print("The response of EventsApi->track_custom_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->track_custom_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events_create_request_body** | [**EventsCreateRequestBody**](EventsCreateRequestBody.md)| Specify the details of the custom event. | [optional] 

### Return type

[**EventsCreateResponseBody**](EventsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the event type if the event was received by the application. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

