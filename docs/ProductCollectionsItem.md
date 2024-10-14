# ProductCollectionsItem

This is an object representing a product collection base. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Product collection ID. | [optional] 
**name** | **str** | Unique user-defined product collection name. | [optional] 
**type** | **str** | Describes whether the product collection is dynamic (products come in and leave based on set criteria) or static (manually selected products). | [optional] 
**filter** | **object** | Defines a set of criteria and boundary conditions for an &#x60;AUTO_UPDATE&#x60; product collection type. | [optional] 
**products** | [**List[ProductCollectionsItemProductsItem]**](ProductCollectionsItemProductsItem.md) | Defines a set of products for a &#x60;STATIC&#x60; product collection type. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the product collection was created. The value is shown in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the static product collection. | [optional] [default to 'products_collection']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


