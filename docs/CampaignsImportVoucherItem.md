# CampaignsImportVoucherItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Value representing the imported code. | [optional] 
**redemption** | [**CampaignsImportVoucherItemRedemption**](CampaignsImportVoucherItemRedemption.md) |  | [optional] 
**active** | **bool** | A flag to toggle the voucher on or off. You can disable a voucher even though it&#39;s within the active period defined by the &#x60;start_date&#x60; and &#x60;expiration_date&#x60;.    - &#x60;true&#x60; indicates an *active* voucher - &#x60;false&#x60; indicates an *inactive* voucher | [optional] 
**metadata** | **object** |  | [optional] 
**category** | **str** | Tag defining the category that this voucher belongs to. Useful when listing vouchers using the [List Vouchers](ref:list-vouchers) endpoint. | [optional] 
**start_date** | **datetime** | Activation timestamp presented in the ISO 8601 format. Voucher is *inactive before* this date. Start date defines when the code starts to be active. Allowed date formats are: - YYYY-MM-DD - YYYY-MM-DDTHH - YYYY-MM-DDTHH:mm - YYYY-MM-DDTHH:mm:ss - YYYY-MM-DDTHH:mm:ssZ - YYYY-MM-DDTHH:mm:ss.SSSZ | [optional] 
**expiration_date** | **datetime** | Expiration date defines when the code expires. Expiration timestamp is presented in the ISO 8601 format.  Voucher is *inactive after* this date. Allowed date formats are: - YYYY-MM-DD - YYYY-MM-DDTHH - YYYY-MM-DDTHH:mm - YYYY-MM-DDTHH:mm:ss - YYYY-MM-DDTHH:mm:ssZ - YYYY-MM-DDTHH:mm:ss.SSSZ | [optional] 
**validity_timeframe** | [**ValidityTimeframe**](ValidityTimeframe.md) |  | [optional] 
**validity_day_of_week** | **List[int]** | Integer array corresponding to the particular days of the week in which the voucher is valid.  - &#x60;0&#x60; Sunday - &#x60;1&#x60; Monday - &#x60;2&#x60; Tuesday - &#x60;3&#x60; Wednesday - &#x60;4&#x60; Thursday - &#x60;5&#x60; Friday - &#x60;6&#x60; Saturday | [optional] 
**additional_info** | **str** | An optional field to keep any extra textual information about the code such as a code description and details. | [optional] 
**type** | **str** |  | [optional] 
**loyalty_card** | [**SimpleLoyaltyCard**](SimpleLoyaltyCard.md) |  | [optional] 
**gift** | [**Gift**](Gift.md) |  | [optional] 
**discount** | [**Discount**](Discount.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


