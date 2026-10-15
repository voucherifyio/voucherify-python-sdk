# RewardsSpendingsReportSummaryEntry

All-time points spent on one reward cost and spending for one card definition. Counts and points that did not occur are 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reward_id** | **str** | Identifies the reward (&#x60;lrew_...&#x60;). | [optional] 
**cost_id** | **str** | Identifies the reward cost (&#x60;lrcst_...&#x60;). | [optional] 
**spending_id** | **str** | Identifies the reward spending (&#x60;lrspn_...&#x60;). | [optional] 
**card_definition_id** | **str** | Identifies the card definition (&#x60;lcdef_...&#x60;). | [optional] 
**id** | **str** | Identifies the summary row (format: &#x60;lprss_&#x60; followed by hexadecimal characters). | [optional] 
**success_count** | **float** | Counts approved reward point spends. | [optional] 
**points** | **float** | Totals points spent on those reward spends. | [optional] 
**object** | **str** | Object type marker. Always &#x60;program_rewards_spendings_summary_report&#x60;. | [optional] [default to 'program_rewards_spendings_summary_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


