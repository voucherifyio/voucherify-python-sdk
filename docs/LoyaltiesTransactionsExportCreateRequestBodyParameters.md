# LoyaltiesTransactionsExportCreateRequestBodyParameters

List of available parameters containing fields and filters that can be exported for transactions in a loyalty card campaign, along with the sorting order of the returned data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** | How the export is ordered, where the dash &#x60;-&#x60; preceding a sorting option means sorting in a descending order. | [optional] 
**fields** | **List[str]** | Data fields that will be exported for the transactions that are associated with balance movements on cards in a campaign. | [optional] 
**filters** | [**ExportCampaignTransactionsFilters**](ExportCampaignTransactionsFilters.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


