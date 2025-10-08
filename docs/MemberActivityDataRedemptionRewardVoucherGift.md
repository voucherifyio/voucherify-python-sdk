# MemberActivityDataRedemptionRewardVoucherGift


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Total gift card income over the lifetime of the card. The value is multiplied by 100 to represent 2 decimal places. For example &#x60;10000 cents&#x60; for &#x60;$100.00&#x60;. | [optional] 
**subtracted_amount** | **int** | Total amount of subtracted credits over the gift card lifetime. and Total amount of subtracted credits over the gift card lifetime. The value is multiplied by 100 to represent 2 decimal places. For example &#x60;10000 cents&#x60; for &#x60;$100.00&#x60;. | [optional] 
**balance** | **float** | Available funds. The value is multiplied by 100 to represent 2 decimal places. For example &#x60;10000 cents&#x60; for &#x60;$100.00&#x60;. &#x60;balance&#x60; &#x3D; &#x60;amount&#x60; - &#x60;subtracted_amount&#x60; - &#x60;redemption.redeemed_amount&#x60;. | [optional] 
**effect** | **str** | Defines how the credits are applied to the customer&#39;s order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


