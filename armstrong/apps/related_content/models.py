from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class RelatedType(TitleMixin, models.Model):
	title = models.CharField(max_length=100)

	def __unicode__(self):
		return self.title


class RelatedContent(models.Model):
	related_type = models.ForeignKey(RelatedType)
    order = models.IntegerField(default=0)
	content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ["order"]

    def __unicode__(self):
        return u"%s (%d): %s" % (self.related_type, self.order,
                                 self.content_object)
