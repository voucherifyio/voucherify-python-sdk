import os
import voucherify as voucherifyClient
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("VOUCHERIFY_HOST", "https://api.voucherify.io")
X_APP_ID = os.getenv("X_APP_ID")
X_APP_TOKEN = os.getenv("X_APP_TOKEN")

X_MANAGEMENT_ID = os.getenv("X_MANAGEMENT_ID")
X_MANAGEMENT_TOKEN = os.getenv("X_MANAGEMENT_TOKEN")

TEST_PROJECT_ID = os.getenv("PROJECT_ID")

if not X_APP_ID or not X_APP_TOKEN:
    raise ValueError("X_APP_ID and X_APP_TOKEN must be set in the .env file.")

configuration = voucherifyClient.Configuration(
    host=HOST, api_key={"X-App-Id": X_APP_ID, "X-App-Token": X_APP_TOKEN}
)

# Management API
management_configuration = voucherifyClient.Configuration(
    host=HOST,
    api_key={
        "X-Management-Id": X_MANAGEMENT_ID,
        "X-Management-Token": X_MANAGEMENT_TOKEN,
    },
)

# Debugging line
api_key_id = configuration.get_api_key_with_prefix("X-App-Id")
api_key_token = configuration.get_api_key_with_prefix("X-App-Token")

# Print whether both API keys are present and valid
are_keys_present = bool(api_key_id) and bool(api_key_token)
print(f"Configuration loaded: {are_keys_present}")
