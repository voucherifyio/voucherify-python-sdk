# PublicationsListResponseBody

Response body schema for listing publications using **GET** `v1/publications`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about publications in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of publications. | [optional] [default to 'publications']
**publications** | [**List[PublicationsListResponseBodyPublicationsItem]**](PublicationsListResponseBodyPublicationsItem.md) | Response schema model for publishing vouchers to a specific customer. | [optional] 
**total** | **int** | Total number of publications. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


