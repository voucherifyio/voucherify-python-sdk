# LoyaltiesEarningRulesUpdateResponseBodyLoyaltyOrderItemsAmount

Defines the ratio based on the property defined in the calculation_type parameter. For every set of value (1, 10, etc) defined in the every parameter for the property defined in calculation_type, give the customer the number of points defined in the points parameter. In other words, for every calculation_type, give points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**every** | **int** | Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $10 order amount is written as 1000. | [optional] 
**points** | **int** | Number of points to be awarded, i.e. how many points to be added to the loyalty card. | [optional] 
**object** | **str** | Type of object taken under consideration. | [optional] 
**id** | **str** | Unique ID of the resource, i.e. pc_75U0dHlr7u75BJodrW1AE3t6, prod_0bae32322150fd0546, or sku_0b7d7dfb090be5c619. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


