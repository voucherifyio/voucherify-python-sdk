# LoyaltiesExamineEarningRulesExamineRequestBodyOrderItem

A hypothetical order line item used for estimation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order item ID assigned by Voucherify. Can be &#x60;null&#x60;. | [optional] 
**source_id** | **str** | Order item source ID, e.g. from an external system. May be provided as a string or a number. Can be &#x60;null&#x60;. | [optional] 
**product_id** | **str** | Product ID. May be provided as a string or a number. Can be &#x60;null&#x60;. | [optional] 
**sku_id** | **str** | SKU ID. May be provided as a string or a number. Can be &#x60;null&#x60;. | [optional] 
**related_object** | **str** | Whether the item refers to a product or a SKU. Can be &#x60;null&#x60;. | [optional] 
**amount** | **float** | Item amount before discounts - a non-negative integer. May be provided as a string or a number. Can be &#x60;null&#x60;. | [optional] 
**discount_amount** | **float** | Item discount amount - a non-negative integer. May be provided as a string or a number. Can be &#x60;null&#x60;. | [optional] 
**quantity** | **float** | Item quantity - a positive integer. May be provided as a string or a number. Can be &#x60;null&#x60;. | [optional] 
**price** | **float** | Item unit price - a non-negative integer. May be provided as a string or a number. Can be &#x60;null&#x60;. | [optional] 
**product** | [**LoyaltiesExamineEarningRulesExamineRequestBodyOrderItemProduct**](LoyaltiesExamineEarningRulesExamineRequestBodyOrderItemProduct.md) |  | [optional] 
**sku** | [**LoyaltiesExamineEarningRulesExamineRequestBodyOrderItemSku**](LoyaltiesExamineEarningRulesExamineRequestBodyOrderItemSku.md) |  | [optional] 
**metadata** | **object** | Arbitrary key-value metadata; any JSON object is accepted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


