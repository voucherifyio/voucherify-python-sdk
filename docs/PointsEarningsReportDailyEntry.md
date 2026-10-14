# PointsEarningsReportDailyEntry

Aggregated daily program points-earnings statistics for one period, earning rule, earning item, and card definition. All numeric fields default to 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earning_rule_id** | **str** | Identifies the earning rule (format &#x60;lern_...&#x60;). | [optional] 
**earning_item_id** | **str** | Identifies the earning item that produced the points (format: &#x60;lernei_&#x60; followed by hexadecimal characters). | [optional] 
**card_definition_id** | **str** | Identifies the card definition (format &#x60;lcdef_...&#x60;). | [optional] 
**var_date** | **date** | Identifies the start of the truncated aggregation period (&#x60;YYYY-MM-DD&#x60;). For &#x60;week&#x60; this is Monday. For &#x60;month&#x60; this is the first day. For &#x60;quarter&#x60; this is the quarter start. | [optional] 
**success_count** | **float** | Counts earning operations that credited points or added pending points in the period. | [optional] 
**points** | **float** | Sums points credited immediately by earning rules in the period. Pending points activated in the period are not included. | [optional] 
**pending_points** | **float** | Sums pending points added in the period. Activated and canceled pending points are not deducted. | [optional] 
**object** | **str** | Object type marker. Always &#x60;program_points_earnings_daily_report&#x60;. | [optional] [default to 'program_points_earnings_daily_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


