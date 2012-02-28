from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from genericm2m.models import RelatedObjectsDescriptor

from . import managers


class RelatedObjectsField(RelatedObjectsDescriptor):
    def __init__(self, model=None, from_field="source_object",
            to_field="destination_object"):
        if not model:
            model = RelatedContent
        super(RelatedObjectsField, self).__init__(model, from_field, to_field)


class RelatedType(models.Model):
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return self.title


class RelatedContent(models.Model):
    related_type = models.ForeignKey(RelatedType)
    order = models.IntegerField(default=0)
    source_type = models.ForeignKey(ContentType, related_name="from")
    source_id = models.PositiveIntegerField()
    source_object = generic.GenericForeignKey('source_type', 'source_id')

    destination_type = models.ForeignKey(ContentType, related_name="to")
    destination_id = models.PositiveIntegerField()
    destination_object = generic.GenericForeignKey('destination_type',
            'destination_id')

    objects = managers.RelatedContentManager()

    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return u"%s (%d): %s" % (self.related_type, self.order,
                                 self.destination_object)
