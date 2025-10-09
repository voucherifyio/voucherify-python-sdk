# MemberActivityDataRedemption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique redemption ID. | [optional] 
**customer_id** | **str** | Unique customer ID of the redeeming customer. | [optional] 
**tracking_id** | **str** | Hashed customer source ID. | [optional] 
**var_date** | **datetime** | Timestamp representing the date and time when the redemption was created in the ISO 8601 format. | [optional] 
**amount** | **int** | For gift cards, this is a positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the number of redeemed credits. For loyalty cards, this is the number of loyalty points used in the transaction. In the case of redemption rollback, the numbers are expressed as negative integers. and For gift cards, this is a positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the number of redeemed credits. For loyalty cards, this is the number of loyalty points used in the transaction. | [optional] 
**order** | [**MemberActivityDataRedemptionOrder**](MemberActivityDataRedemptionOrder.md) |  | [optional] 
**reward** | [**MemberActivityDataRedemptionReward**](MemberActivityDataRedemptionReward.md) |  | [optional] 
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**result** | **str** | Redemption result. | [optional] 
**status** | **str** |  | [optional] 
**voucher** | [**MemberActivityDataRedemptionVoucher**](MemberActivityDataRedemptionVoucher.md) |  | [optional] 
**promotion_tier** | [**MemberActivityDataRedemptionPromotionTier**](MemberActivityDataRedemptionPromotionTier.md) |  | [optional] 
**redemption** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes in the form of key/value pairs assigned to the redemption. and The metadata object stores all custom attributes assigned to the redemption. | [optional] 
**failure_code** | **str** | If the result is &#x60;FAILURE&#x60;, this parameter will provide a generic reason as to why the redemption failed. | [optional] 
**failure_message** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**channel** | [**MemberActivityDataRedemptionChannel**](MemberActivityDataRedemptionChannel.md) |  | [optional] 
**object** | **str** | The type of the object represented by the JSON. This object stores information about the &#x60;redemption&#x60;. | [optional] [default to 'redemption']
**created_at** | **datetime** | Timestamp representing the date and time when the redemption was created. The value is shown in the ISO 8601 format. | [optional] 
**channel_type** | **str** | The source of the channel for the redemption rollback. A &#x60;USER&#x60; corresponds to the Voucherify Dashboard and an &#x60;API&#x60; corresponds to the API. | [optional] 
**channel_id** | **str** | Unique channel ID of the user performing the redemption. This is either a user ID from a user using the Voucherify Dashboard or an X-APP-Id of a user using the API. | [optional] 
**previous_order** | [**MemberActivityDataRedemptionPreviousOrder**](MemberActivityDataRedemptionPreviousOrder.md) |  | [optional] 
**related_redemptions** | [**MemberActivityDataRedemptionRelatedRedemptions**](MemberActivityDataRedemptionRelatedRedemptions.md) |  | [optional] 
**parent_redemption_id** | **str** | Unique redemption ID of the parent redemption. | [optional] 
**related_object_type** | **str** | Defines the related object. | [optional] 
**related_object_id** | **str** | Unique related object ID assigned by Voucherify, i.e. v_lfZi4rcEGe0sN9gmnj40bzwK2FH6QUno for a voucher. | [optional] 
**related_object_parent_id** | **str** | Unique related parent object ID assigned by Voucherify, i.e. v_lfZi4rcEGe0sN9gmnj40bzwK2FH6QUno for a voucher. | [optional] 
**campaign_name** | **str** | Campaign name | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


