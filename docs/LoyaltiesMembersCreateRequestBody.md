# LoyaltiesMembersCreateRequestBody

Request body schema for assigning a loyalty card to a customer using **POST** `/loyalties/{campaignId}/members`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**voucher** | **str** | Code of voucher being published. | [optional] 
**source_id** | **str** | The merchant&#39;s publication ID if it is different from the Voucherify publication ID. It&#39;s an optional tracking identifier of a publication. It is really useful in case of an integration between multiple systems. It can be a publication ID from a CRM system, database or 3rd-party service. If &#x60;source_id&#x60; is provided only 1 voucher can be published per request. | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the publication. A set of key/value pairs that you can attach to a publication object. It can be useful for storing additional information about the publication in a structured format. | [optional] 
**channel** | **str** | Specify the distribution channel. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


