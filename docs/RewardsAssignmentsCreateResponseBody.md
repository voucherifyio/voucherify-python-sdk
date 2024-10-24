# RewardsAssignmentsCreateResponseBody

Response body schema for **POST** `v1/rewards/{rewardId}/assignments/`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique reward assignment ID, assigned by Voucherify. | [optional] 
**reward_id** | **str** | Associated reward ID. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the reward assignment was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the reward assignment was updated. The value is shown in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by the JSON. This object stores information about the reward assignment. | [optional] [default to 'reward_assignment']
**related_object_id** | **str** | Related object ID to which the reward was assigned. | [optional] 
**related_object_type** | **str** | Related object type to which the reward was assigned. | [optional] [default to 'campaign']
**parameters** | [**RewardsAssignmentsCreateResponseBodyParameters**](RewardsAssignmentsCreateResponseBodyParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


