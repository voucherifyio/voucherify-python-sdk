# ProgramRewardAssignment

A reward assigned to a program, with stock configuration and redemption counter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward_id** | **str** | Unique reward identifier. | [optional] 
**stock** | [**ProgramRewardAssignmentStock**](ProgramRewardAssignmentStock.md) |  | 
**redeemed** | **float** | Number of times the reward has been redeemed within the program. Defaults to 0. | [optional] 
**created_at** | **datetime** | Assignment creation timestamp (ISO 8601). | [optional] 
**updated_at** | **datetime** | Last update timestamp (ISO 8601), or &#x60;null&#x60; when never updated. | [optional] 
**object** | **str** | Object type marker. Always &#x60;program_reward&#x60;. | [optional] [default to 'program_reward']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


