# ManagementProjectsWebhooksListResponseBody

Object containing a list of webhook configurations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented by JSON. This object stores information about the webhook configurations in a dictionary. | [optional] [default to 'list']
**data_ref** | **str** | Identifies the name of the attribute that contains the array of webhook objects. | [optional] [default to 'data']
**data** | [**List[ManagementProjectsWebhook]**](ManagementProjectsWebhook.md) | Array of webhook objects. | [optional] 
**total** | **int** | The total number of webhook objects. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


