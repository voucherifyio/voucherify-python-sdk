# V2LoyaltiesProgramsMembersListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/members`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Member]**](Member.md) | Members on the current page (without the &#x60;cards&#x60; array). | [optional] 
**cursor** | [**ListCursor**](ListCursor.md) |  | [optional] 
**object** | **str** | Object type marker, always &#x60;list&#x60;. | [optional] [default to 'list']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


