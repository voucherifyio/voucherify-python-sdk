# Order

Order information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique ID assigned by Voucherify of an existing order that will be linked to the redemption of this request. | [optional] 
**source_id** | **str** | Unique source ID of an existing order that will be linked to the redemption of this request. | [optional] 
**status** | **str** | The order status. | [optional] 
**amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. | [optional] 
**initial_amount** | **int** | A positive integer in the smallest currency unit (e.g. 100 cents for $1.00) representing the total amount of the order. This is the sum of the order items&#39; amounts. | [optional] 
**discount_amount** | **int** | Sum of all order-level discounts applied to the order. It is expressed as an integer in the smallest currency unit (e.g. 100 cents for $1.00). | [optional] 
**items** | [**List[OrderItem]**](OrderItem.md) | Array of items applied to the order. It can include up to 500 items. | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to an order. It can be useful for storing additional information about the order in a structured format. It can be used to define business validation rules or discount formulas. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


