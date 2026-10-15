# V2LoyaltiesBenefitsGetResponseBodyStock

Stock configuration of the benefit. When `type` is `LIMITED`, the `limited` object is required. When `type` is `UNLIMITED`, requests may omit `limited` or set it to `null`; responses omit it. The API validates field combinations that this schema does not express.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Whether the benefit has unlimited or limited stock. | [optional] 
**limited** | [**LoyaltyV2ActivityBenefitStockLimited**](LoyaltyV2ActivityBenefitStockLimited.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


