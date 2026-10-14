# TierTransactionDetails

Details of the tier evaluation. Fields that do not apply to the transaction type are `null`. `JOINED` - `tier_to` set, `tier_from` null. `LEFT` - `tier_from` set, `tier_to` null. `UPGRADED` and `DOWNGRADED` - both `tier_from` and `tier_to` set. `EXPIRATION_CHANGED` - `expires_at` holds the new expiration; `tier_from` and `tier_to` null. `EVALUATION_REFRESHED` - `points` holds the recalculated value; `tier_from` and `tier_to` null.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**points** | **float** | Qualifying points at the time of evaluation. Returns the point balance or the points earned in the tracking period, depending on the tier structure. &#x60;null&#x60; when points were not calculated. | [optional] 
**tier_from** | **str** | Unique identifier of the tier the member moved from (format &#x60;lt_...&#x60;). &#x60;null&#x60; when there is no source tier, including &#x60;JOINED&#x60;, &#x60;EXPIRATION_CHANGED&#x60;, and &#x60;EVALUATION_REFRESHED&#x60; transactions. | [optional] 
**tier_to** | **str** | Unique identifier of the tier the member moved to (format &#x60;lt_...&#x60;). &#x60;null&#x60; when there is no destination tier, including &#x60;LEFT&#x60;, &#x60;EXPIRATION_CHANGED&#x60;, and &#x60;EVALUATION_REFRESHED&#x60; transactions. | [optional] 
**origin** | [**TierTransactionOrigin**](TierTransactionOrigin.md) |  | [optional] 
**rejection** | [**TierTransactionRejection**](TierTransactionRejection.md) |  | [optional] 
**start_at** | **datetime** | Start of the tier membership period, or &#x60;null&#x60;. | [optional] 
**expires_at** | **datetime** | Expiration of the tier membership period, or &#x60;null&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


