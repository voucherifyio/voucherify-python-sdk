# ProductCollectionsProductsListResponseBody

Response body schema for **GET** `v1/product-collections/{productCollectionId}/products`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about products and SKUs. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the JSON property that contains the array of products and SKUs. | [optional] [default to 'data']
**data** | [**List[ProductCollectionsProductsListResponseBodyDataItem]**](ProductCollectionsProductsListResponseBodyDataItem.md) |  | [optional] 
**total** | **int** | Total number of products &amp; SKUs in the product collection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


