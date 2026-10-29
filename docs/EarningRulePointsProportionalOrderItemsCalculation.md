# EarningRulePointsProportionalOrderItemsCalculation

Order items based calculation - \"every X gives Y points\" applied to items matching the `applicable_to` criteria.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**every** | **int** | The divisor - every this amount/quantity awards &#x60;value&#x60; points. | [optional] 
**value** | **float** | Points awarded per &#x60;every&#x60; unit. | [optional] 
**applicable_to** | [**List[EarningRulePointsProportionalApplicableTo]**](EarningRulePointsProportionalApplicableTo.md) | Product/SKU/collection criteria selecting matching order items. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


