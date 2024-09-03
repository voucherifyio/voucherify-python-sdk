# ClientValidationsValidateRequestBodyRedeemablesItemReward

Contains information about the reward that the customer wants to redeem and the number of points the customer is choosing to use for the reward.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique reward ID assigned by Voucherify. The reward must be assigned to the campaign in order for the user to be able to use the reward. | [optional] 
**points** | **int** | The number of loyalty points that the user wants to spend in order to fulfill the order using a **pay with points** reward. The number of points cannot be higher than the current balance on the loyalty card. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


