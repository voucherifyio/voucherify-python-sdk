# LoyaltiesEarningRulesUpdateRequestBodyLoyaltyOrderAmount

Defines the ratio based on the property defined in the calculation_type parameter. For every set of value (1, 10, etc) defined in the every parameter for the property defined in calculation_type, give the customer the number of points defined in the points parameter. In other words, for every calculation_type, give points.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**every** | **int** | Value is multiplied by 100 to precisely represent 2 decimal places. For example, a $10 order amount is written as 1000. | [optional] 
**points** | **int** | Number of points to be awarded, i.e. how many points to be added to the loyalty card. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


