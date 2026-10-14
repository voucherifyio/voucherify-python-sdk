# LoyaltiesProgramsReportsMembersSummaryListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/reports/members/summary`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MembersReportSummaryEntry]**](MembersReportSummaryEntry.md) | List of summary rows for the program. Contains one row when activity was recorded, ordered by &#x60;id&#x60; descending. Empty when no activity was recorded. | [optional] 
**object** | **str** | Object type marker. Always &#x60;report&#x60;. | [optional] [default to 'report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


