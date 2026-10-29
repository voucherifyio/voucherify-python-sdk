# CardSimple

A loyalty card in its simple representation, as embedded in member responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the card. | [optional] 
**card_definition_id** | **str** | Identifies the card definition. | [optional] 
**card_type** | **str** | Card type. Currently only &#x60;INDIVIDUAL&#x60; is supported. | [optional] [default to 'INDIVIDUAL']
**code** | **str** | Human-readable card code. Card code generation is asynchronous - this field is &#x60;null&#x60; right after member creation and is populated shortly after, once the background code generation completes. | [optional] 
**lifetime_bucket** | [**CardLifetimeBucket**](CardLifetimeBucket.md) |  | [optional] 
**balance** | [**CardBalance**](CardBalance.md) |  | [optional] 
**object** | **str** | Object type. Always &#x60;card&#x60;. | [optional] [default to 'card']
**next_expiration** | [**CardNextExpiration**](CardNextExpiration.md) |  | [optional] 
**next_activation** | [**CardNextActivation**](CardNextActivation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


