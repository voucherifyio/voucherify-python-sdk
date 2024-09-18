# EventsCreateResponseBody

Response body schema for **POST** `v1/events`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The object represented is an &#x60;event&#x60;. | [optional] [default to 'event']
**type** | **str** | The event name. | [optional] 
**customer** | [**SimpleCustomerRequiredObjectType**](SimpleCustomerRequiredObjectType.md) |  | 
**referral** | **object** | A &#x60;null&#x60; referral object. | [optional] 
**loyalty** | **object** | A &#x60;null&#x60; loyalty object. | [optional] 
**metadata** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


