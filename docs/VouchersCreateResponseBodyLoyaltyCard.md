# VouchersCreateResponseBodyLoyaltyCard

Object representing loyalty card parameters. Child attributes are present only if `type` is `LOYALTY_CARD`. Defaults to `null`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | Total points incurred over the lifespan of the loyalty card. | [optional] 
**balance** | **int** | Points available for reward redemption. | [optional] 
**next_expiration_date** | **date** | The next closest date when the next set of points are due to expire. | [optional] 
**next_expiration_points** | **int** | The amount of points that are set to expire next. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


