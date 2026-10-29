# EarningRulePointsProportionalApplicableTo

Criterion selecting order items the calculation applies to. Depending on `type`, exactly one of `product`, `sku` or `products_collection` is required and the others must be null/absent. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of the referenced object. | [optional] 
**product** | [**LoyaltyV2ActivityEarningRulePointsProportionalApplicableToProduct**](LoyaltyV2ActivityEarningRulePointsProportionalApplicableToProduct.md) |  | [optional] 
**sku** | [**LoyaltyV2ActivityEarningRulePointsProportionalApplicableToSku**](LoyaltyV2ActivityEarningRulePointsProportionalApplicableToSku.md) |  | [optional] 
**products_collection** | [**LoyaltyV2ActivityEarningRulePointsProportionalApplicableToProductsCollection**](LoyaltyV2ActivityEarningRulePointsProportionalApplicableToProductsCollection.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


