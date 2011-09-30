from django.db import models
from armstrong.core.arm_content.mixins.images import BaseThumbnailMixin
from ...fields import RelatedContentField


class Article(models.Model):
    title = models.CharField(max_length=250)
    related = RelatedContentField()

class TestingThumbnailMixin(BaseThumbnailMixin):
    def render_visual(self, preset_label, presets=None, defaults=None, *args, **kwargs):
        return "Render: %s" % preset_label

    def get_visual_thumbnail_url(self, preset_label, presets=None, defaults=None, *args, **kwargs):
        return "Thumb: %s" % preset_label

class Image(models.Model, TestingThumbnailMixin):
    title = models.CharField(max_length=250)
