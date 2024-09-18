# LoyaltiesEarningRulesCreateRequestBodyItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**validation_rule_id** | **str** | A unique validation rule identifier assigned by the Voucherify API. The validation rule is verified before points are added to the balance. | [optional] 
**loyalty** | [**LoyaltiesEarningRulesCreateRequestBodyItemLoyalty**](LoyaltiesEarningRulesCreateRequestBodyItemLoyalty.md) |  | [optional] 
**event** | **str** |  | [optional] 
**source** | [**LoyaltiesEarningRulesCreateRequestBodyItemSource**](LoyaltiesEarningRulesCreateRequestBodyItemSource.md) |  | [optional] 
**active** | **bool** | A flag to toggle the earning rule on or off. You can disable an earning rule even though it&#39;s within the active period defined by the &#x60;start_date&#x60; and &#x60;expiration_date&#x60; of the campaign or the earning rule&#39;s own &#x60;start_date&#x60; and &#x60;expiration_date&#x60;.    - &#x60;true&#x60; indicates an *active* earning rule - &#x60;false&#x60; indicates an *inactive* earning rule | [optional] 
**start_date** | **datetime** | Start date defines when the earning rule starts to be active. Activation timestamp is presented in the ISO 8601 format. Earning rule is *inactive before* this date. If you don&#39;t define the start date for an earning rule, it&#39;ll inherit the campaign start date by default.  | [optional] 
**expiration_date** | **datetime** | Expiration date defines when the earning rule expires. Expiration timestamp is presented in the ISO 8601 format.  Earning rule is *inactive after* this date.If you don&#39;t define the expiration date for an earning rule, it&#39;ll inherit the campaign expiration date by default. | [optional] 
**validity_timeframe** | [**ValidityTimeframe**](ValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the voucher is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60; Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**validity_hours** | [**ValidityHours**](ValidityHours.md) |  | [optional] 
**metadata** | **object** |  | [optional] 
**segment** | [**LoyaltiesEarningRulesCreateRequestBodyItemSegment**](LoyaltiesEarningRulesCreateRequestBodyItemSegment.md) |  | [optional] 
**custom_event** | [**LoyaltiesEarningRulesCreateRequestBodyItemCustomEvent**](LoyaltiesEarningRulesCreateRequestBodyItemCustomEvent.md) |  | [optional] 
**loyalty_tier** | [**LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyTier**](LoyaltiesEarningRulesCreateRequestBodyItemLoyaltyTier.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


