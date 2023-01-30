from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 200)
	description = models.TextField()
	price = models.FloatField()
	category_id = models.IntegerField()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Товар"
		verbose_name_plural = "Товары"


class Category(models.Model):
	category_id = models.IntegerField()
	name = models.CharField(max_length = 200)
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"


class Order(models.Model):
	name = models.CharField(max_length = 200)
	phone = models.CharField(max_length = 200)
	comment = models.TextField()
	status = models.BooleanField(default = False)

	def __str__(self):
		return self.name + ' ' + str(self.status)

	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'