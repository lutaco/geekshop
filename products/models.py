from django.db import models

class Product(models.Model):
	name = models.CharField(
		max_length=255
	)

	description = models.TextField(
		blank=True,
		null=True
	)

	cost = models.DecimalField(
		max_digits=12,
		decimal_places=2,
		default=0
	)

	image = models.ImageField(
		blank=True,
		upload_to="product"
	)

	def __str__(self):
		return self.name