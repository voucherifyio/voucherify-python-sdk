# TemplatesCampaignsTierSetupCreateResponseBody

Response body schema for **POST** `/v1/templates/campaigns/{campaignTemplateId}/tier-setup`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_resources** | [**List[TemplatesCampaignsTierSetupCreateResponseBodyCreatedResourcesItem]**](TemplatesCampaignsTierSetupCreateResponseBodyCreatedResourcesItem.md) | Contains a list of resources that have been added to the project when the promotion tier has been created out of the template. | [optional] 
**promotion_tier** | [**PromotionTier**](PromotionTier.md) |  | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the campaign created out of the campaign template. | [optional] [default to 'promotion_tier_setup']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


