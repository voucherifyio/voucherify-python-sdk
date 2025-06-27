# EarningRuleExpirationRules

Defines the loyalty point expiration rule. This expiration rule applies only to this earning rule and supersedes `expiration_rules` defined in the `voucher.loyalty_card` object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_type** | **str** | Type of period. Currently, only &#x60;MONTH&#x60; is allowed. | [optional] [default to 'MONTH']
**period_value** | **int** | Value of the period. | [optional] 
**rounding_type** | **str** | Type of rounding of the expiration period. | [optional] 
**rounding_value** | **int** | Value of rounding of the expiration period. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


