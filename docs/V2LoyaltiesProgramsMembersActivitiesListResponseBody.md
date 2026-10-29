# V2LoyaltiesProgramsMembersActivitiesListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/members/{memberId}/activities`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VLMemberActivity]**](VLMemberActivity.md) | Member activities on the current page. | [optional] 
**cursor** | [**ListCursor**](ListCursor.md) |  | [optional] 
**object** | **str** | Object type marker, always &#x60;list&#x60;. | [optional] [default to 'list']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


