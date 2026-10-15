# V2LoyaltiesEarningRulesGetResponseBody

Response body schema for **GET** `/v2/loyalties/earning-rules/{earningRuleId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Earning rule ID (&#x60;lern_...&#x60;). | [optional] 
**name** | **str** | Earning rule name. | [optional] 
**status** | **str** | Current status. &#x60;DELETED&#x60; also exists internally but deleted rules are excluded from API reads. | [optional] 
**earnings** | [**List[EarningRuleEarning]**](EarningRuleEarning.md) | Earning definitions of the rule. Contains at least one earning. | [optional] 
**trigger** | [**EarningRuleTrigger**](EarningRuleTrigger.md) |  | 
**error** | [**LoyaltyV2ActivityEarningRuleError**](LoyaltyV2ActivityEarningRuleError.md) |  | [optional] 
**validity_hours** | [**EarningRuleValidityHours**](EarningRuleValidityHours.md) |  | 
**start_date** | **datetime** | Date-time from which the rule is active. Can be &#x60;null&#x60;. | [optional] 
**end_date** | **datetime** | Date-time until which the rule is active. Can be &#x60;null&#x60;. | [optional] 
**trigger_limits** | [**V2LoyaltiesEarningRulesGetResponseBodyTriggerLimits**](V2LoyaltiesEarningRulesGetResponseBodyTriggerLimits.md) |  | [optional] 
**earning_limits** | [**LoyaltyV2ActivityEarningRuleEarningLimits**](LoyaltyV2ActivityEarningRuleEarningLimits.md) |  | 
**metadata** | **object** | Arbitrary key-value metadata; any JSON object is accepted. | 
**created_at** | **datetime** | Creation timestamp (ISO 8601). | [optional] 
**updated_at** | **datetime** | Last update timestamp (ISO 8601). &#x60;null&#x60; when never updated. | [optional] 
**object** | **str** | Object type marker. Always &#x60;earning_rule&#x60;. | [optional] [default to 'earning_rule']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


