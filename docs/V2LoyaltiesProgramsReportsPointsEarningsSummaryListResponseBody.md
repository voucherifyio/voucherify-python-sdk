# V2LoyaltiesProgramsReportsPointsEarningsSummaryListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/reports/points-earnings/summary`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PointsEarningsReportSummaryEntry]**](PointsEarningsReportSummaryEntry.md) | List of summary rows, one per earning rule, earning item, and card definition with recorded activity, ordered by &#x60;id&#x60; descending. Contains at most 100 rows. Empty when no activity was recorded. | [optional] 
**object** | **str** | Object type marker. Always &#x60;report&#x60;. | [optional] [default to 'report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


