# CampaignLoyaltyCardExpirationRules

Defines the loyalty point expiration rule. This expiration rule applies when there are no `expiration_rules` defined for an earning rule.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_type** | **str** | Type of period. Can be set for &#x60;MONTH&#x60; or &#x60;FIXED_DAY_OF_YEAR&#x60;. &#x60;MONTH&#x60; requires the &#x60;period_value&#x60; field. &#x60;FIXED_DAY_OF_YEAR&#x60; requires the &#x60;fixed_month&#x60; and &#x60;fixed_day&#x60; fields. | [optional] 
**period_value** | **int** | Value of the period. Required for the &#x60;period_type: MONTH&#x60;. | [optional] 
**rounding_type** | **str** | Type of rounding of the expiration period. Optional for the &#x60;period_type: MONTH&#x60;. | [optional] 
**rounding_value** | **int** | Value of rounding of the expiration period. Required for the &#x60;rounding_type&#x60;. | [optional] 
**fixed_month** | **int** | Determines the month when the points expire; &#x60;1&#x60; is January, &#x60;2&#x60; is February, and so on. Required for the &#x60;period_type: FIXED_DAY_OF_YEAR&#x60;. | [optional] 
**fixed_day** | **int** | Determines the day of the month when the points expire. Required for the &#x60;period_type: FIXED_DAY_OF_YEAR&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


