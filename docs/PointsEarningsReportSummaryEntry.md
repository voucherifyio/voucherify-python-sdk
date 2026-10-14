# PointsEarningsReportSummaryEntry

Total program points-earnings statistics for one earning rule, earning item, and card definition. All numeric fields default to 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**earning_rule_id** | **str** | Identifies the earning rule (format &#x60;lern_...&#x60;). | [optional] 
**earning_item_id** | **str** | Identifies the earning item that produced the points (format: &#x60;lernei_&#x60; followed by hexadecimal characters). | [optional] 
**card_definition_id** | **str** | Identifies the card definition (format &#x60;lcdef_...&#x60;). | [optional] 
**id** | **str** | Identifies the summary row (format: &#x60;lppes_&#x60; followed by hexadecimal characters). | [optional] 
**success_count** | **float** | Counts earning operations that credited points or added pending points. | [optional] 
**points** | **float** | Sums points credited immediately by earning rules. Pending points activated later are not included. | [optional] 
**pending_points** | **float** | Sums pending points added. Activated and canceled pending points are not deducted. | [optional] 
**object** | **str** | Object type marker. Always &#x60;program_points_earnings_summary_report&#x60;. | [optional] [default to 'program_points_earnings_summary_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


