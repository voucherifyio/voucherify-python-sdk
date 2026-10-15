# Program

A loyalty program.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique program identifier. | [optional] 
**name** | **str** | Program name. | [optional] 
**status** | **str** | Program status. | [optional] 
**start_date** | **datetime** | Program validity start date (ISO 8601), or &#x60;null&#x60; when not set. | [optional] 
**end_date** | **datetime** | Program validity end date (ISO 8601), or &#x60;null&#x60; when not set. | [optional] 
**validity_hours** | [**ProgramValidityHours**](ProgramValidityHours.md) |  | [optional] 
**metadata** | **object** | Arbitrary key-value metadata. Defaults to &#x60;{}&#x60;. | [optional] 
**created_at** | **datetime** | Creation timestamp (ISO 8601). | [optional] 
**updated_at** | **datetime** | Last update timestamp (ISO 8601), or &#x60;null&#x60; when never updated. | [optional] 
**object** | **str** | Object type marker. | [optional] [default to 'program']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


