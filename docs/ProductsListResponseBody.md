# ProductsListResponseBody

Response body schema for **GET** `v1/products`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about products in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of product objects. | [optional] [default to 'products']
**products** | [**List[Product]**](Product.md) | Contains array of product objects. | [optional] 
**total** | **int** | Total number of product objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


