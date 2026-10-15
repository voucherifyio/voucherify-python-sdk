# CardPointsBucket

A points expiration bucket of a card.

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
**id** | **str** | Unique points expiration bucket ID. | [optional] 
**customer_id** | **str** | Voucherify ID of the customer owning the card. | [optional] 
**points** | [**CardPointsBucketPoints**](CardPointsBucketPoints.md) |  | [optional] 
**expiration_date** | **date** | Date when the points in the bucket expire (&#x60;YYYY-MM-DD&#x60;). | [optional] 
**expiration_type** | **str** | Points expiration type for the bucket. It can be inherited from the card definition or overridden by the earning rule. | [optional] 
**status** | **str** | Bucket status. For the List card expiring points buckets, returns only &#x60;ACTIVE&#x60; buckets. | [optional] 
**object** | **str** | Object type marker, always &#x60;card_points_bucket&#x60;. | [optional] [default to 'card_points_bucket']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


