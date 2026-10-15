# voucherify.LV2ProgramsApi

All URIs are relative to *https://api.voucherify.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_card_pending_points_bucket**](LV2ProgramsApi.md#activate_card_pending_points_bucket) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/pending-points/{bucketId}/activate | Activate pending point bucket
[**activate_program_member**](LV2ProgramsApi.md#activate_program_member) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/activate | Activate program member
[**adjust_card_points**](LV2ProgramsApi.md#adjust_card_points) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/points | Adjust card points
[**batch_create_program_members**](LV2ProgramsApi.md#batch_create_program_members) | **POST** /v2/loyalties/programs/{programId}/members/batch | Batch create program members
[**cancel_card_pending_points_bucket**](LV2ProgramsApi.md#cancel_card_pending_points_bucket) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/pending-points/{bucketId}/cancel | Cancel pending point bucket
[**create_member_order_payment**](LV2ProgramsApi.md#create_member_order_payment) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/orders/payments | Pay for order with points
[**create_program_member**](LV2ProgramsApi.md#create_program_member) | **POST** /v2/loyalties/programs/{programId}/members | Create program member
[**deactivate_program_member**](LV2ProgramsApi.md#deactivate_program_member) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/deactivate | Deactivate program member
[**delete_program_member**](LV2ProgramsApi.md#delete_program_member) | **DELETE** /v2/loyalties/programs/{programId}/members/{memberId} | Delete program member
[**expire_card_points_bucket**](LV2ProgramsApi.md#expire_card_points_bucket) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/expiring-points/{bucketId}/expire | Expire point bucket
[**get_member_earning_rule_daily_report**](LV2ProgramsApi.md#get_member_earning_rule_daily_report) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/earning-rules/{earningRuleId}/reports/daily | List member earning-rule daily reports
[**get_program_member**](LV2ProgramsApi.md#get_program_member) | **GET** /v2/loyalties/programs/{programId}/members/{memberId} | Get program member
[**get_program_membership**](LV2ProgramsApi.md#get_program_membership) | **GET** /v2/loyalties/programs/{programId}/memberships/{customerId} | Get program membership
[**get_program_points_earnings_daily_report**](LV2ProgramsApi.md#get_program_points_earnings_daily_report) | **GET** /v2/loyalties/programs/{programId}/reports/points-earnings/daily | List program points-earnings daily reports
[**get_program_points_earnings_summary_report**](LV2ProgramsApi.md#get_program_points_earnings_summary_report) | **GET** /v2/loyalties/programs/{programId}/reports/points-earnings/summary | List program points-earnings summary reports
[**list_card_activities**](LV2ProgramsApi.md#list_card_activities) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/activities | List card activities
[**list_card_expiring_points**](LV2ProgramsApi.md#list_card_expiring_points) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/expiring-points | List card expiring points buckets
[**list_card_pending_points**](LV2ProgramsApi.md#list_card_pending_points) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/pending-points | List card pending point buckets
[**list_card_transactions**](LV2ProgramsApi.md#list_card_transactions) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/transactions | List card transactions
[**list_member_benefit_transactions**](LV2ProgramsApi.md#list_member_benefit_transactions) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/benefits/transactions | List member benefit transactions
[**list_member_card_daily_reports**](LV2ProgramsApi.md#list_member_card_daily_reports) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/cards/{cardId}/reports/daily | List card daily points reports
[**list_member_order_payments**](LV2ProgramsApi.md#list_member_order_payments) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/orders/payments | List member order payments
[**list_member_reward_purchases**](LV2ProgramsApi.md#list_member_reward_purchases) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/rewards/purchases | List member reward purchases
[**list_member_tier_transactions**](LV2ProgramsApi.md#list_member_tier_transactions) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/tiers/transactions | List member tier transactions
[**list_program_earning_rule_assignments**](LV2ProgramsApi.md#list_program_earning_rule_assignments) | **GET** /v2/loyalties/programs/{programId}/earning-rules | List program earning rule assignments
[**list_program_earning_rules_daily_reports**](LV2ProgramsApi.md#list_program_earning_rules_daily_reports) | **GET** /v2/loyalties/programs/{programId}/reports/earning-rules/daily | List program earning-rules daily reports
[**list_program_earning_rules_summary_reports**](LV2ProgramsApi.md#list_program_earning_rules_summary_reports) | **GET** /v2/loyalties/programs/{programId}/reports/earning-rules/summary | List program earning-rules summary reports
[**list_program_member_activities**](LV2ProgramsApi.md#list_program_member_activities) | **GET** /v2/loyalties/programs/{programId}/members/{memberId}/activities | List program member activities
[**list_program_members**](LV2ProgramsApi.md#list_program_members) | **GET** /v2/loyalties/programs/{programId}/members | List program members
[**list_program_members_daily_reports**](LV2ProgramsApi.md#list_program_members_daily_reports) | **GET** /v2/loyalties/programs/{programId}/reports/members/daily | List program members daily reports
[**list_program_members_summary_reports**](LV2ProgramsApi.md#list_program_members_summary_reports) | **GET** /v2/loyalties/programs/{programId}/reports/members/summary | List program members summary reports
[**list_program_reward_assignments**](LV2ProgramsApi.md#list_program_reward_assignments) | **GET** /v2/loyalties/programs/{programId}/rewards | List program reward assignments
[**list_program_rewards_daily_reports**](LV2ProgramsApi.md#list_program_rewards_daily_reports) | **GET** /v2/loyalties/programs/{programId}/reports/rewards/daily | List program rewards daily reports
[**list_program_rewards_spendings_daily_reports**](LV2ProgramsApi.md#list_program_rewards_spendings_daily_reports) | **GET** /v2/loyalties/programs/{programId}/reports/rewards/spendings/daily | List program rewards spendings daily reports
[**list_program_rewards_spendings_summary_reports**](LV2ProgramsApi.md#list_program_rewards_spendings_summary_reports) | **GET** /v2/loyalties/programs/{programId}/reports/rewards/spendings/summary | List program rewards spendings summary reports
[**list_program_rewards_summary_reports**](LV2ProgramsApi.md#list_program_rewards_summary_reports) | **GET** /v2/loyalties/programs/{programId}/reports/rewards/summary | List program rewards summary reports
[**list_program_spending_daily_reports**](LV2ProgramsApi.md#list_program_spending_daily_reports) | **GET** /v2/loyalties/programs/{programId}/reports/spending/daily | List program spending daily reports
[**list_program_spending_summary_reports**](LV2ProgramsApi.md#list_program_spending_summary_reports) | **GET** /v2/loyalties/programs/{programId}/reports/spending/summary | List program spending summary reports
[**list_program_tier_structure_assignments**](LV2ProgramsApi.md#list_program_tier_structure_assignments) | **GET** /v2/loyalties/programs/{programId}/tier-structures | List program tier structure assignments
[**list_program_tiers_daily_reports**](LV2ProgramsApi.md#list_program_tiers_daily_reports) | **GET** /v2/loyalties/programs/{programId}/reports/tiers/daily | List program tiers daily reports
[**list_program_tiers_summary_reports**](LV2ProgramsApi.md#list_program_tiers_summary_reports) | **GET** /v2/loyalties/programs/{programId}/reports/tiers/summary | List program tiers summary reports
[**purchase_member_reward**](LV2ProgramsApi.md#purchase_member_reward) | **POST** /v2/loyalties/programs/{programId}/members/{memberId}/rewards/purchases | Purchase reward with points
[**refund_reward_purchase**](LV2ProgramsApi.md#refund_reward_purchase) | **POST** /v2/loyalties/programs/{programId}/rewards/purchases/{rewardTransactionId}/refund | Refund reward purchase
[**update_program_member**](LV2ProgramsApi.md#update_program_member) | **PUT** /v2/loyalties/programs/{programId}/members/{memberId} | Update program member


# **activate_card_pending_points_bucket**
> V2LoyaltiesProgramsMembersCardsPendingPointsActivateResponseBody activate_card_pending_points_bucket(program_id, member_id, card_id, bucket_id)

Activate pending point bucket

Activates a pending points bucket and creates a PENDING_POINTS_ACTIVATED card transaction. The transaction is created with status PENDING and processed asynchronously. No request body. The bucket must be PENDING, and its date must be after the current project day. The program and the member must be ACTIVE, and the program must be inside its validity window. Otherwise the response is 423. Returns 404 when the program or the member doesnt exist, when the card isnt assigned to that member, or when the bucket isnt on that card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_cards_pending_points_activate_response_body import V2LoyaltiesProgramsMembersCardsPendingPointsActivateResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    bucket_id = 'bucket_id_example' # str | Identifies the pending points bucket. Format lcppb_[a-f0-9]+.

    try:
        # Activate pending point bucket
        api_response = api_instance.activate_card_pending_points_bucket(program_id, member_id, card_id, bucket_id)
        print("The response of LV2ProgramsApi->activate_card_pending_points_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->activate_card_pending_points_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **bucket_id** | **str**| Identifies the pending points bucket. Format lcppb_[a-f0-9]+. | 

### Return type

[**V2LoyaltiesProgramsMembersCardsPendingPointsActivateResponseBody**](V2LoyaltiesProgramsMembersCardsPendingPointsActivateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Result of the pending points activation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **activate_program_member**
> V2LoyaltiesProgramsMembersActivateResponseBody activate_program_member(program_id, member_id)

Activate program member

Moves an INACTIVE member to ACTIVE and sets updated_at. Records a vl.member.activated activity. No request body. Returns the member without a cards array. Returns 404 when the program doesnt exist, or when the member doesnt exist in that program. The program is checked first. A DELETED member returns 404. Returns 400 with key invalid_state_transition when the member is already ACTIVE.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_activate_response_body import V2LoyaltiesProgramsMembersActivateResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.

    try:
        # Activate program member
        api_response = api_instance.activate_program_member(program_id, member_id)
        print("The response of LV2ProgramsApi->activate_program_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->activate_program_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 

### Return type

[**V2LoyaltiesProgramsMembersActivateResponseBody**](V2LoyaltiesProgramsMembersActivateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The activated member, without cards. Status is always &#x60;ACTIVE&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_card_points**
> V2LoyaltiesProgramsMembersCardsPointsAdjustResponseBody adjust_card_points(program_id, member_id, card_id, v2_loyalties_programs_members_cards_points_adjust_request_body=v2_loyalties_programs_members_cards_points_adjust_request_body)

Adjust card points

Manually adjusts the points balance of the members card. A positive points value creates an ADMIN_CREDIT card transaction. The expiration date comes from the member tier when that tier defines its own points expiration. Otherwise the date comes from the card definition. expiration_date is null when points dont expire. A negative points value creates an ADMIN_DEBIT card transaction. When points is 0, no transaction is created and status is NO_CHANGE. The transaction is created with status PENDING and processed asynchronously. The program and the member must be ACTIVE. The program must also be inside its validity window. Otherwise the response is 423. The response is 404 when the program or the member doesnt exist, or when the card isnt assigned to that member.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_cards_points_adjust_request_body import V2LoyaltiesProgramsMembersCardsPointsAdjustRequestBody
from voucherify.models.v2_loyalties_programs_members_cards_points_adjust_response_body import V2LoyaltiesProgramsMembersCardsPointsAdjustResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    v2_loyalties_programs_members_cards_points_adjust_request_body = {"points":100} # V2LoyaltiesProgramsMembersCardsPointsAdjustRequestBody |  (optional)

    try:
        # Adjust card points
        api_response = api_instance.adjust_card_points(program_id, member_id, card_id, v2_loyalties_programs_members_cards_points_adjust_request_body=v2_loyalties_programs_members_cards_points_adjust_request_body)
        print("The response of LV2ProgramsApi->adjust_card_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->adjust_card_points: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **v2_loyalties_programs_members_cards_points_adjust_request_body** | [**V2LoyaltiesProgramsMembersCardsPointsAdjustRequestBody**](V2LoyaltiesProgramsMembersCardsPointsAdjustRequestBody.md)|  | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersCardsPointsAdjustResponseBody**](V2LoyaltiesProgramsMembersCardsPointsAdjustResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Result of the points adjustment. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_create_program_members**
> V2LoyaltiesProgramsMembersCreateInBulkResponseBody batch_create_program_members(program_id, member_create=member_create)

Batch create program members

Schedules creation of program members from a JSON array and returns 202 with async_action_id. The program must exist, be ACTIVE, and be inside its validity window. The body isnt checked before that response. Entries are processed in batches of 100. The raw body must be at most 10 MB. Each entry uses the same fields as [Create program member](/api-reference/programs/create-program-member). A failed entry is skipped. Its report row sets created to false and explains the failure in error. Skipped cases include an invalid customer_identification, an unknown customer, an invalid status, a duplicate customer in the batch (Duplicate customer ID), a customer who is already a member (Member already exists), metadata that doesnt match the vl_member schema, and entries past the loyalty members plan limit. Successful entries enroll the customer and create a loyalty card for each card definition on the program. Report columns are identification_type, customer_id, customer_source_id, program_id, member_id, created, and error. An empty array or a null entry fails the async action with invalid_request_payload. A body that isnt a JSON array fails it with top_level_object_should_be_an_array. Use [Get async action](/api-reference/async-actions/get-async-action) to read the status and the report. You can also open the result from Audit log, [Background tasks](/analyze/audit-logs#background-tasks).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.member_create import MemberCreate
from voucherify.models.v2_loyalties_programs_members_create_in_bulk_response_body import V2LoyaltiesProgramsMembersCreateInBulkResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_create = [{"customer_identification":{"type":"customer_id","customer_id":"cust_X07elh40iNWLujRmDNmBufxd"}},{"customer_identification":{"type":"customer_source_id","customer_source_id":"crm-1001"},"status":"ACTIVE"}] # List[MemberCreate] |  (optional)

    try:
        # Batch create program members
        api_response = api_instance.batch_create_program_members(program_id, member_create=member_create)
        print("The response of LV2ProgramsApi->batch_create_program_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->batch_create_program_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_create** | [**List[MemberCreate]**](MemberCreate.md)|  | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersCreateInBulkResponseBody**](V2LoyaltiesProgramsMembersCreateInBulkResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The batch is scheduled. Use &#x60;async_action_id&#x60; to follow processing. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_card_pending_points_bucket**
> V2LoyaltiesProgramsMembersCardsPendingPointsCancelResponseBody cancel_card_pending_points_bucket(program_id, member_id, card_id, bucket_id)

Cancel pending point bucket

Cancels a pending points bucket so its points arent activated. Creates a PENDING_POINTS_CANCELED card transaction. The transaction is created with status PENDING and processed asynchronously. No request body. The bucket must be PENDING, and its date must be after the current project day. The program and the member must be ACTIVE, and the program must be inside its validity window. Otherwise the response is 423. Returns 404 when the program or the member doesnt exist, when the card isnt assigned to that member, or when the bucket isnt on that card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_cards_pending_points_cancel_response_body import V2LoyaltiesProgramsMembersCardsPendingPointsCancelResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    bucket_id = 'bucket_id_example' # str | Identifies the pending points bucket. Format lcppb_[a-f0-9]+.

    try:
        # Cancel pending point bucket
        api_response = api_instance.cancel_card_pending_points_bucket(program_id, member_id, card_id, bucket_id)
        print("The response of LV2ProgramsApi->cancel_card_pending_points_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->cancel_card_pending_points_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **bucket_id** | **str**| Identifies the pending points bucket. Format lcppb_[a-f0-9]+. | 

### Return type

[**V2LoyaltiesProgramsMembersCardsPendingPointsCancelResponseBody**](V2LoyaltiesProgramsMembersCardsPendingPointsCancelResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Result of the pending points cancellation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_member_order_payment**
> LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBody create_member_order_payment(program_id, member_id, v2_loyalties_programs_members_orders_payments_create_request_body=v2_loyalties_programs_members_orders_payments_create_request_body)

Pay for order with points

Pays for an order with points from the members card. The amount and points come from the card definitions pay-with-points exchange ratio, limited by the order total, the card balance, card spending caps, and the optional payment_limit. The binding cap is returned as details.spending_cap. The program and member must be ACTIVE, and the program must be inside its validity window. The card must belong to the member. The card definition must have pay-with-points enabled and an exchange-ratio formula. The order must already exist, identified by id or source_id. Modes: - TRANSACTION (default): creates a PENDING order transaction and a PENDING card transaction. Returns 202. The same order can be paid again; each call creates a new transaction. - DRY_RUN: simulates the payment and doesnt create a transaction. Returns 200 with status SIMULATED.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_orders_payments_create_combined_response_body import LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBody
from voucherify.models.v2_loyalties_programs_members_orders_payments_create_request_body import V2LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    v2_loyalties_programs_members_orders_payments_create_request_body = {"payment_limit":{"type":"CARD_BALANCE"},"mode":"TRANSACTION","card_id":"lcrd_128f962dbd8c4ba5e1","order":{"id":"ord_12b4cdf5f30c158825"}} # V2LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody |  (optional)

    try:
        # Pay for order with points
        api_response = api_instance.create_member_order_payment(program_id, member_id, v2_loyalties_programs_members_orders_payments_create_request_body=v2_loyalties_programs_members_orders_payments_create_request_body)
        print("The response of LV2ProgramsApi->create_member_order_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->create_member_order_payment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **v2_loyalties_programs_members_orders_payments_create_request_body** | [**V2LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody**](V2LoyaltiesProgramsMembersOrdersPaymentsCreateRequestBody.md)|  | [optional] 

### Return type

[**LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBody**](LoyaltiesProgramsMembersOrdersPaymentsCreateCombinedResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Dry run result (mode &#x60;DRY_RUN&#x60;). No transaction was created; the returned transaction has status &#x60;SIMULATED&#x60; and no &#x60;id&#x60;. and Payment accepted (mode &#x60;TRANSACTION&#x60;). A &#x60;PENDING&#x60; order transaction was created and will be processed asynchronously. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_program_member**
> V2LoyaltiesProgramsMembersCreateResponseBody create_program_member(program_id, v2_loyalties_programs_members_create_request_body=v2_loyalties_programs_members_create_request_body)

Create program member

Enrolls an existing customer as a member of the loyalty program and creates a loyalty card for each card definition assigned to the program. Card code generation is asynchronous, so code can be null right after creation. The program must be ACTIVE and inside its validity window, and the customer must already exist. A customer can be a member of a program only once. Identify the customer with customer_identification. status defaults to ACTIVE.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_create_request_body import V2LoyaltiesProgramsMembersCreateRequestBody
from voucherify.models.v2_loyalties_programs_members_create_response_body import V2LoyaltiesProgramsMembersCreateResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    v2_loyalties_programs_members_create_request_body = {"customer_identification":{"type":"customer_id","customer_id":"cust_X07elh40iNWLujRmDNmBufxd"}} # V2LoyaltiesProgramsMembersCreateRequestBody |  (optional)

    try:
        # Create program member
        api_response = api_instance.create_program_member(program_id, v2_loyalties_programs_members_create_request_body=v2_loyalties_programs_members_create_request_body)
        print("The response of LV2ProgramsApi->create_program_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->create_program_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **v2_loyalties_programs_members_create_request_body** | [**V2LoyaltiesProgramsMembersCreateRequestBody**](V2LoyaltiesProgramsMembersCreateRequestBody.md)|  | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersCreateResponseBody**](V2LoyaltiesProgramsMembersCreateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The created member with its automatically created cards. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_program_member**
> V2LoyaltiesProgramsMembersDeactivateResponseBody deactivate_program_member(program_id, member_id)

Deactivate program member

Moves an ACTIVE member to INACTIVE and sets updated_at. Records a vl.member.deactivated activity. An INACTIVE member cant earn or spend points. No request body. Returns the member without a cards array. Returns 404 when the program doesnt exist, or when the member doesnt exist in that program. The program is checked first. A DELETED member returns 404. Returns 400 with key invalid_state_transition when the member is already INACTIVE.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_deactivate_response_body import V2LoyaltiesProgramsMembersDeactivateResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.

    try:
        # Deactivate program member
        api_response = api_instance.deactivate_program_member(program_id, member_id)
        print("The response of LV2ProgramsApi->deactivate_program_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->deactivate_program_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 

### Return type

[**V2LoyaltiesProgramsMembersDeactivateResponseBody**](V2LoyaltiesProgramsMembersDeactivateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The deactivated member, without cards. Status is always &#x60;INACTIVE&#x60;. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_program_member**
> V2LoyaltiesProgramsMembersDeleteResponseBody delete_program_member(program_id, member_id)

Delete program member

Deletes the member and sets status to DELETED. Removes the members card assignments in this program. Returns the member without a cards array. Delete doesnt change updated_at. Records a vl.member.deleted activity. Each unassigned card also records vl.member.card.unassigned and vl.card.unassigned. When an assignment has a tier, the delete records a LEFT tier transaction with origin member_card_deleted. The same customer can join the program again. The new member gets a new ID. Returns 404 when the program doesnt exist, or when the member doesnt exist in that program. The program is checked first. Deleting a member that is already DELETED returns 404.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_delete_response_body import V2LoyaltiesProgramsMembersDeleteResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.

    try:
        # Delete program member
        api_response = api_instance.delete_program_member(program_id, member_id)
        print("The response of LV2ProgramsApi->delete_program_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->delete_program_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 

### Return type

[**V2LoyaltiesProgramsMembersDeleteResponseBody**](V2LoyaltiesProgramsMembersDeleteResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The deleted member (without cards). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **expire_card_points_bucket**
> V2LoyaltiesProgramsMembersCardsExpiringPointsExpireResponseBody expire_card_points_bucket(program_id, member_id, card_id, bucket_id)

Expire point bucket

Expires an ACTIVE points bucket. Creates an ADMIN_POINTS_EXPIRATION card transaction. The transaction is created with status PENDING and processed asynchronously. No request body. The bucket must be ACTIVE, and its expiration_date must be on or after the current project day. The program and the member must be ACTIVE, and the program must be inside its validity window. Otherwise the response is 423. Returns 404 when the program, the member, or the card definition doesnt exist, when the card isnt assigned to that member, or when the bucket isnt on that card.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_cards_expiring_points_expire_response_body import V2LoyaltiesProgramsMembersCardsExpiringPointsExpireResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    bucket_id = 'bucket_id_example' # str | Identifies the points expiration bucket. Format lcpeb_[a-f0-9]+.

    try:
        # Expire point bucket
        api_response = api_instance.expire_card_points_bucket(program_id, member_id, card_id, bucket_id)
        print("The response of LV2ProgramsApi->expire_card_points_bucket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->expire_card_points_bucket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **bucket_id** | **str**| Identifies the points expiration bucket. Format lcpeb_[a-f0-9]+. | 

### Return type

[**V2LoyaltiesProgramsMembersCardsExpiringPointsExpireResponseBody**](V2LoyaltiesProgramsMembersCardsExpiringPointsExpireResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Result of the points expiration. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_earning_rule_daily_report**
> V2LoyaltiesProgramsMembersEarningRulesReportsDailyListResponseBody get_member_earning_rule_daily_report(program_id, member_id, earning_rule_id, start_date, end_date, resolution)

List member earning-rule daily reports

Returns aggregated daily usage statistics for a specific earning rule and member over the given date range and resolution. Each entry sums successful earning-rule triggers recorded in one period. Periods without recorded activity are omitted. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program or member does not exist, or when the earning rule does not exist or is not assigned to the program.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_earning_rules_reports_daily_list_response_body import V2LoyaltiesProgramsMembersEarningRulesReportsDailyListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    earning_rule_id = 'earning_rule_id_example' # str | Identifies the earning rule. Format lern_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.

    try:
        # List member earning-rule daily reports
        api_response = api_instance.get_member_earning_rule_daily_report(program_id, member_id, earning_rule_id, start_date, end_date, resolution)
        print("The response of LV2ProgramsApi->get_member_earning_rule_daily_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->get_member_earning_rule_daily_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **earning_rule_id** | **str**| Identifies the earning rule. Format lern_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 

### Return type

[**V2LoyaltiesProgramsMembersEarningRulesReportsDailyListResponseBody**](V2LoyaltiesProgramsMembersEarningRulesReportsDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Member earning-rule daily report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_program_member**
> V2LoyaltiesProgramsMembersGetResponseBody get_program_member(program_id, member_id)

Get program member

Returns one member of the program together with that members loyalty cards. Each card includes balance, lifetime_bucket, next_expiration, and next_activation. tier_progress is not included. Use [Get program membership](/api-reference/programs/get-program-membership) when you need tier progress. card.code can be null shortly after member creation, while code generation is still running. Returns 404 when the program doesnt exist, or when the member doesnt exist in that program. The program is checked first.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_get_response_body import V2LoyaltiesProgramsMembersGetResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.

    try:
        # Get program member
        api_response = api_instance.get_program_member(program_id, member_id)
        print("The response of LV2ProgramsApi->get_program_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->get_program_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 

### Return type

[**V2LoyaltiesProgramsMembersGetResponseBody**](V2LoyaltiesProgramsMembersGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The member with its cards. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_program_membership**
> V2LoyaltiesProgramsMembershipsGetResponseBody get_program_membership(program_id, customer_id, identification_type=identification_type)

Get program membership

Returns the membership for one customer in the program: the member, the program, and the members loyalty cards. A card includes tier_progress when its card definition has a tier structure and the member has a tier on that card. Otherwise tier_progress is omitted. identification_type chooses how customerId is read. It defaults to customer_id.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_memberships_get_response_body import V2LoyaltiesProgramsMembershipsGetResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    customer_id = 'customer_id_example' # str | Identifies the customer or member. identification_type selects the value: a Voucherify customer ID (cust_...), a customer source_id, or a loyalty member ID (lmbr_...).
    identification_type = customer_id # str | Selects how customerId is read. customer_id is the Voucherify customer ID and the default. customer_source_id is the customers source_id. member_id is the loyalty member ID. (optional) (default to customer_id)

    try:
        # Get program membership
        api_response = api_instance.get_program_membership(program_id, customer_id, identification_type=identification_type)
        print("The response of LV2ProgramsApi->get_program_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->get_program_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **customer_id** | **str**| Identifies the customer or member. identification_type selects the value: a Voucherify customer ID (cust_...), a customer source_id, or a loyalty member ID (lmbr_...). | 
 **identification_type** | **str**| Selects how customerId is read. customer_id is the Voucherify customer ID and the default. customer_source_id is the customers source_id. member_id is the loyalty member ID. | [optional] [default to customer_id]

### Return type

[**V2LoyaltiesProgramsMembershipsGetResponseBody**](V2LoyaltiesProgramsMembershipsGetResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The membership in the program. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_program_points_earnings_daily_report**
> V2LoyaltiesProgramsReportsPointsEarningsDailyListResponseBody get_program_points_earnings_daily_report(program_id, start_date, end_date, resolution, filters=filters)

List program points-earnings daily reports

Returns aggregated daily points-earnings statistics for the program over the given date range and resolution, optionally filtered by earning rule and card definition. Each entry sums earning operations recorded for one period, earning rule, earning item, and card definition. Periods without recorded activity are omitted. A filter that matches no rows returns an empty data array. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_reports_points_earnings_daily_list_response_body import V2LoyaltiesProgramsReportsPointsEarningsDailyListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.
    filters = voucherify.PointsEarningsReportListFilters() # PointsEarningsReportListFilters | Filters the results. Pass a deep object, for example filters[earning_rule_id][conditions][$is] lern_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program points-earnings daily reports
        api_response = api_instance.get_program_points_earnings_daily_report(program_id, start_date, end_date, resolution, filters=filters)
        print("The response of LV2ProgramsApi->get_program_points_earnings_daily_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->get_program_points_earnings_daily_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 
 **filters** | [**PointsEarningsReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[earning_rule_id][conditions][$is] lern_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsReportsPointsEarningsDailyListResponseBody**](V2LoyaltiesProgramsReportsPointsEarningsDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program points-earnings daily report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_program_points_earnings_summary_report**
> V2LoyaltiesProgramsReportsPointsEarningsSummaryListResponseBody get_program_points_earnings_summary_report(program_id, filters=filters)

List program points-earnings summary reports

Returns total points-earnings statistics for the program (all time), optionally filtered by earning rule or card definition. Each entry sums earning operations for one earning rule, earning item, and card definition. Returns at most 100 rows, ordered by id descending. limit and order are not query parameters. A filter that matches no rows returns an empty data array. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_reports_points_earnings_summary_list_response_body import V2LoyaltiesProgramsReportsPointsEarningsSummaryListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    filters = voucherify.PointsEarningsReportListFilters() # PointsEarningsReportListFilters | Filters the results. Pass a deep object, for example filters[earning_rule_id][conditions][$is] lern_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program points-earnings summary reports
        api_response = api_instance.get_program_points_earnings_summary_report(program_id, filters=filters)
        print("The response of LV2ProgramsApi->get_program_points_earnings_summary_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->get_program_points_earnings_summary_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **filters** | [**PointsEarningsReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[earning_rule_id][conditions][$is] lern_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsReportsPointsEarningsSummaryListResponseBody**](V2LoyaltiesProgramsReportsPointsEarningsSummaryListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program points-earnings summary report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_card_activities**
> V2LoyaltiesProgramsMembersCardsActivitiesListResponseBody list_card_activities(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)

List card activities

Returns a cursor-paginated list of activities recorded for the members card. The card must still be assigned to that member. Filters are id, type, and created_at. Default order is -created_at, then id ascending. Returns 404 when the program doesnt exist, when the member doesnt exist in that program, or when the card isnt currently assigned to that member. The program is checked first, then the member. A DELETED member returns 404 with resource_type member. A missing assignment and a missing or deleted card both return 404 with resource_type card. Returns 400 with key invalid_query_params when the query fails validation. That check runs before the program, member, and card lookup. A cursor that doesnt match ^lcrsacrd_[a-f0-9]+$, a limit outside 1 to 100, an order other than created_at or -created_at, or an array that orders by both directions fails here. After the program, member, and card are found, an unknown or expired cursor returns invalid_or_expired_cursor. A cursor recorded for different filters or order returns cursor_and_query_mismatch. The cursor stays valid when only limit changes.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_cards_activities_list_response_body import V2LoyaltiesProgramsMembersCardsActivitiesListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrsacrd_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersCardsActivitiesListRequestQueryFilters() # V2LoyaltiesProgramsMembersCardsActivitiesListRequestQueryFilters | Filters the results. Pass a deep object, for example filters[type][conditions][$is] vl.card.created. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List card activities
        api_response = api_instance.list_card_activities(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_card_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_card_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrsacrd_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersCardsActivitiesListRequestQueryFilters**](.md)| Filters the results. Pass a deep object, for example filters[type][conditions][$is] vl.card.created. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersCardsActivitiesListResponseBody**](V2LoyaltiesProgramsMembersCardsActivitiesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Cursor-paginated list of card activities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_card_expiring_points**
> V2LoyaltiesProgramsMembersCardsExpiringPointsListResponseBody list_card_expiring_points(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)

List card expiring points buckets

Returns a cursor-paginated list of ACTIVE point expiration buckets for the members card. Each bucket groups points that share an expiration date and expiration type, including points from separate transactions. The list starts on the current project day. Earlier buckets are omitted. Results can be filtered by card definition ID and expiration date, and ordered by expiration_date. Returns an empty list when the card has no matching buckets. Returns 400 when the query is invalid or the cursor is invalid, expired, or doesnt match the query. Returns 404 when the program or the member doesnt exist, or when the card isnt assigned to that member.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_cards_expiring_points_list_response_body import V2LoyaltiesProgramsMembersCardsExpiringPointsListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to expiration_date. Soonest expiration first. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrspeb_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersCardsExpiringPointsListRequestQuery() # V2LoyaltiesProgramsMembersCardsExpiringPointsListRequestQuery | Filters the results. Pass a deep object, for example filters[card_definition_id][conditions][$is] lcdef_1297339938ae248cea. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List card expiring points buckets
        api_response = api_instance.list_card_expiring_points(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_card_expiring_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_card_expiring_points: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to expiration_date. Soonest expiration first. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrspeb_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersCardsExpiringPointsListRequestQuery**](.md)| Filters the results. Pass a deep object, for example filters[card_definition_id][conditions][$is] lcdef_1297339938ae248cea. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersCardsExpiringPointsListResponseBody**](V2LoyaltiesProgramsMembersCardsExpiringPointsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Cursor-paginated list of points expiration buckets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_card_pending_points**
> V2LoyaltiesProgramsMembersCardsPendingPointsListResponseBody list_card_pending_points(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)

List card pending point buckets

Returns a cursor-paginated list of pending point buckets for the members card. Every bucket has status PENDING. Pending points wait for activation (PERIOD_BASED, FIXED_DATES, or EVENT_BASED), following the card definition. The list starts on the next project day. The current days bucket is omitted because its still accumulating. Results can be filtered by card definition ID and ordered by date. Returns 404 when the program or the member doesnt exist, or when the card isnt assigned to that member. Bucket IDs from this list are the bucketId for [Activate pending point bucket](/api-reference/programs/activate-pending-point-bucket) and [Cancel pending point bucket](/api-reference/programs/cancel-pending-point-bucket).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_cards_pending_points_list_response_body import V2LoyaltiesProgramsMembersCardsPendingPointsListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to date. Soonest activation first. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrscppb_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersCardsPendingPointsListRequestQuery() # V2LoyaltiesProgramsMembersCardsPendingPointsListRequestQuery | Filters the results. Pass a deep object, for example filters[card_definition_id][conditions][$is] lcdef_128f495f720c4bec8c. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List card pending point buckets
        api_response = api_instance.list_card_pending_points(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_card_pending_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_card_pending_points: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to date. Soonest activation first. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrscppb_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersCardsPendingPointsListRequestQuery**](.md)| Filters the results. Pass a deep object, for example filters[card_definition_id][conditions][$is] lcdef_128f495f720c4bec8c. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersCardsPendingPointsListResponseBody**](V2LoyaltiesProgramsMembersCardsPendingPointsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Cursor-paginated list of pending point buckets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_card_transactions**
> V2LoyaltiesProgramsMembersCardsTransactionsListResponseBody list_card_transactions(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)

List card transactions

Returns a cursor-paginated list of transactions on the members card. Filter by id, card_definition_id, and created_at. Order by id (default -id, newest first). Returns 404 when the program, member, or card doesnt exist. The program is checked first, then the member, then the card. A member of another program, or a card that isnt assigned to this member, is not found.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_cards_transactions_list_response_body import V2LoyaltiesProgramsMembersCardsTransactionsListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrsctx_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersCardsTransactionsListRequestQuery() # V2LoyaltiesProgramsMembersCardsTransactionsListRequestQuery | Filters the results. Pass a deep object, for example filters[id][conditions][$is] lctx_0f5d0a8878caa3ee5c. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List card transactions
        api_response = api_instance.list_card_transactions(program_id, member_id, card_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_card_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_card_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrsctx_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersCardsTransactionsListRequestQuery**](.md)| Filters the results. Pass a deep object, for example filters[id][conditions][$is] lctx_0f5d0a8878caa3ee5c. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersCardsTransactionsListResponseBody**](V2LoyaltiesProgramsMembersCardsTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Cursor-paginated list of card transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_benefit_transactions**
> V2LoyaltiesProgramsMembersBenefitsTransactionsListResponseBody list_member_benefit_transactions(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)

List member benefit transactions

Lists benefit transactions (benefit fulfillments) for a given program member, with cursor-based pagination. Supports filtering by benefit ID and creation date.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_benefits_transactions_list_response_body import V2LoyaltiesProgramsMembersBenefitsTransactionsListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrsbtx_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersBenefitsTransactionsListRequestQuery() # V2LoyaltiesProgramsMembersBenefitsTransactionsListRequestQuery | Filters the results. Pass a deep object, for example filters[benefit_id][conditions][$is] lben_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List member benefit transactions
        api_response = api_instance.list_member_benefit_transactions(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_member_benefit_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_member_benefit_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrsbtx_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersBenefitsTransactionsListRequestQuery**](.md)| Filters the results. Pass a deep object, for example filters[benefit_id][conditions][$is] lben_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersBenefitsTransactionsListResponseBody**](V2LoyaltiesProgramsMembersBenefitsTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Paginated list of benefit transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_card_daily_reports**
> LoyaltiesProgramsMembersCardsReportsDailyListResponseBody list_member_card_daily_reports(program_id, member_id, card_id, start_date, end_date, resolution)

List card daily points reports

Returns aggregated points statistics for a members loyalty card over the given date range and resolution. Each entry sums the point operations recorded in one period. Periods without recorded activity are omitted. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program or member does not exist, or when the card does not exist or is not assigned to the member in the program.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_cards_reports_daily_list_response_body import LoyaltiesProgramsMembersCardsReportsDailyListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    card_id = 'card_id_example' # str | Identifies the loyalty card. Format lcrd_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.

    try:
        # List card daily points reports
        api_response = api_instance.list_member_card_daily_reports(program_id, member_id, card_id, start_date, end_date, resolution)
        print("The response of LV2ProgramsApi->list_member_card_daily_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_member_card_daily_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **card_id** | **str**| Identifies the loyalty card. Format lcrd_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 

### Return type

[**LoyaltiesProgramsMembersCardsReportsDailyListResponseBody**](LoyaltiesProgramsMembersCardsReportsDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Card daily points report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_order_payments**
> V2LoyaltiesProgramsMembersOrdersPaymentsListResponseBody list_member_order_payments(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)

List member order payments

Lists stored PAY_WITH_POINTS order transactions for the program member, with cursor pagination. Filter by id, card_definition_id, and created_at. Order by id (default -id, newest first). Dry-run (SIMULATED) results arent stored and dont appear. Returns 404 when the program or the member doesnt exist. The program is checked first.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_orders_payments_list_response_body import V2LoyaltiesProgramsMembersOrdersPaymentsListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrsotx_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersOrdersPaymentsListRequestQuery() # V2LoyaltiesProgramsMembersOrdersPaymentsListRequestQuery | Filters the results. Pass a deep object, for example filters[id][conditions][$is] lotx_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List member order payments
        api_response = api_instance.list_member_order_payments(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_member_order_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_member_order_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrsotx_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersOrdersPaymentsListRequestQuery**](.md)| Filters the results. Pass a deep object, for example filters[id][conditions][$is] lotx_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersOrdersPaymentsListResponseBody**](V2LoyaltiesProgramsMembersOrdersPaymentsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returns a paginated list of persisted order payment transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_reward_purchases**
> V2LoyaltiesProgramsMembersRewardsPurchasesListResponseBody list_member_reward_purchases(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)

List member reward purchases

Lists stored PURCHASE reward transactions for the program member, with cursor pagination. Filter by id, reward_id, card_definition_id, and created_at. Order by id (default -id, newest first). Purchases rejected before a transaction is stored dont appear. A purchase accepted with 202 that later fails is stored as REJECTED with details.rejection. Returns 404 when the program or the member doesnt exist. The program is checked first.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_rewards_purchases_list_response_body import V2LoyaltiesProgramsMembersRewardsPurchasesListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrstrx_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersRewardsPurchasesListRequestQuery() # V2LoyaltiesProgramsMembersRewardsPurchasesListRequestQuery | Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List member reward purchases
        api_response = api_instance.list_member_reward_purchases(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_member_reward_purchases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_member_reward_purchases: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrstrx_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersRewardsPurchasesListRequestQuery**](.md)| Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersRewardsPurchasesListResponseBody**](V2LoyaltiesProgramsMembersRewardsPurchasesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Paginated list of reward purchase transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_member_tier_transactions**
> V2LoyaltiesProgramsMembersTiersTransactionsListResponseBody list_member_tier_transactions(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)

List member tier transactions

Lists tier transactions for the member: joins, leaves, upgrades, downgrades, expiration changes, and evaluation refreshes. Results use cursor pagination. Default order is -id, newest first. Filters are card_id, card_definition_id, and created_at. Returns 404 when the program doesnt exist, or when the member doesnt exist in that program. The program is checked first. A DELETED member returns 404. Returns 400 with key invalid_query_params when the query fails validation. That check runs before the program and member lookup. order must be id or -id. An array that orders by both directions is rejected. A cursor that doesnt match ^lcrsttx_[a-f0-9]+$ fails here. After the program and member are found, an unknown or expired cursor returns invalid_or_expired_cursor. A cursor recorded for different filters or order returns cursor_and_query_mismatch. The cursor stays valid when only limit changes.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_tiers_transactions_list_response_body import V2LoyaltiesProgramsMembersTiersTransactionsListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrsttx_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersTiersTransactionsListRequestQuery() # V2LoyaltiesProgramsMembersTiersTransactionsListRequestQuery | Filters the results. Pass a deep object, for example filters[card_id][conditions][$is] lcrd_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List member tier transactions
        api_response = api_instance.list_member_tier_transactions(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_member_tier_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_member_tier_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -id. Newest first. The same field cannot be used in both directions. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrsttx_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersTiersTransactionsListRequestQuery**](.md)| Filters the results. Pass a deep object, for example filters[card_id][conditions][$is] lcrd_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersTiersTransactionsListResponseBody**](V2LoyaltiesProgramsMembersTiersTransactionsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Paginated list of tier transactions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_earning_rule_assignments**
> V2LoyaltiesProgramsEarningRulesListResponseBody list_program_earning_rule_assignments(program_id, limit=limit, order=order, cursor=cursor)

List program earning rule assignments

Returns a cursor-paginated list of earning rules assigned to the program.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_earning_rules_list_response_body import V2LoyaltiesProgramsEarningRulesListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    limit = '10' # str | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to '10')
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrserna_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)

    try:
        # List program earning rule assignments
        api_response = api_instance.list_program_earning_rule_assignments(program_id, limit=limit, order=order, cursor=cursor)
        print("The response of LV2ProgramsApi->list_program_earning_rule_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_earning_rule_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **limit** | **str**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to &#39;10&#39;]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrserna_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 

### Return type

[**V2LoyaltiesProgramsEarningRulesListResponseBody**](V2LoyaltiesProgramsEarningRulesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Paginated list of earning rule assignments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_earning_rules_daily_reports**
> V2LoyaltiesProgramsReportsEarningRulesDailyListResponseBody list_program_earning_rules_daily_reports(program_id, start_date, end_date, resolution, filters=filters)

List program earning-rules daily reports

Returns aggregated daily earning-rule evaluation statistics for the program over the given date range and resolution, optionally filtered by earning rule. Each entry counts eligibility checks for one period and earning rule. Periods without recorded activity are omitted. failures_breakdown is always an empty object. A filter that matches no rows returns an empty data array. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.earning_rules_report_list_filters import EarningRulesReportListFilters
from voucherify.models.v2_loyalties_programs_reports_earning_rules_daily_list_response_body import V2LoyaltiesProgramsReportsEarningRulesDailyListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.
    filters = voucherify.EarningRulesReportListFilters() # EarningRulesReportListFilters | Filters the results. Pass a deep object, for example filters[earning_rule_id][conditions][$is] lern_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program earning-rules daily reports
        api_response = api_instance.list_program_earning_rules_daily_reports(program_id, start_date, end_date, resolution, filters=filters)
        print("The response of LV2ProgramsApi->list_program_earning_rules_daily_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_earning_rules_daily_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 
 **filters** | [**EarningRulesReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[earning_rule_id][conditions][$is] lern_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsReportsEarningRulesDailyListResponseBody**](V2LoyaltiesProgramsReportsEarningRulesDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program earning-rules daily report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_earning_rules_summary_reports**
> V2LoyaltiesProgramsReportsEarningRulesSummaryListResponseBody list_program_earning_rules_summary_reports(program_id, filters=filters)

List program earning-rules summary reports

Returns total earning-rule evaluation statistics for the program (all time), optionally filtered by earning rule. Includes success and failure counts with a failures breakdown. Each entry counts eligibility checks for one earning rule. Returns at most 100 rows, ordered by id descending. limit and order are not query parameters. A filter that matches no rows returns an empty data array. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.earning_rules_report_list_filters import EarningRulesReportListFilters
from voucherify.models.v2_loyalties_programs_reports_earning_rules_summary_list_response_body import V2LoyaltiesProgramsReportsEarningRulesSummaryListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    filters = voucherify.EarningRulesReportListFilters() # EarningRulesReportListFilters | Filters the results. Pass a deep object, for example filters[earning_rule_id][conditions][$is] lern_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program earning-rules summary reports
        api_response = api_instance.list_program_earning_rules_summary_reports(program_id, filters=filters)
        print("The response of LV2ProgramsApi->list_program_earning_rules_summary_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_earning_rules_summary_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **filters** | [**EarningRulesReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[earning_rule_id][conditions][$is] lern_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsReportsEarningRulesSummaryListResponseBody**](V2LoyaltiesProgramsReportsEarningRulesSummaryListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program earning-rules summary report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_member_activities**
> V2LoyaltiesProgramsMembersActivitiesListResponseBody list_program_member_activities(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)

List program member activities

Returns a cursor-paginated list of lifecycle and card-assignment activities recorded for the member. Filters are id, type, and created_at. Default order is -created_at, then id ascending. Returns 404 when the program doesnt exist, or when the member doesnt exist in that program. The program is checked first. A DELETED member returns 404. Returns 400 with key invalid_query_params when the query fails validation. That check runs before the program and member lookup. A cursor that doesnt match ^lcrsambr_[a-f0-9]+$, a limit outside 1 to 100, an order other than created_at or -created_at, or an array that orders by both directions fails here. After the program and member are found, an unknown or expired cursor returns invalid_or_expired_cursor. A cursor recorded for different filters or order returns cursor_and_query_mismatch. The cursor stays valid when only limit changes.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_activities_list_response_body import V2LoyaltiesProgramsMembersActivitiesListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrsambr_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersActivitiesListRequestQueryFilters() # V2LoyaltiesProgramsMembersActivitiesListRequestQueryFilters | Filters the results. Pass a deep object, for example filters[type][conditions][$is] vl.member.created. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program member activities
        api_response = api_instance.list_program_member_activities(program_id, member_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_program_member_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_member_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrsambr_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersActivitiesListRequestQueryFilters**](.md)| Filters the results. Pass a deep object, for example filters[type][conditions][$is] vl.member.created. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersActivitiesListResponseBody**](V2LoyaltiesProgramsMembersActivitiesListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Cursor-paginated list of member activities. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_members**
> V2LoyaltiesProgramsMembersListResponseBody list_program_members(program_id, limit=limit, order=order, cursor=cursor, filters=filters)

List program members

Returns a cursor-paginated list of members of the program. Deleted members are omitted. Results can be filtered by ID, status, customer ID and creation date. Results can be ordered by creation date, status, or customer ID (ascending or descending). The same field cannot be ordered both ascending and descending at the same time. Returns 404 when the program does not exist. List items do not include the cards array. Use the following endpoints to retrieve cards for a given member: - [Get customer memberships](/api-reference/programs/get-customer-memberships), - [Get program member](/api-reference/programs/get-program-member), - [Get program membership](/api-reference/programs/get-program-membership).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_list_response_body import V2LoyaltiesProgramsMembersListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    limit = 10 # int | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to 10)
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrsmbr_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)
    filters = voucherify.V2LoyaltiesProgramsMembersListRequestQuery() # V2LoyaltiesProgramsMembersListRequestQuery | Filters the results. Pass a deep object, for example filters[status][conditions][$is] ACTIVE. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program members
        api_response = api_instance.list_program_members(program_id, limit=limit, order=order, cursor=cursor, filters=filters)
        print("The response of LV2ProgramsApi->list_program_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **limit** | **int**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to 10]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrsmbr_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 
 **filters** | [**V2LoyaltiesProgramsMembersListRequestQuery**](.md)| Filters the results. Pass a deep object, for example filters[status][conditions][$is] ACTIVE. Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersListResponseBody**](V2LoyaltiesProgramsMembersListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Cursor-paginated list of members. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_members_daily_reports**
> LoyaltiesProgramsReportsMembersDailyListResponseBody list_program_members_daily_reports(program_id, start_date, end_date, resolution)

List program members daily reports

Returns member and card changes for the program over the given date range and resolution. Each row covers one period with recorded activity. Periods without activity are omitted. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_reports_members_daily_list_response_body import LoyaltiesProgramsReportsMembersDailyListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.

    try:
        # List program members daily reports
        api_response = api_instance.list_program_members_daily_reports(program_id, start_date, end_date, resolution)
        print("The response of LV2ProgramsApi->list_program_members_daily_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_members_daily_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 

### Return type

[**LoyaltiesProgramsReportsMembersDailyListResponseBody**](LoyaltiesProgramsReportsMembersDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program members daily report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_members_summary_reports**
> LoyaltiesProgramsReportsMembersSummaryListResponseBody list_program_members_summary_reports(program_id)

List program members summary reports

Returns all-time member and card totals for the program. The response contains one row when activity was recorded, and an empty data array otherwise. limit and order are not query parameters. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_reports_members_summary_list_response_body import LoyaltiesProgramsReportsMembersSummaryListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.

    try:
        # List program members summary reports
        api_response = api_instance.list_program_members_summary_reports(program_id)
        print("The response of LV2ProgramsApi->list_program_members_summary_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_members_summary_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 

### Return type

[**LoyaltiesProgramsReportsMembersSummaryListResponseBody**](LoyaltiesProgramsReportsMembersSummaryListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program members summary report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_reward_assignments**
> V2LoyaltiesProgramsRewardsListResponseBody list_program_reward_assignments(program_id, limit=limit, order=order, cursor=cursor)

List program reward assignments

Returns a cursor-paginated list of rewards assigned to the program, including their stock configuration and redemption counters.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_rewards_list_response_body import V2LoyaltiesProgramsRewardsListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    limit = '10' # str | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to '10')
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrsrewa_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)

    try:
        # List program reward assignments
        api_response = api_instance.list_program_reward_assignments(program_id, limit=limit, order=order, cursor=cursor)
        print("The response of LV2ProgramsApi->list_program_reward_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_reward_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **limit** | **str**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to &#39;10&#39;]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrsrewa_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 

### Return type

[**V2LoyaltiesProgramsRewardsListResponseBody**](V2LoyaltiesProgramsRewardsListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Paginated list of reward assignments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_rewards_daily_reports**
> LoyaltiesProgramsReportsRewardsDailyListResponseBody list_program_rewards_daily_reports(program_id, start_date, end_date, resolution, filters=filters)

List program rewards daily reports

Returns aggregated reward-purchase statistics for the program over the given date range and resolution, optionally filtered by reward. Each row covers one reward and one period with recorded purchases. Periods without recorded purchases are omitted. failures_breakdown is always an empty object. A filter that matches no rows returns an empty data array. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_reports_rewards_daily_list_response_body import LoyaltiesProgramsReportsRewardsDailyListResponseBody
from voucherify.models.rewards_report_list_filters import RewardsReportListFilters
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.
    filters = voucherify.RewardsReportListFilters() # RewardsReportListFilters | Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program rewards daily reports
        api_response = api_instance.list_program_rewards_daily_reports(program_id, start_date, end_date, resolution, filters=filters)
        print("The response of LV2ProgramsApi->list_program_rewards_daily_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_rewards_daily_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 
 **filters** | [**RewardsReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**LoyaltiesProgramsReportsRewardsDailyListResponseBody**](LoyaltiesProgramsReportsRewardsDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program rewards daily report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_rewards_spendings_daily_reports**
> LoyaltiesProgramsReportsRewardsSpendingsDailyListResponseBody list_program_rewards_spendings_daily_reports(program_id, start_date, end_date, resolution, filters=filters)

List program rewards spendings daily reports

Returns aggregated points spent on reward purchases for the program over the given date range and resolution. Each row covers one reward, reward cost, reward spending, card definition, and period with an approved point spend. Periods without an approved point spend are omitted. Optionally filters by reward, cost, spending, and card definition. A filter that matches no rows returns an empty data array. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_reports_rewards_spendings_daily_list_response_body import LoyaltiesProgramsReportsRewardsSpendingsDailyListResponseBody
from voucherify.models.rewards_spendings_report_list_filters import RewardsSpendingsReportListFilters
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.
    filters = voucherify.RewardsSpendingsReportListFilters() # RewardsSpendingsReportListFilters | Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program rewards spendings daily reports
        api_response = api_instance.list_program_rewards_spendings_daily_reports(program_id, start_date, end_date, resolution, filters=filters)
        print("The response of LV2ProgramsApi->list_program_rewards_spendings_daily_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_rewards_spendings_daily_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 
 **filters** | [**RewardsSpendingsReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**LoyaltiesProgramsReportsRewardsSpendingsDailyListResponseBody**](LoyaltiesProgramsReportsRewardsSpendingsDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program rewards spendings daily report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_rewards_spendings_summary_reports**
> LoyaltiesProgramsReportsRewardsSpendingsSummaryListResponseBody list_program_rewards_spendings_summary_reports(program_id, filters=filters)

List program rewards spendings summary reports

Returns all-time points spent on reward purchases for the program. Each row covers one reward, reward cost, reward spending, and card definition with an approved point spend. Filters rows by reward, cost, spending, and card definition. Returns at most 100 rows, ordered by id descending. limit and order are not query parameters. A filter that matches no rows returns an empty data array. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_reports_rewards_spendings_summary_list_response_body import LoyaltiesProgramsReportsRewardsSpendingsSummaryListResponseBody
from voucherify.models.rewards_spendings_report_list_filters import RewardsSpendingsReportListFilters
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    filters = voucherify.RewardsSpendingsReportListFilters() # RewardsSpendingsReportListFilters | Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program rewards spendings summary reports
        api_response = api_instance.list_program_rewards_spendings_summary_reports(program_id, filters=filters)
        print("The response of LV2ProgramsApi->list_program_rewards_spendings_summary_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_rewards_spendings_summary_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **filters** | [**RewardsSpendingsReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**LoyaltiesProgramsReportsRewardsSpendingsSummaryListResponseBody**](LoyaltiesProgramsReportsRewardsSpendingsSummaryListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program rewards spendings summary report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_rewards_summary_reports**
> LoyaltiesProgramsReportsRewardsSummaryListResponseBody list_program_rewards_summary_reports(program_id, filters=filters)

List program rewards summary reports

Returns all-time reward-purchase totals for the program, one row per reward with a recorded purchase attempt. Filters rows with filters[reward_id]. Returns at most 100 rows, ordered by id descending. limit and order are not query parameters. A filter that matches no rows returns an empty data array. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_reports_rewards_summary_list_response_body import LoyaltiesProgramsReportsRewardsSummaryListResponseBody
from voucherify.models.rewards_report_list_filters import RewardsReportListFilters
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    filters = voucherify.RewardsReportListFilters() # RewardsReportListFilters | Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program rewards summary reports
        api_response = api_instance.list_program_rewards_summary_reports(program_id, filters=filters)
        print("The response of LV2ProgramsApi->list_program_rewards_summary_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_rewards_summary_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **filters** | [**RewardsReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[reward_id][conditions][$is] lrew_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**LoyaltiesProgramsReportsRewardsSummaryListResponseBody**](LoyaltiesProgramsReportsRewardsSummaryListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program rewards summary report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_spending_daily_reports**
> LoyaltiesProgramsReportsSpendingDailyListResponseBody list_program_spending_daily_reports(program_id, start_date, end_date, resolution, filters=filters)

List program spending daily reports

Returns aggregated points-spending statistics for the program over the given date range and resolution. Each row covers one card definition and one period with recorded spending. Periods without recorded spending are omitted. Optionally filters by card definition. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_reports_spending_daily_list_response_body import LoyaltiesProgramsReportsSpendingDailyListResponseBody
from voucherify.models.spending_report_list_filters import SpendingReportListFilters
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.
    filters = voucherify.SpendingReportListFilters() # SpendingReportListFilters | Filters the results. Pass a deep object, for example filters[card_definition_id][conditions][$is] lcdef_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program spending daily reports
        api_response = api_instance.list_program_spending_daily_reports(program_id, start_date, end_date, resolution, filters=filters)
        print("The response of LV2ProgramsApi->list_program_spending_daily_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_spending_daily_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 
 **filters** | [**SpendingReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[card_definition_id][conditions][$is] lcdef_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**LoyaltiesProgramsReportsSpendingDailyListResponseBody**](LoyaltiesProgramsReportsSpendingDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program spending daily report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_spending_summary_reports**
> LoyaltiesProgramsReportsSpendingSummaryListResponseBody list_program_spending_summary_reports(program_id, filters=filters)

List program spending summary reports

Returns all-time point-spending totals for the program, one row per card definition that has recorded spending. Filters rows with filters[card_definition_id]. Returns at most 10 rows (max number of card definitions per program), ordered by id descending. limit and order are not query parameters. Returns 200 with an empty data array when no spending is recorded. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_reports_spending_summary_list_response_body import LoyaltiesProgramsReportsSpendingSummaryListResponseBody
from voucherify.models.spending_report_list_filters import SpendingReportListFilters
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    filters = voucherify.SpendingReportListFilters() # SpendingReportListFilters | Filters the results. Pass a deep object, for example filters[card_definition_id][conditions][$is] lcdef_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program spending summary reports
        api_response = api_instance.list_program_spending_summary_reports(program_id, filters=filters)
        print("The response of LV2ProgramsApi->list_program_spending_summary_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_spending_summary_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **filters** | [**SpendingReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[card_definition_id][conditions][$is] lcdef_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**LoyaltiesProgramsReportsSpendingSummaryListResponseBody**](LoyaltiesProgramsReportsSpendingSummaryListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program spending summary report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_tier_structure_assignments**
> V2LoyaltiesProgramsTierStructuresListResponseBody list_program_tier_structure_assignments(program_id, limit=limit, order=order, cursor=cursor)

List program tier structure assignments

Returns a cursor-paginated list of tier structures assigned to the program. Currently, a program can have only one tier structure assigned.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_tier_structures_list_response_body import V2LoyaltiesProgramsTierStructuresListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    limit = '10' # str | Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. (optional) (default to '10')
    order = 'order_example' # str | Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. (optional)
    cursor = 'cursor_example' # str | Continues pagination. Pass the cursor.next value from a previous response. Format lcrstsa_[a-f0-9]+. The cursor matches the filters and order of that response. (optional)

    try:
        # List program tier structure assignments
        api_response = api_instance.list_program_tier_structure_assignments(program_id, limit=limit, order=order, cursor=cursor)
        print("The response of LV2ProgramsApi->list_program_tier_structure_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_tier_structure_assignments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **limit** | **str**| Limits the page size to an integer from 1 to 100. Defaults to 10. A numeric string is accepted and rounded to the nearest integer. | [optional] [default to &#39;10&#39;]
 **order** | **str**| Orders the results. Accepts one value or an array. Prefix a field with - for descending order. Defaults to -created_at. The same field cannot be used in both directions. Rows with the same sort value are then ordered by id ascending. | [optional] 
 **cursor** | **str**| Continues pagination. Pass the cursor.next value from a previous response. Format lcrstsa_[a-f0-9]+. The cursor matches the filters and order of that response. | [optional] 

### Return type

[**V2LoyaltiesProgramsTierStructuresListResponseBody**](V2LoyaltiesProgramsTierStructuresListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Paginated list of tier structure assignments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_tiers_daily_reports**
> V2LoyaltiesProgramsReportsTiersDailyListResponseBody list_program_tiers_daily_reports(program_id, start_date, end_date, resolution, filters=filters)

List program tiers daily reports

Returns aggregated tier-movement statistics for the program over the given date range and resolution, optionally filtered by tier structure and tier. Each row covers one tier structure, one tier, and one period with recorded movement. Periods without recorded movement are omitted. A filter that matches no rows returns an empty data array. The date range is limited per resolution: - 90 days for day, - 12 weeks for week, - 12 months for month, - 4 quarters for quarter, - start_date must be before end_date, - start_date and end_date are inclusive. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.tiers_report_list_filters import TiersReportListFilters
from voucherify.models.v2_loyalties_programs_reports_tiers_daily_list_response_body import V2LoyaltiesProgramsReportsTiersDailyListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    start_date = '2013-10-20' # date | Sets the inclusive start of the report date range. Format YYYY-MM-DD.
    end_date = '2013-10-20' # date | Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date.
    resolution = 'resolution_example' # str | Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters.
    filters = voucherify.TiersReportListFilters() # TiersReportListFilters | Filters the results. Pass a deep object, for example filters[tier_structure_id][conditions][$is] lts_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program tiers daily reports
        api_response = api_instance.list_program_tiers_daily_reports(program_id, start_date, end_date, resolution, filters=filters)
        print("The response of LV2ProgramsApi->list_program_tiers_daily_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_tiers_daily_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **start_date** | **date**| Sets the inclusive start of the report date range. Format YYYY-MM-DD. | 
 **end_date** | **date**| Sets the inclusive end of the report date range. Format YYYY-MM-DD. Must be after start_date. | 
 **resolution** | **str**| Sets the aggregation resolution. day allows at most 90 days, week at most 12 weeks, month at most 12 months, and quarter at most 4 quarters. | 
 **filters** | [**TiersReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[tier_structure_id][conditions][$is] lts_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsReportsTiersDailyListResponseBody**](V2LoyaltiesProgramsReportsTiersDailyListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program tiers daily report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_program_tiers_summary_reports**
> V2LoyaltiesProgramsReportsTiersSummaryListResponseBody list_program_tiers_summary_reports(program_id, filters=filters)

List program tiers summary reports

Returns all-time tier-movement totals for the program, one row per tier structure and tier that has recorded movement. Filters rows with filters[tier_structure_id] and filters[tier_id]. Returns at most 100 rows, ordered by id descending. limit and order are not query parameters. A filter that matches no rows returns an empty data array. Returns 400 when query validation fails. Returns 404 when the program does not exist.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.tiers_report_list_filters import TiersReportListFilters
from voucherify.models.v2_loyalties_programs_reports_tiers_summary_list_response_body import V2LoyaltiesProgramsReportsTiersSummaryListResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    filters = voucherify.TiersReportListFilters() # TiersReportListFilters | Filters the results. Pass a deep object, for example filters[tier_id][conditions][$is] lt_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. (optional)

    try:
        # List program tiers summary reports
        api_response = api_instance.list_program_tiers_summary_reports(program_id, filters=filters)
        print("The response of LV2ProgramsApi->list_program_tiers_summary_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->list_program_tiers_summary_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **filters** | [**TiersReportListFilters**](.md)| Filters the results. Pass a deep object, for example filters[tier_id][conditions][$is] lt_.... Fields combine through junction, which defaults to AND. Omit filters to apply no field filter. | [optional] 

### Return type

[**V2LoyaltiesProgramsReportsTiersSummaryListResponseBody**](V2LoyaltiesProgramsReportsTiersSummaryListResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Program tiers summary report. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **purchase_member_reward**
> LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBody purchase_member_reward(program_id, member_id, v2_loyalties_programs_members_rewards_purchases_create_request_body=v2_loyalties_programs_members_rewards_purchases_create_request_body)

Purchase reward with points

Purchases a reward for the program member by spending points from the members card. The card comes from the matching reward costs card definition. The program, reward, and member must be ACTIVE. The program and reward must be inside their validity windows. The reward must be assigned to the program with stock available, a cost must match the customer, and the purchase must stay inside frequency, cooldown, balance, and spending limits. Modes: - TRANSACTION (default): creates a PENDING reward transaction and a PENDING card transaction. Returns 202. - DRY_RUN: simulates the purchase and doesnt create a transaction. Returns 200 with status SIMULATED.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.loyalties_programs_members_rewards_purchases_create_combined_response_body import LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBody
from voucherify.models.v2_loyalties_programs_members_rewards_purchases_create_request_body import V2LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    v2_loyalties_programs_members_rewards_purchases_create_request_body = voucherify.V2LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody() # V2LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody |  (optional)

    try:
        # Purchase reward with points
        api_response = api_instance.purchase_member_reward(program_id, member_id, v2_loyalties_programs_members_rewards_purchases_create_request_body=v2_loyalties_programs_members_rewards_purchases_create_request_body)
        print("The response of LV2ProgramsApi->purchase_member_reward:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->purchase_member_reward: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **v2_loyalties_programs_members_rewards_purchases_create_request_body** | [**V2LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody**](V2LoyaltiesProgramsMembersRewardsPurchasesCreateRequestBody.md)|  | [optional] 

### Return type

[**LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBody**](LoyaltiesProgramsMembersRewardsPurchasesCreateCombinedResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Dry run result (mode &#x60;DRY_RUN&#x60;). No transaction was created; the returned transaction has status &#x60;SIMULATED&#x60; and no &#x60;id&#x60;. and Purchase accepted (mode &#x60;TRANSACTION&#x60;). A &#x60;PENDING&#x60; reward transaction was created and will be processed asynchronously. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refund_reward_purchase**
> V2LoyaltiesProgramsRewardsPurchasesRefundResponseBody refund_reward_purchase(program_id, reward_transaction_id, v2_loyalties_programs_rewards_purchases_refund_request_body=v2_loyalties_programs_rewards_purchases_refund_request_body)

Refund reward purchase

Refunds an APPROVED reward purchase made by a program member. The purchase transaction is marked REFUNDED, a new REFUND reward transaction is created with status APPROVED, and the points spent on the purchase are returned to the members card. The request body is optional and an empty payload is allowed. Policies default to refund: DEFAULT and stock: DEFAULT. The endpoint responds with 202 before the card balance changes. A POINTS_RETURNED card transaction is created for the members card and processed shortly after the response. When the members tier or the card definition expires points, returned points receive a new expiration date from that setting. They dont inherit the expiration of the originally spent points. A NO_EXPIRATION setting leaves the returned points without an expiration date. Card earning limits dont block the refund. For a LOYALTY_CARD_POINTS reward, the points credited to the target card are also reversed, with a POINTS_PURCHASE_REVERSED card transaction on that card. That transaction is processed shortly after the response. Its expiration is copied from the original points-purchased transaction. A DISCOUNT_COUPONS refund deletes the issued vouchers. details.result.digital.discount_coupons[].result is DELETED, or SKIPPED when the voucher isnt deleted. A GIFT_VOUCHERS refund subtracts the credited amount. details.result.digital.gift_vouchers[].result is CREDITS_SUBTRACTED, or SKIPPED when the balance update is rejected. The refund reverses that purchase in the rewards purchase limits for the project-local day of the original purchase. A day whose purchases are all refunded no longer counts as the members last purchase. Only rewards whose refunds.type is REFUNDABLE can be refunded. Any other reward is rejected with 423 and key reward_refund_policy_does_not_allow_refunds. policies.refund set to ALLOW refunds it anyway. The program must exist, and the reward transaction must belong to that program. Otherwise the request fails with 404. The program is checked first. The request is rejected with 423 when: - The program isnt ACTIVE (non_active_program) or is outside its validity window (program_outside_validity_window), - The transaction isnt a purchase (non_purchase_reward_transaction) or isnt APPROVED (non_approved_reward_transaction); refunding the same purchase twice fails here, - The reward no longer exists (reward_not_found), isnt assigned to the program (refund_reward_not_assigned_to_program), the members card is gone (refund_card_not_found), or the card definition is gone (refund_card_definition_not_found), - The reward type isnt supported (reward_type_not_supported_for_refunds), - For a LOYALTY_CARD_POINTS reward, the purchase result is missing (loyalty_card_points_purchase_result_not_found), the target card is gone (loyalty_card_points_target_card_not_found), the points-purchased card transaction is missing (loyalty_card_points_purchase_not_found), the target cards available balance is lower than the purchased points (loyalty_card_points_insufficient_balance), or the target card definition is gone (loyalty_card_points_target_card_definition_not_found).

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_rewards_purchases_refund_request_body import V2LoyaltiesProgramsRewardsPurchasesRefundRequestBody
from voucherify.models.v2_loyalties_programs_rewards_purchases_refund_response_body import V2LoyaltiesProgramsRewardsPurchasesRefundResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    reward_transaction_id = 'reward_transaction_id_example' # str | Identifies the reward transaction of the purchase to refund. Format lrtx_[a-f0-9]+.
    v2_loyalties_programs_rewards_purchases_refund_request_body = voucherify.V2LoyaltiesProgramsRewardsPurchasesRefundRequestBody() # V2LoyaltiesProgramsRewardsPurchasesRefundRequestBody | Optional refund policies. An empty payload is allowed. (optional)

    try:
        # Refund reward purchase
        api_response = api_instance.refund_reward_purchase(program_id, reward_transaction_id, v2_loyalties_programs_rewards_purchases_refund_request_body=v2_loyalties_programs_rewards_purchases_refund_request_body)
        print("The response of LV2ProgramsApi->refund_reward_purchase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->refund_reward_purchase: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **reward_transaction_id** | **str**| Identifies the reward transaction of the purchase to refund. Format lrtx_[a-f0-9]+. | 
 **v2_loyalties_programs_rewards_purchases_refund_request_body** | [**V2LoyaltiesProgramsRewardsPurchasesRefundRequestBody**](V2LoyaltiesProgramsRewardsPurchasesRefundRequestBody.md)| Optional refund policies. An empty payload is allowed. | [optional] 

### Return type

[**V2LoyaltiesProgramsRewardsPurchasesRefundResponseBody**](V2LoyaltiesProgramsRewardsPurchasesRefundResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Refund accepted. The refund reward transaction has been created with status APPROVED and points will be returned to the member&#39;s card asynchronously. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_program_member**
> V2LoyaltiesProgramsMembersUpdateResponseBody update_program_member(program_id, member_id, v2_loyalties_programs_members_update_request_body=v2_loyalties_programs_members_update_request_body)

Update program member

Updates a program members metadata. Provided object keys are merged into the existing metadata; omitted keys are preserved. Pass metadata: null to clear all metadata (sets it to an empty object). This endpoint cannot change status. Use [Activate program member](/api-reference/programs/activate-program-member) or [Deactivate program member](/api-reference/programs/deactivate-program-member) for status transitions. Records a vl.member.updated activity. Returns the updated member without the cards array. Returns 404 when the program or member does not exist. Returns 400 when the request body fails validation or the project vl_member metadata schema rejects the payload.

### Example

* Api Key Authentication (X-App-Id):
* Api Key Authentication (X-App-Token):

```python
import voucherify
from voucherify.models.v2_loyalties_programs_members_update_request_body import V2LoyaltiesProgramsMembersUpdateRequestBody
from voucherify.models.v2_loyalties_programs_members_update_response_body import V2LoyaltiesProgramsMembersUpdateResponseBody
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
    api_instance = voucherify.LV2ProgramsApi(api_client)
    program_id = 'program_id_example' # str | Identifies the loyalty program. Format lprg_[a-f0-9]+.
    member_id = 'member_id_example' # str | Identifies the member. Format lmbr_[a-f0-9]+.
    v2_loyalties_programs_members_update_request_body = voucherify.V2LoyaltiesProgramsMembersUpdateRequestBody() # V2LoyaltiesProgramsMembersUpdateRequestBody |  (optional)

    try:
        # Update program member
        api_response = api_instance.update_program_member(program_id, member_id, v2_loyalties_programs_members_update_request_body=v2_loyalties_programs_members_update_request_body)
        print("The response of LV2ProgramsApi->update_program_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LV2ProgramsApi->update_program_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **program_id** | **str**| Identifies the loyalty program. Format lprg_[a-f0-9]+. | 
 **member_id** | **str**| Identifies the member. Format lmbr_[a-f0-9]+. | 
 **v2_loyalties_programs_members_update_request_body** | [**V2LoyaltiesProgramsMembersUpdateRequestBody**](V2LoyaltiesProgramsMembersUpdateRequestBody.md)|  | [optional] 

### Return type

[**V2LoyaltiesProgramsMembersUpdateResponseBody**](V2LoyaltiesProgramsMembersUpdateResponseBody.md)

### Authorization

[X-App-Id](../README.md#X-App-Id), [X-App-Token](../README.md#X-App-Token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | The updated member (without cards). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

