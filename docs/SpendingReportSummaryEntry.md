# SpendingReportSummaryEntry

Total program spending statistics for one card definition that has recorded spending. Numeric fields default to `0`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the summary row (&#x60;lssum_...&#x60;). | [optional] 
**card_definition_id** | **str** | Identifies the card definition (&#x60;lcdef_...&#x60;). | [optional] 
**success** | **float** | Counts successful spending operations. | [optional] 
**success_on_reward** | **float** | Counts successful reward purchases. | [optional] 
**success_on_order** | **float** | Counts successful order payments. | [optional] 
**points** | **float** | Totals points spent. | [optional] 
**points_on_rewards** | **float** | Totals points spent on reward purchases. | [optional] 
**points_on_order** | **float** | Totals points spent on order payments. | [optional] 
**amount_on_order** | **float** | Totals order amount paid with points. | [optional] 
**object** | **str** | Object type marker. Always &#x60;spending_summary_report&#x60;. | [optional] [default to 'spending_summary_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


