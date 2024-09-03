# AsyncActionBase

This is an object representing an asynchronous action.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Async action unique ID. | [optional] 
**type** | **str** | Type of async action. | [optional] 
**status** | **str** | Status of the async action. Informs you whether the async action has already been completed. | [optional] 
**operation_status** | **str** | Status of async action processing. Informs about the async action status, whether it failed, succeeded, or the status is unknown. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the async action was scheduled in ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the async action was updated. The value is shown in the ISO 8601 format. | [optional] 
**request_id** | **str** | Unique request ID. | [optional] 
**processing_time** | **int** | The length of time it took to process the request in milliseconds. | [optional] 
**progress** | **int** | % progress to completion of the asynchronous action. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the &#x60;async_action&#x60;. | [optional] [default to 'async_action']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


