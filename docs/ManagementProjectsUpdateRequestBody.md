# ManagementProjectsUpdateRequestBody

Request body schema for **PUT** `/management/v1/projects/{projectId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**api_usage_notifications** | [**ManagementProjectsUpdateRequestBodyApiUsageNotifications**](ManagementProjectsUpdateRequestBodyApiUsageNotifications.md) |  | [optional] 
**webhooks_callout_notifications** | [**ManagementProjectsUpdateRequestBodyWebhooksCalloutNotifications**](ManagementProjectsUpdateRequestBodyWebhooksCalloutNotifications.md) |  | [optional] 
**default_code_config** | [**ManagementProjectsUpdateRequestBodyDefaultCodeConfig**](ManagementProjectsUpdateRequestBodyDefaultCodeConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


