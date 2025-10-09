# ParameterFiltersListCampaignsStatusConditions

Data conditions used to narrow down the data records to be returned in the result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **object** | Campaigns finished generation codes. This also returns campaigns regardless of their &#x60;expiration_date&#x60; and &#x60;start_date&#x60;. | [optional] 
**failed** | **object** | Campaigs failed to generated codes. | [optional] 
**in_progress** | **object** | Campaigns are generating codes or they are updating. | [optional] 
**expired** | **object** | Campaigns generated codes, but their &#x60;expiration_date&#x60; is in the past. | [optional] 
**before_start** | **object** | Campaigns generated codes, but their &#x60;start_date&#x60; is in the future. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


