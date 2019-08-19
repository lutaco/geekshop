from django.db import models


class Category(models.Model):

	name = models.CharField(
		max_length=255
	)

	description = models.TextField(
		blank=True,
		null=True
	)

	def __str__(self):
		return self.name


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
		null=True,
		upload_to="product"
	)

	category = models.ForeignKey(
		Category,
		on_delete=models.CASCADE,
		blank=True,
		null=True
	)

	def __str__(self):
		return self.name
