# CustomerRedeemable

Single customer's redeemable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique redeemable holder identifier. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the redeemable was assigned. The value is shown in the ISO 8601 format. | [optional] 
**redeemable_id** | **str** | Identifier of the redeemable item. | [optional] 
**redeemable_object** | **str** | Type of the redeemable. | [optional] 
**customer_id** | **str** | Identifier of the customer. | [optional] 
**holder_role** | **str** | Role of the holder. | [optional] [default to 'OWNER']
**campaign_id** | **str** | Unique campaign identifier, assigned by Voucherify. | [optional] 
**campaign_type** | **str** | Defines the type of the campaign. | [optional] [default to 'DISCOUNT_COUPONS']
**voucher_type** | **str** | Defines the type of the voucher. | [optional] [default to 'DISCOUNT_VOUCHER']
**redeemable** | [**CustomerRedeemableRedeemable**](CustomerRedeemableRedeemable.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


