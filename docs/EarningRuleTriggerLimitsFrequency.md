# EarningRuleTriggerLimitsFrequency

Frequency limit for triggers per member. With `NO_LIMIT`, `limits` must be null or an empty array. With `LIMITED`, `limits` is required and must contain exactly one limit. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Frequency limit type. | [optional] 
**limits** | **List[object]** | Frequency limits (at most one). Can be &#x60;null&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


