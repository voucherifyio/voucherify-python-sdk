# V2LoyaltiesProgramsRewardsListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/rewards`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Object type marker. Always &#x60;list&#x60;. | [optional] [default to 'list']
**data** | [**List[ProgramRewardAssignment]**](ProgramRewardAssignment.md) | Reward assignments on the current page. | [optional] 
**cursor** | [**ProgramListCursor**](ProgramListCursor.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


