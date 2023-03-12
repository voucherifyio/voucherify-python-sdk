try:
    from urllib.parse import urlencode, quote
except ImportError:
    from urllib import urlencode
    from urllib import quote

class Balance:
	def __init__(self, client):
		self.client = client

	def create(self, code, properties):
		return self.client.post('/vouchers/{}/balance'.format(quote(code)), properties)
