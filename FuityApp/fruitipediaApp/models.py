from django.core import validators
from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length=255, unique=True)


class Fruits(models.Model):
	name = models.CharField(
		max_length=255,
		validators=[
					validators.MinLengthValidator(limit_value=2),
					validators.MaxLengthValidator(max_length=30),

		]
	)