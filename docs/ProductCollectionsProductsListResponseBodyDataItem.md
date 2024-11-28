# ProductCollectionsProductsListResponseBodyDataItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**source_id** | **str** |  | [optional] 
**name** | **str** | Unique user-defined product name. | [optional] 
**price** | **int** | Unit price. It is represented by a value multiplied by 100 to accurately reflect 2 decimal places, such as &#x60;$100.00&#x60; being expressed as &#x60;10000&#x60;. | [optional] 
**attributes** | **List[str]** | A list of product attributes whose values you can customize for given SKUs: &#x60;[\&quot;color\&quot;,\&quot;size\&quot;,\&quot;ranking\&quot;]&#x60;. Each child SKU can have a unique value for a given attribute. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the product. A set of key/value pairs that you can attach to a product object. It can be useful for storing additional information about the product in a structured format. It can be used to create product collections. and The metadata object stores all custom attributes assigned to the SKU. A set of key/value pairs that you can attach to a SKU object. It can be useful for storing additional information about the SKU in a structured format. It can be used to create product collections. | [optional] 
**image_url** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**product_id** | **str** | The parent product&#39;s unique ID. | [optional] 
**sku** | **str** | Unique user-defined SKU name. | [optional] 
**currency** | **str** | SKU price currency. | [optional] 
**product** | [**ProductWithoutSkus**](ProductWithoutSkus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


