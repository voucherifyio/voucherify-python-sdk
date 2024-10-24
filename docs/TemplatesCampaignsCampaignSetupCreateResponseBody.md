# TemplatesCampaignsCampaignSetupCreateResponseBody

Response body schema for **POST** `/v1/templates/campaigns/{campaignTemplateId}/campaign-setup`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_resources** | [**List[TemplatesCampaignsCampaignSetupCreateResponseBodyCreatedResourcesItem]**](TemplatesCampaignsCampaignSetupCreateResponseBodyCreatedResourcesItem.md) | Contains a list of resources that have been added to the project when the campaign has been created out of the template. | [optional] 
**campaign** | [**Campaign**](Campaign.md) |  | 
**object** | **str** | The type of the object represented by JSON. This object stores information about the campaign created out of the campaign template. | [optional] [default to 'campaign_setup']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


