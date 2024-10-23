# ValidationRulesGetResponseBody

Response body schema for **GET** `v1/validation-rules/{validationRuleId}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Custom, unique name for set of validation rules. | [optional] 
**rules** | **object** | Contains all the rule definitions for the validation rule. It is a set of key value pairs representing the rules and logic between the rules. The keys are numbered consecutively beginning from &#x60;1&#x60;. The values are objects containing the rule conditions. | [optional] 
**error** | [**ValidationRulesGetResponseBodyError**](ValidationRulesGetResponseBodyError.md) |  | [optional] 
**applicable_to** | [**ValidationRulesGetResponseBodyApplicableTo**](ValidationRulesGetResponseBodyApplicableTo.md) |  | [optional] 
**type** | **str** | Type of validation rule. | [optional] [default to 'expression']
**context_type** | **str** | Validation rule context type.    | **Context Type** | **Definition** | |:---|:---| | earning_rule.order.paid |  | | earning_rule.custom_event |  | | earning_rule.customer.segment.entered |  | | campaign.discount_coupons |  | | campaign.discount_coupons.discount.apply_to_order |  | | campaign.discount_coupons.discount.apply_to_items |  | | campaign.discount_coupons.discount.apply_to_items_proportionally |  | | campaign.discount_coupons.discount.apply_to_items_proportionally_by_quantity |  | | campaign.discount_coupons.discount.fixed.apply_to_items |  | | campaign.gift_vouchers |  | | campaign.gift_vouchers.gift.apply_to_order |  | | campaign.gift_vouchers.gift.apply_to_items |  | | campaign.referral_program |  | | campaign.referral_program.discount.apply_to_order |  | | campaign.referral_program.discount.apply_to_items |  | | campaign.referral_program.discount.apply_to_items_proportionally |  | | campaign.referral_program.discount.apply_to_items_proportionally_by_quantity |  | | campaign.referral_program.discount.fixed.apply_to_items |  | | campaign.promotion |  | | campaign.promotion.discount.apply_to_order |  | | campaign.promotion.discount.apply_to_items |  | | campaign.promotion.discount.apply_to_items_proportionally |  | | campaign.promotion.discount.apply_to_items_proportionally_by_quantity |  | | campaign.promotion.discount.fixed.apply_to_items |  | | campaign.loyalty_program |  | | voucher.discount_voucher |  | | voucher.discount_voucher.discount.apply_to_order |  | | voucher.discount_voucher.discount.apply_to_items |  | | voucher.discount_voucher.discount.apply_to_items_proportionally |  | | voucher.discount_voucher.discount.apply_to_items_proportionally_by_quantity |  | | voucher.discount_voucher.discount.fixed.apply_to_items |  | | voucher.gift_voucher |  | | voucher.gift_voucher.gift.apply_to_order |  | | voucher.gift_voucher.gift.apply_to_items |  | | voucher.loyalty_card |  | | distribution.custom_event |  | | reward_assignment.pay_with_points |  | | global |  | | [optional] [default to 'global']
**id** | **str** | Unique validation rule ID. | [optional] 
**created_at** | **datetime** | Timestamp representing the date and time when the validation rule was created. The value is shown in the ISO 8601 format. | [optional] 
**updated_at** | **datetime** | Timestamp representing the date and time when the validation rule was updated. The value is shown in the ISO 8601 format. | [optional] 
**assignments_count** | **int** | The number of instances the validation rule has been assigned to different types of redeemables. | [optional] 
**object** | **str** | The type of the object represented by JSON. This object stores information about the validation rule. | [optional] [default to 'validation_rules']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

