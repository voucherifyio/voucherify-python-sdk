# LoyaltiesMembersPointsExpirationListResponseBodyDataItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique loyalty points bucket ID. | 
**voucher_id** | **str** | Unique parent loyalty card ID. | 
**campaign_id** | **str** |  Unique parent campaign ID. | 
**bucket** | [**LoyaltiesMembersPointsExpirationListResponseBodyDataItemBucket**](LoyaltiesMembersPointsExpirationListResponseBodyDataItemBucket.md) |  | 
**created_at** | **datetime** | Timestamp representing the date and time when the loyalty points bucket object was created. The value is shown in the ISO 8601 format. | 
**status** | **str** | Loyalty points bucket point status. | 
**expires_at** | **datetime** | Date when the number of points defined in the bucket object are due to expire. | 
**updated_at** | **datetime** | Timestamp representing the date and time when the loyalty points bucket object was updated. The value is shown in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the loyalty points bucket. | [default to 'loyalty_points_bucket']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


