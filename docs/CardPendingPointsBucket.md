# CardPendingPointsBucket

A pending point bucket of a card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | ID of the card the bucket belongs to. | [optional] 
**card_definition_id** | **str** | ID of the card definition of the card. | [optional] 
**program_id** | **str** | ID of the loyalty program. | [optional] 
**member_id** | **str** | ID of the member owning the card. | [optional] 
**card_type** | **str** | Card type. Currently, only &#x60;INDIVIDUAL&#x60; is supported. | [optional] [default to 'INDIVIDUAL']
**created_at** | **datetime** | Timestamp when the bucket was created (ISO 8601). | [optional] 
**updated_at** | **datetime** | Timestamp when the bucket was last updated (ISO 8601), or &#x60;null&#x60;. | [optional] 
**id** | **str** | Unique pending point bucket ID. | [optional] 
**points** | [**CardPendingPointsBucketPoints**](CardPendingPointsBucketPoints.md) |  | [optional] 
**var_date** | **date** | Scheduled activation date of the pending points (&#x60;YYYY-MM-DD&#x60;). For the &#x60;EVENT_BASED&#x60; type this is the cancellation deadline. | [optional] 
**type** | **str** | Pending points activation type from the card definition. | [optional] 
**status** | **str** | Bucket status. | [optional] 
**object** | **str** | Object type marker, always &#x60;card_pending_points_bucket&#x60;. | [optional] [default to 'card_pending_points_bucket']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


