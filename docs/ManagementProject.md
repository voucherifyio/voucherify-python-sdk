# ManagementProject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the project. | [optional] 
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
**webhooks_callout_notifications** | [**ManagementProjectWebhooksCalloutNotifications**](ManagementProjectWebhooksCalloutNotifications.md) |  | [optional] 
**api_usage_notifications** | [**ManagementProjectApiUsageNotifications**](ManagementProjectApiUsageNotifications.md) |  | [optional] 
**cluster_id** | **str** | The identifier of the cluster where the project will be created. | [optional] 
**case_sensitive_codes** | **bool** | Determines if the vouchers in the project will be: - case sensitive - if &#x60;true&#x60;, &#x60;C0dE-cfV&#x60; is **not** equal to &#x60;c0de-cfv&#x60;), - case insensitive - if &#x60;false&#x60;, &#x60;C0dE-cfV&#x60; is equal to &#x60;c0de-cfv&#x60;. | [optional] 
**api_version** | **str** | The API version used in the project. Currently, the default and only value is &#x60;v2018-08-01&#x60;. | [optional] [default to 'v2018-08-01']
**is_sandbox** | **bool** | Determines if the project is a sandbox project. | [optional] 
**webhook_token** | **str** | Webhook token used for authentication. | [optional] 
**default_code_config** | [**ManagementProjectDefaultCodeConfig**](ManagementProjectDefaultCodeConfig.md) |  | [optional] 
**limits** | [**ManagementProjectLimits**](ManagementProjectLimits.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


