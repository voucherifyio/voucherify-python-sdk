# MemberActivityData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**campaign** | [**SimpleCampaign**](SimpleCampaign.md) |  | [optional] 
**loyalty_tier_from** | [**LoyaltyTier**](LoyaltyTier.md) |  | [optional] 
**loyalty_tier_to** | [**LoyaltyTier**](LoyaltyTier.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**loyalty_tier** | [**LoyaltyTier**](LoyaltyTier.md) |  | [optional] 
**expiration_date** | **datetime** |  | [optional] 
**publication** | [**ListPublicationsItemValidSingleVoucher**](ListPublicationsItemValidSingleVoucher.md) |  | [optional] 
**order** | [**MemberActivityDataOrder**](MemberActivityDataOrder.md) |  | [optional] 
**voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**holder** | [**SimpleCustomer**](SimpleCustomer.md) |  | [optional] 
**promotion_tier** | [**SimplePromotionTier**](SimplePromotionTier.md) |  | [optional] 
**promotion_stack** | [**SimplePromotionStack**](SimplePromotionStack.md) |  | [optional] 
**redemption** | [**MemberActivityDataRedemption**](MemberActivityDataRedemption.md) |  | [optional] 
**redemption_rollback** | [**SimpleRedemption**](SimpleRedemption.md) |  | [optional] 
**reward** | [**SimpleRedemptionRewardResult**](SimpleRedemptionRewardResult.md) |  | [optional] 
**referral_tier** | [**SimpleReferralTier**](SimpleReferralTier.md) |  | [optional] 
**balance** | [**MemberActivityDataBalance**](MemberActivityDataBalance.md) |  | [optional] 
**custom_event** | [**CustomEvent**](CustomEvent.md) |  | [optional] 
**customer_event** | [**MemberActivityDataCustomerEvent**](MemberActivityDataCustomerEvent.md) |  | [optional] 
**earning_rule** | [**EarningRule**](EarningRule.md) |  | [optional] 
**event** | [**SimpleEvent**](SimpleEvent.md) |  | [optional] 
**reward_redemption** | **object** |  | [optional] 
**reward_assignment** | [**RewardAssignment**](RewardAssignment.md) |  | [optional] 
**source** | **str** |  | [optional] 
**transaction** | [**MemberActivityDataTransaction**](MemberActivityDataTransaction.md) |  | [optional] 
**pending_points** | [**LoyaltyPendingPoints**](LoyaltyPendingPoints.md) |  | [optional] 
**voucher_pending_points_balance** | [**VoucherBalance**](VoucherBalance.md) |  | [optional] 
**source_voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**destination_voucher** | [**SimpleVoucher**](SimpleVoucher.md) |  | [optional] 
**points** | **int** | The number of expired points. | [optional] 
**buckets** | [**List[LoyaltyPointsBucket]**](LoyaltyPointsBucket.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


