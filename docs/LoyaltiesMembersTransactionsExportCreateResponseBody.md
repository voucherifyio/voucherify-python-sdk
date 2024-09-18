# LoyaltiesMembersTransactionsExportCreateResponseBody

Response body schema for **POST** `v1/loyalties/members/{memberId}/transactions/export` and for **POST** `v1/loyalties/{campaignId}/members/{memberId}/transactions/export`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique export ID. | [optional] 
**object** | **str** | The type of object being represented. This object stores information about the export. | [optional] [default to 'export']
**created_at** | **datetime** | Timestamp representing the date and time when the export was scheduled in ISO 8601 format. | [optional] 
**status** | **str** | Status of the export. Informs you whether the export has already been completed, i.e. indicates whether the file containing the exported data has been generated. | [optional] [default to 'SCHEDULED']
**channel** | **str** | The channel through which the export was triggered. | [optional] 
**result** | **object** | Contains the URL of the CSV file. | [optional] 
**user_id** | **str** | Identifies the specific user who initiated the export through the Voucherify Dashboard; returned when the channel value is WEBSITE. | [optional] 
**exported_object** | **str** | The type of object to be exported. | [optional] [default to 'voucher_transactions']
**parameters** | [**LoyaltiesMembersTransactionsExportCreateResponseBodyParameters**](LoyaltiesMembersTransactionsExportCreateResponseBodyParameters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


