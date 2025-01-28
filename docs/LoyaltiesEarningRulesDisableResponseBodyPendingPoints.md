# LoyaltiesEarningRulesDisableResponseBodyPendingPoints

Defines the configuration for pending points. Pending points can be used only with the `order.paid` event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_type** | **str** | Defines the type of the period during which the points are in the pending state. Currently, only &#x60;DAY&#x60; value is accepted. | [optional] [default to 'DAY']
**period_value** | **int** | Defines for how long the points are in the pending state. The minimum value is 1, maximum is 90. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


