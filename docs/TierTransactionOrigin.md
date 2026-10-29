# TierTransactionOrigin

Origin of the tier transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Origin type. &#x60;card_operations&#x60; - point operations on the card. &#x60;daily_task_operations&#x60; - scheduled daily tier processing. &#x60;member_card_created&#x60; - a member card was created. &#x60;member_card_deleted&#x60; - a member card was deleted. &#x60;segment_change&#x60; - the customer entered or left a segment used in tier qualification. | [optional] 
**card_transaction_ids** | **List[str]** | Unique identifiers of the card transactions that triggered the transaction (format &#x60;lctx_...&#x60;). Returned for the &#x60;card_operations&#x60; origin. | [optional] 
**segment_ids** | **List[str]** | Unique identifiers of the customer segments that triggered the transaction. Returned for the &#x60;segment_change&#x60; origin. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


