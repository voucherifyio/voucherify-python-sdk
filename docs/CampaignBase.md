# CampaignBase

This is an object representing a campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique campaign ID, assigned by Voucherify. | [optional] 
**name** | **str** | Campaign name. | [optional] 
**description** | **str** | An optional field to keep any extra textual information about the campaign such as a campaign description and details. | [optional] 
**campaign_type** | **str** | Type of campaign. | [optional] 
**type** | **str** | Defines whether the campaign can be updated with new vouchers after campaign creation.      - &#x60;AUTO_UPDATE&#x60;: the campaign is dynamic, i.e. vouchers will generate based on set criteria     -  &#x60;STATIC&#x60;: vouchers need to be manually published | [optional] 
**voucher** | [**CampaignVoucher**](CampaignVoucher.md) |  | [optional] 
**auto_join** | **bool** | Indicates whether customers will be able to auto-join a loyalty campaign if any earning rule is fulfilled. | [optional] 
**join_once** | **bool** | If this value is set to &#x60;true&#x60;, customers will be able to join the campaign only once. | [optional] 
**use_voucher_metadata_schema** | **bool** | Flag indicating whether the campaign is to use the voucher&#39;s metadata schema instead of the campaign metadata schema. | [optional] 
**validity_timeframe** | [**ValidityTimeframe**](ValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the voucher is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60; Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**validity_hours** | [**ValidityHours**](ValidityHours.md) |  | [optional] 
**activity_duration_after_publishing** | **str** | Defines the amount of time the vouchers will be active after publishing. The value is shown in the ISO 8601 format. For example, a voucher with the value of P24D will be valid for a duration of 24 days. | [optional] 
**vouchers_count** | **int** | Total number of unique vouchers in campaign. | [optional] 
**start_date** | **datetime** | Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is *inactive before* this date.  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is *inactive after* this date. | [optional] 
**active** | **bool** | A flag to toggle the campaign on or off. You can disable a campaign even though it&#39;s within the active period defined by the &#x60;start_date&#x60; and &#x60;expiration_date&#x60;.    - &#x60;true&#x60; indicates an *active* campaign - &#x60;false&#x60; indicates an *inactive* campaign | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the campaign. A set of key/value pairs that you can attach to a campaign object. It can be useful for storing additional information about the campaign in a structured format. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the campaign was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the campaign was last updated in ISO 8601 format. | [optional] 
**category** | **str** | Unique category name. | [optional] 
**creation_status** | **str** | Indicates the status of the campaign creation. | [optional] 
**vouchers_generation_status** | **str** | Indicates the status of the campaign&#39;s voucher generation. | [optional] 
**protected** | **bool** | Indicates whether the resource can be deleted. | [optional] 
**category_id** | **str** | Unique category ID that this campaign belongs to. | [optional] 
**categories** | [**List[Category]**](Category.md) | Contains details about the category. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the campaign. | [optional] [default to 'campaign']
**referral_program** | [**ReferralProgram**](ReferralProgram.md) |  | [optional] 
**loyalty_tiers_expiration** | [**LoyaltyTiersExpirationAll**](LoyaltyTiersExpirationAll.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


