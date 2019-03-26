class Promotions:
	def __init__(self, client, campaigns_namespace, promotion_tiers_namespace):
		self.client = client
		self.url = '/promotions'
		self.campaigns_namespace = campaigns_namespace
		self.tiers = promotion_tiers_namespace