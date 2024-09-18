# ProductsUpdateInBulkRequestBody

Request schema for **POST** `v1/products/bulk/async`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_id** | **str** | Unique product source ID from your inventory system. | [optional] 
**name** | **str** | Unique user-defined product name. | [optional] 
**price** | **int** | Unit price. It is represented by a value multiplied by 100 to accurately reflect 2 decimal places, such as &#x60;$100.00&#x60; being expressed as &#x60;10000&#x60;. | [optional] 
**attributes** | **List[str]** | A list of product attributes whose values you can customize for given SKUs: &#x60;[\&quot;color\&quot;,\&quot;size\&quot;,\&quot;ranking\&quot;]&#x60;. Each child SKU can have a unique value for a given attribute. | [optional] 
**image_url** | **str** | The HTTPS URL pointing to the .png or .jpg file that will be used to render the product image. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the product. A set of key/value pairs that you can attach to a product object. It can be useful for storing additional information about the product in a structured format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


