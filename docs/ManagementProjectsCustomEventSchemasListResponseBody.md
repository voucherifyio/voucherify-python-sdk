# ManagementProjectsCustomEventSchemasListResponseBody

Object containing a list of custom event schemas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about the custom event schemas in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of custom event schema objects. | [optional] [default to 'data']
**data** | [**List[ManagementProjectsCustomEventSchema]**](ManagementProjectsCustomEventSchema.md) | Array of custom event schema objects. | [optional] 
**total** | **int** | The total number of custom event schema objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


