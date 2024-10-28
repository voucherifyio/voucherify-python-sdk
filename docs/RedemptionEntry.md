# RedemptionEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**var_date** | **datetime** | Timestamp representing the date and time when the object was created. The value is shown in the ISO 8601 format. | [optional] 
**customer_id** | **str** | Unique customer ID of the redeeming customer. | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the redemption. | [optional] 
**amount** | **int** | For gift cards, this is a positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the number of redeemed credits. For loyalty cards, this is the number of loyalty points used in the transaction. and For gift cards, this represents the number of the credits restored to the card in the rolledback redemption. The number is a negative integer in the smallest currency unit, e.g. -100 cents for $1.00 added back to the card. For loyalty cards, this represents the number of loyalty points restored to the card in the rolledback redemption. The number is a negative integer. | [optional] 
**redemption** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**result** | **str** | Redemption result. | [optional] 
**status** | **str** |  | [optional] 
**related_redemptions** | [**RedemptionEntryRelatedRedemptions**](RedemptionEntryRelatedRedemptions.md) |  | [optional] 
**failure_code** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a generic reason as to why the redemption failed. | [optional] 
**failure_message** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a more expanded reason as to why the redemption failed. | [optional] 
**order** | [**RedemptionEntryOrder**](RedemptionEntryOrder.md) |  | [optional] 
**channel** | [**RedemptionEntryChannel**](RedemptionEntryChannel.md) |  | [optional] 
**customer** | [**RedemptionEntryCustomer**](RedemptionEntryCustomer.md) |  | [optional] 
**related_object_type** | **str** | Defines the related object. | [optional] 
**related_object_id** | **str** |  | [optional] 
**promotion_tier** | [**RedemptionEntryPromotionTier**](RedemptionEntryPromotionTier.md) |  | [optional] 
**reward** | [**RedemptionRewardResult**](RedemptionRewardResult.md) |  | [optional] 
**gift** | [**RedemptionEntryGift**](RedemptionEntryGift.md) |  | [optional] 
**loyalty_card** | [**RedemptionEntryLoyaltyCard**](RedemptionEntryLoyaltyCard.md) |  | [optional] 
**voucher** | [**RedemptionEntryVoucher**](RedemptionEntryVoucher.md) |  | [optional] 
**reason** | **str** | System generated cause for the redemption being invalid in the context of the provided parameters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


