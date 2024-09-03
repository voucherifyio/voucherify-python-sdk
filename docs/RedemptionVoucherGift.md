# RedemptionVoucherGift

Object representing gift parameters. Child attributes are present only if `type` is `GIFT_VOUCHER`. Defaults to `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | Total gift card income over the lifetime of the card. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000. | [optional] 
**balance** | **int** | Available funds. Value is multiplied by 100 to precisely represent 2 decimal places. For example, $100 amount is written as 10000. | [optional] 
**effect** | **str** | Defines how the credits are applied to the customer&#39;s order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


