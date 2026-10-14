# V2LoyaltiesProgramsRewardsPurchasesRefundResponseBody

Response body schema for **POST** `/v2/loyalties/programs/{programId}/rewards/purchases/{rewardTransactionId}/refund`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction** | [**RewardPurchaseTransaction**](RewardPurchaseTransaction.md) |  | 
**status** | **str** | Result status. Always &#x60;APPROVED&#x60; on success. | [optional] [default to 'APPROVED']
**message** | **str** | Returns the result message: \&quot;Reward refund transaction created. Points will be returned to the member&#39;s card shortly.\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


