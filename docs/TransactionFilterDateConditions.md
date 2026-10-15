# TransactionFilterDateConditions

Date filter conditions. `$before`/`$after` accept an ISO date-time string. `$is`/`$more_than`/`$less_than` accept a non-negative integer number of days ago. `$has_value`/`$is_unknown` accept any single value and match rows where the field is set / not set. Single values may also be passed as 1-element arrays.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**TransactionFilterDateConditionsConditions**](TransactionFilterDateConditionsConditions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


