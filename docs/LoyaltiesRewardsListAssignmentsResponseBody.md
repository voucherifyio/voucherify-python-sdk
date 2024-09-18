# LoyaltiesRewardsListAssignmentsResponseBody

Response body schema for **GET** `v1/loyalties/{campaignId}/rewards`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about loyalty reward assignments in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of reward assignment objects. | [optional] [default to 'data']
**data** | [**List[RewardAssignment]**](RewardAssignment.md) | Contains array of reward assignment objects. | [optional] 
**total** | **int** | Total number of reward assignment objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


