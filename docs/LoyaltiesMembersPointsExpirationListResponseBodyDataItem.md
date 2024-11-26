# LoyaltiesMembersPointsExpirationListResponseBodyDataItem

Contains the details about expiring loyalty points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the loyalty points bucket. | [optional] 
**voucher_id** | **str** | Unique identifier of the parent loyalty card. | [optional] 
**campaign_id** | **str** | Unique identifier of the parent campaign. | [optional] 
**bucket** | [**LoyaltiesMembersPointsExpirationListResponseBodyDataItemBucket**](LoyaltiesMembersPointsExpirationListResponseBodyDataItemBucket.md) |  | [optional] 
**status** | **str** | Loyalty point point bucket status. | [optional] 
**expires_at** | **datetime** | Date when the number of points defined in the bucket object are due to expire. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the loyalty point bucket object was created in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the loyalty point bucket object was updated in ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the loyalty point bucket. | [optional] [default to 'loyalty_points_bucket']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


