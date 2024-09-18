# PublicationsCreateResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique publication ID, assigned by Voucherify. | [optional] 
**object** | **str** | The type of the object represented by the JSON. This object stores information about the &#x60;publication&#x60;. | [optional] [default to 'publication']
**created_at** | **datetime** | Timestamp representing the date and time when the publication was created. The value is shown in the ISO 8601 format. | [optional] 
**customer_id** | **str** | Unique customer ID of the customer receiving the publication. | [optional] 
**tracking_id** | **str** | Customer&#39;s &#x60;source_id&#x60;. | [optional] 
**metadata** | **object** |  | [optional] 
**channel** | **str** | How the publication was originated. It can be your own custom channel or an example value provided here. | [optional] [default to 'API']
**source_id** | **str** | The merchant&#39;s publication ID if it is different from the Voucherify publication ID. It&#39;s an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service.  | [optional] 
**result** | **str** | Status of the publication attempt. | [optional] [default to 'SUCCESS']
**customer** | [**CustomerWithSummaryLoyaltyReferrals**](CustomerWithSummaryLoyaltyReferrals.md) |  | [optional] 
**vouchers_id** | **List[str]** | Contains the unique internal voucher ID that was assigned by Voucherify. | [optional] 
**voucher** | [**Voucher**](Voucher.md) |  | [optional] 
**vouchers** | **List[str]** | Contains the unique voucher codes that was assigned by Voucherify. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


