from voucherify import Client as voucherifyClient
import json
import os
base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, 'config.json'), 'r') as f:
    config = json.load(f)

client = voucherifyClient(
        application_id=config['voucherify']['applicationId'],
        client_secret_key=config['voucherify']['secret']
    )


def getConfig():
    return config


def getConfiguredClient():
    return client
