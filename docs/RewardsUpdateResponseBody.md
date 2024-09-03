# RewardsUpdateResponseBody

Response body schema for **PUT** `v1/rewards/{rewardId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique reward ID, assigned by Voucherify. | [optional] 
**name** | **str** | Reward name. | [optional] 
**stock** | **int** | Configurable for **material rewards**. The number of units of the product that you want to share as reward. | [optional] 
**redeemed** | **int** | Defines the number of already invoked (successful) reward redemptions.  | [optional] 
**attributes** | [**RewardsUpdateResponseBodyAttributes**](RewardsUpdateResponseBodyAttributes.md) |  | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the reward. A set of key/value pairs that you can attach to a reward object. It can be useful for storing additional information about the reward in a structured format. | [optional] 
**type** | **str** | Reward type. | [optional] 
**parameters** | [**RewardType**](RewardType.md) |  | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the reward was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the reward was updated. The value is shown in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by the JSON. This object stores information about the reward. | [default to 'reward']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


