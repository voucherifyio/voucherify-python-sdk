# ProductCollectionsListResponseBody

Response body schema for **GET** `v1/product-collections`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about product collections. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the JSON property that contains the array of product collections. | [optional] [default to 'data']
**data** | [**List[ProductCollectionsItem]**](ProductCollectionsItem.md) | A dictionary that contains an array of product collections and their details. | [optional] 
**total** | **int** | Total number of product collections. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


