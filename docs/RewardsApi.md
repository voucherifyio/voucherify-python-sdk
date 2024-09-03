# voucherify.RewardsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_reward**](RewardsApi.md#create_reward) | **POST** /v1/rewards | Create Reward
[**create_reward_assignment**](RewardsApi.md#create_reward_assignment) | **POST** /v1/rewards/{rewardId}/assignments | Create Reward Assignment
[**delete_reward**](RewardsApi.md#delete_reward) | **DELETE** /v1/rewards/{rewardId} | Delete Reward
[**delete_reward_assignment**](RewardsApi.md#delete_reward_assignment) | **DELETE** /v1/rewards/{rewardId}/assignments/{assignmentId} | Delete Reward Assignment
[**get_reward**](RewardsApi.md#get_reward) | **GET** /v1/rewards/{rewardId} | Get Reward
[**get_reward_assignment**](RewardsApi.md#get_reward_assignment) | **GET** /v1/rewards/{rewardId}/assignments/{assignmentId} | Get Reward Assignment
[**list_reward_assignments**](RewardsApi.md#list_reward_assignments) | **GET** /v1/rewards/{rewardId}/assignments | List Reward Assignments
[**list_rewards**](RewardsApi.md#list_rewards) | **GET** /v1/rewards | List Rewards
[**update_reward**](RewardsApi.md#update_reward) | **PUT** /v1/rewards/{rewardId} | Update Reward
[**update_reward_assignment**](RewardsApi.md#update_reward_assignment) | **PUT** /v1/rewards/{rewardId}/assignments/{assignmentId} | Update Reward Assignment


# **create_reward**
> RewardsCreateResponseBody create_reward(rewards_create_request_body=rewards_create_request_body)

Create Reward

Create a new reward.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.rewards_create_request_body import RewardsCreateRequestBody
from voucherify.models.rewards_create_response_body import RewardsCreateResponseBody
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
    api_instance = voucherify.RewardsApi(api_client)
    rewards_create_request_body = {"name":"Digital - Gift Card Reward","type":"CAMPAIGN","metadata":{"Type":"Gift"},"parameters":{"campaign":{"id":"camp_hC2GdqYtOmTT45zfhib62cK1","balance":3000}}} # RewardsCreateRequestBody | Define parameters of the new reward. (optional)

    try:
        # Create Reward
        api_response = api_instance.create_reward(rewards_create_request_body=rewards_create_request_body)
        print("The response of RewardsApi->create_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->create_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rewards_create_request_body** | [**RewardsCreateRequestBody**](RewardsCreateRequestBody.md)| Define parameters of the new reward. | [optional] 

### Return type

[**RewardsCreateResponseBody**](RewardsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a reward object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reward_assignment**
> RewardsAssignmentsCreateResponseBody create_reward_assignment(reward_id, rewards_assignments_create_request_body=rewards_assignments_create_request_body)

Create Reward Assignment

Assigns a reward to a specified loyalty campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.rewards_assignments_create_request_body import RewardsAssignmentsCreateRequestBody
from voucherify.models.rewards_assignments_create_response_body import RewardsAssignmentsCreateResponseBody
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
    api_instance = voucherify.RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | A unique reward ID.
    rewards_assignments_create_request_body = {"campaign":"camp_OTuGGP90PivbvROsRvfM65El","parameters":{"loyalty":{"points":39}}} # RewardsAssignmentsCreateRequestBody | Provide the campaign ID of the campaign to which the reward is to be assigned and define the cost of the reward in terms of loyalty points. (optional)

    try:
        # Create Reward Assignment
        api_response = api_instance.create_reward_assignment(reward_id, rewards_assignments_create_request_body=rewards_assignments_create_request_body)
        print("The response of RewardsApi->create_reward_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->create_reward_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| A unique reward ID. | 
 **rewards_assignments_create_request_body** | [**RewardsAssignmentsCreateRequestBody**](RewardsAssignmentsCreateRequestBody.md)| Provide the campaign ID of the campaign to which the reward is to be assigned and define the cost of the reward in terms of loyalty points. | [optional] 

### Return type

[**RewardsAssignmentsCreateResponseBody**](RewardsAssignmentsCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a reward assignment object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reward**
> delete_reward(reward_id)

Delete Reward

Delete a reward.

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
    api_instance = voucherify.RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | A unique reward ID.

    try:
        # Delete Reward
        api_instance.delete_reward(reward_id)
    except Exception as e:
        print("Exception when calling RewardsApi->delete_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| A unique reward ID. | 

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

# **delete_reward_assignment**
> delete_reward_assignment(reward_id, assignment_id)

Delete Reward Assignment

This method deletes a reward assignment for a particular reward.

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
    api_instance = voucherify.RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | A unique reward ID.
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID.

    try:
        # Delete Reward Assignment
        api_instance.delete_reward_assignment(reward_id, assignment_id)
    except Exception as e:
        print("Exception when calling RewardsApi->delete_reward_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| A unique reward ID. | 
 **assignment_id** | **str**| A unique reward assignment ID. | 

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

# **get_reward**
> Reward get_reward(reward_id)

Get Reward

Retrieve a reward by the reward ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.reward import Reward
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
    api_instance = voucherify.RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | A unique reward ID.

    try:
        # Get Reward
        api_response = api_instance.get_reward(reward_id)
        print("The response of RewardsApi->get_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->get_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| A unique reward ID. | 

### Return type

[**Reward**](Reward.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a reward object if a valid identifier was provided.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_assignment**
> RewardsAssignmentsGetResponseBody get_reward_assignment(reward_id, assignment_id)

Get Reward Assignment

Retrieve a reward assignment.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.rewards_assignments_get_response_body import RewardsAssignmentsGetResponseBody
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
    api_instance = voucherify.RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | A unique reward ID.
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID.

    try:
        # Get Reward Assignment
        api_response = api_instance.get_reward_assignment(reward_id, assignment_id)
        print("The response of RewardsApi->get_reward_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->get_reward_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| A unique reward ID. | 
 **assignment_id** | **str**| A unique reward assignment ID. | 

### Return type

[**RewardsAssignmentsGetResponseBody**](RewardsAssignmentsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a reward assignment object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reward_assignments**
> RewardsAssignmentsListResponseBody list_reward_assignments(reward_id, limit=limit, page=page)

List Reward Assignments

Retrieve reward assignments by the reward ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.rewards_assignments_list_response_body import RewardsAssignmentsListResponseBody
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
    api_instance = voucherify.RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | A unique reward ID.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)

    try:
        # List Reward Assignments
        api_response = api_instance.list_reward_assignments(reward_id, limit=limit, page=page)
        print("The response of RewardsApi->list_reward_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->list_reward_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| A unique reward ID. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 

### Return type

[**RewardsAssignmentsListResponseBody**](RewardsAssignmentsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of reward assignment objects. Each object contains information regarding the resource to which the reward was assigned and the cost in loyalty points for the reward. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rewards**
> RewardsListResponseBody list_rewards(limit=limit, page=page, assignment_id=assignment_id)

List Rewards

Retrieve rewards.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.rewards_list_response_body import RewardsListResponseBody
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
    api_instance = voucherify.RewardsApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID. Use this parameter to get the reward details in the context of an assignment ID. (optional)

    try:
        # List Rewards
        api_response = api_instance.list_rewards(limit=limit, page=page, assignment_id=assignment_id)
        print("The response of RewardsApi->list_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->list_rewards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **assignment_id** | **str**| A unique reward assignment ID. Use this parameter to get the reward details in the context of an assignment ID. | [optional] 

### Return type

[**RewardsListResponseBody**](RewardsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of reward objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reward**
> RewardsUpdateResponseBody update_reward(reward_id, rewards_update_request_body=rewards_update_request_body)

Update Reward

Update the details of a reward.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.rewards_update_request_body import RewardsUpdateRequestBody
from voucherify.models.rewards_update_response_body import RewardsUpdateResponseBody
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
    api_instance = voucherify.RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | A unique reward ID.
    rewards_update_request_body = {"name":"Digital - Gift Card Reward","metadata":{"Type":"Gift"},"parameters":{"campaign":{"id":"camp_hC2GdqYtOmTT45zfhib62cK1","balance":3000}}} # RewardsUpdateRequestBody | Define the parameters to be updated for the reward. (optional)

    try:
        # Update Reward
        api_response = api_instance.update_reward(reward_id, rewards_update_request_body=rewards_update_request_body)
        print("The response of RewardsApi->update_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->update_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| A unique reward ID. | 
 **rewards_update_request_body** | [**RewardsUpdateRequestBody**](RewardsUpdateRequestBody.md)| Define the parameters to be updated for the reward. | [optional] 

### Return type

[**RewardsUpdateResponseBody**](RewardsUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an updated reward object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reward_assignment**
> RewardsAssignmentsUpdateResponseBody update_reward_assignment(reward_id, assignment_id, rewards_assignments_update_request_body=rewards_assignments_update_request_body)

Update Reward Assignment

Update the number of points needed to successfully redeem the reward.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.rewards_assignments_update_request_body import RewardsAssignmentsUpdateRequestBody
from voucherify.models.rewards_assignments_update_response_body import RewardsAssignmentsUpdateResponseBody
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
    api_instance = voucherify.RewardsApi(api_client)
    reward_id = 'reward_id_example' # str | A unique reward ID.
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID.
    rewards_assignments_update_request_body = {"parameters":{"loyalty":{"points":35}}} # RewardsAssignmentsUpdateRequestBody | Define the number of points required to exchange for the reward. (optional)

    try:
        # Update Reward Assignment
        api_response = api_instance.update_reward_assignment(reward_id, assignment_id, rewards_assignments_update_request_body=rewards_assignments_update_request_body)
        print("The response of RewardsApi->update_reward_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RewardsApi->update_reward_assignment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reward_id** | **str**| A unique reward ID. | 
 **assignment_id** | **str**| A unique reward assignment ID. | 
 **rewards_assignments_update_request_body** | [**RewardsAssignmentsUpdateRequestBody**](RewardsAssignmentsUpdateRequestBody.md)| Define the number of points required to exchange for the reward. | [optional] 

### Return type

[**RewardsAssignmentsUpdateResponseBody**](RewardsAssignmentsUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the updated reward assignment object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

