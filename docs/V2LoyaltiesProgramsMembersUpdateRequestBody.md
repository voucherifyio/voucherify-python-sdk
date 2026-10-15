# V2LoyaltiesProgramsMembersUpdateRequestBody

Request body schema for **PUT** `/v2/loyalties/programs/{programId}/members/{memberId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** | Member metadata to apply. Object keys are merged into existing metadata (omitted keys are preserved). Validated against the &#x60;vl_member&#x60; metadata schema when configured. Pass &#x60;null&#x60; to clear all metadata. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


