# AccessSettingsAssign

Assigns the campaign to an area or a store. Provide the area and/or store IDs in the respective arrays. If a campaign changes assignments between areas or stores, unassign it from the area. For example, if a campaign is assigned to Area-01, but it must be now assigned to Store-01 within this area, you have to unassign the campaign from Area-01 and assign to Store-01 only.  If you want to assign the campaign to stores only, you do not have to send the area ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areas_ids** | **List[str]** | List all area IDs to which the campaign will be assigned. | [optional] 
**area_stores_ids** | **List[str]** | List all store IDs to which the campaign will be assigned. | [optional] 
**area_all_stores_ids** | **List[str]** | List all area IDs where the campaign is assigned to all stores in the area. This assignment is not equal to the assignment to all &#x60;area_stores_ids&#x60; listed separately. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


