# MembersReportSummaryEntry

All-time member and card changes for the program. Counters that did not change are 0.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the summary row (format: &#x60;lpmrs_&#x60; followed by hexadecimal characters). | [optional] 
**members_joined** | **float** | Counts members who joined the program. | [optional] 
**members_deactivated** | **float** | Counts members deactivated. Decreases by 1 when a member is activated again. | [optional] 
**members_deleted** | **float** | Counts members deleted. | [optional] 
**cards** | **float** | Counts cards created. Decreases by 1 when a card is unassigned (e.g. when a member is deleted). | [optional] 
**object** | **str** | Object type marker. Always &#x60;program_members_summary_report&#x60;. | [optional] [default to 'program_members_summary_report']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


