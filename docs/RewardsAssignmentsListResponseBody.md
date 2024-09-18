# RewardsAssignmentsListResponseBody

Response body schema for **GET** `v1/rewards/{rewardID}/assignments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about reward assignments in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of reward assignments. | [optional] [default to 'data']
**data** | [**List[RewardAssignment]**](RewardAssignment.md) |  | [optional] 
**total** | **int** | Total number of reward assignments. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


