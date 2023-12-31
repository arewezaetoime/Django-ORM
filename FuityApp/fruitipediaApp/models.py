from django.core import validators
from django.db import models

from fruitipediaApp.FruityApp.validators import only_alphabetic


# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=255, unique=True)


class Fruits(models.Model):
	name = models.CharField(
		max_length=255,
		validators=[
					validators.MinLengthValidator(2),
					validators.MaxLengthValidator(30),
					only_alphabetic
		]
	)
	image_url = models.URLField()
	description = models.TextField()
	nutrition = models.TextField()
