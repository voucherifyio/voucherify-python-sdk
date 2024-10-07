# ManagementProjectsWebhooksCreateRequestBody

Request body schema for **POST** `/management/v1/projects/{projectId}/webhooks/{webhookId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_url** | **str** | URL address that receives webhooks. | [optional] 
**events** | **List[str]** | Lists the events that trigger webhook sendout. | [optional] 
**active** | **bool** | Determines if the webhook configuration is active. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


