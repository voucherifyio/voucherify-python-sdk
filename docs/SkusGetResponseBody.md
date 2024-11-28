# SkusGetResponseBody

Response body schema for **GET** `v1/skus/{skuId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier that represents the SKU and is assigned by Voucherify. | [optional] 
**source_id** | **str** | A unique SKU identifier from your inventory system. | [optional] 
**product_id** | **str** | The parent product&#39;s unique ID. | [optional] 
**sku** | **str** | Unique user-defined SKU name. | [optional] 
**price** | **int** | Unit price. It is represented by a value multiplied by 100 to accurately reflect 2 decimal places, such as &#x60;$100.00&#x60; being expressed as &#x60;10000&#x60;. | [optional] 
**currency** | **str** | SKU price currency. | [optional] 
**attributes** | **object** | The attributes object stores values for all custom attributes inherited by the SKU from the parent product. A set of key/value pairs that are attached to a SKU object and are unique to each SKU within a product family. | [optional] 
**image_url** | **str** | The HTTPS URL pointing to the .png or .jpg file that will be used to render the SKU image. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the SKU. A set of key/value pairs that you can attach to a SKU object. It can be useful for storing additional information about the SKU in a structured format. It can be used to create product collections. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the SKU was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the SKU was updated. The value is shown in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the &#x60;SKU&#x60;. | [optional] [default to 'sku']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


