# LoyaltiesProgramsMembersRewardsPurchasesListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/rewards/purchases`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RewardPurchaseTransaction]**](RewardPurchaseTransaction.md) | Reward purchase transactions (type &#x60;PURCHASE&#x60; only). | [optional] 
**cursor** | **object** |  | [optional] 
**object** | **str** | Object type marker. Always &#x60;list&#x60;. | [optional] [default to 'list']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


