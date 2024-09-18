# CampaignsListResponseBody

Schema model for **GET** `v1/campaigns`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about campaigns in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of campaign objects. | [optional] [default to 'campaigns']
**campaigns** | [**List[CampaignBase]**](CampaignBase.md) | Contains array of campaign objects. | [optional] 
**total** | **int** | Total number of campaigns. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


