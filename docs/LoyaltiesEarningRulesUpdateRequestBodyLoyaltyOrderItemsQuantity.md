# LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderItemsQuantity

Defines the ratio based on the property defined in the calculation_type parameter. For every set of value (1, 10, etc) defined in the every parameter for the property defined in calculation_type, give the customer the number of points defined in the points parameter. In other words, for every calculation_type, give points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**every** | **int** | Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $10 order amount is written as 1000. | [optional] 
**points** | **int** | Number of points to be awarded, i.e. how many points to be added to the loyalty card. | [optional] 
**points_formula** | **str** | Formula used to dynamically calculate the rewarded points. | [optional] 
**object** | **str** | Type of object which will be covered by the earning rule. This is required together with &#x60;id&#x60;. Can be replaced by the &#x60;applicable_to&#x60; array. In response, the value of the first object is returned even if &#x60;applicable_to&#x60; array was used. | [optional] 
**id** | **str** | Unique ID of the resource assigned by Voucherify. This is required together with &#x60;object&#x60;. Can be replaced by the &#x60;applicable_to&#x60; array. In response, the value of the first object is returned even if &#x60;applicable_to&#x60; array was used. Values are, for example, &#x60;pc_75U0dHlr7u75BJodrW1AE3t6&#x60; for product collection, &#x60;prod_0bae32322150fd0546&#x60; for a product, or &#x60;sku_0b7d7dfb090be5c619&#x60; for a SKU. | [optional] 
**applicable_to** | [**List[LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderItemsQuantityApplicableToItem]**](LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderItemsQuantityApplicableToItem.md) | Defines products, SKUs, or product collections covered by the earning rule. Can be replaced by &#x60;object&#x60; and &#x60;id&#x60; to define only one object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


