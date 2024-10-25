# VoucherPublish

Stores a summary of publication events: an event counter and endpoint to return details of each event. Publication is an assignment of a code to a customer, e.g. through a distribution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented is by default &#x60;list&#x60;. To get this list, you need to make a call to the endpoint returned in the &#x60;url&#x60; attribute. | [optional] [default to 'list']
**count** | **int** | Publication events counter. | [optional] 
**url** | **str** | The endpoint where this list of publications can be accessed using a **GET** method. &#x60;/v1/vouchers/{voucher_code}/publications&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


