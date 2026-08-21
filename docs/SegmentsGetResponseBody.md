# SegmentsGetResponseBody

Response body schema for **GET** `v1/segments/{segmentId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique segment ID. | [optional] 
**name** | **str** | Segment name. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the segment was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp in ISO 8601 format indicating when the segment was updated. | [optional] 
**type** | **str** | Defines whether the segment is: - Active (&#x60;auto-update&#x60;): customers enter and leave the segment based on the defined filters and the &#x60;customer.segment.entered&#x60; and &#x60;customer.segment.left&#x60; events are triggered, - Passive (&#x60;passive&#x60;): customers enter and leave the segment based on the defined filters, but the &#x60;customer.segment.entered&#x60; and &#x60;customer.segment.left&#x60; events are not triggered, - Static (&#x60;static&#x60;): manually selected customers. | [optional] 
**filter** | **object** | Defines a set of criteria for an &#x60;auto-update&#x60; or &#x60;passive&#x60; segment type. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the customer segment. | [optional] [default to 'segment']
**initial_sync_status** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


