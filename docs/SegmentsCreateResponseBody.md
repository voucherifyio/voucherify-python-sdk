# SegmentsCreateResponseBody

Response body schema for **POST** `v1/segments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique segment ID. | [optional] 
**name** | **str** | Segment name. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the segment was created. The value is shown in the ISO 8601 format. | [optional] 
**type** | **str** | Describes whether the segment is dynamic (customers come in and leave based on set criteria) or static (manually selected customers). | [optional] 
**filter** | **object** | Defines a set of criteria for an &#x60;auto-update&#x60; segment type.   | [optional] 
**initial_sync_status** | **str** |  | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the customer segment. | [optional] [default to 'segment']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


