from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import query

get_for_model = ContentType.objects.get_for_model


class RelatedContentQuerySet(query.QuerySet):
    def filter(self, destination_object=None, source_object=None, **kwargs):
        """
        See ``QuerySet.filter`` for full documentation

        This adds support for ``destination_object`` and ``source_object``
        as kwargs.  This converts those objects into the values necessary
        to handle the ``GenericForeignKey`` fields.
        """
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

    def by_destination(self, destination):
        """
        Retrieve any ``RelatedContent`` where the ``destination_object``
        is equal to the provided ``destination``.

        This is a shortcut for calling::

            RelatedContent.objects.filter(destination_object=destination)
        """
        return self.filter(destination_object=destination)

    def by_source(self, source):
        """
        Retrieve any ``RelatedContent`` where the ``source_object``
        is equal to the provided ``source``.

        This is a shortcut for calling::

            RelatedContent.objects.filter(source_object=source)
        """
        return self.filter(source_object=source)

    def by_type(self, type):
        """
        Shortcut for retrieving ``RelatedContent`` based on the string
        value of the ``related_type``.
        """
        return self.filter(related_type__title=type)


class RelatedContentManager(models.Manager):
    def get_query_set(self):
        return RelatedContentQuerySet(self.model, using=self._db)

    def by_destination(self, destination):
        """
        See ``RelatedContentQuerySet.by_destination``
        """
        return self.get_query_set().by_destination(destination)

    def by_source(self, source):
        """
        See ``RelatedContentQuerySet.by_source``
        """
        return self.get_query_set().by_source(source)

    def by_type(self, type):
        """
        See ``RelatedContentQuerySet.by_type``
        """
        return self.get_query_set().by_type(type)
