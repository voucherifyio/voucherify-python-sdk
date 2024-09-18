# voucherify.ValidationRulesApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_validation_rule_assignment**](ValidationRulesApi.md#create_validation_rule_assignment) | **POST** /v1/validation-rules/{validationRuleId}/assignments | Create Validation Rules Assignments
[**create_validation_rules**](ValidationRulesApi.md#create_validation_rules) | **POST** /v1/validation-rules | Create Validation Rules
[**delete_validation_rule_assignment**](ValidationRulesApi.md#delete_validation_rule_assignment) | **DELETE** /v1/validation-rules/{validationRuleId}/assignments/{assignmentId} | Delete Validation Rule Assignment
[**delete_validation_rules**](ValidationRulesApi.md#delete_validation_rules) | **DELETE** /v1/validation-rules/{validationRuleId} | Delete Validation Rule
[**get_validation_rule**](ValidationRulesApi.md#get_validation_rule) | **GET** /v1/validation-rules/{validationRuleId} | Get Validation Rule
[**list_validation_rule_assignments**](ValidationRulesApi.md#list_validation_rule_assignments) | **GET** /v1/validation-rules/{validationRuleId}/assignments | List Validation Rule Assignments
[**list_validation_rules**](ValidationRulesApi.md#list_validation_rules) | **GET** /v1/validation-rules | List Validation Rules
[**list_validation_rules_assignments**](ValidationRulesApi.md#list_validation_rules_assignments) | **GET** /v1/validation-rules-assignments | List Validation Rules&#39; Assignment(s)
[**update_validation_rule**](ValidationRulesApi.md#update_validation_rule) | **PUT** /v1/validation-rules/{validationRuleId} | Update Validation Rule


# **create_validation_rule_assignment**
> ValidationRulesAssignmentsCreateResponseBody create_validation_rule_assignment(validation_rule_id, force=force, validation_rules_assignments_create_request_body=validation_rules_assignments_create_request_body)

Create Validation Rules Assignments

Assign validation rule to either one of the following objects: voucher, campaign, promotion tier, earning rule, reward, distribution.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.validation_rules_assignments_create_request_body import ValidationRulesAssignmentsCreateRequestBody
from voucherify.models.validation_rules_assignments_create_response_body import ValidationRulesAssignmentsCreateResponseBody
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    validation_rule_id = 'validation_rule_id_example' # str | Unique validation rule ID.
    force = True # bool | If this flag is set to true, the previous assignment with the same data will be deleted and a new one will be added. (optional)
    validation_rules_assignments_create_request_body = {"voucher":"v_ssR6vhswwh5odSloN2Vc3O60w7aea018"} # ValidationRulesAssignmentsCreateRequestBody | Specify the resource that you would like to assign the validation rule to. (optional)

    try:
        # Create Validation Rules Assignments
        api_response = api_instance.create_validation_rule_assignment(validation_rule_id, force=force, validation_rules_assignments_create_request_body=validation_rules_assignments_create_request_body)
        print("The response of ValidationRulesApi->create_validation_rule_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->create_validation_rule_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_rule_id** | **str**| Unique validation rule ID. | 
 **force** | **bool**| If this flag is set to true, the previous assignment with the same data will be deleted and a new one will be added. | [optional] 
 **validation_rules_assignments_create_request_body** | [**ValidationRulesAssignmentsCreateRequestBody**](ValidationRulesAssignmentsCreateRequestBody.md)| Specify the resource that you would like to assign the validation rule to. | [optional] 

### Return type

[**ValidationRulesAssignmentsCreateResponseBody**](ValidationRulesAssignmentsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a validation rules assignment object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_validation_rules**
> ValidationRulesCreateResponseBody create_validation_rules(validation_rules_create_request_body=validation_rules_create_request_body)

Create Validation Rules

Create validation rules.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.validation_rules_create_request_body import ValidationRulesCreateRequestBody
from voucherify.models.validation_rules_create_response_body import ValidationRulesCreateResponseBody
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    validation_rules_create_request_body = {"name":"Set of Validation Rules","error":{"message":"Your order does not meet at least one of the required criteria."},"applicable_to":{"included_all":false,"excluded":[{"object":"product","id":"prod_0bae45ffc7003ffc52","source_id":"second_product","strict":false,"effect":"APPLY_TO_EVERY"}],"included":[{"object":"product","id":"prod_0b72b00ffed198e344","source_id":null,"effect":"APPLY_TO_MOST_EXPENSIVE","quantity_limit":1},{"object":"products_collection","id":"pc_4ndRXAsTOzwSdHcQcxf489uU","source_id":null,"effect":"APPLY_TO_EVERY","quantity_limit":5}]},"rules":{"1":{"name":"order.metadata","property":"location","rules":{},"conditions":{"$is":["Santorini"]},"error":{"message":"Your order must be placed at one of our Santorini shops."}},"2":{"name":"custom_event.metadata","property":"test","rules":{},"conditions":{"$greater_than_or_equal":[1]}},"3":{"name":"order.items.every","rules":{"1":{"name":"order.items.metadata","property":"test","rules":{},"conditions":{"$greater_than_or_equal":[1]}}},"conditions":{"$is":[{"id":"<PROD_ID>","effect":"APPLY_TO_EVERY","object":"product","source_id":"<SOURCE_ID>"}]}},"logic":"1 or 2"}} # ValidationRulesCreateRequestBody | Specify the validation rules parameters. (optional)

    try:
        # Create Validation Rules
        api_response = api_instance.create_validation_rules(validation_rules_create_request_body=validation_rules_create_request_body)
        print("The response of ValidationRulesApi->create_validation_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->create_validation_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_rules_create_request_body** | [**ValidationRulesCreateRequestBody**](ValidationRulesCreateRequestBody.md)| Specify the validation rules parameters. | [optional] 

### Return type

[**ValidationRulesCreateResponseBody**](ValidationRulesCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a validation rule object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_validation_rule_assignment**
> delete_validation_rule_assignment(validation_rule_id, assignment_id)

Delete Validation Rule Assignment

This method deletes a validation rule assignment.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    validation_rule_id = 'validation_rule_id_example' # str | A unique validation rule ID.
    assignment_id = 'assignment_id_example' # str | A unique validation rule assignment ID.

    try:
        # Delete Validation Rule Assignment
        api_instance.delete_validation_rule_assignment(validation_rule_id, assignment_id)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->delete_validation_rule_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_rule_id** | **str**| A unique validation rule ID. | 
 **assignment_id** | **str**| A unique validation rule assignment ID. | 

### Return type

void (empty response body)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if deletion is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_validation_rules**
> delete_validation_rules(validation_rule_id)

Delete Validation Rule

This method deletes a validation rule.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    validation_rule_id = 'validation_rule_id_example' # str | A unique validation rule ID.

    try:
        # Delete Validation Rule
        api_instance.delete_validation_rules(validation_rule_id)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->delete_validation_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_rule_id** | **str**| A unique validation rule ID. | 

### Return type

void (empty response body)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if deletion is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_validation_rule**
> ValidationRulesGetResponseBody get_validation_rule(validation_rule_id)

Get Validation Rule

Retrieve the details of a validation rule.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.validation_rules_get_response_body import ValidationRulesGetResponseBody
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    validation_rule_id = 'validation_rule_id_example' # str | A unique validation rule ID.

    try:
        # Get Validation Rule
        api_response = api_instance.get_validation_rule(validation_rule_id)
        print("The response of ValidationRulesApi->get_validation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->get_validation_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_rule_id** | **str**| A unique validation rule ID. | 

### Return type

[**ValidationRulesGetResponseBody**](ValidationRulesGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the validation rule object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_validation_rule_assignments**
> ValidationRulesAssignmentsListResponseBody list_validation_rule_assignments(validation_rule_id, limit=limit, page=page, order=order)

List Validation Rule Assignments

Retrieve validation rule assignments for a specific validation rule.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_order_list_validation_rule_assignments import ParameterOrderListValidationRuleAssignments
from voucherify.models.validation_rules_assignments_list_response_body import ValidationRulesAssignmentsListResponseBody
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    validation_rule_id = 'validation_rule_id_example' # str | Unique validation rule ID.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListValidationRuleAssignments() # ParameterOrderListValidationRuleAssignments | This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Validation Rule Assignments
        api_response = api_instance.list_validation_rule_assignments(validation_rule_id, limit=limit, page=page, order=order)
        print("The response of ValidationRulesApi->list_validation_rule_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->list_validation_rule_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_rule_id** | **str**| Unique validation rule ID. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListValidationRuleAssignments**](.md)| This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**ValidationRulesAssignmentsListResponseBody**](ValidationRulesAssignmentsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of validation rule assignments.  If the validation rule ID provided in the path parameter cannot be found, the endpoint will return an empty &#x60;data&#x60; array and a total of &#x60;0&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_validation_rules**
> ValidationRulesListResponseBody list_validation_rules(limit=limit, page=page, order=order, start_date=start_date, end_date=end_date)

List Validation Rules

Retrieve validation rules.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.parameter_order_list_validation_rules import ParameterOrderListValidationRules
from voucherify.models.validation_rules_list_response_body import ValidationRulesListResponseBody
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListValidationRules() # ParameterOrderListValidationRules | This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    start_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must start on. Represented in ISO 8601 format. (optional)
    end_date = '2013-10-20T19:20:30+01:00' # datetime | Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. (optional)

    try:
        # List Validation Rules
        api_response = api_instance.list_validation_rules(limit=limit, page=page, order=order, start_date=start_date, end_date=end_date)
        print("The response of ValidationRulesApi->list_validation_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->list_validation_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListValidationRules**](.md)| This is a property that controls the sorting direction of the results. Sort the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **start_date** | **datetime**| Timestamp representing the date and time which results must start on. Represented in ISO 8601 format. | [optional] 
 **end_date** | **datetime**| Timestamp representing the date and time which results must end on. Represented in ISO 8601 format. | [optional] 

### Return type

[**ValidationRulesListResponseBody**](ValidationRulesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of validation rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_validation_rules_assignments**
> ValidationRulesAssignmentsListResponseBody list_validation_rules_assignments(related_object_id=related_object_id, rule=rule, page=page, limit=limit, order=order)

List Validation Rules' Assignment(s)

List all validation rules assignments or filter the results using the related object ID or the validation rule ID query parameters.  # How to retrieve specific validation rule assignments(s) ## Related object ID To find an assignment for a particular resource, you can use the ID of the object to which the validation rule was assigned. This could be, for example, an ID of a: voucher, campaign, distribution, reward assignment, earning rule, promotion tier.    ## Validation rule ID You can use the validation rule ID to find assignment(s) for a specific validation rule.  

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.validation_rules_assignments_list_response_body import ValidationRulesAssignmentsListResponseBody
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    related_object_id = 'related_object_id_example' # str | The resource ID to which the validation rule was assigned; this could be, for example, a resource ID of a voucher, campaign, earning rule, reward assignment, promotion tier, or distribution. (optional)
    rule = 'rule_example' # str | Validation rule ID. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = 'order_example' # str | Sorts the results using one of the filtering options: -created_at, created_at, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Validation Rules' Assignment(s)
        api_response = api_instance.list_validation_rules_assignments(related_object_id=related_object_id, rule=rule, page=page, limit=limit, order=order)
        print("The response of ValidationRulesApi->list_validation_rules_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->list_validation_rules_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **related_object_id** | **str**| The resource ID to which the validation rule was assigned; this could be, for example, a resource ID of a voucher, campaign, earning rule, reward assignment, promotion tier, or distribution. | [optional] 
 **rule** | **str**| Validation rule ID. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | **str**| Sorts the results using one of the filtering options: -created_at, created_at, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**ValidationRulesAssignmentsListResponseBody**](ValidationRulesAssignmentsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with a data property that contains an array of validation rule assignments. Each entry in the array is a separate object. If no more validation rule assignments are available, the resulting array will be empty. The result can be narrowed down according to default filters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_validation_rule**
> ValidationRulesUpdateResponseBody update_validation_rule(validation_rule_id, validation_rules_update_request_body=validation_rules_update_request_body)

Update Validation Rule

Update validation rule parameters.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.validation_rules_update_request_body import ValidationRulesUpdateRequestBody
from voucherify.models.validation_rules_update_response_body import ValidationRulesUpdateResponseBody
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
    api_instance = voucherify.ValidationRulesApi(api_client)
    validation_rule_id = 'validation_rule_id_example' # str | A unique validation rule ID.
    validation_rules_update_request_body = {"name":"Set of Validation Rules Updated","error":{"message":"Your orders do not meet at least one of the required criteria."},"applicable_to":{"included_all":false,"excluded":[{"object":"product","id":"prod_0bae45ffc7003ffccc","source_id":"second_product","strict":false,"effect":"APPLY_TO_EVERY"}],"included":[{"object":"product","id":"prod_0b72b00ffed198e333","source_id":null,"effect":"APPLY_TO_CHEAPEST","quantity_limit":1},{"object":"products_collection","id":"pc_4ndRXAsTOzwSdHcQcxf489uU","source_id":null,"effect":"APPLY_TO_EVERY","quantity_limit":5}]},"rules":{"1":{"name":"order.metadata","property":"place","rules":{},"conditions":{"$is":["Santorini"]},"error":{"message":"Your order must be placed at one of our Santorini shops on the beach."}},"2":{"name":"custom_event.metadata","property":"lining","rules":{},"conditions":{"$greater_than_or_equal":[1]}},"3":{"name":"order.items.every","rules":{"1":{"name":"order.items.metadata","property":"test","rules":{},"conditions":{"$greater_than_or_equal":[1]}}},"conditions":{"$is":[{"id":"<PRODs_ID>","effect":"APPLY_TO_EVERY","object":"product","source_id":"<SOURCEs_ID>"}]}},"logic":"1 and 2"}} # ValidationRulesUpdateRequestBody | Specify the parameters to be updated. (optional)

    try:
        # Update Validation Rule
        api_response = api_instance.update_validation_rule(validation_rule_id, validation_rules_update_request_body=validation_rules_update_request_body)
        print("The response of ValidationRulesApi->update_validation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ValidationRulesApi->update_validation_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_rule_id** | **str**| A unique validation rule ID. | 
 **validation_rules_update_request_body** | [**ValidationRulesUpdateRequestBody**](ValidationRulesUpdateRequestBody.md)| Specify the parameters to be updated. | [optional] 

### Return type

[**ValidationRulesUpdateResponseBody**](ValidationRulesUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the validation rule object with the updated parameters. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

