# RewardsReportDailyEntry

Aggregated reward-purchase counts for one period and reward. Counts that did not occur in the period are 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Identifies the start of the truncated aggregation period (&#x60;YYYY-MM-DD&#x60;). For &#x60;week&#x60; this is Monday. For &#x60;month&#x60; this is the first day. For &#x60;quarter&#x60; this is the quarter start. | [optional] 
**reward_id** | **str** | Identifies the reward (&#x60;lrew_...&#x60;). | [optional] 
**success_count** | **float** | Counts approved reward purchases in the period. | [optional] 
**failures_count** | **float** | Counts reward purchase attempts that failed in the period. | [optional] 
**failures_breakdown** | **object** | Always an empty object even if &#x60;failures_count&#x60; is above zero. | [optional] 
**object** | **str** | Object type marker. Always &#x60;program_rewards_daily_report&#x60;. | [optional] [default to 'program_rewards_daily_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


