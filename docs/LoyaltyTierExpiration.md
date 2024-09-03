# LoyaltyTierExpiration

Defines loyalty tier expiration date.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Unique customer ID of the customer making the purchase. | [optional] 
**campaign_id** | **str** | Unique campaign ID, assigned by Voucherify. | [optional] 
**tier_id** | **str** | Unique tier ID, assigned by Voucherify. | [optional] 
**start_date** | **str** | Activation timestamp defines when the loyalty tier starts to be active in ISO 8601 format. Loyalty tier is inactive before this date. | [optional] 
**expiration_date** | **str** | Expiration timestamp defines when the loyalty tier expires in ISO 8601 format. Loyalty tier is inactive after this date. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the loyalty tier was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the loyalty tier was updated. The value is shown in the ISO 8601 format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


