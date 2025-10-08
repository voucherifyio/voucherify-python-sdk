# SimpleCampaign

Simplified campaign data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Campaign ID. | [optional] 
**name** | **str** | Campaign name. | [optional] 
**campaign_type** | **str** | Type of campaign. | [optional] 
**type** | **str** | Defines whether the campaign can be updated with new vouchers after campaign creation or if the campaign consists of generic (standalone) voucherss.  - &#x60;AUTO_UPDATE&#x60;: the campaign is dynamic, i.e. vouchers will generate based on set criteria -  &#x60;STATIC&#x60;: vouchers need to be manually published - &#x60;STANDALONE&#x60;: campaign for single vouchers | [optional] 
**is_referral_code** | **bool** | Flag indicating whether this voucher is a referral code; &#x60;true&#x60; for campaign type &#x60;REFERRAL_PROGRAM&#x60;. | [optional] 
**voucher** | [**SimpleCampaignVoucher**](SimpleCampaignVoucher.md) |  | [optional] 
**referral_program** | [**ReferralProgram**](ReferralProgram.md) |  | [optional] 
**auto_join** | **bool** | Indicates whether customers will be able to auto-join the campaign if any earning rule is fulfilled. | [optional] 
**join_once** | **bool** | If this value is set to &#x60;true&#x60;, customers will be able to join the campaign only once. It is always &#x60;false&#x60; for generic (standalone) vouchers campaigns and it cannot be changed in them. It is always &#x60;true&#x60; for loyalty campaigns and it cannot be changed in them. | [optional] 
**active** | **bool** | Indicates whether the campaign is active. | [optional] 
**category_id** | **str** | The unique category ID that this campaign belongs to. | [optional] 
**category** | **str** | Unique category name. | [optional] 
**categories** | [**List[Category]**](Category.md) | Contains details about the category. | [optional] 
**metadata** | **object** | A set of custom key/value pairs that you can attach to a campaign. The metadata object stores all custom attributes assigned to the campaign. | [optional] 
**start_date** | **datetime** | Activation timestamp defines when the campaign starts to be active in ISO 8601 format. Campaign is inactive *before* this date.  | [optional] 
**expiration_date** | **datetime** | Expiration timestamp defines when the campaign expires in ISO 8601 format.  Campaign is inactive *after* this date. | [optional] 
**description** | **str** | An optional field to keep extra textual information about the campaign such as a campaign description and details. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the campaign was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the campaign was updated in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the campaign. | [optional] [default to 'campaign']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


