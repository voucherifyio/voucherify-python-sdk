# RedemptionsRollbackCreateResponseBody

Response body schema for **POST** `v1/redemptions/{redemptionId}/rollback`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the redemption rollback. | [optional] 
**object** | **str** | The type of the object represented by the JSON | [optional] [default to 'redemption_rollback']
**var_date** | **datetime** | Timestamp representing the date and time when the object was created. The value is shown in the ISO 8601 format. | [optional] 
**customer_id** | **str** | Unique customer ID of the redeeming customer. | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the redemption. | [optional] 
**amount** | **int** | For gift cards, this represents the number of the credits restored to the card in the rolledback redemption. The number is a negative integer in the smallest currency unit, e.g. -100 cents for $1.00 added back to the card. For loyalty cards, this represents the number of loyalty points restored to the card in the rolledback redemption. The number is a negative integer. | [optional] 
**redemption** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**reason** | **str** | System generated cause for the redemption being invalid in the context of the provided parameters. | [optional] 
**result** | **str** | Redemption result. | [optional] 
**status** | **str** | Redemption status. | [optional] 
**related_redemptions** | [**RedemptionsRollbackCreateResponseBodyRelatedRedemptions**](RedemptionsRollbackCreateResponseBodyRelatedRedemptions.md) |  | [optional] 
**failure_code** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a generic reason as to why the redemption failed. | [optional] 
**failure_message** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a more expanded reason as to why the redemption failed. | [optional] 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**channel** | [**RedemptionsRollbackCreateResponseBodyChannel**](RedemptionsRollbackCreateResponseBodyChannel.md) |  | [optional] 
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**related_object_type** | **str** | Defines the related object. | [optional] 
**related_object_id** | **str** | Unique identifier of the related object. It is assigned by Voucherify, i.e. &#x60;v_lfZi4rcEGe0sN9gmnj40bzwK2FH6QUno&#x60; for a voucher. | [optional] 
**voucher** | [**Voucher**](Voucher.md) |  | [optional] 
**promotion_tier** | [**PromotionTier**](PromotionTier.md) |  | [optional] 
**reward** | [**RedemptionRewardResult**](RedemptionRewardResult.md) |  | [optional] 
**gift** | [**RedemptionsRollbackCreateResponseBodyGift**](RedemptionsRollbackCreateResponseBodyGift.md) |  | [optional] 
**loyalty_card** | [**RedemptionsRollbackCreateResponseBodyLoyaltyCard**](RedemptionsRollbackCreateResponseBodyLoyaltyCard.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


