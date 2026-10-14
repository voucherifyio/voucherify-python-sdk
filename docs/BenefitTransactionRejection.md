# BenefitTransactionRejection

Rejection details for a benefit transaction.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **str** | Machine-readable rejection reason. Known values are &#x60;OUT_OF_STOCK&#x60;, &#x60;BENEFIT_NOT_FOUND&#x60;, &#x60;UNEXPECTED_ERROR&#x60;, &#x60;TRIGGER_LIMIT_COOLDOWN_NOT_PASSED&#x60;, and &#x60;TRIGGER_LIMIT_FREQUENCY_EXCEEDED&#x60;. Other error keys can be passed through, so treat this list as non-exhaustive. | [optional] 
**details** | **object** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


