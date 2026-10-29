# V2LoyaltiesRewardsGetResponseBody

Response body schema for **GET** `/v2/loyalties/rewards/{rewardId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique reward identifier, prefixed with &#x60;lrew_&#x60;. | [optional] 
**name** | **str** | Display name of the reward. | [optional] 
**type** | **str** | Reward type. | [optional] 
**status** | **str** | Current lifecycle status of the reward. | [optional] 
**start_date** | **datetime** | Date from which the reward is available, or &#x60;null&#x60; when not set. | [optional] 
**end_date** | **datetime** | Date until which the reward is available, or &#x60;null&#x60; when not set. | [optional] 
**validity_hours** | [**RewardValidityHoursResponse**](RewardValidityHoursResponse.md) |  | 
**material** | [**RewardMaterialResponse**](RewardMaterialResponse.md) |  | [optional] 
**digital** | [**RewardDigitalResponse**](RewardDigitalResponse.md) |  | [optional] 
**refunds** | [**LoyaltyV2ActivityRewardRefunds**](LoyaltyV2ActivityRewardRefunds.md) |  | 
**costs** | [**List[RewardCostResponse]**](RewardCostResponse.md) | Point costs of the reward. Empty array when no costs are defined. | [optional] 
**purchase_limits** | [**RewardPurchaseLimits**](RewardPurchaseLimits.md) |  | 
**metadata** | **object** | Arbitrary key-value metadata attached to the reward. Empty object when not set. | [optional] 
**created_at** | **datetime** | Timestamp when the reward was created (ISO-8601). | [optional] 
**updated_at** | **datetime** | Timestamp when the reward was last updated (ISO-8601), or &#x60;null&#x60; when never updated. | [optional] 
**object** | **str** | Object type marker; always &#x60;reward&#x60;. | [optional] [default to 'reward']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


