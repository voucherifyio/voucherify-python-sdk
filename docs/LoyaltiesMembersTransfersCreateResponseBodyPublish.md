# LoyaltiesMembersTransfersCreateResponseBodyPublish

This object stores a summary of publish events: an events counter and an endpoint which can be called to return details of each event. A publication is required for loyalty cards and referral codes. This object gets updated whenever a voucher has been published. Publication means assigning a code to a particular customer. Typically, a publication is made by distributing your codes to your customers, e.g. through Export to MailChimp or publish voucher API method.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** | The type of the object represented is by default list. To get this list, you need to make a call to the endpoint returned in the url attribute. | [optional] [default to 'list']
**count** | **int** | Publication events counter. | [optional] 
**entries** | **List[str]** |  | [optional] 
**url** | **str** | The endpoint where this list of publications can be accessed using a GET method. /v1/vouchers/{voucher_code}/publications | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


