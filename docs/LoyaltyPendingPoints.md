# LoyaltyPendingPoints

Contains details about the pending point entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the pending point entry, assigned by Voucherify. | [optional] 
**voucher_id** | **str** | Unique identifier of the loyalty card, assigned by Voucherify. | [optional] 
**campaign_id** | **str** | Unique campaign identifier, assigned by Voucherify. | [optional] 
**customer_id** | **str** | Unique customer identifier, assigned by Voucherify. | [optional] 
**order_id** | **str** | Unique order identifier, assigned by Voucherify. | [optional] 
**points** | **int** | Number of points in the pending state. | [optional] 
**activates_at** | **date** | Date when the pending points are activated and added to the customer&#39;s loyalty card. | [optional] 
**details** | [**LoyaltyPendingPointsDetails**](LoyaltyPendingPointsDetails.md) |  | 
**created_at** | **datetime** | Timestamp representing the date and time when the pending point entry was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the pending point entry was modified. The value is shown in the ISO 8601 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


