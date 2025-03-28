# RedeemableLoyaltyCard

Redeemable loyalty card object response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | Total points incurred over the lifespan of the loyalty card, minus the expired points. | [optional] 
**balance** | **int** | Points available for reward redemption. | [optional] 
**exchange_ratio** | **float** | The cash equivalent of the points defined in the points_ratio property. | [optional] 
**points_ratio** | **int** | The number of loyalty points that will map to the predefined cash amount defined by the exchange_ratio property. | [optional] 
**transfers** | [**List[LoyaltiesTransferPoints]**](LoyaltiesTransferPoints.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


