# ManagementProjectsWebhooksUpdateResponseBody

Response body schema for **PUT** `v1/management/v1/projects/{projectId}/webhooks/{webhookId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the webhook. | [optional] 
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'webhook']
**created_at** | **datetime** | Timestamp representing the date and time when the webhook configuration was created. The value for this parameter is shown in the ISO 8601 format. | [optional] 
**target_url** | **str** | URL address that receives webhooks. | [optional] 
**events** | **List[str]** | Lists the events that trigger webhook sendout. | [optional] 
**active** | **bool** | Determines if the webhook configuration is active. | [optional] [default to True]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


