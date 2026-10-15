# Card

A full loyalty card snapshot.

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
**program_id** | **str** | Identifies the loyalty program. | [optional] 
**customer_id** | **str** | Identifies the customer linked to the card. | [optional] 
**member_id** | **str** | Identifies the member linked to the card. | [optional] 
**created_at** | **datetime** | Records when the card was created (ISO 8601). | [optional] 
**updated_at** | **datetime** | Records the last update (ISO 8601). &#x60;null&#x60; if the card has never been updated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


