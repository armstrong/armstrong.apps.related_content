from django.contrib.contenttypes.generic import GenericRelation
from genericm2m.models import RelatedObjectsDescriptor

from .models import RelatedContent


class ReverseRelatedObjectsField(RelatedObjectsDescriptor):
    def __init__(self, model=None, from_field="destination_object",
            to_field="source_object"):
        if not model:
            model = RelatedContent
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
add_ignored_fields(["^armstrong\.apps\.related_content\.fields\.RelatedContentField"])