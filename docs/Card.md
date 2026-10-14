# Card

A full loyalty card snapshot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | Card type. Currently only &#x60;INDIVIDUAL&#x60; is supported. | [optional] [default to 'INDIVIDUAL']
**lifetime_bucket** | [**CardLifetimeBucket**](CardLifetimeBucket.md) |  | [optional] 
**balance** | [**CardBalance**](CardBalance.md) |  | [optional] 
**id** | **str** | Identifies the card. | [optional] 
**program_id** | **str** | Identifies the loyalty program. | [optional] 
**card_definition_id** | **str** | Identifies the card definition. | [optional] 
**code** | **str** | Human-readable card code. &#x60;null&#x60; until asynchronous code generation finishes. | [optional] 
**customer_id** | **str** | Identifies the customer linked to the card. | [optional] 
**member_id** | **str** | Identifies the member linked to the card. | [optional] 
**created_at** | **datetime** | Records when the card was created (ISO 8601). | [optional] 
**updated_at** | **datetime** | Records the last update (ISO 8601). &#x60;null&#x60; if the card has never been updated. | [optional] 
**object** | **str** | Object type. Always &#x60;card&#x60;. | [optional] [default to 'card']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


