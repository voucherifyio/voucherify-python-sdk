# AsyncActionsListResponseBody

Response body schema for **GET** `v1/async-actions`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about asynchronous actions. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the JSON property that contains the array of asynchronous actions. | [optional] [default to 'async_actions']
**async_actions** | [**List[AsyncActionBase]**](AsyncActionBase.md) |  | [optional] 
**has_more** | **bool** | As query results are always limited by parameters, the &#x60;has_more&#x60; flag indicates if there are more records available. This lets you know if you can run another request to get more records returned in the results. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


