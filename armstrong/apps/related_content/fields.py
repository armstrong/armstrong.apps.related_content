from django.contrib.contenttypes.generic import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models.query import QuerySet

from armstrong.core.arm_wells.querysets import GenericForeignKeyQuerySet

from .models import RelatedContent


class BoundRelatedContentAccessor(object):
    def __init__(self, instance, model, from_field, to_field, *args, **kwargs):
        self.instance = instance
        self.model = model
        self.from_field = from_field
        self.to_field = to_field
        self.params = None

    def get_query_set_params(self):
        if self.params:
            return self.params
        for field in self.model._meta.virtual_fields:
            if field.name == self.from_field:
                self.params = {
                    field.ct_field: ContentType.objects.get_for_model(
                            self.instance).pk,
                    field.fk_field: self.instance.pk
                }
                break
        else:
            self.params = {self.from_field: self.instance}
        return self.params

    def get_query_set(self):
        qs = QuerySet(self.model)
        return qs.filter(**self.get_query_set_params())

    def all(self):
        qs = self.get_query_set()
        return GenericForeignKeyQuerySet(qs, gfk=self.to_field)

    def by_type(self, type):
        qs = self.get_query_set().filter(related_type__title=type)
        return GenericForeignKeyQuerySet(qs, gfk=self.to_field)

    def __getitem__(self, index):
        """
        See ``RelatedContentQuerySet.__getitem__``
        """
        if isinstance(index, basestring):
            return self.by_type(index)
        else:
            raise IndexError("RelatedFields can only be filtered by "
                    "related_type title")


class NonAssignableError(RuntimeError):
    pass


class RelatedM2MDescriptor(object):
    def __init__(self, model=RelatedContent, from_field="source_object",
            to_field="destination_object"):
        self.model = model
        self.from_field = from_field
        self.to_field = to_field

    def __get__(self, instance, cls=None):
        return BoundRelatedContentAccessor(
            instance=instance,
            model=self.model,
            from_field=self.from_field,
            to_field=self.to_field,
        )

    def __set__(self, instance, value):
        raise NonAssignableError("RelatedFields cannot be used to assign "
                "RelatedContent objects, use a RelatedContentField")


class RelatedObjectsField(object):
    def __init__(self, model=RelatedContent, from_field="source_object",
            to_field="destination_object"):
        self.model = model
        self.from_field = from_field
        self.to_field = to_field

    def contribute_to_class(self, cls, name):
        setattr(cls, name, RelatedM2MDescriptor(
                        model=self.model,
                        from_field=self.from_field,
                        to_field=self.to_field
                    )
        )


class ReverseRelatedObjectsField(RelatedObjectsField):
    def __init__(self, model=RelatedContent, from_field="destination_object",
            to_field="source_object"):
        super(ReverseRelatedObjectsField, self).__init__(
                model, from_field, to_field)


class RelatedContentField(GenericRelation):
    def __init__(self, **kwargs):
        defaults = {
            "object_id_field": "source_id",
            "content_type_field": "source_type",
        }
        defaults.update(kwargs)
        super(RelatedContentField, self).__init__(RelatedContent, **defaults)


from south.modelsinspector import add_ignored_fields
add_ignored_fields(
        ["^armstrong\.apps\.related_content\.fields\.RelatedContentField"])
