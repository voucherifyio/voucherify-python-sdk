# LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody

Request body schema for **POST** `/v2/loyalties/programs/{programId}/members/{memberId}/orders/payments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Unique identifier of the member&#39;s loyalty card to spend points from (format &#x60;lcrd_...&#x60;). | [optional] 
**order** | [**OrderPaymentOrder**](OrderPaymentOrder.md) |  | 
**payment_limit** | **object** |  | [optional] 
**mode** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


