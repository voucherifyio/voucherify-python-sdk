# BenefitPointsProportionalApplicableTo

A single applicability rule. Exactly one of `product`, `sku`, or `products_collection` is required, matching the `type`. In requests, the other two may be omitted or set to `null`. In responses, they are omitted. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the referenced object. | [optional] 
**product** | [**LoyaltyV2ActivityBenefitPointsProportionalApplicableToProduct**](LoyaltyV2ActivityBenefitPointsProportionalApplicableToProduct.md) |  | [optional] 
**sku** | [**LoyaltyV2ActivityBenefitPointsProportionalApplicableToSku**](LoyaltyV2ActivityBenefitPointsProportionalApplicableToSku.md) |  | [optional] 
**products_collection** | [**LoyaltyV2ActivityBenefitPointsProportionalApplicableToProductsCollection**](LoyaltyV2ActivityBenefitPointsProportionalApplicableToProductsCollection.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


