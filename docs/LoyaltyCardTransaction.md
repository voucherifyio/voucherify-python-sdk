# LoyaltyCardTransaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique transaction ID. | [optional] 
**source_id** | **str** | The merchant&#39;s transaction ID if it is different from the Voucherify transaction ID. It is really useful in case of an integration between multiple systems. It can be a transaction ID from a CRM system, database or 3rd-party service. In case of a redemption, this value is null. | [optional] 
**voucher_id** | **str** | Unique voucher ID. | [optional] 
**campaign_id** | **str** | Unqiue campaign ID of the voucher&#39;s parent campaign if it is part of campaign that generates bulk codes. | [optional] 
**source** | **str** | The channel through which the transaction took place, whether through the API or the the Dashboard. In case of a redemption, this value is null. | [optional] 
**reason** | **str** | Reason why the transaction occurred. In case of a redemption, this value is null. | [optional] 
**related_transaction_id** | **str** | The related transaction ID on the receiving card. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the transaction was created. The value is shown in the ISO 8601 format. | [optional] 
**details** | [**LoyaltyCardTransactionDetails**](LoyaltyCardTransactionDetails.md) |  | [optional] 
**type** | [**LoyaltyCardTransactionsType**](LoyaltyCardTransactionsType.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


