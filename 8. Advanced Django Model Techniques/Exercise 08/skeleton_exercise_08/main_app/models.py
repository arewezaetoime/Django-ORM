from django.core import validators
from django.db import models

from main_app.validators import validate_phone_number, validate_name_v2


# Create your models here.


class Customer(models.Model):
	name = models.CharField(
		max_length=100,
		validators=[validate_name_v2]
	)
	age = models.PositiveSmallIntegerField(
		validators=[validators.MinValueValidator(
			18, message="Age must be greater than 18"
		)]
	)
	email = models.EmailField(
		error_messages={'invalid': 'Enter a valid email address'},
	)
	phone_number = models.CharField(
		max_length=13,
		validators=[validate_phone_number]
	)
	website_url = models.URLField(
		error_messages={'invalid': 'Enter a valid URL'},
	)