from django.db import models


class RelatedContentManager(models.Manager):
    def by_type(self, type):
        return self.filter(related_type__title=type)
