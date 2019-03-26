class Redemptions:
	def __init__(self, client, promotions_namespace):
		self.client = client
		self.url = '/redemptions'
		self.promotions_namespace = promotions_namespace