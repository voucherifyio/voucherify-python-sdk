# V2LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody

Request body schema for **POST** `/v2/loyalties/programs/{programId}/members/{memberId}/orders/payments`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Unique identifier of the member&#39;s loyalty card to spend points from (format &#x60;lcrd_...&#x60;). | [optional] 
**order** | [**OrderPaymentOrder**](OrderPaymentOrder.md) |  | 
**payment_limit** | [**LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBodyLimit**](LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBodyLimit.md) |  | [optional] 
**mode** | **str** | Payment mode. &#x60;TRANSACTION&#x60; creates a &#x60;PENDING&#x60; order transaction processed asynchronously (HTTP &#x60;202&#x60;). &#x60;DRY_RUN&#x60; only simulates the payment and returns the calculation result (HTTP &#x60;200&#x60;); no transaction is created. Defaults to &#x60;TRANSACTION&#x60; when omitted or &#x60;null&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


