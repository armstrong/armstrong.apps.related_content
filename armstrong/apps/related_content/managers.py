from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import query

get_for_model = ContentType.objects.get_for_model


class RelatedContentQuerySet(query.QuerySet):
    def filter(self, destination_object=None, source_object=None, **kwargs):
        if destination_object:
            kwargs.update({
                "destination_id": destination_object.pk,
                "destination_type": get_for_model(destination_object),
            })
        if source_object:
            kwargs.update({
                "source_id": source_object.pk,
                "source_type": get_for_model(source_object),
            })
        return super(RelatedContentQuerySet, self).filter(**kwargs)


class RelatedContentManager(models.Manager):
    def get_query_set(self):
        return RelatedContentQuerySet(self.model, using=self._db)

    def by_type(self, type):
        return self.filter(related_type__title=type)
