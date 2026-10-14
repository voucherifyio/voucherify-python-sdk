# LoyaltiesProgramsReportsRewardsDailyListResponseBody

Response body schema for **GET** `/v2/loyalties/programs/{programId}/reports/rewards/daily`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RewardsReportDailyEntry]**](RewardsReportDailyEntry.md) | List of report entries, one per reward and aggregation period with recorded purchases, ordered by &#x60;date&#x60; ascending. Empty when no purchases were recorded in the range. | [optional] 
**object** | **str** | Object type marker. Always &#x60;report&#x60;. | [optional] [default to 'report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


