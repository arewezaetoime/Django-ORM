from django.core import validators
from django.db import models


class ReviewMixin(models.Model):
	class Meta:
		abstract = True
		ordering = ['-rating']

	rating = models.PositiveIntegerField(
		validators=[validators.MaxValueValidator(5)]
	)
	review_content = models.TextField()
