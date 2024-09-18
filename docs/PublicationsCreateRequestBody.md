# PublicationsCreateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher** | **str** | Code of the voucher being published. | [optional] 
**source_id** | **str** | The merchant&#39;s publication ID if it is different from the Voucherify publication ID. It&#39;s an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. If &#x60;source_id&#x60; is provided only 1 voucher can be published per request. | [optional] 
**customer** | [**PublicationsCreateRequestBodyCustomer**](PublicationsCreateRequestBodyCustomer.md) |  | [optional] 
**metadata** | **object** |  | [optional] 
**channel** | **str** | Specify the distribution channel. | [optional] 
**campaign** | [**CreatePublicationCampaign**](CreatePublicationCampaign.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


