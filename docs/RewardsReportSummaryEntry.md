# RewardsReportSummaryEntry

All-time reward-purchase counts for one reward. Counts that did not occur are 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the summary row (format: &#x60;lprrs_&#x60; followed by hexadecimal characters). | [optional] 
**reward_id** | **str** | Identifies the reward (&#x60;lrew_...&#x60;). | [optional] 
**success_count** | **float** | Counts approved reward purchases. | [optional] 
**failures_count** | **float** | Counts reward purchase attempts that failed. | [optional] 
**failures_breakdown** | [**RewardsReportFailuresBreakdown**](RewardsReportFailuresBreakdown.md) |  | 
**object** | **str** | Object type marker. Always &#x60;program_rewards_summary_report&#x60;. | [optional] [default to 'program_rewards_summary_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


