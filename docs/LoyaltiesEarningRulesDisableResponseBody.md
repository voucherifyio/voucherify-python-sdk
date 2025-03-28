# LoyaltiesEarningRulesDisableResponseBody

Response body schema for **POST** `v1/loyalties/{campaignId}/earning-rules/{earningRuleId}/disable`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Assigned by the Voucherify API, identifies the earning rule object. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the earning rule was created. The value is shown in the ISO 8601 format. | [optional] 
**loyalty** | [**LoyaltiesEarningRulesDisableResponseBodyLoyalty**](LoyaltiesEarningRulesDisableResponseBodyLoyalty.md) |  | [optional] 
**event** | **str** |  | [optional] 
**custom_event** | [**LoyaltiesEarningRulesDisableResponseBodyCustomEvent**](LoyaltiesEarningRulesDisableResponseBodyCustomEvent.md) |  | [optional] 
**segment** | [**LoyaltiesEarningRulesDisableResponseBodySegment**](LoyaltiesEarningRulesDisableResponseBodySegment.md) |  | [optional] 
**loyalty_tier** | [**LoyaltiesEarningRulesDisableResponseBodyLoyaltyTier**](LoyaltiesEarningRulesDisableResponseBodyLoyaltyTier.md) |  | [optional] 
**pending_points** | [**LoyaltiesEarningRulesDisableResponseBodyPendingPoints**](LoyaltiesEarningRulesDisableResponseBodyPendingPoints.md) |  | [optional] 
**source** | [**LoyaltiesEarningRulesDisableResponseBodySource**](LoyaltiesEarningRulesDisableResponseBodySource.md) |  | [optional] 
**object** | **str** | The type of the object represented by JSON. Default is earning_rule. | [optional] [default to 'earning_rule']
**automation_id** | **str** | For internal use by Voucherify. | [optional] 
**start_date** | **str** | Start date defines when the earning rule starts to be active. Activation timestamp is presented in the ISO 8601 format. The earning rule is inactive before this date. If you do not define the start date for an earning rule, it will inherit the campaign start date by default. | [optional] 
**expiration_date** | **str** | Expiration date defines when the earning rule expires. Expiration timestamp is presented in the ISO 8601 format. The earning rule is inactive after this date. If you do not define the expiration date for an earning rule, it will inherit the campaign expiration date by default. | [optional] 
**validity_timeframe** | [**ValidityTimeframe**](ValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the voucher is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60; Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**validity_hours** | [**ValidityHours**](ValidityHours.md) |  | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the earning rule. A set of key/value pairs that you can attach to an earning rule object. It can be useful for storing additional information about the earning rule in a structured format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the earning rule was last updated in ISO 8601 format. | [optional] 
**active** | **bool** | A flag to toggle the earning rule on or off. You can disable an earning rule even though it&#39;s within the active period defined by the start_date and expiration_date of the campaign or the earning rule&#39;s own start_date and expiration_date. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


