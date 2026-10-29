# CardActivity

An activity recorded for a card.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp when the activity was recorded (ISO 8601). | [optional] 
**group_id** | **str** | ID grouping activities recorded within the same request. | [optional] 
**source** | [**ActivitySource**](ActivitySource.md) |  | [optional] 
**id** | **str** | Unique activity ID. | [optional] 
**card_id** | **str** | ID of the card the activity relates to. | [optional] 
**type** | **str** | Activity type. Allowed values: &#x60;vl.card.created&#x60;, &#x60;vl.card.assigned&#x60;, &#x60;vl.card.unassigned&#x60;, &#x60;vl.card.code_generation.succeeded&#x60;, and &#x60;vl.card.code_generation.failed&#x60;. | [optional] 
**data** | [**CardActivityData**](CardActivityData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


