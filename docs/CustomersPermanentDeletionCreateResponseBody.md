# CustomersPermanentDeletionCreateResponseBody

Response body schema for **POST** `v1/customers/{customerId}/permanent-deletion`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique permanent deletion object ID. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the customer was requested to be deleted in ISO 8601 format. | [optional] 
**related_object_id** | **str** | Unique customer ID that is being deleted. | [optional] 
**related_object** | **str** | Object being deleted. | [optional] [default to 'customer']
**status** | **str** | Deletion status. | [optional] [default to 'DONE']
**data_json** | [**CustomersPermanentDeletionCreateResponseBodyDataJson**](CustomersPermanentDeletionCreateResponseBodyDataJson.md) |  | [optional] 
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'pernament_deletion']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


