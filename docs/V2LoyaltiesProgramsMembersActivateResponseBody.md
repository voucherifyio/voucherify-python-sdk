# V2LoyaltiesProgramsMembersActivateResponseBody

Response body schema for **POST** `/v2/loyalties/programs/{programId}/members/{memberId}/activate`. On success, `status` is always `ACTIVE`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the member. | [optional] 
**customer_id** | **str** | Identifies the enrolled customer. | [optional] 
**program_id** | **str** | Identifies the loyalty program. | [optional] 
**status** | **str** | Current member status. Allowed values: &#x60;ACTIVE&#x60;, &#x60;INACTIVE&#x60;, &#x60;DELETED&#x60;. &#x60;INACTIVE&#x60; members cannot earn points or redeem rewards. | [optional] 
**metadata** | **object** | Stores custom member metadata. Empty object when none is set. | [optional] 
**created_at** | **datetime** | Records when the member was created (ISO 8601). | [optional] 
**updated_at** | **datetime** | Records the last update (ISO 8601). &#x60;null&#x60; if the member has never been updated. | [optional] 
**object** | **str** | Object type. Always &#x60;member&#x60;. | [optional] [default to 'member']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


