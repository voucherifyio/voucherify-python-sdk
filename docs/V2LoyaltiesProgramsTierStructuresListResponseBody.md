# V2LoyaltiesProgramsTierStructuresListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/tier-structures`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | Object type marker. | [optional] [default to 'list']
**data** | [**List[ProgramTierStructureAssignment]**](ProgramTierStructureAssignment.md) | Tier structure assignments on the current page. | [optional] 
**cursor** | [**ProgramListCursor**](ProgramListCursor.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


