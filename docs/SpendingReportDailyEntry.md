# SpendingReportDailyEntry

Aggregated program spending statistics for one period and card definition. Numeric fields default to `0`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Identifies the start of the truncated aggregation period (&#x60;YYYY-MM-DD&#x60;). For &#x60;week&#x60; this is Monday. For &#x60;month&#x60; this is the first day. For &#x60;quarter&#x60; this is the quarter start. | [optional] 
**card_definition_id** | **str** | Identifies the card definition (&#x60;lcdef_...&#x60;). | [optional] 
**success** | **float** | Counts successful spending operations in the period. | [optional] 
**success_on_reward** | **float** | Counts successful reward purchases in the period. | [optional] 
**success_on_order** | **float** | Counts successful order payments in the period. | [optional] 
**points** | **float** | Totals points spent in the period. | [optional] 
**points_on_rewards** | **float** | Totals points spent on reward purchases in the period. | [optional] 
**points_on_order** | **float** | Totals points spent on order payments in the period. | [optional] 
**amount_on_order** | **float** | Totals order amount paid with points in the period. | [optional] 
**object** | **str** | Object type marker. Always &#x60;spending_daily_report&#x60;. | [optional] [default to 'spending_daily_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


