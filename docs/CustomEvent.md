# CustomEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique custom event ID. | [optional] 
**object** | **str** | The object represented is an &#x60;event&#x60;. | [optional] [default to 'event']
**type** | **str** | The event name. | [optional] 
**customer** | [**SimpleCustomerRequiredObjectType**](SimpleCustomerRequiredObjectType.md) |  | 
**referral** | [**CustomEventReferral**](CustomEventReferral.md) |  | [optional] 
**loyalty** | [**CustomEventLoyalty**](CustomEventLoyalty.md) |  | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to a customer. The metadata object stores all custom attributes assigned to the customer object. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the custom event was created. The value is shown in the ISO 8601 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


