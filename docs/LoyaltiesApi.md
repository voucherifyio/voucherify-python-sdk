# voucherify.LoyaltiesApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member**](LoyaltiesApi.md#add_member) | **POST** /v1/loyalties/{campaignId}/members | Add Member
[**create_earning_rule**](LoyaltiesApi.md#create_earning_rule) | **POST** /v1/loyalties/{campaignId}/earning-rules | Create Earning Rule
[**create_in_bulk_loyalty_tiers**](LoyaltiesApi.md#create_in_bulk_loyalty_tiers) | **POST** /v1/loyalties/{campaignId}/tiers | Create loyalty tiers
[**create_loyalty_program**](LoyaltiesApi.md#create_loyalty_program) | **POST** /v1/loyalties | Create Loyalty Campaign
[**create_points_expiration_export**](LoyaltiesApi.md#create_points_expiration_export) | **POST** /v1/loyalties/{campaignId}/points-expiration/export | Create Points Expiration Export
[**create_reward_assignment1**](LoyaltiesApi.md#create_reward_assignment1) | **POST** /v1/loyalties/{campaignId}/rewards | Create Reward Assignment
[**delete_earning_rule**](LoyaltiesApi.md#delete_earning_rule) | **DELETE** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId} | Delete Earning Rule
[**delete_loyalty_program**](LoyaltiesApi.md#delete_loyalty_program) | **DELETE** /v1/loyalties/{campaignId} | Delete Loyalty Campaign
[**delete_reward_assignment1**](LoyaltiesApi.md#delete_reward_assignment1) | **DELETE** /v1/loyalties/{campaignId}/rewards/{assignmentId} | Delete Reward Assignment
[**disable_earning_rule**](LoyaltiesApi.md#disable_earning_rule) | **POST** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId}/disable | Disable Earning Rule
[**enable_earning_rule**](LoyaltiesApi.md#enable_earning_rule) | **POST** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId}/enable | Enable Earning Rule
[**export_loyalty_card_transactions**](LoyaltiesApi.md#export_loyalty_card_transactions) | **POST** /v1/loyalties/members/{memberId}/transactions/export | Export Loyalty Card Transactions
[**export_loyalty_card_transactions1**](LoyaltiesApi.md#export_loyalty_card_transactions1) | **POST** /v1/loyalties/{campaignId}/members/{memberId}/transactions/export | Export Loyalty Card Transactions
[**get_earning_rule**](LoyaltiesApi.md#get_earning_rule) | **GET** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId} | Get Earning Rule
[**get_loyalty_program**](LoyaltiesApi.md#get_loyalty_program) | **GET** /v1/loyalties/{campaignId} | Get Loyalty Campaign
[**get_loyalty_tier**](LoyaltiesApi.md#get_loyalty_tier) | **GET** /v1/loyalties/{campaignId}/tiers/{loyaltyTierId} | Get Loyalty Tier
[**get_member**](LoyaltiesApi.md#get_member) | **GET** /v1/loyalties/members/{memberId} | Get Member
[**get_member1**](LoyaltiesApi.md#get_member1) | **GET** /v1/loyalties/{campaignId}/members/{memberId} | Get Member
[**get_reward_assignment1**](LoyaltiesApi.md#get_reward_assignment1) | **GET** /v1/loyalties/{campaignId}/reward-assignments/{assignmentId} | Get Reward Assignment
[**get_reward_assignment2**](LoyaltiesApi.md#get_reward_assignment2) | **GET** /v1/loyalties/{campaignId}/rewards/{assignmentId} | Get Reward Assignment
[**get_reward_details**](LoyaltiesApi.md#get_reward_details) | **GET** /v1/loyalties/{campaignId}/reward-assignments/{assignmentId}/reward | Get Reward Details
[**list_earning_rules**](LoyaltiesApi.md#list_earning_rules) | **GET** /v1/loyalties/{campaignId}/earning-rules | List Earning Rules
[**list_loyalty_card_transactions**](LoyaltiesApi.md#list_loyalty_card_transactions) | **GET** /v1/loyalties/members/{memberId}/transactions | List Loyalty Card Transactions
[**list_loyalty_card_transactions1**](LoyaltiesApi.md#list_loyalty_card_transactions1) | **GET** /v1/loyalties/{campaignId}/members/{memberId}/transactions | List Loyalty Card Transactions
[**list_loyalty_programs**](LoyaltiesApi.md#list_loyalty_programs) | **GET** /v1/loyalties | List Loyalty Campaigns
[**list_loyalty_tier_earning_rules**](LoyaltiesApi.md#list_loyalty_tier_earning_rules) | **GET** /v1/loyalties/{campaignId}/tiers/{loyaltyTierId}/earning-rules | List Loyalty Tier Earning Rules
[**list_loyalty_tier_rewards**](LoyaltiesApi.md#list_loyalty_tier_rewards) | **GET** /v1/loyalties/{campaignId}/tiers/{loyaltyTierId}/rewards | List Loyalty Tier Rewards
[**list_loyalty_tiers**](LoyaltiesApi.md#list_loyalty_tiers) | **GET** /v1/loyalties/{campaignId}/tiers | List Loyalty Tiers
[**list_member_activity**](LoyaltiesApi.md#list_member_activity) | **GET** /v1/loyalties/members/{memberId}/activity | List Member Activity
[**list_member_activity1**](LoyaltiesApi.md#list_member_activity1) | **GET** /v1/loyalties/{campaignId}/members/{memberId}/activity | List Member Activity
[**list_member_loyalty_tier**](LoyaltiesApi.md#list_member_loyalty_tier) | **GET** /v1/loyalties/members/{memberId}/tiers | List Member&#39;s Loyalty Tiers
[**list_member_rewards**](LoyaltiesApi.md#list_member_rewards) | **GET** /v1/loyalties/members/{memberId}/rewards | List Member Rewards
[**list_members**](LoyaltiesApi.md#list_members) | **GET** /v1/loyalties/{campaignId}/members | List Members
[**list_points_expiration**](LoyaltiesApi.md#list_points_expiration) | **GET** /v1/loyalties/{campaignId}/members/{memberId}/points-expiration | Get Points Expiration
[**list_reward_assignments1**](LoyaltiesApi.md#list_reward_assignments1) | **GET** /v1/loyalties/{campaignId}/reward-assignments | List Reward Assignments
[**list_reward_assignments2**](LoyaltiesApi.md#list_reward_assignments2) | **GET** /v1/loyalties/{campaignId}/rewards | List Reward Assignments
[**redeem_reward**](LoyaltiesApi.md#redeem_reward) | **POST** /v1/loyalties/members/{memberId}/redemption | Redeem Reward
[**redeem_reward1**](LoyaltiesApi.md#redeem_reward1) | **POST** /v1/loyalties/{campaignId}/members/{memberId}/redemption | Redeem Reward
[**transfer_points**](LoyaltiesApi.md#transfer_points) | **POST** /v1/loyalties/{campaignId}/members/{memberId}/transfers | Transfer Loyalty Points
[**update_earning_rule**](LoyaltiesApi.md#update_earning_rule) | **PUT** /v1/loyalties/{campaignId}/earning-rules/{earningRuleId} | Update Earning Rule
[**update_loyalty_card_balance**](LoyaltiesApi.md#update_loyalty_card_balance) | **POST** /v1/loyalties/members/{memberId}/balance | Add or Remove Loyalty Card Balance
[**update_loyalty_card_balance1**](LoyaltiesApi.md#update_loyalty_card_balance1) | **POST** /v1/loyalties/{campaignId}/members/{memberId}/balance | Add or Remove Loyalty Card Balance
[**update_loyalty_program**](LoyaltiesApi.md#update_loyalty_program) | **PUT** /v1/loyalties/{campaignId} | Update Loyalty Campaign
[**update_reward_assignment1**](LoyaltiesApi.md#update_reward_assignment1) | **PUT** /v1/loyalties/{campaignId}/rewards/{assignmentId} | Update Reward Assignment


# **add_member**
> LoyaltiesMembersCreateResponseBody add_member(campaign_id, loyalties_members_create_request_body=loyalties_members_create_request_body)

Add Member

This method assigns a loyalty card to a customer. It selects a loyalty card suitable for publication, adds a publish entry, and returns the published voucher.   A voucher is suitable for publication when its active and hasnt been published yet.    📘 Auto-update campaign  In case you want to ensure the number of publishable codes increases automatically with the number of customers, you should use **auto-update** campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_create_request_body import LoyaltiesMembersCreateRequestBody
from voucherify.models.loyalties_members_create_response_body import LoyaltiesMembersCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID of the loyalty program.
    loyalties_members_create_request_body = {"customer":"source_customer_1","metadata":{"year":2022},"channel":"postman","voucher":"KpzbHUY5"} # LoyaltiesMembersCreateRequestBody | Provide details to whom the loyalty card should be assigned.     You can choose to either specify the exact loyalty card code that you want to publish from existin (non-assigned) codes, or choose not to specify a voucher code. If you choose not to specify a code in the request paylaod, then the system will choose the next available voucher code available to be assigned to a customer.   You can also include metadata in the request payload. This metadata will be assigned to the publication object, but will not be returned in the response to this endpoint. To see of publications (assignments of particular codes to customers) and publication metadata, use the List Publications endpoint. (optional)

    try:
        # Add Member
        api_response = api_instance.add_member(campaign_id, loyalties_members_create_request_body=loyalties_members_create_request_body)
        print("The response of LoyaltiesApi->add_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->add_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID of the loyalty program. | 
 **loyalties_members_create_request_body** | [**LoyaltiesMembersCreateRequestBody**](LoyaltiesMembersCreateRequestBody.md)| Provide details to whom the loyalty card should be assigned.     You can choose to either specify the exact loyalty card code that you want to publish from existin (non-assigned) codes, or choose not to specify a voucher code. If you choose not to specify a code in the request paylaod, then the system will choose the next available voucher code available to be assigned to a customer.   You can also include metadata in the request payload. This metadata will be assigned to the publication object, but will not be returned in the response to this endpoint. To see of publications (assignments of particular codes to customers) and publication metadata, use the List Publications endpoint. | [optional] 

### Return type

[**LoyaltiesMembersCreateResponseBody**](LoyaltiesMembersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the voucher object that was published to the customer provided in the request payload. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_earning_rule**
> List[LoyaltiesEarningRulesCreateResponseBody] create_earning_rule(campaign_id, loyalties_earning_rules_create_request_body_item=loyalties_earning_rules_create_request_body_item)

Create Earning Rule

Create earning rules for a loyalty campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_earning_rules_create_request_body_item import LoyaltiesEarningRulesCreateRequestBodyItem
from voucherify.models.loyalties_earning_rules_create_response_body import LoyaltiesEarningRulesCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    loyalties_earning_rules_create_request_body_item = [{"event":"order.paid","validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"type":"FIXED","points":"5"},"source":{"banner":"Order paid 5 points."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid - fixed amount of points"}},{"event":"order.paid","validation_rule_id":null,"loyalty":{"type":"PROPORTIONAL","calculation_type":"ORDER_AMOUNT","order":{"amount":{"every":1,"points":1}}},"source":{"banner":"Order paid - 1 point for 1 dollar spent excluding discounts."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid- points proportional to order amount"}},{"event":"order.paid","validation_rule_id":null,"loyalty":{"type":"PROPORTIONAL","calculation_type":"ORDER_TOTAL_AMOUNT","order":{"total_amount":{"every":1,"points":1}}},"source":{"banner":"Order paid - 1 point for 1 dollar spent including discounts."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid- points proportional to order total amount"}},{"event":"order.paid","validation_rule_id":null,"loyalty":{"type":"PROPORTIONAL","calculation_type":"ORDER_METADATA","order":{"metadata":{"every":2,"points":1,"property":"number_of_store_visits"}}},"source":{"banner":"Order paid - 2 points for each store visit."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid- points proportional to numerical order metadata property "}},{"event":"order.paid","validation_rule_id":null,"loyalty":{"type":"PROPORTIONAL","calculation_type":"ORDER_ITEMS_AMOUNT","order_items":{"amount":{"every":2,"points":1,"object":"product","id":"prod_0bae32322150fd0546"}}},"source":{"banner":"Order paid - 2 points for 1 dollar spent on items excluding discounts."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid- points proportional to order items amount"}},{"event":"order.paid","validation_rule_id":null,"loyalty":{"type":"PROPORTIONAL","calculation_type":"ORDER_ITEMS_SUBTOTAL_AMOUNT","order_items":{"subtotal_amount":{"every":2,"points":1,"object":"products_collection","id":"pc_75U0dHlr7u75BJodrW1AE3t6"}}},"source":{"banner":"Order paid - 2 points for every dollar spent on the product collection."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid- points proportional to order items subtotal amount"}},{"event":"order.paid","validation_rule_id":null,"loyalty":{"type":"PROPORTIONAL","calculation_type":"ORDER_ITEMS_QUANTITY","order_items":{"quantity":{"every":1,"points":1,"object":"sku","id":"sku_0b7d7dfb090be5c619"}}},"source":{"banner":"Order paid - 1 point for every brand phone in your cart."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid - points proportional to quantity of items in a cart of a product varient."}},{"event":"order.paid","validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"type":"PROPORTIONAL","calculation_type":"CUSTOMER_METADATA","customer":{"metadata":{"every":1,"points":1,"property":"customer_life_time_value"}}},"source":{"banner":"Order paid 1 point for 1 month of being a customer with us."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid - points proportional to customer metadata property"}},{"event":"customer.segment.entered","segment":{"id":"seg_OlE7DmfzMI5pHyD5VAv512r1"},"validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"type":"PROPORTIONAL","calculation_type":"CUSTOMER_METADATA","customer":{"metadata":{"every":1,"points":1,"property":"customer_life_time_value"}}},"source":{"banner":"Customer entered birthday segment - 1 point for each month of being a customer with us."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Entered segment - points proportional to customer metadata property"}},{"event":"customer.segment.entered","segment":{"id":"seg_OlE7DmfzMI5pHyD5VAv512r1"},"validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"type":"FIXED","points":"5"},"source":{"banner":"Customer entered birthday segment - 5 points"},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Entered segment - fixed points"}},{"event":"page_view","validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"points":3,"type":"FIXED"},"custom_event":{"schema_id":"ms_gn4Qe4xsFPf7orCArCiNVY13"},"source":{"banner":"See page - 3 points"},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Custom Event - fixed points for viewing a page"}},{"event":"page_view","validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"type":"PROPORTIONAL","calculation_type":"CUSTOM_EVENT_METADATA","custom_event":{"metadata":{"every":1,"points":2,"property":"volume_number"}}},"custom_event":{"schema_id":"ms_gn4Qe4xsFPf7orCArCiNVY13"},"source":{"banner":"See page X - get 2 points multiplied by the page number"},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Custom Event - proportional points for viewing a page based on custom event metadata"}},{"event":"page_view","validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"type":"PROPORTIONAL","calculation_type":"CUSTOMER_METADATA","customer":{"metadata":{"every":1,"points":2,"property":"customer_life_time_value"}}},"custom_event":{"schema_id":"ms_gn4Qe4xsFPf7orCArCiNVY13"},"source":{"banner":"Get 2 points for every month you're a customer for viewing a page"},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Custom Event - proportional points for viewing a page based on customer metadata"}},{"event":"customer.loyalty.tier.prolonged","validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"type":"PROPORTIONAL","calculation_type":"CUSTOMER_METADATA","customer":{"metadata":{"every":1,"points":2,"property":"customer_life_time_value"}}},"loyalty_tier":{"id":"ltr_pudTGWasuIqxdiDM0go31OV1"},"source":{"banner":"Get 2 points for every month you're a customer when your loyalty tier is prolonged."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Custom Event - proportional points for extending a loyalty tier based on customer metadata."}}] # List[LoyaltiesEarningRulesCreateRequestBodyItem] | Customize the request body based on the type of earning rules you would like to create. The request body is an array of objects. The required minimum properties to include in the payload for each object are event and loyalty. Additionally, if you choose to add a validity_timeframe, you must include a start_date. Furthermore, an earning rule event type:   - customer.segment.entered requires a segment object - a custom event requires a custom_event object - a customer.loyalty.tier.joined, customer.loyalty.tier.left, customer.loyalty.tier.upgraded, customer.loyalty.tier.downgraded, customer.loyalty.tier.prolonged requires a loyalty_tier object (optional)

    try:
        # Create Earning Rule
        api_response = api_instance.create_earning_rule(campaign_id, loyalties_earning_rules_create_request_body_item=loyalties_earning_rules_create_request_body_item)
        print("The response of LoyaltiesApi->create_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->create_earning_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **loyalties_earning_rules_create_request_body_item** | [**List[LoyaltiesEarningRulesCreateRequestBodyItem]**](LoyaltiesEarningRulesCreateRequestBodyItem.md)| Customize the request body based on the type of earning rules you would like to create. The request body is an array of objects. The required minimum properties to include in the payload for each object are event and loyalty. Additionally, if you choose to add a validity_timeframe, you must include a start_date. Furthermore, an earning rule event type:   - customer.segment.entered requires a segment object - a custom event requires a custom_event object - a customer.loyalty.tier.joined, customer.loyalty.tier.left, customer.loyalty.tier.upgraded, customer.loyalty.tier.downgraded, customer.loyalty.tier.prolonged requires a loyalty_tier object | [optional] 

### Return type

[**List[LoyaltiesEarningRulesCreateResponseBody]**](LoyaltiesEarningRulesCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an array of earning rule objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_in_bulk_loyalty_tiers**
> List[LoyaltyTier] create_in_bulk_loyalty_tiers(campaign_id, loyalties_tiers_create_in_bulk_request_body_item=loyalties_tiers_create_in_bulk_request_body_item)

Create loyalty tiers

Creates loyalty tiers for desired campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_tiers_create_in_bulk_request_body_item import LoyaltiesTiersCreateInBulkRequestBodyItem
from voucherify.models.loyalty_tier import LoyaltyTier
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique loyalty campaign ID or name.
    loyalties_tiers_create_in_bulk_request_body_item = [voucherify.LoyaltiesTiersCreateInBulkRequestBodyItem()] # List[LoyaltiesTiersCreateInBulkRequestBodyItem] | Provide tier definitions you want to add to existing loyalty campaign. (optional)

    try:
        # Create loyalty tiers
        api_response = api_instance.create_in_bulk_loyalty_tiers(campaign_id, loyalties_tiers_create_in_bulk_request_body_item=loyalties_tiers_create_in_bulk_request_body_item)
        print("The response of LoyaltiesApi->create_in_bulk_loyalty_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->create_in_bulk_loyalty_tiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique loyalty campaign ID or name. | 
 **loyalties_tiers_create_in_bulk_request_body_item** | [**List[LoyaltiesTiersCreateInBulkRequestBodyItem]**](LoyaltiesTiersCreateInBulkRequestBodyItem.md)| Provide tier definitions you want to add to existing loyalty campaign. | [optional] 

### Return type

[**List[LoyaltyTier]**](LoyaltyTier.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns created loyalty tiers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loyalty_program**
> LoyaltiesCreateCampaignResponseBody create_loyalty_program(loyalties_create_campaign_request_body=loyalties_create_campaign_request_body)

Create Loyalty Campaign

Creates a batch of loyalty cards aggregated in a single loyalty campaign. It also allows you to define a custom codes pattern.    📘 Global uniqueness  All codes are unique across the whole project. Voucherify wont allow to generate the same codes in any of your campaigns.  🚧 Asyncronous action!  This is an asynchronous action, you cant read or modify a newly created campaign until the code generation is completed. See creation_status field in the loyalty campaign object description.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_create_campaign_request_body import LoyaltiesCreateCampaignRequestBody
from voucherify.models.loyalties_create_campaign_response_body import LoyaltiesCreateCampaignResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    loyalties_create_campaign_request_body = {"name":"Loyalty Program 4","description":"This is a campaign description.","auto_join":true,"join_once":true,"use_voucher_metadata_schema":true,"start_date":"2016-10-26T00:00:00Z","expiration_date":"2024-10-26T00:00:00Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"activity_duration_after_publishing":"P24D","category_id":"cat_0b6152ce12414820dc","vouchers_count":2,"voucher":{"type":"LOYALTY_CARD","loyalty_card":{"points":0,"expiration_rules":{"period_type":"MONTH","period_value":3,"rounding_type":"END_OF_QUARTER"}},"redemption":{"quantity":2},"code_config":{"pattern":"L-CARD-#######"}},"metadata":{"test":true},"type":"STATIC","loyalty_tiers_expiration":{"qualification_type":"BALANCE","start_date":{"type":"IMMEDIATE"},"expiration_date":{"type":"CUSTOM","extend":"P3M","rounding":{"type":"MONTH","strategy":"END"}}}} # LoyaltiesCreateCampaignRequestBody | Specify the loyalty campaign details. (optional)

    try:
        # Create Loyalty Campaign
        api_response = api_instance.create_loyalty_program(loyalties_create_campaign_request_body=loyalties_create_campaign_request_body)
        print("The response of LoyaltiesApi->create_loyalty_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->create_loyalty_program: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loyalties_create_campaign_request_body** | [**LoyaltiesCreateCampaignRequestBody**](LoyaltiesCreateCampaignRequestBody.md)| Specify the loyalty campaign details. | [optional] 

### Return type

[**LoyaltiesCreateCampaignResponseBody**](LoyaltiesCreateCampaignResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a campaign object with its settings but without the loyalty card codes. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_points_expiration_export**
> LoyaltiesPointsExpirationExportCreateResponseBody create_points_expiration_export(campaign_id, loyalties_points_expiration_export_create_request_body=loyalties_points_expiration_export_create_request_body)

Create Points Expiration Export

Schedule the generation of a points expiration CSV file for a particular campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_points_expiration_export_create_request_body import LoyaltiesPointsExpirationExportCreateRequestBody
from voucherify.models.loyalties_points_expiration_export_create_response_body import LoyaltiesPointsExpirationExportCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    loyalties_points_expiration_export_create_request_body = {"parameters":{"fields":["id","campaign_id","voucher_id","status","expires_at","points"],"order":"-expires_at","filters":{"junction":"and","voucher_id":{"conditions":{"$in":["v_0aMj6Mdp0i3zuXrd9NnBKboc7746mlgF","v_YLn0WVWXSXbUfDvxgrgUbtfJ3SQIY655"]}}}}} # LoyaltiesPointsExpirationExportCreateRequestBody | Specify the data filters, types of data to return and order in which the results should be returned. (optional)

    try:
        # Create Points Expiration Export
        api_response = api_instance.create_points_expiration_export(campaign_id, loyalties_points_expiration_export_create_request_body=loyalties_points_expiration_export_create_request_body)
        print("The response of LoyaltiesApi->create_points_expiration_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->create_points_expiration_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **loyalties_points_expiration_export_create_request_body** | [**LoyaltiesPointsExpirationExportCreateRequestBody**](LoyaltiesPointsExpirationExportCreateRequestBody.md)| Specify the data filters, types of data to return and order in which the results should be returned. | [optional] 

### Return type

[**LoyaltiesPointsExpirationExportCreateResponseBody**](LoyaltiesPointsExpirationExportCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an object with the export ID of the scheduled generation of CSV file with exported points expirations. You can use either the &lt;!-- [Get Export](OpenAPI.json/paths/~1exports~1{exportId}/get) --&gt;[Get Export](ref:get-export) endpoint to view the status and obtain the URL of the CSV file or &lt;!-- [Download Export](OpenAPI.json/paths/~1exports~1{export_Id}/get) --&gt;[Download Export](ref:download-export) endpoint to download the CSV file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_reward_assignment1**
> LoyaltiesRewardsCreateAssignmentResponseBody create_reward_assignment1(campaign_id, loyalties_rewards_create_assignment_item_request_body=loyalties_rewards_create_assignment_item_request_body)

Create Reward Assignment

Add rewards to a loyalty campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_rewards_create_assignment_item_request_body import LoyaltiesRewardsCreateAssignmentItemRequestBody
from voucherify.models.loyalties_rewards_create_assignment_response_body import LoyaltiesRewardsCreateAssignmentResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    loyalties_rewards_create_assignment_item_request_body = [{"reward":"rew_wg2pvCr5LDhCq4uVQZ9LhuZm","parameters":{"loyalty":{"points":2}}},{"reward":"rew_z35ffKoH0tCcck8EL56p6SIs","parameters":{"loyalty":{"points":2}}}] # List[LoyaltiesRewardsCreateAssignmentItemRequestBody] | Define the cost of the rewards in loyalty points. (optional)

    try:
        # Create Reward Assignment
        api_response = api_instance.create_reward_assignment1(campaign_id, loyalties_rewards_create_assignment_item_request_body=loyalties_rewards_create_assignment_item_request_body)
        print("The response of LoyaltiesApi->create_reward_assignment1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->create_reward_assignment1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **loyalties_rewards_create_assignment_item_request_body** | [**List[LoyaltiesRewardsCreateAssignmentItemRequestBody]**](LoyaltiesRewardsCreateAssignmentItemRequestBody.md)| Define the cost of the rewards in loyalty points. | [optional] 

### Return type

[**LoyaltiesRewardsCreateAssignmentResponseBody**](LoyaltiesRewardsCreateAssignmentResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of reward assignment objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_earning_rule**
> delete_earning_rule(campaign_id, earning_rule_id)

Delete Earning Rule

This method deletes an earning rule for a specific loyalty campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    earning_rule_id = 'earning_rule_id_example' # str | A unique earning rule ID.

    try:
        # Delete Earning Rule
        api_instance.delete_earning_rule(campaign_id, earning_rule_id)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->delete_earning_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **earning_rule_id** | **str**| A unique earning rule ID. | 

### Return type

void (empty response body)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if deletion is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_loyalty_program**
> LoyaltiesDeleteResponseBody delete_loyalty_program(campaign_id, force=force)

Delete Loyalty Campaign

Deletes a loyalty campaign and all related loyalty cards. This action cannot be undone. Also, it immediately removes any redemptions on loyalty cards. If the force parameter is set to false or not set at all, the loyalty campaign and all related loyalty cards will be moved to the bin.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_delete_response_body import LoyaltiesDeleteResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    force = True # bool | If this flag is set to true, the campaign and related vouchers will be removed permanently. If it is set to false or not set at all, the loyalty campaign and all related loyalty cards will be moved to the bin. Going forward, the user will be able to create the next campaign with the same name. (optional)

    try:
        # Delete Loyalty Campaign
        api_response = api_instance.delete_loyalty_program(campaign_id, force=force)
        print("The response of LoyaltiesApi->delete_loyalty_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->delete_loyalty_program: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **force** | **bool**| If this flag is set to true, the campaign and related vouchers will be removed permanently. If it is set to false or not set at all, the loyalty campaign and all related loyalty cards will be moved to the bin. Going forward, the user will be able to create the next campaign with the same name. | [optional] 

### Return type

[**LoyaltiesDeleteResponseBody**](LoyaltiesDeleteResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the ID of the scheduled asynchronous action, informing you that your request has been accepted and the loyalty campaign will be deleted from the repository asynchronously. To check the deletion status and result, copy the &#x60;async_action_id&#x60; from the response and pass it using &lt;!-- [Get Async Action](OpenAPI.json/paths/~1async-actions~1{asyncActionId}/get) --&gt;[Get Async Action](ref:get-async-action) endpoint. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_reward_assignment1**
> delete_reward_assignment1(campaign_id, assignment_id)

Delete Reward Assignment

This method deletes a reward assignment for a particular loyalty campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID.

    try:
        # Delete Reward Assignment
        api_instance.delete_reward_assignment1(campaign_id, assignment_id)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->delete_reward_assignment1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **assignment_id** | **str**| A unique reward assignment ID. | 

### Return type

void (empty response body)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns no content if deletion is successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_earning_rule**
> LoyaltiesEarningRulesDisableResponseBody disable_earning_rule(campaign_id, earning_rule_id)

Disable Earning Rule

Disable an earning rule.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_earning_rules_disable_response_body import LoyaltiesEarningRulesDisableResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    earning_rule_id = 'earning_rule_id_example' # str | Unique earning rule ID.

    try:
        # Disable Earning Rule
        api_response = api_instance.disable_earning_rule(campaign_id, earning_rule_id)
        print("The response of LoyaltiesApi->disable_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->disable_earning_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **earning_rule_id** | **str**| Unique earning rule ID. | 

### Return type

[**LoyaltiesEarningRulesDisableResponseBody**](LoyaltiesEarningRulesDisableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an earning rule object with the &#x60;active&#x60; parameter set to &#x60;false&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_earning_rule**
> LoyaltiesEarningRulesEnableResponseBody enable_earning_rule(campaign_id, earning_rule_id)

Enable Earning Rule

Enable an earning rule.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_earning_rules_enable_response_body import LoyaltiesEarningRulesEnableResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    earning_rule_id = 'earning_rule_id_example' # str | Unique earning rule ID.

    try:
        # Enable Earning Rule
        api_response = api_instance.enable_earning_rule(campaign_id, earning_rule_id)
        print("The response of LoyaltiesApi->enable_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->enable_earning_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **earning_rule_id** | **str**| Unique earning rule ID. | 

### Return type

[**LoyaltiesEarningRulesEnableResponseBody**](LoyaltiesEarningRulesEnableResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an earning rule object with the &#x60;active&#x60; parameter set to &#x60;true&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_card_transactions**
> LoyaltiesMembersTransactionsExportCreateResponseBody export_loyalty_card_transactions(member_id, loyalties_members_transactions_export_create_request_body=loyalties_members_transactions_export_create_request_body)

Export Loyalty Card Transactions

Export transactions that are associated with point movements on a loyalty card.   

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_transactions_export_create_request_body import LoyaltiesMembersTransactionsExportCreateRequestBody
from voucherify.models.loyalties_members_transactions_export_create_response_body import LoyaltiesMembersTransactionsExportCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card that you are looking to export transaction data for.
    loyalties_members_transactions_export_create_request_body = {"parameters":{"order":"-created_at","fields":["id","type","source_id","reason","balance","amount","created_at","voucher_id","campaign_id","details","related_transaction_id"]}} # LoyaltiesMembersTransactionsExportCreateRequestBody | Specify the parameters and filters for the transaction export. (optional)

    try:
        # Export Loyalty Card Transactions
        api_response = api_instance.export_loyalty_card_transactions(member_id, loyalties_members_transactions_export_create_request_body=loyalties_members_transactions_export_create_request_body)
        print("The response of LoyaltiesApi->export_loyalty_card_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->export_loyalty_card_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| A unique code identifying the loyalty card that you are looking to export transaction data for. | 
 **loyalties_members_transactions_export_create_request_body** | [**LoyaltiesMembersTransactionsExportCreateRequestBody**](LoyaltiesMembersTransactionsExportCreateRequestBody.md)| Specify the parameters and filters for the transaction export. | [optional] 

### Return type

[**LoyaltiesMembersTransactionsExportCreateResponseBody**](LoyaltiesMembersTransactionsExportCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an export object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_loyalty_card_transactions1**
> LoyaltiesMembersTransactionsExportCreateResponseBody export_loyalty_card_transactions1(campaign_id, member_id, loyalties_members_transactions_export_create_request_body=loyalties_members_transactions_export_create_request_body)

Export Loyalty Card Transactions

Export transactions that are associated with point movements on a loyalty card.   

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_transactions_export_create_request_body import LoyaltiesMembersTransactionsExportCreateRequestBody
from voucherify.models.loyalties_members_transactions_export_create_response_body import LoyaltiesMembersTransactionsExportCreateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | A unique identifier of the loyalty campaign containing the voucher whose transactions you would like to export.
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card that you are looking to export transaction data for.
    loyalties_members_transactions_export_create_request_body = {"parameters":{"order":"-created_at","fields":["id","type","source_id","reason","balance","amount","created_at","voucher_id","campaign_id","details","related_transaction_id"]}} # LoyaltiesMembersTransactionsExportCreateRequestBody | Specify the parameters and filters for the transaction export. (optional)

    try:
        # Export Loyalty Card Transactions
        api_response = api_instance.export_loyalty_card_transactions1(campaign_id, member_id, loyalties_members_transactions_export_create_request_body=loyalties_members_transactions_export_create_request_body)
        print("The response of LoyaltiesApi->export_loyalty_card_transactions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->export_loyalty_card_transactions1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| A unique identifier of the loyalty campaign containing the voucher whose transactions you would like to export. | 
 **member_id** | **str**| A unique code identifying the loyalty card that you are looking to export transaction data for. | 
 **loyalties_members_transactions_export_create_request_body** | [**LoyaltiesMembersTransactionsExportCreateRequestBody**](LoyaltiesMembersTransactionsExportCreateRequestBody.md)| Specify the parameters and filters for the transaction export. | [optional] 

### Return type

[**LoyaltiesMembersTransactionsExportCreateResponseBody**](LoyaltiesMembersTransactionsExportCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an export object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_earning_rule**
> LoyaltiesEarningRulesGetResponseBody get_earning_rule(campaign_id, earning_rule_id)

Get Earning Rule

Retrieves an earning rule assigned to a campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_earning_rules_get_response_body import LoyaltiesEarningRulesGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    earning_rule_id = 'earning_rule_id_example' # str | A unique earning rule ID.

    try:
        # Get Earning Rule
        api_response = api_instance.get_earning_rule(campaign_id, earning_rule_id)
        print("The response of LoyaltiesApi->get_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_earning_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **earning_rule_id** | **str**| A unique earning rule ID. | 

### Return type

[**LoyaltiesEarningRulesGetResponseBody**](LoyaltiesEarningRulesGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns an earning rule object with the earning rule details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_program**
> LoyaltiesGetCampaignResponseBody get_loyalty_program(campaign_id)

Get Loyalty Campaign

Retrieve a specific loyalty campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_get_campaign_response_body import LoyaltiesGetCampaignResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 

    try:
        # Get Loyalty Campaign
        api_response = api_instance.get_loyalty_program(campaign_id)
        print("The response of LoyaltiesApi->get_loyalty_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_loyalty_program: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 

### Return type

[**LoyaltiesGetCampaignResponseBody**](LoyaltiesGetCampaignResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a loyalty campaign object for a given loyalty campaign ID.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loyalty_tier**
> LoyaltiesTiersGetResponseBody get_loyalty_tier(campaign_id, loyalty_tier_id)

Get Loyalty Tier

Retrieve a loyalty tier from a loyalty campaign by the loyalty tier ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_tiers_get_response_body import LoyaltiesTiersGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique loyalty campaign ID or name.
    loyalty_tier_id = 'loyalty_tier_id_example' # str | Unique loyalty tier ID.

    try:
        # Get Loyalty Tier
        api_response = api_instance.get_loyalty_tier(campaign_id, loyalty_tier_id)
        print("The response of LoyaltiesApi->get_loyalty_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_loyalty_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique loyalty campaign ID or name. | 
 **loyalty_tier_id** | **str**| Unique loyalty tier ID. | 

### Return type

[**LoyaltiesTiersGetResponseBody**](LoyaltiesTiersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a loyalty tier object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member**
> LoyaltiesMembersGetResponseBody get_member(member_id)

Get Member

Retrieve loyalty card with the given member ID (i.e. voucher code).      📘 Alternative endpoint  This endpoint is an alternative to this endpoint. The URL was re-designed to allow you to retrieve loyalty card details without having to provide the campaignId as a path parameter.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_get_response_body import LoyaltiesMembersGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card code assigned to a particular customer.

    try:
        # Get Member
        api_response = api_instance.get_member(member_id)
        print("The response of LoyaltiesApi->get_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card code assigned to a particular customer. | 

### Return type

[**LoyaltiesMembersGetResponseBody**](LoyaltiesMembersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns loyalty card details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member1**
> LoyaltiesMembersGetResponseBody get_member1(campaign_id, member_id)

Get Member

Retrieves the loyalty card with the given member ID (i.e. voucher code).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_get_response_body import LoyaltiesMembersGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID.
    member_id = 'member_id_example' # str | Unique code that identifies the loyalty card.

    try:
        # Get Member
        api_response = api_instance.get_member1(campaign_id, member_id)
        print("The response of LoyaltiesApi->get_member1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_member1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID. | 
 **member_id** | **str**| Unique code that identifies the loyalty card. | 

### Return type

[**LoyaltiesMembersGetResponseBody**](LoyaltiesMembersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns loyalty card details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_assignment1**
> LoyaltiesRewardAssignmentsGetResponseBody get_reward_assignment1(campaign_id, assignment_id)

Get Reward Assignment

Retrieve specific reward assignment.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_reward_assignments_get_response_body import LoyaltiesRewardAssignmentsGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    assignment_id = 'assignment_id_example' # str | Unique reward assignment ID.

    try:
        # Get Reward Assignment
        api_response = api_instance.get_reward_assignment1(campaign_id, assignment_id)
        print("The response of LoyaltiesApi->get_reward_assignment1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_reward_assignment1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **assignment_id** | **str**| Unique reward assignment ID. | 

### Return type

[**LoyaltiesRewardAssignmentsGetResponseBody**](LoyaltiesRewardAssignmentsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns specific reward assignment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_assignment2**
> LoyaltiesRewardsGetResponseBody get_reward_assignment2(campaign_id, assignment_id)

Get Reward Assignment

Retrieve specific reward assignment.  📘 Alternative endpoint  This endpoint is an alternative to this endpoint. 

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_rewards_get_response_body import LoyaltiesRewardsGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID.

    try:
        # Get Reward Assignment
        api_response = api_instance.get_reward_assignment2(campaign_id, assignment_id)
        print("The response of LoyaltiesApi->get_reward_assignment2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_reward_assignment2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **assignment_id** | **str**| A unique reward assignment ID. | 

### Return type

[**LoyaltiesRewardsGetResponseBody**](LoyaltiesRewardsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns specific reward assignment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reward_details**
> LoyaltiesRewardAssignmentsRewardGetResponseBody get_reward_details(campaign_id, assignment_id)

Get Reward Details

Get reward details in the context of a loyalty campaign and reward assignment ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_reward_assignments_reward_get_response_body import LoyaltiesRewardAssignmentsRewardGetResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    assignment_id = 'assignment_id_example' # str | Unique reward assignment ID.

    try:
        # Get Reward Details
        api_response = api_instance.get_reward_details(campaign_id, assignment_id)
        print("The response of LoyaltiesApi->get_reward_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->get_reward_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **assignment_id** | **str**| Unique reward assignment ID. | 

### Return type

[**LoyaltiesRewardAssignmentsRewardGetResponseBody**](LoyaltiesRewardAssignmentsRewardGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns reward details in the context of a loyalty *campaign* and reward assignment ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_earning_rules**
> LoyaltiesEarningRulesListResponseBody list_earning_rules(campaign_id, limit=limit, page=page, order=order)

List Earning Rules

Returns a list of all earning rules within a given campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_earning_rules_list_response_body import LoyaltiesEarningRulesListResponseBody
from voucherify.models.parameter_order_list_earning_rules import ParameterOrderListEarningRules
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListEarningRules() # ParameterOrderListEarningRules | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Earning Rules
        api_response = api_instance.list_earning_rules(campaign_id, limit=limit, page=page, order=order)
        print("The response of LoyaltiesApi->list_earning_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_earning_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListEarningRules**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**LoyaltiesEarningRulesListResponseBody**](LoyaltiesEarningRulesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of earning rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_card_transactions**
> LoyaltiesMembersTransactionsListResponseBody list_loyalty_card_transactions(member_id, limit=limit, order=order, starting_after_id=starting_after_id)

List Loyalty Card Transactions

Retrieve transaction data related to point movements for a specific loyalty card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_transactions_list_response_body import LoyaltiesMembersTransactionsListResponseBody
from voucherify.models.parameter_order_list_transactions import ParameterOrderListTransactions
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card that you are looking to retrieve transaction data for.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderListTransactions() # ParameterOrderListTransactions | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the transactions starting after a transaction with the given ID. (optional)

    try:
        # List Loyalty Card Transactions
        api_response = api_instance.list_loyalty_card_transactions(member_id, limit=limit, order=order, starting_after_id=starting_after_id)
        print("The response of LoyaltiesApi->list_loyalty_card_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_card_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| A unique code identifying the loyalty card that you are looking to retrieve transaction data for. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderListTransactions**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the transactions starting after a transaction with the given ID. | [optional] 

### Return type

[**LoyaltiesMembersTransactionsListResponseBody**](LoyaltiesMembersTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of loyalty card transaction objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_card_transactions1**
> LoyaltiesMembersTransactionsListResponseBody list_loyalty_card_transactions1(campaign_id, member_id, limit=limit, order=order, starting_after_id=starting_after_id)

List Loyalty Card Transactions

Retrieve transaction data related to point movements for a specific loyalty card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_transactions_list_response_body import LoyaltiesMembersTransactionsListResponseBody
from voucherify.models.parameter_order_list_transactions import ParameterOrderListTransactions
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | A unique identifier of the loyalty campaign containing the voucher whose transactions you would like to return.
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card that you are looking to retrieve transaction data for.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderListTransactions() # ParameterOrderListTransactions | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the transactions starting after a transaction with the given ID. (optional)

    try:
        # List Loyalty Card Transactions
        api_response = api_instance.list_loyalty_card_transactions1(campaign_id, member_id, limit=limit, order=order, starting_after_id=starting_after_id)
        print("The response of LoyaltiesApi->list_loyalty_card_transactions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_card_transactions1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| A unique identifier of the loyalty campaign containing the voucher whose transactions you would like to return. | 
 **member_id** | **str**| A unique code identifying the loyalty card that you are looking to retrieve transaction data for. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderListTransactions**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the transactions starting after a transaction with the given ID. | [optional] 

### Return type

[**LoyaltiesMembersTransactionsListResponseBody**](LoyaltiesMembersTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of loyalty card transaction objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_programs**
> LoyaltiesListCampaignsResponseBody list_loyalty_programs(limit=limit, page=page, order=order)

List Loyalty Campaigns

Returns a list of your loyalty campaigns.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_list_campaigns_response_body import LoyaltiesListCampaignsResponseBody
from voucherify.models.parameter_order_list_campaigns import ParameterOrderListCampaigns
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    order = voucherify.ParameterOrderListCampaigns() # ParameterOrderListCampaigns | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Loyalty Campaigns
        api_response = api_instance.list_loyalty_programs(limit=limit, page=page, order=order)
        print("The response of LoyaltiesApi->list_loyalty_programs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_programs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **order** | [**ParameterOrderListCampaigns**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**LoyaltiesListCampaignsResponseBody**](LoyaltiesListCampaignsResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with loyalty program objects. The loyalty campaigns are returned sorted by creation date, with the most recent campaigns appearing first. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_tier_earning_rules**
> LoyaltiesTiersEarningRulesListResponseBody list_loyalty_tier_earning_rules(campaign_id, loyalty_tier_id, limit=limit, page=page)

List Loyalty Tier Earning Rules

Retrieve available earning rules for a given tier and the calculation method for earning points.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_tiers_earning_rules_list_response_body import LoyaltiesTiersEarningRulesListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    loyalty_tier_id = 'loyalty_tier_id_example' # str | Unique loyalty tier ID.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)

    try:
        # List Loyalty Tier Earning Rules
        api_response = api_instance.list_loyalty_tier_earning_rules(campaign_id, loyalty_tier_id, limit=limit, page=page)
        print("The response of LoyaltiesApi->list_loyalty_tier_earning_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_tier_earning_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **loyalty_tier_id** | **str**| Unique loyalty tier ID. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 

### Return type

[**LoyaltiesTiersEarningRulesListResponseBody**](LoyaltiesTiersEarningRulesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of earning rules for a given tier. The object for each earning rule also contains information about how the points are calculated; this includes mapping. If a specific multiplier was used to calculate points for a given tier, then the &#x60;loyalty.points&#x60; parameter will account for this calculation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_tier_rewards**
> LoyaltiesTiersRewardsListResponseBody list_loyalty_tier_rewards(campaign_id, loyalty_tier_id)

List Loyalty Tier Rewards

Get available rewards for a given tier.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_tiers_rewards_list_response_body import LoyaltiesTiersRewardsListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name.
    loyalty_tier_id = 'loyalty_tier_id_example' # str | Unique loyalty tier ID.

    try:
        # List Loyalty Tier Rewards
        api_response = api_instance.list_loyalty_tier_rewards(campaign_id, loyalty_tier_id)
        print("The response of LoyaltiesApi->list_loyalty_tier_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_tier_rewards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name. | 
 **loyalty_tier_id** | **str**| Unique loyalty tier ID. | 

### Return type

[**LoyaltiesTiersRewardsListResponseBody**](LoyaltiesTiersRewardsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary of loyalty tier reward objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loyalty_tiers**
> LoyaltiesTiersListResponseBody list_loyalty_tiers(campaign_id, limit=limit, order=order)

List Loyalty Tiers

Retrieve a list of loyalty tiers which were added to the loyalty program.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_tiers_list_response_body import LoyaltiesTiersListResponseBody
from voucherify.models.parameter_order_list_loyalty_tiers import ParameterOrderListLoyaltyTiers
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique loyalty campaign ID or name.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderListLoyaltyTiers() # ParameterOrderListLoyaltyTiers | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)

    try:
        # List Loyalty Tiers
        api_response = api_instance.list_loyalty_tiers(campaign_id, limit=limit, order=order)
        print("The response of LoyaltiesApi->list_loyalty_tiers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_loyalty_tiers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique loyalty campaign ID or name. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderListLoyaltyTiers**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 

### Return type

[**LoyaltiesTiersListResponseBody**](LoyaltiesTiersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of loyalty tier objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_activity**
> LoyaltiesMemberActivityListResponseBody list_member_activity(member_id, limit=limit, order=order, starting_after_id=starting_after_id)

List Member Activity

  📘 Alternative endpoint  This endpoint is an alternative to this endpoint. The URL was re-designed to allow you to get member activities without having to provide the campaignId as a path parameter. Retrieves the list of activities for the given member ID related to a voucher and customer who is the holder of the voucher.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_member_activity_list_response_body import LoyaltiesMemberActivityListResponseBody
from voucherify.models.parameter_order_created_at import ParameterOrderCreatedAt
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderCreatedAt() # ParameterOrderCreatedAt | Apply this filter to order the events according the date and time when it was created. The dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the events starting after an event with the given ID. (optional)

    try:
        # List Member Activity
        api_response = api_instance.list_member_activity(member_id, limit=limit, order=order, starting_after_id=starting_after_id)
        print("The response of LoyaltiesApi->list_member_activity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_member_activity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderCreatedAt**](.md)| Apply this filter to order the events according the date and time when it was created. The dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the events starting after an event with the given ID. | [optional] 

### Return type

[**LoyaltiesMemberActivityListResponseBody**](LoyaltiesMemberActivityListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of event objects related to the loyalty card. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_activity1**
> LoyaltiesMemberActivityListResponseBody list_member_activity1(campaign_id, member_id, limit=limit, order=order, starting_after_id=starting_after_id)

List Member Activity

Retrieves the list of activities for the given member ID related to a voucher and customer who is the holder of the voucher.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_member_activity_list_response_body import LoyaltiesMemberActivityListResponseBody
from voucherify.models.parameter_order_created_at import ParameterOrderCreatedAt
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID.
    member_id = 'member_id_example' # str | A code that identifies the loyalty card.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    order = voucherify.ParameterOrderCreatedAt() # ParameterOrderCreatedAt | Apply this filter to order the events according the date and time when it was created. The dash - preceding a sorting option means sorting in a descending order. (optional)
    starting_after_id = 'starting_after_id_example' # str | A cursor for pagination. It retrieves the events starting after an event with the given ID. (optional)

    try:
        # List Member Activity
        api_response = api_instance.list_member_activity1(campaign_id, member_id, limit=limit, order=order, starting_after_id=starting_after_id)
        print("The response of LoyaltiesApi->list_member_activity1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_member_activity1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID. | 
 **member_id** | **str**| A code that identifies the loyalty card. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **order** | [**ParameterOrderCreatedAt**](.md)| Apply this filter to order the events according the date and time when it was created. The dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **starting_after_id** | **str**| A cursor for pagination. It retrieves the events starting after an event with the given ID. | [optional] 

### Return type

[**LoyaltiesMemberActivityListResponseBody**](LoyaltiesMemberActivityListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of event objects related to the loyalty card. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_loyalty_tier**
> LoyaltiesMembersTiersListResponseBody list_member_loyalty_tier(member_id)

List Member's Loyalty Tiers

Retrieve member tiers using the loyalty card ID.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_tiers_list_response_body import LoyaltiesMembersTiersListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.

    try:
        # List Member's Loyalty Tiers
        api_response = api_instance.list_member_loyalty_tier(member_id)
        print("The response of LoyaltiesApi->list_member_loyalty_tier:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_member_loyalty_tier: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 

### Return type

[**LoyaltiesMembersTiersListResponseBody**](LoyaltiesMembersTiersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a data array containing the member&#39;s loyalty tiers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_rewards**
> LoyaltiesMembersRewardsListResponseBody list_member_rewards(member_id, affordable_only=affordable_only)

List Member Rewards

Retrieves the list of rewards that the given customer (identified by member_id, which is a loyalty card assigned to a particular customer) **can get in exchange for loyalty points**.   You can use the affordable_only parameter to limit the results to rewards that the customer can actually afford (only rewards whose price in points is not higher than the loyalty points balance on a loyalty card).   Please note that rewards that are disabled (i.e. set to Not Available in the Dashboard) for a given loyalty tier reward mapping will not be returned in this endpoint.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_rewards_list_response_body import LoyaltiesMembersRewardsListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.
    affordable_only = True # bool | Limit the results to rewards that the customer can actually afford (only rewards whose price in points is not higher than the loyalty points balance on a loyalty card). Set this flag to true to return rewards which the customer can actually afford. (optional)

    try:
        # List Member Rewards
        api_response = api_instance.list_member_rewards(member_id, affordable_only=affordable_only)
        print("The response of LoyaltiesApi->list_member_rewards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_member_rewards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 
 **affordable_only** | **bool**| Limit the results to rewards that the customer can actually afford (only rewards whose price in points is not higher than the loyalty points balance on a loyalty card). Set this flag to true to return rewards which the customer can actually afford. | [optional] 

### Return type

[**LoyaltiesMembersRewardsListResponseBody**](LoyaltiesMembersRewardsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of rewards for the given &#x60;member_id&#x60;. Returns a filtered list if the query parameter &#x60;affordable_only&#x60; is set to &#x60;true&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_members**
> LoyaltiesListMembersResponseBody list_members(campaign_id, limit=limit, page=page, customer=customer, created_at=created_at, updated_at=updated_at, order=order, code=code, ids=ids)

List Members

Returns a list of your loyalty cards. The loyalty cards are sorted by creation date, with the most recent loyalty cards appearing first.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_list_members_response_body import LoyaltiesListMembersResponseBody
from voucherify.models.parameter_created_before_after import ParameterCreatedBeforeAfter
from voucherify.models.parameter_order_vouchers import ParameterOrderVouchers
from voucherify.models.parameter_updated_before_after import ParameterUpdatedBeforeAfter
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID of the loyalty program.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    customer = 'customer_example' # str | A tracking identifier of a customer who is the holder of the vouchers. It can be an id generated by Voucherify or the source_id. Remember to use the proper URL escape codes if the source_id contains special characters. (optional)
    created_at = voucherify.ParameterCreatedBeforeAfter() # ParameterCreatedBeforeAfter | A filter on the list based on the object created_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z (optional)
    updated_at = voucherify.ParameterUpdatedBeforeAfter() # ParameterUpdatedBeforeAfter | A filter on the list based on the object updated_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [updated_at][before] 2017-09-08T13:52:18.227Z (optional)
    order = voucherify.ParameterOrderVouchers() # ParameterOrderVouchers | Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. (optional)
    code = 'code_example' # str |  (optional)
    ids = ['ids_example'] # List[str] |  (optional)

    try:
        # List Members
        api_response = api_instance.list_members(campaign_id, limit=limit, page=page, customer=customer, created_at=created_at, updated_at=updated_at, order=order, code=code, ids=ids)
        print("The response of LoyaltiesApi->list_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID of the loyalty program. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **customer** | **str**| A tracking identifier of a customer who is the holder of the vouchers. It can be an id generated by Voucherify or the source_id. Remember to use the proper URL escape codes if the source_id contains special characters. | [optional] 
 **created_at** | [**ParameterCreatedBeforeAfter**](.md)| A filter on the list based on the object created_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [created_at][before] 2017-09-08T13:52:18.227Z | [optional] 
 **updated_at** | [**ParameterUpdatedBeforeAfter**](.md)| A filter on the list based on the object updated_at field. The value is a dictionary with the following options: before, after. A date value must be presented in ISO 8601 format (2016-11-16T14:14:31Z or 2016-11-16). An example: [updated_at][before] 2017-09-08T13:52:18.227Z | [optional] 
 **order** | [**ParameterOrderVouchers**](.md)| Sorts the results using one of the filtering options, where the dash - preceding a sorting option means sorting in a descending order. | [optional] 
 **code** | **str**|  | [optional] 
 **ids** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**LoyaltiesListMembersResponseBody**](LoyaltiesListMembersResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of loyalty cards within a campaign. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_points_expiration**
> LoyaltiesMembersPointsExpirationListResponseBody list_points_expiration(campaign_id, member_id, limit=limit, page=page)

Get Points Expiration

Retrieve loyalty point expiration buckets for a given loyalty card. Expired point buckets are not returned in this endpoint. You can use the Exports API to retrieve a list of both ACTIVE and EXPIRED point buckets.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_points_expiration_list_response_body import LoyaltiesMembersPointsExpirationListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    member_id = 'member_id_example' # str | Loyalty card code.
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)

    try:
        # Get Points Expiration
        api_response = api_instance.list_points_expiration(campaign_id, member_id, limit=limit, page=page)
        print("The response of LoyaltiesApi->list_points_expiration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_points_expiration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **member_id** | **str**| Loyalty card code. | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 

### Return type

[**LoyaltiesMembersPointsExpirationListResponseBody**](LoyaltiesMembersPointsExpirationListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a list of loyalty points expiration buckets along with an expiration date if the points are due to expire. No expiration date parameter is returned if the loyalty points bucket does not expire. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reward_assignments1**
> LoyaltiesRewardAssignmentsListResponseBody list_reward_assignments1(campaign_id, limit=limit, page=page, assignment_id=assignment_id)

List Reward Assignments

Returns reward assignments from a given loyalty campaign.  📘 Alternative endpoint  This endpoint is an alternative to this endpoint. The URL was re-designed to be more contextual to the type of data returned in the response.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_reward_assignments_list_response_body import LoyaltiesRewardAssignmentsListResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID. (optional)

    try:
        # List Reward Assignments
        api_response = api_instance.list_reward_assignments1(campaign_id, limit=limit, page=page, assignment_id=assignment_id)
        print("The response of LoyaltiesApi->list_reward_assignments1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_reward_assignments1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **assignment_id** | **str**| A unique reward assignment ID. | [optional] 

### Return type

[**LoyaltiesRewardAssignmentsListResponseBody**](LoyaltiesRewardAssignmentsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with reward assignment objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_reward_assignments2**
> LoyaltiesRewardsListAssignmentsResponseBody list_reward_assignments2(campaign_id, limit=limit, page=page, assignment_id=assignment_id)

List Reward Assignments

Returns active rewards from a given loyalty campaign.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_rewards_list_assignments_response_body import LoyaltiesRewardsListAssignmentsResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    limit = 56 # int | Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. (optional)
    page = 56 # int | Which page of results to return. The lowest value is 1. (optional)
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID. (optional)

    try:
        # List Reward Assignments
        api_response = api_instance.list_reward_assignments2(campaign_id, limit=limit, page=page, assignment_id=assignment_id)
        print("The response of LoyaltiesApi->list_reward_assignments2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->list_reward_assignments2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **limit** | **int**| Limits the number of objects to be returned. The limit can range between 1 and 100 items. If no limit is set, it returns 10 items. | [optional] 
 **page** | **int**| Which page of results to return. The lowest value is 1. | [optional] 
 **assignment_id** | **str**| A unique reward assignment ID. | [optional] 

### Return type

[**LoyaltiesRewardsListAssignmentsResponseBody**](LoyaltiesRewardsListAssignmentsResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a dictionary with reward assignment objects. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_reward**
> LoyaltiesMembersRedemptionRedeemResponseBody redeem_reward(member_id, loyalties_members_redemption_redeem_request_body=loyalties_members_redemption_redeem_request_body)

Redeem Reward

  📘 Alternative endpoint  This endpoint is an alternative to this endpoint. The URL was re-designed to allow you to redeem a reward without having to provide the campaignId as a path parameter.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_redemption_redeem_request_body import LoyaltiesMembersRedemptionRedeemRequestBody
from voucherify.models.loyalties_members_redemption_redeem_response_body import LoyaltiesMembersRedemptionRedeemResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.
    loyalties_members_redemption_redeem_request_body = {"reward":{"id":"rew_INt3fGH3n7xIr3ZQcq4kkUZ1","points":100},"order":{"items":[{"product_id":"prod_0c5d6689b39320059b","quantity":"1"},{"product_id":"prod_0b2c36568000039138","quantity":"2"}]}} # LoyaltiesMembersRedemptionRedeemRequestBody | Specify the reward to be redeemed. In case of a pay with points reward, specify the order and the number of points to be applied to the order. Please note that if you do not specify the amount of points, the application will default to applying the number of points to pay for the remainder of the order. If the limit of available points on the card is reached, then only the available points on the card will be applied to the order. (optional)

    try:
        # Redeem Reward
        api_response = api_instance.redeem_reward(member_id, loyalties_members_redemption_redeem_request_body=loyalties_members_redemption_redeem_request_body)
        print("The response of LoyaltiesApi->redeem_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->redeem_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 
 **loyalties_members_redemption_redeem_request_body** | [**LoyaltiesMembersRedemptionRedeemRequestBody**](LoyaltiesMembersRedemptionRedeemRequestBody.md)| Specify the reward to be redeemed. In case of a pay with points reward, specify the order and the number of points to be applied to the order. Please note that if you do not specify the amount of points, the application will default to applying the number of points to pay for the remainder of the order. If the limit of available points on the card is reached, then only the available points on the card will be applied to the order. | [optional] 

### Return type

[**LoyaltiesMembersRedemptionRedeemResponseBody**](LoyaltiesMembersRedemptionRedeemResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a redemption object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redeem_reward1**
> LoyaltiesMembersRedemptionRedeemResponseBody redeem_reward1(campaign_id, member_id, loyalties_members_redemption_redeem_request_body=loyalties_members_redemption_redeem_request_body)

Redeem Reward

Exchange points from a loyalty card for a specified reward. This API method returns an assigned award in the response. It means that if a requesting customer gets a coupon code with a discount for the next order, that discount code will be visible in response as part of the reward object definition.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_redemption_redeem_request_body import LoyaltiesMembersRedemptionRedeemRequestBody
from voucherify.models.loyalties_members_redemption_redeem_response_body import LoyaltiesMembersRedemptionRedeemResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID.
    member_id = 'member_id_example' # str | A code that identifies the loyalty card.
    loyalties_members_redemption_redeem_request_body = {"reward":{"id":"rew_INt3fGH3n7xIr3ZQcq4kkUZ1","points":100},"order":{"items":[{"product_id":"prod_0c5d6689b39320059b","quantity":"1"},{"product_id":"prod_0b2c36568000039138","quantity":"2"}]}} # LoyaltiesMembersRedemptionRedeemRequestBody | Specify the reward to be redeemed. In case of a pay with points reward, specify the order and the number of points to be applied to the order. Please note that if you do not specify the amount of points, the application will default to applying the number of points to pay for the remainder of the order. If the limit of available points on the card is reached, then only the available points on the card will be applied to the order. (optional)

    try:
        # Redeem Reward
        api_response = api_instance.redeem_reward1(campaign_id, member_id, loyalties_members_redemption_redeem_request_body=loyalties_members_redemption_redeem_request_body)
        print("The response of LoyaltiesApi->redeem_reward1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->redeem_reward1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID. | 
 **member_id** | **str**| A code that identifies the loyalty card. | 
 **loyalties_members_redemption_redeem_request_body** | [**LoyaltiesMembersRedemptionRedeemRequestBody**](LoyaltiesMembersRedemptionRedeemRequestBody.md)| Specify the reward to be redeemed. In case of a pay with points reward, specify the order and the number of points to be applied to the order. Please note that if you do not specify the amount of points, the application will default to applying the number of points to pay for the remainder of the order. If the limit of available points on the card is reached, then only the available points on the card will be applied to the order. | [optional] 

### Return type

[**LoyaltiesMembersRedemptionRedeemResponseBody**](LoyaltiesMembersRedemptionRedeemResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a redemption object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_points**
> LoyaltiesMembersTransfersCreateResponseBody transfer_points(campaign_id, member_id, loyalties_transfer_points=loyalties_transfer_points)

Transfer Loyalty Points

Transfer points between different loyalty cards. You need to provide the campaign ID and the loyalty card ID you want the points to be transferred to as path parameters in the URL. In the request body, you provide the loyalty cards you want the points to be transferred from and the number of points to transfer from each card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_transfers_create_response_body import LoyaltiesMembersTransfersCreateResponseBody
from voucherify.models.loyalties_transfer_points import LoyaltiesTransferPoints
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | A unique identifier of the loyalty campaign containing the voucher to which the loyalty points will be sent (destination).
    member_id = 'member_id_example' # str | A unique code identifying the loyalty card to which the user wants to transfer loyalty points (destination).
    loyalties_transfer_points = [{"code":"0PmQ7JQI","points":1},{"code":"kCeufB8i","points":1}] # List[LoyaltiesTransferPoints] | Provide the loyalty cards you want the points to be transferred from and the number of points to transfer from each card. (optional)

    try:
        # Transfer Loyalty Points
        api_response = api_instance.transfer_points(campaign_id, member_id, loyalties_transfer_points=loyalties_transfer_points)
        print("The response of LoyaltiesApi->transfer_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->transfer_points: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| A unique identifier of the loyalty campaign containing the voucher to which the loyalty points will be sent (destination). | 
 **member_id** | **str**| A unique code identifying the loyalty card to which the user wants to transfer loyalty points (destination). | 
 **loyalties_transfer_points** | [**List[LoyaltiesTransferPoints]**](LoyaltiesTransferPoints.md)| Provide the loyalty cards you want the points to be transferred from and the number of points to transfer from each card. | [optional] 

### Return type

[**LoyaltiesMembersTransfersCreateResponseBody**](LoyaltiesMembersTransfersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a loyalty card object for the loaded loyalty card, ie. the one that that points were transferred to from the other cards(s). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_earning_rule**
> LoyaltiesEarningRulesUpdateResponseBody update_earning_rule(campaign_id, earning_rule_id, loyalties_earning_rules_update_request_body=loyalties_earning_rules_update_request_body)

Update Earning Rule

Update an earning rule definition.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_earning_rules_update_request_body import LoyaltiesEarningRulesUpdateRequestBody
from voucherify.models.loyalties_earning_rules_update_response_body import LoyaltiesEarningRulesUpdateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    earning_rule_id = 'earning_rule_id_example' # str | A unique earning rule ID.
    loyalties_earning_rules_update_request_body = {"validation_rule_id":"val_7SxpdhPeBngA","loyalty":{"type":"FIXED","points":"5"},"source":{"banner":"Order paid 5 points."},"active":true,"start_date":"2022-11-02T13:00:00.000Z","expiration_date":"2023-03-03T14:30:00.000Z","validity_timeframe":{"duration":"PT1H","interval":"P1D"},"validity_day_of_week":[0,1,2,3,4,5],"metadata":{"Type":"Order paid - fixed amount of points"}} # LoyaltiesEarningRulesUpdateRequestBody | Specify the parameters that you would like to update for the given earning rule. (optional)

    try:
        # Update Earning Rule
        api_response = api_instance.update_earning_rule(campaign_id, earning_rule_id, loyalties_earning_rules_update_request_body=loyalties_earning_rules_update_request_body)
        print("The response of LoyaltiesApi->update_earning_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->update_earning_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **earning_rule_id** | **str**| A unique earning rule ID. | 
 **loyalties_earning_rules_update_request_body** | [**LoyaltiesEarningRulesUpdateRequestBody**](LoyaltiesEarningRulesUpdateRequestBody.md)| Specify the parameters that you would like to update for the given earning rule. | [optional] 

### Return type

[**LoyaltiesEarningRulesUpdateResponseBody**](LoyaltiesEarningRulesUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the updated earning rule object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loyalty_card_balance**
> LoyaltiesMembersBalanceUpdateResponseBody update_loyalty_card_balance(member_id, loyalties_members_balance_update_request_body=loyalties_members_balance_update_request_body)

Add or Remove Loyalty Card Balance

This method gives adds or removes balance to an existing loyalty card. The removal of points will consume the points that expire the soonest.   >🚧 Async Action    This is an async action. If you want to perform several add or remove loyalty card balance actions in a short time and their order matters, set up sufficient time-out between the calls.  📘 Alternative endpoint  This endpoint is an alternative to this endpoint. The URL was re-designed to allow you to add or remove loyalty card balance without having to provide the campaignId as a path parameter.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_balance_update_request_body import LoyaltiesMembersBalanceUpdateRequestBody
from voucherify.models.loyalties_members_balance_update_response_body import LoyaltiesMembersBalanceUpdateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    member_id = 'member_id_example' # str | Unique loyalty card assigned to a particular customer.
    loyalties_members_balance_update_request_body = {"points":-100} # LoyaltiesMembersBalanceUpdateRequestBody | Specify the point adjustment along with the expiration mechanism. (optional)

    try:
        # Add or Remove Loyalty Card Balance
        api_response = api_instance.update_loyalty_card_balance(member_id, loyalties_members_balance_update_request_body=loyalties_members_balance_update_request_body)
        print("The response of LoyaltiesApi->update_loyalty_card_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->update_loyalty_card_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_id** | **str**| Unique loyalty card assigned to a particular customer. | 
 **loyalties_members_balance_update_request_body** | [**LoyaltiesMembersBalanceUpdateRequestBody**](LoyaltiesMembersBalanceUpdateRequestBody.md)| Specify the point adjustment along with the expiration mechanism. | [optional] 

### Return type

[**LoyaltiesMembersBalanceUpdateResponseBody**](LoyaltiesMembersBalanceUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a balance object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loyalty_card_balance1**
> LoyaltiesMembersBalanceUpdateResponseBody update_loyalty_card_balance1(campaign_id, member_id, loyalties_members_balance_update_request_body=loyalties_members_balance_update_request_body)

Add or Remove Loyalty Card Balance

This method adds or removes balance to an existing loyalty card. The removal of points will consume the points that expire the soonest.   >🚧 Async Action    This is an async action. If you want to perform several add or remove loyalty card balance actions in a short time and their order matters, set up sufficient time-out between the calls.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_members_balance_update_request_body import LoyaltiesMembersBalanceUpdateRequestBody
from voucherify.models.loyalties_members_balance_update_response_body import LoyaltiesMembersBalanceUpdateResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | Unique campaign ID.
    member_id = 'member_id_example' # str | A code that identifies the loyalty card.
    loyalties_members_balance_update_request_body = {"points":100,"expiration_type":"CUSTOM_DATE","expiration_date":"2023-05-30"} # LoyaltiesMembersBalanceUpdateRequestBody | Specify the point adjustment along with the expiration mechanism. (optional)

    try:
        # Add or Remove Loyalty Card Balance
        api_response = api_instance.update_loyalty_card_balance1(campaign_id, member_id, loyalties_members_balance_update_request_body=loyalties_members_balance_update_request_body)
        print("The response of LoyaltiesApi->update_loyalty_card_balance1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->update_loyalty_card_balance1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| Unique campaign ID. | 
 **member_id** | **str**| A code that identifies the loyalty card. | 
 **loyalties_members_balance_update_request_body** | [**LoyaltiesMembersBalanceUpdateRequestBody**](LoyaltiesMembersBalanceUpdateRequestBody.md)| Specify the point adjustment along with the expiration mechanism. | [optional] 

### Return type

[**LoyaltiesMembersBalanceUpdateResponseBody**](LoyaltiesMembersBalanceUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a balance object. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loyalty_program**
> LoyaltiesUpdateCampaignResponseBody update_loyalty_program(campaign_id, loyalties_update_campaign_request_body=loyalties_update_campaign_request_body)

Update Loyalty Campaign

Updates a loyalty program.  Fields other than those specified in the allowed request body payload wont be modified (even if provided they are silently skipped). Any parameters not provided will be left unchanged.  This method will update the loyalty cards which have not been published or redeemed yet.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_update_campaign_request_body import LoyaltiesUpdateCampaignRequestBody
from voucherify.models.loyalties_update_campaign_response_body import LoyaltiesUpdateCampaignResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    loyalties_update_campaign_request_body = {"description":"This is a campaign description. Updated","auto_join":false,"join_once":false,"start_date":"2013-10-26T00:00:00Z","expiration_date":"2025-10-26T00:00:00Z","validity_timeframe":{"duration":"PT2H","interval":"P2D"},"validity_day_of_week":[0,1,2,3,4,5,6],"activity_duration_after_publishing":"P25D","category_id":"cat_0b6152ce12414820dd","loyalty_card":{"points":1,"expiration_rules":{"period_type":"MONTH","period_value":4,"rounding_type":"END_OF_YEAR"}},"metadata":{"test":false},"type":"AUTO_UPDATE","loyalty_tiers_expiration":{"qualification_type":"BALANCE","start_date":{"type":"IMMEDIATE"},"expiration_date":{"type":"CUSTOM","extend":"P4M","rounding":{"type":"CUSTOM","unit":"MONTH","value":1}}}} # LoyaltiesUpdateCampaignRequestBody | Specify the new values for the parameters that you would like to update for the given loyalty campaign. (optional)

    try:
        # Update Loyalty Campaign
        api_response = api_instance.update_loyalty_program(campaign_id, loyalties_update_campaign_request_body=loyalties_update_campaign_request_body)
        print("The response of LoyaltiesApi->update_loyalty_program:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->update_loyalty_program: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **loyalties_update_campaign_request_body** | [**LoyaltiesUpdateCampaignRequestBody**](LoyaltiesUpdateCampaignRequestBody.md)| Specify the new values for the parameters that you would like to update for the given loyalty campaign. | [optional] 

### Return type

[**LoyaltiesUpdateCampaignResponseBody**](LoyaltiesUpdateCampaignResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns the loyalty campaign object if the update succeeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_reward_assignment1**
> LoyaltiesRewardsUpdateAssignmentResponseBody update_reward_assignment1(campaign_id, assignment_id, loyalties_rewards_update_assignment_request_body=loyalties_rewards_update_assignment_request_body)

Update Reward Assignment

Updates rewards parameters, i.e. the points cost for the specific reward.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_rewards_update_assignment_request_body import LoyaltiesRewardsUpdateAssignmentRequestBody
from voucherify.models.loyalties_rewards_update_assignment_response_body import LoyaltiesRewardsUpdateAssignmentResponseBody
from voucherify.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.voucherify.io
# See configuration.py for a list of all supported configuration parameters.
configuration = voucherify.Configuration(
    host = "https://api.voucherify.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: X-App-Id
configuration.api_key['X-App-Id'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Id'] = 'Bearer'

# Configure API key authorization: X-App-Token
configuration.api_key['X-App-Token'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-App-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with voucherify.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = voucherify.LoyaltiesApi(api_client)
    campaign_id = 'campaign_id_example' # str | The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign. 
    assignment_id = 'assignment_id_example' # str | A unique reward assignment ID.
    loyalties_rewards_update_assignment_request_body = {"parameters":{"loyalty":{"points":3}}} # LoyaltiesRewardsUpdateAssignmentRequestBody | Update the points cost for the reward assignment. (optional)

    try:
        # Update Reward Assignment
        api_response = api_instance.update_reward_assignment1(campaign_id, assignment_id, loyalties_rewards_update_assignment_request_body=loyalties_rewards_update_assignment_request_body)
        print("The response of LoyaltiesApi->update_reward_assignment1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoyaltiesApi->update_reward_assignment1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaign_id** | **str**| The campaign ID or name of the loyalty campaign. You can either pass the campaign ID, which was assigned by Voucherify, or the name of the campaign as the path parameter value, e.g., Loyalty%20Campaign.  | 
 **assignment_id** | **str**| A unique reward assignment ID. | 
 **loyalties_rewards_update_assignment_request_body** | [**LoyaltiesRewardsUpdateAssignmentRequestBody**](LoyaltiesRewardsUpdateAssignmentRequestBody.md)| Update the points cost for the reward assignment. | [optional] 

### Return type

[**LoyaltiesRewardsUpdateAssignmentResponseBody**](LoyaltiesRewardsUpdateAssignmentResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a reward assignment with an updated points value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

