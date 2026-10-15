# RewardsSpendingsReportDailyEntry

Aggregated points spent on one reward cost and spending for one period and card definition. Counts and points that did not occur in the period are 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward_id** | **str** | Identifies the reward (&#x60;lrew_...&#x60;). | [optional] 
**cost_id** | **str** | Identifies the reward cost (&#x60;lrcst_...&#x60;). | [optional] 
**spending_id** | **str** | Identifies the reward spending (&#x60;lrspn_...&#x60;). | [optional] 
**card_definition_id** | **str** | Identifies the card definition (&#x60;lcdef_...&#x60;). | [optional] 
**var_date** | **date** | Identifies the start of the truncated aggregation period (&#x60;YYYY-MM-DD&#x60;). For &#x60;week&#x60; this is Monday. For &#x60;month&#x60; this is the first day. For &#x60;quarter&#x60; this is the quarter start. | [optional] 
**success_count** | **float** | Counts approved reward point spends in the period. | [optional] 
**points** | **float** | Totals points spent on those reward spends in the period. | [optional] 
**object** | **str** | Object type marker. Always &#x60;program_rewards_spendings_daily_report&#x60;. | [optional] [default to 'program_rewards_spendings_daily_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


