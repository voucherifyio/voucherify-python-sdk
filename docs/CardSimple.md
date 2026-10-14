# CardSimple

A loyalty card in its simple representation, as embedded in member responses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | Card type. Currently only &#x60;INDIVIDUAL&#x60; is supported. | [optional] [default to 'INDIVIDUAL']
**lifetime_bucket** | [**CardLifetimeBucket**](CardLifetimeBucket.md) |  | [optional] 
**balance** | [**CardBalance**](CardBalance.md) |  | [optional] 
**id** | **str** | Unique Voucherify ID of the card. | [optional] 
**card_definition_id** | **str** | Unique Voucherify ID of the card definition the card was created from. | [optional] 
**code** | **str** | Human-readable card code. Card code generation is asynchronous - this field is &#x60;null&#x60; right after member creation and is populated shortly after, once the background code generation completes. | [optional] 
**next_expiration** | [**CardNextExpiration**](CardNextExpiration.md) |  | [optional] 
**next_activation** | [**CardNextActivation**](CardNextActivation.md) |  | [optional] 
**object** | **str** | Object type marker, always &#x60;card&#x60;. | [optional] [default to 'card']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


