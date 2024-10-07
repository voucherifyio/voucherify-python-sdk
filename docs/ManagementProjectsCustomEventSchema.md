# ManagementProjectsCustomEventSchema

Object containing the response to creating a custom event schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the custom event schema. | [optional] 
**name** | **str** | User-defined name of the custom event. This is also shown in **Project Settings** &gt; **Event Schema** in the Voucherify Dashboard. | [optional] 
**var_schema** | [**ManagementProjectsCustomEventSchemaSchema**](ManagementProjectsCustomEventSchemaSchema.md) |  | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the custom event schema was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the custom event schema was updated. The value is shown in the ISO 8601 format. | [optional] 
**object** | **str** | The type of the object represented by JSON. | [optional] [default to 'custom-event-schema']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


