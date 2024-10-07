# ManagementProjectsBrandingListResponseBody

Object containing a list of brand configurations. It always contains one item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about the brand in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of brand objects. | [optional] [default to 'data']
**data** | [**List[ManagementProjectsBranding]**](ManagementProjectsBranding.md) | Array of brand objects. It contains only one object. | [optional] 
**total** | **int** | The total number of brand objects. It is always &#x60;1&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


