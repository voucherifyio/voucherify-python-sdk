# MemberActivityDataRedemptionRewardVoucher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**gift** | [**MemberActivityDataRedemptionRewardVoucherGift**](MemberActivityDataRedemptionRewardVoucherGift.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 
**loyalty_card** | [**MemberActivityDataRedemptionRewardVoucherLoyaltyCard**](MemberActivityDataRedemptionRewardVoucherLoyaltyCard.md) |  | [optional] 
**type** | **str** |  | [optional] 
**campaign** | **str** |  | [optional] 
**campaign_id** | **str** |  | [optional] 
**is_referral_code** | **bool** | Flag indicating whether this voucher is a referral code; &#x60;true&#x60; for campaign type &#x60;REFERRAL_PROGRAM&#x60;. | [optional] 
**holder_id** | **str** | Unique customer identifier of the redeemable holder. It equals to the customer ID assigned by Voucherify. | [optional] 
**referrer_id** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**categories** | [**List[Category]**](Category.md) | Contains details about the category. | [optional] 
**active** | **bool** | Shows whether the voucher is on or off. &#x60;true&#x60; indicates an *active* voucher and &#x60;false&#x60; indicates an *inactive* voucher. and A flag to toggle the voucher on or off. You can disable a voucher even though it&#39;s within the active period defined by the &#x60;start_date&#x60; and &#x60;expiration_date&#x60;.    - &#x60;true&#x60; indicates an *active* voucher - &#x60;false&#x60; indicates an *inactive* voucher | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**redemption** | [**MemberActivityDataRedemptionRewardVoucherRedemption**](MemberActivityDataRedemptionRewardVoucherRedemption.md) |  | [optional] 
**start_date** | **str** |  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the code expires in ISO 8601 format.  Voucher is *inactive after* this date. | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to a voucher. The metadata object stores all custom attributes assigned to the voucher. and The metadata object stores all custom attributes assigned to the code. A set of key/value pairs that you can attach to a voucher object. It can be useful for storing additional information about the voucher in a structured format. | [optional] 
**object** | **str** |  | [optional] 
**category** | **str** | Tag defining the category that this voucher belongs to. Useful when listing vouchers using the List Vouchers endpoint. | [optional] 
**validity_timeframe** | [**ValidityTimeframe**](ValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the voucher is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60; Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**validity_hours** | [**ValidityHours**](ValidityHours.md) |  | [optional] 
**additional_info** | **str** | An optional field to keep any extra textual information about the code such as a code description and details. | [optional] 
**assets** | [**VoucherAssets**](VoucherAssets.md) |  | [optional] 
**publish** | [**MemberActivityDataRedemptionRewardVoucherPublish**](MemberActivityDataRedemptionRewardVoucherPublish.md) |  | [optional] 
**validation_rules_assignments** | [**ValidationRulesAssignmentsList**](ValidationRulesAssignmentsList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


