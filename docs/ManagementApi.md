# voucherify.ManagementApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_user**](ManagementApi.md#assign_user) | **POST** /management/v1/projects/{projectId}/users | Assign User
[**create_brand**](ManagementApi.md#create_brand) | **POST** /management/v1/projects/{projectId}/branding | Create Brand
[**create_custom_event_schema**](ManagementApi.md#create_custom_event_schema) | **POST** /management/v1/projects/{projectId}/custom-event-schemas | Create Custom Event Schema
[**create_metadata_schema**](ManagementApi.md#create_metadata_schema) | **POST** /management/v1/projects/{projectId}/metadata-schemas | Create Metadata Schema
[**create_project**](ManagementApi.md#create_project) | **POST** /management/v1/projects | Create Project
[**create_stacking_rules**](ManagementApi.md#create_stacking_rules) | **POST** /management/v1/projects/{projectId}/stacking-rules | Create Stacking Rules
[**create_webhook**](ManagementApi.md#create_webhook) | **POST** /management/v1/projects/{projectId}/webhooks | Create Webhook
[**delete_brand**](ManagementApi.md#delete_brand) | **DELETE** /management/v1/projects/{projectId}/branding/{brandingId} | Delete Brand
[**delete_custom_event_schema**](ManagementApi.md#delete_custom_event_schema) | **DELETE** /management/v1/projects/{projectId}/custom-event-schemas/{customEventSchemaId} | Delete Custom Event Schema
[**delete_metadata_schema**](ManagementApi.md#delete_metadata_schema) | **DELETE** /management/v1/projects/{projectId}/metadata-schemas/{metadataSchemaId} | Delete Metadata Schema
[**delete_project**](ManagementApi.md#delete_project) | **DELETE** /management/v1/projects/{projectId} | Delete Project
[**delete_stacking_rules**](ManagementApi.md#delete_stacking_rules) | **DELETE** /management/v1/projects/{projectId}/stacking-rules/{stackingRulesId} | Delete Stacking Rules
[**delete_webhook**](ManagementApi.md#delete_webhook) | **DELETE** /management/v1/projects/{projectId}/webhooks/{webhookId} | Delete Webhook
[**get_brand**](ManagementApi.md#get_brand) | **GET** /management/v1/projects/{projectId}/branding/{brandingId} | Get Brand
[**get_custom_event_schema**](ManagementApi.md#get_custom_event_schema) | **GET** /management/v1/projects/{projectId}/custom-event-schemas/{customEventSchemaId} | Get Custom Event Schema
[**get_metadata_schema1**](ManagementApi.md#get_metadata_schema1) | **GET** /management/v1/projects/{projectId}/metadata-schemas/{metadataSchemaId} | Get Metadata Schema
[**get_project**](ManagementApi.md#get_project) | **GET** /management/v1/projects/{projectId} | Get Project
[**get_stacking_rules**](ManagementApi.md#get_stacking_rules) | **GET** /management/v1/projects/{projectId}/stacking-rules/{stackingRulesId} | Get Stacking Rules
[**get_user**](ManagementApi.md#get_user) | **GET** /management/v1/projects/{projectId}/users/{userId} | Get User
[**get_webhook**](ManagementApi.md#get_webhook) | **GET** /management/v1/projects/{projectId}/webhooks/{webhookId} | Get Webhook
[**invite_user**](ManagementApi.md#invite_user) | **POST** /management/v1/projects/users/invite | Invite a New User
[**list_brands**](ManagementApi.md#list_brands) | **GET** /management/v1/projects/{projectId}/branding | List Brands
[**list_custom_event_schemas**](ManagementApi.md#list_custom_event_schemas) | **GET** /management/v1/projects/{projectId}/custom-event-schemas | List Custom Event Schemas
[**list_metadata_schemas1**](ManagementApi.md#list_metadata_schemas1) | **GET** /management/v1/projects/{projectId}/metadata-schemas | List Metadata Schemas
[**list_projects**](ManagementApi.md#list_projects) | **GET** /management/v1/projects | List Projects
[**list_stacking_rules**](ManagementApi.md#list_stacking_rules) | **GET** /management/v1/projects/{projectId}/stacking-rules | List Stacking Rules
[**list_users**](ManagementApi.md#list_users) | **GET** /management/v1/projects/{projectId}/users | List Users
[**list_webhooks**](ManagementApi.md#list_webhooks) | **GET** /management/v1/projects/{projectId}/webhooks | List Webhooks
[**management_copy_campaign_template**](ManagementApi.md#management_copy_campaign_template) | **POST** /management/v1/projects/{projectId}/templates/campaigns/{campaignTemplateId}/copy | Copy Campaign Template to a Project
[**management_list_campaign_templates**](ManagementApi.md#management_list_campaign_templates) | **GET** /management/v1/projects/{projectId}/templates/campaigns | List Campaign Templates
[**unassign_user**](ManagementApi.md#unassign_user) | **DELETE** /management/v1/projects/{projectId}/users/{userId} | Unassign User
[**update_brand**](ManagementApi.md#update_brand) | **PUT** /management/v1/projects/{projectId}/branding/{brandingId} | Update Brand
[**update_custom_event_schema**](ManagementApi.md#update_custom_event_schema) | **PUT** /management/v1/projects/{projectId}/custom-event-schemas/{customEventSchemaId} | Update Custom Event Schema
[**update_metadata_schema**](ManagementApi.md#update_metadata_schema) | **PUT** /management/v1/projects/{projectId}/metadata-schemas/{metadataSchemaId} | Update Metadata Schema
[**update_project**](ManagementApi.md#update_project) | **PUT** /management/v1/projects/{projectId} | Update Project
[**update_stacking_rules**](ManagementApi.md#update_stacking_rules) | **PUT** /management/v1/projects/{projectId}/stacking-rules/{stackingRulesId} | Update Stacking Rules
[**update_user**](ManagementApi.md#update_user) | **PUT** /management/v1/projects/{projectId}/users/{userId} | Update User
[**update_webhook**](ManagementApi.md#update_webhook) | **PUT** /management/v1/projects/{projectId}/webhooks/{webhookId} | Update Webhook


# **assign_user**
> ManagementProjectsUsersAssignResponseBody assign_user(project_id, management_projects_users_assign_request_body=management_projects_users_assign_request_body)

Assign User

Assigns a user to a given project. The user must be an existing user in Voucherify.  🚧 Correct Use of Data To avoid errors, use the role key with either id or login keys.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_users_assign_request_body import ManagementProjectsUsersAssignRequestBody
from voucherify.models.management_projects_users_assign_response_body import ManagementProjectsUsersAssignResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    management_projects_users_assign_request_body = voucherify.ManagementProjectsUsersAssignRequestBody() # ManagementProjectsUsersAssignRequestBody | Defines the user details. (optional)

    try:
        # Assign User
        api_response = api_instance.assign_user(project_id, management_projects_users_assign_request_body=management_projects_users_assign_request_body)
        print("The response of ManagementApi->assign_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->assign_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **management_projects_users_assign_request_body** | [**ManagementProjectsUsersAssignRequestBody**](ManagementProjectsUsersAssignRequestBody.md)| Defines the user details. | [optional] 

### Return type

[**ManagementProjectsUsersAssignResponseBody**](ManagementProjectsUsersAssignResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the user assigned to the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_brand**
> ManagementProjectsBrandingCreateResponseBody create_brand(project_id, management_projects_branding_create_request_body=management_projects_branding_create_request_body)

Create Brand

Creates a new brand configuration. You can have only one brand configured for a project.  📘 White Labelling  The white labelling settings which can be found in Project Settings > Brand Details and which are available only for Enterprise clients as a separate service can be configured only in the user interface.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_branding_create_request_body import ManagementProjectsBrandingCreateRequestBody
from voucherify.models.management_projects_branding_create_response_body import ManagementProjectsBrandingCreateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    management_projects_branding_create_request_body = {"brand":{"name":"Voucherify PSA","privacy_policy_url":null,"terms_of_use_url":null,"permission_reminder":"You are receiving this email because you opted in at our website.","website_url":"voucherify.io"},"address":{"street":"Porcelanowa 23","city":"Katowice","postal":"43-246","state":null,"country":"Poland"},"contact":{"email":"support@voucherify.io","phone":null},"cockpits":{"campaigns_overview_enabled":false,"loyalty_enabled":true,"gift_cards_enabled":true,"coupons_enabled":true,"referrals_enabled":true,"theme":"default","use_custom_double_opt_in_redirect_url":false,"custom_double_opt_in_redirect_url":null}} # ManagementProjectsBrandingCreateRequestBody | Defines a brand configuration. (optional)

    try:
        # Create Brand
        api_response = api_instance.create_brand(project_id, management_projects_branding_create_request_body=management_projects_branding_create_request_body)
        print("The response of ManagementApi->create_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->create_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **management_projects_branding_create_request_body** | [**ManagementProjectsBrandingCreateRequestBody**](ManagementProjectsBrandingCreateRequestBody.md)| Defines a brand configuration. | [optional] 

### Return type

[**ManagementProjectsBrandingCreateResponseBody**](ManagementProjectsBrandingCreateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the brand configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_custom_event_schema**
> ManagementProjectsCustomEventSchemasCreateResponseBody create_custom_event_schema(project_id, management_projects_custom_event_schemas_create_request_body=management_projects_custom_event_schemas_create_request_body)

Create Custom Event Schema

Creates a custom event schema. The properties object is required, but it can be empty, however. This object is for optional custom properties (metadata).  📘 Custom Event Documentation  Read [Custom Events](https://support.voucherify.io/article/111-custom-events) article to learn how custom events work in Voucherify. Read also the details about the Track Custom Event endpoint and the Custom Event Object.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_custom_event_schemas_create_request_body import ManagementProjectsCustomEventSchemasCreateRequestBody
from voucherify.models.management_projects_custom_event_schemas_create_response_body import ManagementProjectsCustomEventSchemasCreateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    management_projects_custom_event_schemas_create_request_body = voucherify.ManagementProjectsCustomEventSchemasCreateRequestBody() # ManagementProjectsCustomEventSchemasCreateRequestBody | Defines the custom event schema. (optional)

    try:
        # Create Custom Event Schema
        api_response = api_instance.create_custom_event_schema(project_id, management_projects_custom_event_schemas_create_request_body=management_projects_custom_event_schemas_create_request_body)
        print("The response of ManagementApi->create_custom_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->create_custom_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **management_projects_custom_event_schemas_create_request_body** | [**ManagementProjectsCustomEventSchemasCreateRequestBody**](ManagementProjectsCustomEventSchemasCreateRequestBody.md)| Defines the custom event schema. | [optional] 

### Return type

[**ManagementProjectsCustomEventSchemasCreateResponseBody**](ManagementProjectsCustomEventSchemasCreateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the custom event schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_metadata_schema**
> ManagementProjectsMetadataSchemasCreateResponseBody create_metadata_schema(project_id, management_projects_metadata_schemas_create_request_body=management_projects_metadata_schemas_create_request_body)

Create Metadata Schema

Creates a new metadata (custom attribute) schema. The schema consists of a set of key-value pairs to customize Voucherify resources.  You can nest your object within a standard metadata schema, e.g. within a campaign or customer schema. However, your nested object cannot include another nested object. The standard metadata schemas are: - Campaign - Voucher - Publication - Redemption - Product - Customer - Order - Order line item - Loyalty Tier - Promotion Tier - Earning rule - Reward  📘 Metadata Documentation  Read the Getting Started with Metadata articles to learn how metadata work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_metadata_schemas_create_request_body import ManagementProjectsMetadataSchemasCreateRequestBody
from voucherify.models.management_projects_metadata_schemas_create_response_body import ManagementProjectsMetadataSchemasCreateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    management_projects_metadata_schemas_create_request_body = voucherify.ManagementProjectsMetadataSchemasCreateRequestBody() # ManagementProjectsMetadataSchemasCreateRequestBody | Defines the metadata schema. (optional)

    try:
        # Create Metadata Schema
        api_response = api_instance.create_metadata_schema(project_id, management_projects_metadata_schemas_create_request_body=management_projects_metadata_schemas_create_request_body)
        print("The response of ManagementApi->create_metadata_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->create_metadata_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **management_projects_metadata_schemas_create_request_body** | [**ManagementProjectsMetadataSchemasCreateRequestBody**](ManagementProjectsMetadataSchemasCreateRequestBody.md)| Defines the metadata schema. | [optional] 

### Return type

[**ManagementProjectsMetadataSchemasCreateResponseBody**](ManagementProjectsMetadataSchemasCreateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the metadata schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> ManagementProjectsCreateResponseBody create_project(management_projects_create_request_body=management_projects_create_request_body)

Create Project

Creates a new project. You can add users, specify the cluster, timezone, currency, and other details. All owners are added to the project by default.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_create_request_body import ManagementProjectsCreateRequestBody
from voucherify.models.management_projects_create_response_body import ManagementProjectsCreateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    management_projects_create_request_body = voucherify.ManagementProjectsCreateRequestBody() # ManagementProjectsCreateRequestBody | Define project details. (optional)

    try:
        # Create Project
        api_response = api_instance.create_project(management_projects_create_request_body=management_projects_create_request_body)
        print("The response of ManagementApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->create_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **management_projects_create_request_body** | [**ManagementProjectsCreateRequestBody**](ManagementProjectsCreateRequestBody.md)| Define project details. | [optional] 

### Return type

[**ManagementProjectsCreateResponseBody**](ManagementProjectsCreateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details of a created project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_stacking_rules**
> ManagementProjectsStackingRulesCreateResponseBody create_stacking_rules(project_id, management_projects_stacking_rules_create_request_body=management_projects_stacking_rules_create_request_body)

Create Stacking Rules

Overwrites the default stacking rules. If new stacking rules have been created for the project earlier (e.g. in the user interface), it returns an error. Use Update Stacking Rules endpoint to change the rules.  📘 Stacking Rules Documentation  Read [the Stacking Rules article](https://support.voucherify.io/article/604-stacking-rules) to learn how they work.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_stacking_rules_create_request_body import ManagementProjectsStackingRulesCreateRequestBody
from voucherify.models.management_projects_stacking_rules_create_response_body import ManagementProjectsStackingRulesCreateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    management_projects_stacking_rules_create_request_body = voucherify.ManagementProjectsStackingRulesCreateRequestBody() # ManagementProjectsStackingRulesCreateRequestBody | Defines the stacking rule parameters. (optional)

    try:
        # Create Stacking Rules
        api_response = api_instance.create_stacking_rules(project_id, management_projects_stacking_rules_create_request_body=management_projects_stacking_rules_create_request_body)
        print("The response of ManagementApi->create_stacking_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->create_stacking_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **management_projects_stacking_rules_create_request_body** | [**ManagementProjectsStackingRulesCreateRequestBody**](ManagementProjectsStackingRulesCreateRequestBody.md)| Defines the stacking rule parameters. | [optional] 

### Return type

[**ManagementProjectsStackingRulesCreateResponseBody**](ManagementProjectsStackingRulesCreateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the stacking rules assigned to the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_webhook**
> ManagementProjectsWebhooksCreateResponseBody create_webhook(project_id, management_projects_webhooks_create_request_body=management_projects_webhooks_create_request_body)

Create Webhook

Creates a new webhook configuration.  📘 Webhook Documentation  Read Webhooks v2024-01-01 article to learn how webhooks work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_webhooks_create_request_body import ManagementProjectsWebhooksCreateRequestBody
from voucherify.models.management_projects_webhooks_create_response_body import ManagementProjectsWebhooksCreateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    management_projects_webhooks_create_request_body = voucherify.ManagementProjectsWebhooksCreateRequestBody() # ManagementProjectsWebhooksCreateRequestBody | Defines a webhook configuration. (optional)

    try:
        # Create Webhook
        api_response = api_instance.create_webhook(project_id, management_projects_webhooks_create_request_body=management_projects_webhooks_create_request_body)
        print("The response of ManagementApi->create_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->create_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **management_projects_webhooks_create_request_body** | [**ManagementProjectsWebhooksCreateRequestBody**](ManagementProjectsWebhooksCreateRequestBody.md)| Defines a webhook configuration. | [optional] 

### Return type

[**ManagementProjectsWebhooksCreateResponseBody**](ManagementProjectsWebhooksCreateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the webhook configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brand**
> delete_brand(project_id, branding_id)

Delete Brand

Deletes permanently a brand configuration.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    branding_id = 'branding_id_example' # str | Provide the unique identifier of the brand configuration.

    try:
        # Delete Brand
        api_instance.delete_brand(project_id, branding_id)
    except Exception as e:
        print("Exception when calling ManagementApi->delete_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **branding_id** | **str**| Provide the unique identifier of the brand configuration. | 

### Return type

void (empty response body)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if the brand configuration has been successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_event_schema**
> delete_custom_event_schema(project_id, custom_event_schema_id)

Delete Custom Event Schema

Deletes permanently the custom event schema with its custom properties (metadata).  📘 Custom Event Documentation  Read [Custom Events](https://support.voucherify.io/article/111-custom-events) article to learn how custom events work in Voucherify. Read also the details about the Track Custom Event endpoint and the Custom Event Object.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    custom_event_schema_id = 'custom_event_schema_id_example' # str | Provide the unique identifier of the custom event schema.

    try:
        # Delete Custom Event Schema
        api_instance.delete_custom_event_schema(project_id, custom_event_schema_id)
    except Exception as e:
        print("Exception when calling ManagementApi->delete_custom_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **custom_event_schema_id** | **str**| Provide the unique identifier of the custom event schema. | 

### Return type

void (empty response body)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if the custom event schema has been successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_metadata_schema**
> delete_metadata_schema(project_id, metadata_schema_id)

Delete Metadata Schema

Deletes permanently the metadata schema. In standard metadata schemas, this endpoint removes permanently all definitions. The standard metadata schemas are: - Campaign - Voucher - Publication - Redemption - Product - Customer - Order - Order line item - Loyalty Tier - Promotion Tier - Earning rule - Reward If you want to delete only one definition, use the Update Metadata Schema endpoint. In the request, provide the deleted: true pair in the definition object. This definition will be moved to Removed definitions. If you want to create a new standard metadata schema, use the Create Metadata Schema endpoint.  🚧 Metadata Purging This endpoint deletes permanently the metadata schemas only. However, it does not purge the metadata from associated entities, so the metadata added to those entities will remain. If you want to purge metadata from the entities: 1. Remove all the definitions you want to purge. You can do this either in Voucherify Project Settings > Metadata Schema tab or with the Update Metadata Schema endpoint. 2. In Voucherify Project Settings > Metadata Schema tab, go to the relevant metadata schema. 3. In Removed definitions, click the bin button next to the definitions whose metadata you want to purge from entities. Note: - This is an asynchronous action. You will be notified when it has been completed. - You cannot purge metadata for the Redemption and Publication schemas. 4. Use the Delete Metadata Schema request to delete the metadata schema from Voucherify.  📘 Metadata Documentation  Read the Getting Started with Metadata articles to learn how metadata work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    metadata_schema_id = 'metadata_schema_id_example' # str | Provide the unique identifier of the metadata schema.

    try:
        # Delete Metadata Schema
        api_instance.delete_metadata_schema(project_id, metadata_schema_id)
    except Exception as e:
        print("Exception when calling ManagementApi->delete_metadata_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **metadata_schema_id** | **str**| Provide the unique identifier of the metadata schema. | 

### Return type

void (empty response body)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if the metadata schema has been successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Delete Project

Deletes an existing project. The users currently using the deleted project will be automatically logged out.  🚧 Sandbox Project The sandbox project cannot be deleted.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.

    try:
        # Delete Project
        api_instance.delete_project(project_id)
    except Exception as e:
        print("Exception when calling ManagementApi->delete_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 

### Return type

void (empty response body)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if deletion is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stacking_rules**
> delete_stacking_rules(project_id, stacking_rules_id)

Delete Stacking Rules

Deletes permanently the current settings for the stacking rules. The stacking rules are restored to default values.  📘 Stacking Rules Documentation  Read [the Stacking Rules article](https://support.voucherify.io/article/604-stacking-rules) to learn how they work.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    stacking_rules_id = 'stacking_rules_id_example' # str | Provide the unique identifier of the stacking rules.

    try:
        # Delete Stacking Rules
        api_instance.delete_stacking_rules(project_id, stacking_rules_id)
    except Exception as e:
        print("Exception when calling ManagementApi->delete_stacking_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **stacking_rules_id** | **str**| Provide the unique identifier of the stacking rules. | 

### Return type

void (empty response body)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if the stacking rules have been successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_webhook**
> delete_webhook(project_id, webhook_id)

Delete Webhook

Deletes a webhook configuration.  📘 Webhook Documentation  Read Webhooks v2024-01-1 article to learn how webhooks work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    webhook_id = 'webhook_id_example' # str | Provide the unique identifier of the webhook configuration.

    try:
        # Delete Webhook
        api_instance.delete_webhook(project_id, webhook_id)
    except Exception as e:
        print("Exception when calling ManagementApi->delete_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **webhook_id** | **str**| Provide the unique identifier of the webhook configuration. | 

### Return type

void (empty response body)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if the webhook configuration has been successfully deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand**
> ManagementProjectsBrandingGetResponseBody get_brand(project_id, branding_id)

Get Brand

Retrieves a brand configuration.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_branding_get_response_body import ManagementProjectsBrandingGetResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    branding_id = 'branding_id_example' # str | Provide the unique identifier of the brand configuration.

    try:
        # Get Brand
        api_response = api_instance.get_brand(project_id, branding_id)
        print("The response of ManagementApi->get_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->get_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **branding_id** | **str**| Provide the unique identifier of the brand configuration. | 

### Return type

[**ManagementProjectsBrandingGetResponseBody**](ManagementProjectsBrandingGetResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the brand configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_event_schema**
> ManagementProjectsCustomEventSchemasGetResponseBody get_custom_event_schema(project_id, custom_event_schema_id)

Get Custom Event Schema

Retrieves a custom event schema.  📘 Custom Event Documentation  Read [Custom Events](https://support.voucherify.io/article/111-custom-events) article to learn how custom events work in Voucherify. Read also the details about the Track Custom Event endpoint and the Custom Event Object.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_custom_event_schemas_get_response_body import ManagementProjectsCustomEventSchemasGetResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    custom_event_schema_id = 'custom_event_schema_id_example' # str | Provide the unique identifier of the custom event schema.

    try:
        # Get Custom Event Schema
        api_response = api_instance.get_custom_event_schema(project_id, custom_event_schema_id)
        print("The response of ManagementApi->get_custom_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->get_custom_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **custom_event_schema_id** | **str**| Provide the unique identifier of the custom event schema. | 

### Return type

[**ManagementProjectsCustomEventSchemasGetResponseBody**](ManagementProjectsCustomEventSchemasGetResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the custom event schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_schema1**
> ManagementProjectsMetadataSchemasGetResponseBody get_metadata_schema1(project_id, metadata_schema_id)

Get Metadata Schema

Retrieves a metadata schema.  📘 Metadata Documentation  Read the Getting Started with Metadata articles to learn how metadata work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_metadata_schemas_get_response_body import ManagementProjectsMetadataSchemasGetResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    metadata_schema_id = 'metadata_schema_id_example' # str | Provide the unique identifier of the metadata schema.

    try:
        # Get Metadata Schema
        api_response = api_instance.get_metadata_schema1(project_id, metadata_schema_id)
        print("The response of ManagementApi->get_metadata_schema1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->get_metadata_schema1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **metadata_schema_id** | **str**| Provide the unique identifier of the metadata schema. | 

### Return type

[**ManagementProjectsMetadataSchemasGetResponseBody**](ManagementProjectsMetadataSchemasGetResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the metadata schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> ManagementProjectsGetResponseBody get_project(project_id)

Get Project

Retrieves an existing project.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_get_response_body import ManagementProjectsGetResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.

    try:
        # Get Project
        api_response = api_instance.get_project(project_id)
        print("The response of ManagementApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->get_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 

### Return type

[**ManagementProjectsGetResponseBody**](ManagementProjectsGetResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details of a project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stacking_rules**
> ManagementProjectsStackingRulesGetResponseBody get_stacking_rules(project_id, stacking_rules_id)

Get Stacking Rules

Retrieves the stacking rules for the project.  📘 Stacking Rules Documentation  Read [the Stacking Rules article](https://support.voucherify.io/article/604-stacking-rules) to learn how they work.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_stacking_rules_get_response_body import ManagementProjectsStackingRulesGetResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    stacking_rules_id = 'stacking_rules_id_example' # str | Provide the unique identifier of the stacking rules.

    try:
        # Get Stacking Rules
        api_response = api_instance.get_stacking_rules(project_id, stacking_rules_id)
        print("The response of ManagementApi->get_stacking_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->get_stacking_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **stacking_rules_id** | **str**| Provide the unique identifier of the stacking rules. | 

### Return type

[**ManagementProjectsStackingRulesGetResponseBody**](ManagementProjectsStackingRulesGetResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the stacking rules for the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> ManagementProjectsUsersGetUserResponseBody get_user(project_id, user_id)

Get User

Retrieves the project users details.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_users_get_user_response_body import ManagementProjectsUsersGetUserResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    user_id = 'user_id_example' # str | Provide the unique identifier of the user. Alternatively, provide the users login.

    try:
        # Get User
        api_response = api_instance.get_user(project_id, user_id)
        print("The response of ManagementApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **user_id** | **str**| Provide the unique identifier of the user. Alternatively, provide the users login. | 

### Return type

[**ManagementProjectsUsersGetUserResponseBody**](ManagementProjectsUsersGetUserResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the project user&#39;s details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook**
> ManagementProjectsWebhooksGetResponseBody get_webhook(project_id, webhook_id)

Get Webhook

Retrieves a webhook configuration.  📘 Webhook Documentation  Read Webhooks v2024-01-1 article to learn how webhooks work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_webhooks_get_response_body import ManagementProjectsWebhooksGetResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    webhook_id = 'webhook_id_example' # str | Provide the unique identifier of the webhook configuration.

    try:
        # Get Webhook
        api_response = api_instance.get_webhook(project_id, webhook_id)
        print("The response of ManagementApi->get_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->get_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **webhook_id** | **str**| Provide the unique identifier of the webhook configuration. | 

### Return type

[**ManagementProjectsWebhooksGetResponseBody**](ManagementProjectsWebhooksGetResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the webhook configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user**
> invite_user(management_projects_users_invite_create_request_body=management_projects_users_invite_create_request_body)

Invite a New User

Sends an invitation to an email address that has not been used yet as a Voucherify user login. You can specify the projects to which the invited user will be assigned and define their roles.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_users_invite_create_request_body import ManagementProjectsUsersInviteCreateRequestBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    management_projects_users_invite_create_request_body = voucherify.ManagementProjectsUsersInviteCreateRequestBody() # ManagementProjectsUsersInviteCreateRequestBody | Defines the details of the invitation, the project, and roles to which the user will be assigned. (optional)

    try:
        # Invite a New User
        api_instance.invite_user(management_projects_users_invite_create_request_body=management_projects_users_invite_create_request_body)
    except Exception as e:
        print("Exception when calling ManagementApi->invite_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **management_projects_users_invite_create_request_body** | [**ManagementProjectsUsersInviteCreateRequestBody**](ManagementProjectsUsersInviteCreateRequestBody.md)| Defines the details of the invitation, the project, and roles to which the user will be assigned. | [optional] 

### Return type

void (empty response body)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if the invitation has been sent successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_brands**
> ManagementProjectsBrandingListResponseBody list_brands(project_id)

List Brands

Lists all brand configurations. Because a project can have only one brand, it always returns a list with one item. This endpoint can be used to retrieve the brand configuration created with the Voucherify Dashboard and the ID.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_branding_list_response_body import ManagementProjectsBrandingListResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.

    try:
        # List Brands
        api_response = api_instance.list_brands(project_id)
        print("The response of ManagementApi->list_brands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_brands: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 

### Return type

[**ManagementProjectsBrandingListResponseBody**](ManagementProjectsBrandingListResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the brand created in the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_custom_event_schemas**
> ManagementProjectsCustomEventSchemasListResponseBody list_custom_event_schemas(project_id)

List Custom Event Schemas

Lists all custom event schemas available in the project.  📘 Custom Event Documentation  Read [Custom Events](https://support.voucherify.io/article/111-custom-events) article to learn how custom events work in Voucherify. Read also the details about the Track Custom Event endpoint and the Custom Event Object.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_custom_event_schemas_list_response_body import ManagementProjectsCustomEventSchemasListResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.

    try:
        # List Custom Event Schemas
        api_response = api_instance.list_custom_event_schemas(project_id)
        print("The response of ManagementApi->list_custom_event_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_custom_event_schemas: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 

### Return type

[**ManagementProjectsCustomEventSchemasListResponseBody**](ManagementProjectsCustomEventSchemasListResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the custom event schemas created in the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metadata_schemas1**
> ManagementProjectsMetadataSchemasListResponseBody list_metadata_schemas1(project_id)

List Metadata Schemas

Lists all metadata schemas available in the project.  📘 Metadata Documentation  Read the Getting Started with Metadata articles to learn how metadata work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_metadata_schemas_list_response_body import ManagementProjectsMetadataSchemasListResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.

    try:
        # List Metadata Schemas
        api_response = api_instance.list_metadata_schemas1(project_id)
        print("The response of ManagementApi->list_metadata_schemas1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_metadata_schemas1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 

### Return type

[**ManagementProjectsMetadataSchemasListResponseBody**](ManagementProjectsMetadataSchemasListResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the metadata schemas created in the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ManagementProjectsListResponseBody list_projects()

List Projects

Lists all projects for the organization. The endpoint does not require any query parameters.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_list_response_body import ManagementProjectsListResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)

    try:
        # List Projects
        api_response = api_instance.list_projects()
        print("The response of ManagementApi->list_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ManagementProjectsListResponseBody**](ManagementProjectsListResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the list of all projects with their details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stacking_rules**
> ManagementProjectsStackingRulesListResponseBody list_stacking_rules(project_id)

List Stacking Rules

Lists all stacking rules. Returns always a list with one item. This endpoint can be used to retrieve the default stacking rules. The default stacking rules do not have an ID that could be used with the Get Stacking Rules or Update Stacking Rules endpoints.  📘 Stacking Rules Documentation  Read [the Stacking Rules article](https://support.voucherify.io/article/604-stacking-rules) to learn how they work.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_stacking_rules_list_response_body import ManagementProjectsStackingRulesListResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.

    try:
        # List Stacking Rules
        api_response = api_instance.list_stacking_rules(project_id)
        print("The response of ManagementApi->list_stacking_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_stacking_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 

### Return type

[**ManagementProjectsStackingRulesListResponseBody**](ManagementProjectsStackingRulesListResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the stacking rules assigned to the project. These can be either the default stacking rules or the created ones. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> ManagementProjectsUsersListResponseBody list_users(project_id)

List Users

Lists all users assigned to the project.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_users_list_response_body import ManagementProjectsUsersListResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.

    try:
        # List Users
        api_response = api_instance.list_users(project_id)
        print("The response of ManagementApi->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 

### Return type

[**ManagementProjectsUsersListResponseBody**](ManagementProjectsUsersListResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the list of all the users assigned to the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks**
> ManagementProjectsWebhooksListResponseBody list_webhooks(project_id)

List Webhooks

Lists all webhook configurations for the project.  📘 Webhook Documentation  Read Webhooks v2024-01-1 article to learn how webhooks work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_webhooks_list_response_body import ManagementProjectsWebhooksListResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.

    try:
        # List Webhooks
        api_response = api_instance.list_webhooks(project_id)
        print("The response of ManagementApi->list_webhooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->list_webhooks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 

### Return type

[**ManagementProjectsWebhooksListResponseBody**](ManagementProjectsWebhooksListResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about webhook configurations created in the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **management_copy_campaign_template**
> ManagementProjectsTemplatesCampaignsCopyCreateResponseBody management_copy_campaign_template(project_id, campaign_template_id, management_projects_templates_campaigns_copy_create_request_body=management_projects_templates_campaigns_copy_create_request_body)

Copy Campaign Template to a Project

Copies a campaign template to another project. The resources, like validation rules or products, will not be copied to the destination project yet. When the template is used to create a new campaign or add a new promotion tier, the resources will be created in the destination project.  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_templates_campaigns_copy_create_request_body import ManagementProjectsTemplatesCampaignsCopyCreateRequestBody
from voucherify.models.management_projects_templates_campaigns_copy_create_response_body import ManagementProjectsTemplatesCampaignsCopyCreateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    campaign_template_id = 'campaign_template_id_example' # str | Provide the unique identifier of the campaign template.
    management_projects_templates_campaigns_copy_create_request_body = voucherify.ManagementProjectsTemplatesCampaignsCopyCreateRequestBody() # ManagementProjectsTemplatesCampaignsCopyCreateRequestBody | Determines the details about the template in the destination project as well as the destination project itself. (optional)

    try:
        # Copy Campaign Template to a Project
        api_response = api_instance.management_copy_campaign_template(project_id, campaign_template_id, management_projects_templates_campaigns_copy_create_request_body=management_projects_templates_campaigns_copy_create_request_body)
        print("The response of ManagementApi->management_copy_campaign_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->management_copy_campaign_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **campaign_template_id** | **str**| Provide the unique identifier of the campaign template. | 
 **management_projects_templates_campaigns_copy_create_request_body** | [**ManagementProjectsTemplatesCampaignsCopyCreateRequestBody**](ManagementProjectsTemplatesCampaignsCopyCreateRequestBody.md)| Determines the details about the template in the destination project as well as the destination project itself. | [optional] 

### Return type

[**ManagementProjectsTemplatesCampaignsCopyCreateResponseBody**](ManagementProjectsTemplatesCampaignsCopyCreateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the copied campaign template. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **management_list_campaign_templates**
> ManagementProjectsTemplatesCampaignsListResponseBody management_list_campaign_templates(project_id, limit=limit, starting_after_id=starting_after_id, order=order, include_total=include_total, filters=filters)

List Campaign Templates

Lists all campaign templates available in the project.  👍 List Campaign Templates  This endpoint works in the same way as the List Campaign Templates endpoint.  📘 Campaign Templates – Documentation Read the [Campaign Templates documentation](https://support.voucherify.io/article/620-campaign-templates) to learn more about this feature.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_templates_campaigns_list_response_body import ManagementProjectsTemplatesCampaignsListResponseBody
from voucherify.models.parameter_filters_list_templates import ParameterFiltersListTemplates
from voucherify.models.parameter_templates_list import ParameterTemplatesList
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the campaign templates created after a template with the given ID. (optional)
    order = voucherify.ParameterTemplatesList() # ParameterTemplatesList | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    include_total = True # bool | If set to true, the response returns the number of all campaign templates, regardless of the applied filters or limits. Set to false by default. (optional)
    filters = voucherify.ParameterFiltersListTemplates() # ParameterFiltersListTemplates | Filters for listing templates. (optional)

    try:
        # List Campaign Templates
        api_response = api_instance.management_list_campaign_templates(project_id, limit=limit, starting_after_id=starting_after_id, order=order, include_total=include_total, filters=filters)
        print("The response of ManagementApi->management_list_campaign_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->management_list_campaign_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the campaign templates created after a template with the given ID. | [optional] 
 **order** | [**ParameterTemplatesList**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **include_total** | **bool**| If set to true, the response returns the number of all campaign templates, regardless of the applied filters or limits. Set to false by default. | [optional] 
 **filters** | [**ParameterFiltersListTemplates**](.md)| Filters for listing templates. | [optional] 

### Return type

[**ManagementProjectsTemplatesCampaignsListResponseBody**](ManagementProjectsTemplatesCampaignsListResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of campaign template objects. The templates are returned by creation date by default. The most recent objects appear last unless specified otherwise with the &#x60;order&#x60; parameter. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unassign_user**
> unassign_user(project_id, user_id)

Unassign User

Unassigns the user from the project. If the user is currently logged in, they are automatically logged out. If the user is assigned to only one project, they cannot be unassigned from that project.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    user_id = 'user_id_example' # str | Provide the unique identifier of the user. Alternatively, provide the users login.

    try:
        # Unassign User
        api_instance.unassign_user(project_id, user_id)
    except Exception as e:
        print("Exception when calling ManagementApi->unassign_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **user_id** | **str**| Provide the unique identifier of the user. Alternatively, provide the users login. | 

### Return type

void (empty response body)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if the user has been successfully unnassigned. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_brand**
> ManagementProjectsBrandingUpdateResponseBody update_brand(project_id, branding_id, management_projects_branding_update_request_body=management_projects_branding_update_request_body)

Update Brand

Updates a brand configuration. Only the fields sent in the request will be updated. The fields omitted in the request will remain unchanged.  📘 White Labelling  The white labelling settings which can be found in Project Settings > Brand Details and which are available only for Enterprise clients as a separate service can be configured only in the user interface.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_branding_update_request_body import ManagementProjectsBrandingUpdateRequestBody
from voucherify.models.management_projects_branding_update_response_body import ManagementProjectsBrandingUpdateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    branding_id = 'branding_id_example' # str | Provide the unique identifier of the brand configuration.
    management_projects_branding_update_request_body = voucherify.ManagementProjectsBrandingUpdateRequestBody() # ManagementProjectsBrandingUpdateRequestBody | Defines the brand configuration to be updated. (optional)

    try:
        # Update Brand
        api_response = api_instance.update_brand(project_id, branding_id, management_projects_branding_update_request_body=management_projects_branding_update_request_body)
        print("The response of ManagementApi->update_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->update_brand: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **branding_id** | **str**| Provide the unique identifier of the brand configuration. | 
 **management_projects_branding_update_request_body** | [**ManagementProjectsBrandingUpdateRequestBody**](ManagementProjectsBrandingUpdateRequestBody.md)| Defines the brand configuration to be updated. | [optional] 

### Return type

[**ManagementProjectsBrandingUpdateResponseBody**](ManagementProjectsBrandingUpdateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the updated brand configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_custom_event_schema**
> ManagementProjectsCustomEventSchemasUpdateResponseBody update_custom_event_schema(project_id, custom_event_schema_id, management_projects_custom_event_schemas_update_request_body=management_projects_custom_event_schemas_update_request_body)

Update Custom Event Schema

Updates a custom event schema. With this request, you can: - Add a non-existing property to a custom event schema. - Update an existing property. In the request, you can provide only those properties you want to add or update. Definitions omitted in the request remain unchanged.  👍 Additional Notes - You can change the type of an existing property, e.g. from string to number. - You can remove a custom property with this endpoint by providing deleted: true in the request. However, you cannot permanently remove an event definition or its property with this endpoint.  📘 Custom Event Documentation  Read [Custom Events](https://support.voucherify.io/article/111-custom-events) article to learn how custom events work in Voucherify. Read also the details about the Track Custom Event endpoint and the Custom Event Object.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_custom_event_schemas_update_request_body import ManagementProjectsCustomEventSchemasUpdateRequestBody
from voucherify.models.management_projects_custom_event_schemas_update_response_body import ManagementProjectsCustomEventSchemasUpdateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    custom_event_schema_id = 'custom_event_schema_id_example' # str | Provide the unique identifier of the custom event schema.
    management_projects_custom_event_schemas_update_request_body = voucherify.ManagementProjectsCustomEventSchemasUpdateRequestBody() # ManagementProjectsCustomEventSchemasUpdateRequestBody | Defines the custom event schema to be updated. (optional)

    try:
        # Update Custom Event Schema
        api_response = api_instance.update_custom_event_schema(project_id, custom_event_schema_id, management_projects_custom_event_schemas_update_request_body=management_projects_custom_event_schemas_update_request_body)
        print("The response of ManagementApi->update_custom_event_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->update_custom_event_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **custom_event_schema_id** | **str**| Provide the unique identifier of the custom event schema. | 
 **management_projects_custom_event_schemas_update_request_body** | [**ManagementProjectsCustomEventSchemasUpdateRequestBody**](ManagementProjectsCustomEventSchemasUpdateRequestBody.md)| Defines the custom event schema to be updated. | [optional] 

### Return type

[**ManagementProjectsCustomEventSchemasUpdateResponseBody**](ManagementProjectsCustomEventSchemasUpdateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the updated custom event schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_metadata_schema**
> ManagementProjectsMetadataSchemasUpdateResponseBody update_metadata_schema(project_id, metadata_schema_id, management_projects_metadata_schemas_update_request_body=management_projects_metadata_schemas_update_request_body)

Update Metadata Schema

Updates a metadata schema. With this request, you can: - Add a non-existing attribute definition to the metadata schema. - Update an existing attribute definition by overwriting its current values. In the request, you can provide only those definitions you want to add or update. Definitions omitted in the request remain unchanged. However, if you want to update a definition, you will have to add all its current key-value pairs as well. Only the pairs sent in the request are saved for this definition. This means that the key-value pairs that are not sent in a request are restored to default values. For example, if your definition has an array with values and it is not sent in an update request, the array values will be deleted.  👍 Additional Notes - You cannot change the type of an existing schema, e.g. from string to number. - You can remove a definition with this endpoint by providing deleted: true in the request. It will be moved to the Removed definitions section in the user interface. However, you cannot permanently remove a definition with this endpoint.  📘 Metadata Documentation  Read the Getting Started with Metadata articles to learn how metadata work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_metadata_schemas_update_request_body import ManagementProjectsMetadataSchemasUpdateRequestBody
from voucherify.models.management_projects_metadata_schemas_update_response_body import ManagementProjectsMetadataSchemasUpdateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    metadata_schema_id = 'metadata_schema_id_example' # str | Provide the unique identifier of the metadata schema.
    management_projects_metadata_schemas_update_request_body = voucherify.ManagementProjectsMetadataSchemasUpdateRequestBody() # ManagementProjectsMetadataSchemasUpdateRequestBody | Defines the metadata schema to be updated. (optional)

    try:
        # Update Metadata Schema
        api_response = api_instance.update_metadata_schema(project_id, metadata_schema_id, management_projects_metadata_schemas_update_request_body=management_projects_metadata_schemas_update_request_body)
        print("The response of ManagementApi->update_metadata_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->update_metadata_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **metadata_schema_id** | **str**| Provide the unique identifier of the metadata schema. | 
 **management_projects_metadata_schemas_update_request_body** | [**ManagementProjectsMetadataSchemasUpdateRequestBody**](ManagementProjectsMetadataSchemasUpdateRequestBody.md)| Defines the metadata schema to be updated. | [optional] 

### Return type

[**ManagementProjectsMetadataSchemasUpdateResponseBody**](ManagementProjectsMetadataSchemasUpdateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the updated metadata schema. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ManagementProjectsUpdateResponseBody update_project(project_id, management_projects_update_request_body=management_projects_update_request_body)

Update Project

Updates an existing project. You can add or modify settings for timezone, currency, notifications, and other details. Only the fields sent in the request will be updated.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_update_request_body import ManagementProjectsUpdateRequestBody
from voucherify.models.management_projects_update_response_body import ManagementProjectsUpdateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    management_projects_update_request_body = voucherify.ManagementProjectsUpdateRequestBody() # ManagementProjectsUpdateRequestBody | Define the project details to be updated. (optional)

    try:
        # Update Project
        api_response = api_instance.update_project(project_id, management_projects_update_request_body=management_projects_update_request_body)
        print("The response of ManagementApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->update_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **management_projects_update_request_body** | [**ManagementProjectsUpdateRequestBody**](ManagementProjectsUpdateRequestBody.md)| Define the project details to be updated. | [optional] 

### Return type

[**ManagementProjectsUpdateResponseBody**](ManagementProjectsUpdateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details of an updated project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stacking_rules**
> ManagementProjectsStackingRulesUpdateResponseBody update_stacking_rules(project_id, stacking_rules_id, management_projects_stacking_rules_update_request_body=management_projects_stacking_rules_update_request_body)

Update Stacking Rules

Updates the stacking rules. Only the provided fields will be updated. However, if you update an array, the content of the array is overwritten. This means that if you want to add new values to an array and retain existing ones, you need to provide both the existing and new values in the request.  📘 Stacking Rules Documentation  Read [the Stacking Rules article](https://support.voucherify.io/article/604-stacking-rules) to learn how they work.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_stacking_rules_update_request_body import ManagementProjectsStackingRulesUpdateRequestBody
from voucherify.models.management_projects_stacking_rules_update_response_body import ManagementProjectsStackingRulesUpdateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    stacking_rules_id = 'stacking_rules_id_example' # str | Provide the unique identifier of the stacking rules.
    management_projects_stacking_rules_update_request_body = voucherify.ManagementProjectsStackingRulesUpdateRequestBody() # ManagementProjectsStackingRulesUpdateRequestBody | Defines the stacking rules to be updated. (optional)

    try:
        # Update Stacking Rules
        api_response = api_instance.update_stacking_rules(project_id, stacking_rules_id, management_projects_stacking_rules_update_request_body=management_projects_stacking_rules_update_request_body)
        print("The response of ManagementApi->update_stacking_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->update_stacking_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **stacking_rules_id** | **str**| Provide the unique identifier of the stacking rules. | 
 **management_projects_stacking_rules_update_request_body** | [**ManagementProjectsStackingRulesUpdateRequestBody**](ManagementProjectsStackingRulesUpdateRequestBody.md)| Defines the stacking rules to be updated. | [optional] 

### Return type

[**ManagementProjectsStackingRulesUpdateResponseBody**](ManagementProjectsStackingRulesUpdateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the updated stacking rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> ManagementProjectsUsersUpdateRoleResponseBody update_user(project_id, user_id, management_projects_users_update_role_request_body=management_projects_users_update_role_request_body)

Update User

Updates the users role.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_users_update_role_request_body import ManagementProjectsUsersUpdateRoleRequestBody
from voucherify.models.management_projects_users_update_role_response_body import ManagementProjectsUsersUpdateRoleResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    user_id = 'user_id_example' # str | Provide the unique identifier of the user. Alternatively, provide the users login.
    management_projects_users_update_role_request_body = voucherify.ManagementProjectsUsersUpdateRoleRequestBody() # ManagementProjectsUsersUpdateRoleRequestBody | Defines the users new role. (optional)

    try:
        # Update User
        api_response = api_instance.update_user(project_id, user_id, management_projects_users_update_role_request_body=management_projects_users_update_role_request_body)
        print("The response of ManagementApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **user_id** | **str**| Provide the unique identifier of the user. Alternatively, provide the users login. | 
 **management_projects_users_update_role_request_body** | [**ManagementProjectsUsersUpdateRoleRequestBody**](ManagementProjectsUsersUpdateRoleRequestBody.md)| Defines the users new role. | [optional] 

### Return type

[**ManagementProjectsUsersUpdateRoleResponseBody**](ManagementProjectsUsersUpdateRoleResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the user assigned to the project. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook**
> ManagementProjectsWebhooksUpdateResponseBody update_webhook(project_id, webhook_id, management_projects_webhooks_update_request_body=management_projects_webhooks_update_request_body)

Update Webhook

Updates a webhook configuration. The events listed in the request are overwritten. If you want to add more events, provide also the events that are already in the webhook configuration.  📘 Webhook Documentation  Read Webhooks v2024-01-1 article to learn how webhooks work in Voucherify.

### Example

* Api Key Authentication (X-Management-Token):
* Api Key Authentication (X-Management-Id):

```python
import voucherify
from voucherify.models.management_projects_webhooks_update_request_body import ManagementProjectsWebhooksUpdateRequestBody
from voucherify.models.management_projects_webhooks_update_response_body import ManagementProjectsWebhooksUpdateResponseBody
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

# Configure API key authorization: X-Management-Token
configuration.api_key['X-Management-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Token'] = 'Bearer'

# Configure API key authorization: X-Management-Id
configuration.api_key['X-Management-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Management-Id'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.ManagementApi(api_client)
    project_id = 'project_id_example' # str | Provide the unique identifier of the project.
    webhook_id = 'webhook_id_example' # str | Provide the unique identifier of the webhook configuration.
    management_projects_webhooks_update_request_body = voucherify.ManagementProjectsWebhooksUpdateRequestBody() # ManagementProjectsWebhooksUpdateRequestBody | Defines the webhook configuration to be updated. (optional)

    try:
        # Update Webhook
        api_response = api_instance.update_webhook(project_id, webhook_id, management_projects_webhooks_update_request_body=management_projects_webhooks_update_request_body)
        print("The response of ManagementApi->update_webhook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManagementApi->update_webhook: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Provide the unique identifier of the project. | 
 **webhook_id** | **str**| Provide the unique identifier of the webhook configuration. | 
 **management_projects_webhooks_update_request_body** | [**ManagementProjectsWebhooksUpdateRequestBody**](ManagementProjectsWebhooksUpdateRequestBody.md)| Defines the webhook configuration to be updated. | [optional] 

### Return type

[**ManagementProjectsWebhooksUpdateResponseBody**](ManagementProjectsWebhooksUpdateResponseBody.md)

### Authorization

[X-Management-Token](../README.md#X-Management-Token), [X-Management-Id](../README.md#X-Management-Id)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the details about the updated webhook configuration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

