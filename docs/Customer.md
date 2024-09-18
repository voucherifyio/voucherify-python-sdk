# Customer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of an existing customer. | [optional] 
**source_id** | **str** | A unique identifier of the customer who validates a voucher. It can be a customer ID or email from a CRM system, database, or a third-party service. If you also pass a customer ID (unique ID assigned by Voucherify), the source ID will be ignored. | [optional] 
**name** | **str** | Customer&#39;s first and last name. | [optional] 
**description** | **str** | An arbitrary string that you can attach to a customer object. | [optional] 
**email** | **str** | Customer&#39;s email address. | [optional] 
**phone** | **str** | Customer&#39;s phone number. This parameter is mandatory when you try to send out codes to customers via an SMS channel. | [optional] 
**birthday** | **date** | &#x60;Deprecated&#x60;. ~~Customer&#39;s birthdate; format YYYY-MM-DD~~. | [optional] 
**birthdate** | **date** | Customer&#39;s birthdate; format YYYY-MM-DD. | [optional] 
**address** | [**CustomerAddress**](CustomerAddress.md) |  | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to a customer. The metadata object stores all custom attributes assigned to the customer. It can be useful for storing additional information about the customer in a structured format. This metadata can be used for validating whether the customer qualifies for a discount or it can be used in building customer segments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


