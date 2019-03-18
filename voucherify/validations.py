from urllib.parse import quote

class Validations:
	def __init__(self, client, promotions_namespace: str ):
		self.client = client
		self.promotions_namespace = promotions_namespace
		self.url = '/validations'
