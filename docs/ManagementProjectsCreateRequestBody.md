# ManagementProjectsCreateRequestBody

Request body schema for **POST** `/management/v1/projects`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_sensitive_codes** | **bool** | Determines if the vouchers in the project will be case sensitive (if &#x60;true&#x60;, &#x60;C0dE-cfV&#x60; is not equal to &#x60;c0de-cfv&#x60;) or case insensitive (if false, &#x60;C0dE-cfV&#x60; is equal to &#x60;c0de-cfv&#x60;). | [optional] 
**name** | **str** | The name of the project. | [optional] 
**description** | **str** | A user-defined description of the project, e.g. its purpose, scope, region. | [optional] 
**timezone** | **str** | The time zone in which the project is established. It can be in the GMT format or in accordance with IANA time zone database. | [optional] 
**currency** | **str** | The currency used in the project. It is equal to a 3-letter ISO 4217 code. | [optional] 
**dial_code** | **str** | The country dial code for the project. It is equal to an ITU country code. | [optional] 
**webhook_version** | **str** | The webhook version used in the project. | [optional] [default to 'v2024-01-01']
**client_trusted_domains** | **List[str]** | An array of URL addresses that allow client requests. | [optional] 
**client_redeem_enabled** | **bool** | Enables client-side redemption. | [optional] 
**client_publish_enabled** | **bool** | Enables client-side publication. | [optional] 
**client_list_vouchers_enabled** | **bool** | Enables client-side listing of vouchers. | [optional] 
**client_create_customer_enabled** | **bool** | Enables client-side creation of customers. | [optional] 
**client_loyalty_events_enabled** | **bool** | Enables client-side events for loyalty and referral programs. | [optional] 
**client_set_voucher_expiration_date_enabled** | **bool** | Enables client-side setting of voucher expiration date. | [optional] 
**api_usage_notifications** | [**ManagementProjectsCreateRequestBodyApiUsageNotifications**](ManagementProjectsCreateRequestBodyApiUsageNotifications.md) |  | [optional] 
**webhooks_callout_notifications** | [**ManagementProjectsCreateRequestBodyWebhooksCalloutNotifications**](ManagementProjectsCreateRequestBodyWebhooksCalloutNotifications.md) |  | [optional] 
**cluster_id** | **str** | The identifier of the cluster where the project will be created. The default cluster is &#x60;eu1&#x60; unless otherwise configured. | [optional] 
**api_version** | **str** | The API version used in the project. Currently, the default and only value is &#x60;v2018-08-01&#x60;. | [optional] [default to 'v2018-08-01']
**users** | [**List[ManagementProjectsCreateRequestBodyUsersItem]**](ManagementProjectsCreateRequestBodyUsersItem.md) | The users (their identifiers, logins, and roles) who will be assigned to the project. You can assign only existing Voucherify users.  It must be used either in the following combinations: - &#x60;id&#x60; and &#x60;role&#x60;, or - &#x60;login&#x60; and &#x60;role&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


