try:
    from urllib.parse import urlencode, quote
except ImportError:
    from urllib import urlencode
    from urllib import quote


class Events:
	def __init__(self, client):
		self.client = client
		self.url = '/events'

	def track(self, event_name, metadata, customer):
		"""
			https://docs.voucherify.io/v2018-08-01/reference#create-custom-event
		"""
		return self.client.post(self.url, {
			'event': event_name,
			'customer': customer,
			'metadata': metadata,
		})
