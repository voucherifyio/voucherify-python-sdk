# OrdersListResponseBody

Response body schema representing **GET** `v1/orders`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about orders in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of order objects. | [optional] [default to 'orders']
**orders** | [**List[OrderCalculated]**](OrderCalculated.md) | Contains array of order objects. | [optional] 
**total** | **int** | Total number of orders. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


