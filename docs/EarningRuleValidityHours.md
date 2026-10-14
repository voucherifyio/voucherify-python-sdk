# EarningRuleValidityHours

Hours during which the earning rule is active. With `ANY_TIME`, `daily` must be null/absent. With `DAILY`, `daily` is required (at least one entry). The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Validity hours type. | [optional] 
**daily** | [**List[LoyaltyV2ActivityEarningRuleValidityDailyHours]**](LoyaltyV2ActivityEarningRuleValidityDailyHours.md) | Daily validity windows. Can be &#x60;null&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


