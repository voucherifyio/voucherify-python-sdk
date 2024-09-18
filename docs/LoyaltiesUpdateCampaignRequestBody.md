# LoyaltiesUpdateCampaignRequestBody

Request body schema for **PUT** `/loyalties/{campaignId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **datetime** | Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date.  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date. | [optional] 
**validity_timeframe** | [**ValidityTimeframe**](ValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the voucher is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60; Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**validity_hours** | [**ValidityHours**](ValidityHours.md) |  | [optional] 
**description** | **str** | An optional field to keep any extra textual information about the campaign such as a campaign description and details. | [optional] 
**category** | **str** | The category assigned to the campaign. Either pass this parameter OR the &#x60;category_id&#x60;. | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the campaign. A set of key/value pairs that you can attach to a campaign object. It can be useful for storing additional information about the campaign in a structured format. | [optional] 
**unset_metadata_fields** | **List[str]** | Determine which metadata should be removed from campaign. | [optional] 
**category_id** | **str** | Unique category ID that this campaign belongs to. Either pass this parameter OR the &#x60;category&#x60;. | [optional] 
**activity_duration_after_publishing** | **str** | Defines the amount of time the vouchers will be active after publishing. The value is shown in the ISO 8601 format. For example, a voucher with the value of P24D will be valid for a duration of 24 days. | [optional] 
**join_once** | **bool** | If this value is set to &#x60;true&#x60;, customers will be able to join the campaign only once. | [optional] 
**auto_join** | **bool** | Indicates whether customers will be able to auto-join a loyalty campaign if any earning rule is fulfilled. | [optional] 
**type** | **str** | Defines whether the campaign can be updated with new vouchers after campaign creation.      - &#x60;AUTO_UPDATE&#x60;: By choosing the auto update option you will create a campaign that can be enhanced by new vouchers after the time of creation (e.g. by publish vouchers method).     -  &#x60;STATIC&#x60;: vouchers need to be manually published. | [optional] 
**loyalty_tiers_expiration** | [**LoyaltyTiersExpirationAll**](LoyaltyTiersExpirationAll.md) |  | [optional] 
**options** | [**LoyaltiesUpdateCampaignRequestBodyOptions**](LoyaltiesUpdateCampaignRequestBodyOptions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


