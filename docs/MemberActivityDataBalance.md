# MemberActivityDataBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** |  | [optional] 
**points** | **int** | Points added or subtracted in the transaction of a loyalty card. | [optional] 
**type** | **str** | The type of voucher whose balance is being adjusted due to the transaction. | [optional] 
**total** | **int** | The number of all points or credits accumulated on the card as affected by add or subtract operations. | [optional] 
**object** | **str** | The type of the object represented by the JSON. | [optional] [default to 'balance']
**balance** | **int** | The available points or credits on the card after the transaction as affected by redemption or rollback. | [optional] 
**operation_type** | **str** | The type of the operation being performed. The operation type is &#x60;AUTOMATIC&#x60; if it is an automatic redemption. | [optional] 
**related_object** | [**MemberActivityDataBalanceRelatedObject**](MemberActivityDataBalanceRelatedObject.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


