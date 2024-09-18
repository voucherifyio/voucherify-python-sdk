# PromotionsTiersDisableResponseBodyCampaign

Contains details about promotion tier's parent campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique campaign ID. | [optional] 
**start_date** | **datetime** | Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date.  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date. | [optional] 
**validity_timeframe** | [**ValidityTimeframe**](ValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the voucher is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60; Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**validity_hours** | [**ValidityHours**](ValidityHours.md) |  | [optional] 
**active** | **bool** | A flag indicating whether the campaign is active or not active. A campaign can be disabled even though it&#39;s within the active period defined by the &#x60;start_date&#x60; and &#x60;expiration_date&#x60; using the &lt;!-- [Disable Campaign](OpenAPI.json/paths/~1campaigns~1{campaignId}~1disable) --&gt;[Disable Campaign](ref:disable-campaign) endpoint.    - &#x60;true&#x60; indicates an *active* campaign - &#x60;false&#x60; indicates an *inactive* campaign | [optional] 
**category_id** | **str** | Unique category ID that this campaign belongs to. | [optional] 
**object** | **str** | The type of the object represented by the campaign object. This object stores information about the campaign. | [optional] [default to 'campaign']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


