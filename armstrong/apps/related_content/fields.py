from django.db import models

from .models import RelatedContent


class RelatedContentField(models.ManyToManyField):
	def __init__(self, **kwargs):
		super(RelatedContentField, self).__init__(RelatedContent, **kwargs)
