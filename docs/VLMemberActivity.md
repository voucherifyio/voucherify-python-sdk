# VLMemberActivity

An activity recorded for a member.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp when the activity was recorded (ISO 8601). | [optional] 
**group_id** | **str** | ID grouping activities recorded within the same request. | [optional] 
**source** | [**ActivitySource**](ActivitySource.md) |  | [optional] 
**id** | **str** | Unique activity ID. | [optional] 
**member_id** | **str** | ID of the member the activity relates to. | [optional] 
**type** | **str** | Activity type. Allowed values: &#x60;vl.member.created&#x60;, &#x60;vl.member.updated&#x60;, &#x60;vl.member.deleted&#x60;, &#x60;vl.member.activated&#x60;, &#x60;vl.member.deactivated&#x60;, &#x60;vl.member.card.assigned&#x60;, and &#x60;vl.member.card.unassigned&#x60;. | [optional] 
**data** | [**VLMemberActivityData**](VLMemberActivityData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


