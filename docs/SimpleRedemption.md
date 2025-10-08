# SimpleRedemption

Simplified redemption data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique redemption ID. | [optional] 
**customer_id** | **str** | Unique customer ID of the redeeming customer. | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**var_date** | **datetime** | Timestamp representing the date and time when the redemption was created in the ISO 8601 format. | [optional] 
**amount** | **int** | For gift cards, this is a positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the number of redeemed credits. For loyalty cards, this is the number of loyalty points used in the transaction. In the case of redemption rollback, the numbers are expressed as negative integers. | [optional] 
**order** | [**SimpleOrder**](SimpleOrder.md) |  | [optional] 
**reward** | [**SimpleRedemptionRewardResult**](SimpleRedemptionRewardResult.md) |  | [optional] 
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**result** | **str** | Redemption result. | [optional] 
**status** | **str** |  | [optional] 
**voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**promotion_tier** | [**SimplePromotionTier**](SimplePromotionTier.md) |  | [optional] 
**redemption** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes in the form of key/value pairs assigned to the redemption. | [optional] 
**failure_code** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a generic reason as to why the redemption failed. | [optional] 
**failure_message** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide an expanded reason as to why the redemption failed. | [optional] 
**reason** | **str** | The reason for the redemption rollback. | [optional] 
**channel** | [**SimpleRedemptionChannel**](SimpleRedemptionChannel.md) |  | [optional] 
**object** | **str** | The type of the object represented by the JSON. This object stores information about the &#x60;redemption&#x60;. | [optional] [default to 'redemption']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


