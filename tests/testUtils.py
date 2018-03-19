from voucherify import Client as voucherifyClient
import os

from dotenv import load_dotenv
load_dotenv()

config = {
    "campaignName": os.getenv('CAMPAIGN_NAME'),
    "voucherify": {
        "applicationId": os.getenv('VOUCHERIFY_APP_ID'),
        "secret": os.getenv('VOUCHERIFY_SECRET')
    }
}

client = voucherifyClient(
        application_id=config['voucherify']['applicationId'],
        client_secret_key=config['voucherify']['secret']
    )


def getConfig():
    return config


def getConfiguredClient():
    return client
