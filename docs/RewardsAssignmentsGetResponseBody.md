# RewardsAssignmentsGetResponseBody

Response body schema for **GET** `v1/rewards/{rewardId}/assignments/{assignmentId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique reward assignment ID, assigned by Voucherify. | [optional] 
**reward_id** | **str** | Associated reward ID. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the reward assignment was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the reward assignment was updated. The value is shown in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by the JSON. This object stores information about the reward assignment. | [optional] [default to 'reward_assignment']
**related_object_id** | **str** | Related object ID to which the reward was assigned. For &#x60;related_object_type&#x60; &#x60;campaign&#x60;, this is the campaign ID. For &#x60;referral_tier&#x60;, this is the referral tier ID. | [optional] 
**related_object_type** | **str** | Related object type to which the reward was assigned. Use &#x60;campaign&#x60; for **legacy loyalty** campaign rewards. Use &#x60;referral_tier&#x60; for &#x60;LOYALTY_POINTS&#x60; rewards that credit a &#x60;v2/loyalties&#x60; (loyalty hub) card from a referral tier. A &#x60;LOYALTY_POINTS&#x60; reward can only be assigned to a referral tier. | [optional] [default to 'campaign']
**parameters** | [**RewardsAssignmentsGetResponseBodyParameters**](RewardsAssignmentsGetResponseBodyParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


