# LoyaltiesProgramsReportsSpendingSummaryListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/reports/spending/summary`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SpendingReportSummaryEntry]**](SpendingReportSummaryEntry.md) | Lists summary rows, one per card definition that has recorded spending. Contains at most 10 rows (max number of card definitions per program), ordered by &#x60;id&#x60; descending. | [optional] 
**object** | **str** | Object type marker. Always &#x60;report&#x60;. | [optional] [default to 'report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


