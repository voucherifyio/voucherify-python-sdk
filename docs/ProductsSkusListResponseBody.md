# ProductsSkusListResponseBody

Response body schema for **GET** `v1/products/{productId}/skus`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about SKUs. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the JSON property that contains the array of SKUs. | [optional] [default to 'data']
**skus** | [**List[Sku]**](Sku.md) | A dictionary that contains an array of SKUs. | [optional] 
**total** | **int** | Total number of SKUs in the product. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


