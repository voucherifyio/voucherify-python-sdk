# RewardPurchaseDigitalGiftVoucher

Gift voucher fulfillment entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Voucher identifier of the gift voucher. | [optional] 
**code** | **str** | Gift voucher code. | [optional] 
**amount** | **float** | Amount added to (or, for refunds, subtracted from) the gift voucher balance. | [optional] 
**balance** | **float** | Gift voucher balance after the operation. | [optional] 
**result** | **str** | Refund handling result for this gift voucher (present in refund results):  - &#x60;CREDITS_SUBTRACTED&#x60;: The credited balance was subtracted.  - &#x60;SKIPPED&#x60;: The voucher was left intact. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


