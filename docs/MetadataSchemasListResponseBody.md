# MetadataSchemasListResponseBody

Object containing a list of metadata schemas.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about the metadata schemas in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of metadata schema objects. | [optional] [default to 'schemas']
**schemas** | [**List[MetadataSchemaDeprecated]**](MetadataSchemaDeprecated.md) | Array of metadata schema objects. The metadata schemas are listed by related object properties. | [optional] 
**total** | **int** | The total number of metadata schema objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


