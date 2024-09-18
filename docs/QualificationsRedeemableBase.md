# QualificationsRedeemableBase

Data of single redeemable which was properly qualified.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the redeemable. | [optional] 
**object** | **str** | Object type of the redeemable. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the object was created. The value is shown in the ISO 8601 format. | [optional] 
**result** | [**RedeemableResult**](RedeemableResult.md) |  | [optional] 
**order** | [**OrderCalculated**](OrderCalculated.md) |  | [optional] 
**validation_rule_id** | **str** | A unique validation rule identifier assigned by the Voucherify API. The validation rule is verified before points are added to the balance. | [optional] 
**applicable_to** | [**ApplicableToResultList**](ApplicableToResultList.md) |  | [optional] 
**inapplicable_to** | [**InapplicableToResultList**](InapplicableToResultList.md) |  | [optional] 
**metadata** | **object** | The metadata object stores all custom attributes assigned to the product. A set of key/value pairs that you can attach to a product object. It can be useful for storing additional information about the product in a structured format. | [optional] 
**categories** | [**List[Category]**](Category.md) | List of category information. | [optional] 
**banner** | **str** | Name of the earning rule. This is displayed as a header for the earning rule in the Dashboard. | [optional] 
**name** | **str** | Name of the redeemable. | [optional] 
**campaign_name** | **str** | Name of the campaign associated to the redeemable. This field is available only if object is not &#x60;campaign&#x60; | [optional] 
**campaign_id** | **str** | Id of the campaign associated to the redeemable. This field is available only if object is not &#x60;campaign&#x60; | [optional] 
**validation_rules_assignments** | [**ValidationRulesAssignmentsList**](ValidationRulesAssignmentsList.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


