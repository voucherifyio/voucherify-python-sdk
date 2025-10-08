# MemberActivityDataRedemptionVoucherLoyaltyCard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **int** | Total number of points added to the loyalty card over its lifespan. | [optional] 
**balance** | **int** | Points available for reward redemption. This is calculated as follows: &#x60;balance&#x60; &#x3D; &#x60;points&#x60; - &#x60;expired_points&#x60; - &#x60;subtracted_points&#x60; - &#x60;redemption.redeemed_points&#x60;. | [optional] 
**next_expiration_date** | **str** |  | [optional] 
**next_expiration_points** | **int** | The amount of points that are set to expire next. | [optional] 
**pending_points** | **int** | Shows the number of pending points that will be added to the loyalty card when they are activated automatically or manually. | [optional] 
**expired_points** | **int** | Shows the total number of expired points over the lifetime of the loyalty card. | [optional] 
**subtracted_points** | **int** | Shows the total number of subtracted points over the lifetime of the loyalty card. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


