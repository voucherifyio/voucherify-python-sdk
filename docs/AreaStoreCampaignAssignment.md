# AreaStoreCampaignAssignment

An object representing an assignment of a campaign to an area or store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the campaign assignment. | [optional] 
**area_id** | **str** | Unique identifier of the area to which the campaign is assigned. | [optional] 
**all_stores** | **bool** | Determines if the campaign is assigned to all of the stores in the area, i.e. if an area ID is passed in the &#x60;access_settings.assign.area_all_stores_ids&#x60; in the request. | [optional] 
**area_store_id** | **str** | Unique identifier of the store to which the campaign is assigned. | [optional] 
**created_at** | **datetime** | Date and time when the assignment was made. The value is shown in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the campaign assignment to areas or stores. | [optional] [default to 'area_store_campaign_assignment']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


