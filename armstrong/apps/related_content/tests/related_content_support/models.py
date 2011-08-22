from django.db import models
from ...fields import RelatedContentField


class Article(models.Model):
    title = models.CharField(max_length=250)
    related = RelatedContentField()
