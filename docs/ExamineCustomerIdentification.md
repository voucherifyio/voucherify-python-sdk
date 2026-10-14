# ExamineCustomerIdentification

Identifies the customer to examine. Depending on `type`, requires one of `customer_id`, `customer_source_id`, or `member_id`. Non-selected identifiers may be omitted or set to `null`. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Identification method. | [optional] 
**customer_id** | **str** | Unique customer ID (&#x60;cust_...&#x60;). Required when &#x60;type&#x60; is &#x60;customer_id&#x60;. | [optional] 
**customer_source_id** | **str** | Customer source ID, e.g. from an external system. May be provided as a string or a number. Required when &#x60;type&#x60; is &#x60;customer_source_id&#x60;. | [optional] 
**member_id** | **str** | Loyalty member ID (&#x60;lmbr_...&#x60;). Required when &#x60;type&#x60; is &#x60;member_id&#x60;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


