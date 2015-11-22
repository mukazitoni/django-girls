from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=10)
	price =models.IntegerField(max_length=4)
	quality=models.CharField(max_length=5)
	quantity=models.IntegerField(max_length=6)
	colour=models.CharField(max_length=7)