# ManagementProjectsBrandingCreateRequestBodyCockpits

Defines customer cockpit details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaigns_overview_enabled** | **bool** | Enables the campaign overview for customers. | [optional] [default to False]
**loyalty_enabled** | **bool** | Enables the loyalty campaign overview for customers. | [optional] [default to True]
**gift_cards_enabled** | **bool** | Enables the gift card overview for customers. | [optional] [default to True]
**coupons_enabled** | **bool** | Enables the discount coupon overview for customers. | [optional] [default to True]
**referrals_enabled** | **bool** | Enables the referral campaign overview for customers. | [optional] [default to True]
**theme** | **str** | Determines the color scheme of the customer cockpit. | [optional] [default to 'default']
**use_custom_double_opt_in_redirect_url** | **bool** | Enables the double opt-in option. It must be a valid URL format. | [optional] [default to False]
**custom_double_opt_in_redirect_url** | **str** | Defines the URL for the double opt-in consent. It must be a valid URL format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


