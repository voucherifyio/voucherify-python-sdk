# CardDailyReportEntry

Aggregated card points statistics for one period. Each field sums the operations of one kind recorded in the period. All numeric fields default to 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Identifies the start of the truncated aggregation period (&#x60;YYYY-MM-DD&#x60;). For &#x60;week&#x60; this is Monday. For &#x60;month&#x60; this is the first day. For &#x60;quarter&#x60; this is the quarter start. | [optional] 
**points_total** | **float** | Points credited to the card in the period. Sums &#x60;points_earned&#x60;, &#x60;points_added&#x60;, and &#x60;points_purchased&#x60;. Points spent, expired, subtracted, refunded, returned, or reversed are not deducted. | [optional] 
**points_earned** | **float** | Points earned through earning rules in the period. Includes pending points activated in the period. | [optional] 
**points_added** | **float** | Points added manually in the period. | [optional] 
**points_purchased** | **float** | Points purchased (e.g. via loyalty-card-points rewards) in the period. | [optional] 
**points_purchased_reversed** | **float** | Purchased points reversed (e.g. by reward refunds) in the period. | [optional] 
**points_subtracted** | **float** | Points subtracted manually in the period. | [optional] 
**points_expired** | **float** | Points expired in the period. | [optional] 
**points_spent** | **float** | Points spent (on rewards and order payments) in the period. | [optional] 
**points_refunded** | **float** | Points refunded in the period. | [optional] 
**points_returned** | **float** | Points returned in the period. | [optional] 
**points_locked** | **float** | Points locked in the period. | [optional] 
**points_unlocked** | **float** | Points unlocked in the period. Includes points released when a spending transaction is approved (also counted in &#x60;points_spent&#x60;) or rejected. | [optional] 
**pending_points_total** | **float** | Pending points added in the period. Activated and canceled pending points are not deducted. | [optional] 
**pending_points_activated** | **float** | Pending points activated in the period. Also counted in &#x60;points_earned&#x60; and &#x60;points_total&#x60;. | [optional] 
**pending_points_canceled** | **float** | Pending points canceled in the period. | [optional] 
**object** | **str** | Object type marker. Always &#x60;card_daily_report&#x60;. | [optional] [default to 'card_daily_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


