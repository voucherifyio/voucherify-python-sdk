# CardTransactionDetails

Card transaction details. Variant-dependent fields are not present on all variants.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Reason for the transaction (e.g. the reason provided in a manual adjustment request). | [optional] 
**rejection** | [**CardTransactionDetailsRejection**](CardTransactionDetailsRejection.md) |  | [optional] 
**metadata** | **object** | Transaction metadata (empty object when none). | [optional] 
**points** | [**CardTransactionDetailsPoints**](CardTransactionDetailsPoints.md) |  | [optional] 
**bucket** | [**LoyaltyV2CardPointsBucketSimple**](LoyaltyV2CardPointsBucketSimple.md) |  | [optional] 
**buckets** | [**List[LoyaltyV2CardPointsBucketSimple]**](LoyaltyV2CardPointsBucketSimple.md) | The points buckets that expired (&#x60;POINTS_EXPIRED&#x60; only). | [optional] 
**var_date** | **date** | Expiration date (&#x60;POINTS_EXPIRED&#x60; only, &#x60;YYYY-MM-DD&#x60;). | [optional] 
**reward** | [**CardTransactionDetailsReward**](CardTransactionDetailsReward.md) |  | [optional] 
**reward_transaction** | [**CardTransactionDetailsRewardTransaction**](CardTransactionDetailsRewardTransaction.md) |  | [optional] 
**card_transaction** | [**CardTransactionDetailsCardTransaction**](CardTransactionDetailsCardTransaction.md) |  | [optional] 
**purchase** | [**CardTransactionDetailsPurchase**](CardTransactionDetailsPurchase.md) |  | [optional] 
**order** | [**CardTransactionDetailsOrder**](CardTransactionDetailsOrder.md) |  | [optional] 
**order_transaction** | [**CardTransactionDetailsOrderTransaction**](CardTransactionDetailsOrderTransaction.md) |  | [optional] 
**target_card** | [**CardTransactionDetailsTargetCard**](CardTransactionDetailsTargetCard.md) |  | [optional] 
**purchase_transaction** | [**CardTransactionDetailsPurchaseTransaction**](CardTransactionDetailsPurchaseTransaction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


