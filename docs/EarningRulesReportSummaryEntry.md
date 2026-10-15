# EarningRulesReportSummaryEntry

Total program earning-rule evaluation statistics for one earning rule. All numeric fields default to 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the summary row (format: &#x60;lpers_&#x60; followed by hexadecimal characters). | [optional] 
**earning_rule_id** | **str** | Identifies the earning rule (format &#x60;lern_...&#x60;). | [optional] 
**success_count** | **float** | Counts eligibility checks that passed the trigger limit. | [optional] 
**failures_count** | **float** | Counts eligibility checks that failed the trigger limit. | [optional] 
**failures_breakdown** | [**EarningRulesReportFailuresBreakdown**](EarningRulesReportFailuresBreakdown.md) |  | 
**object** | **str** | Object type marker. Always &#x60;program_earning_rules_summary_report&#x60;. | [optional] [default to 'program_earning_rules_summary_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


