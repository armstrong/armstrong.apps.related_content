from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from .models import RelatedContent
from .models import RelatedType


class RelatedContentInline(GenericTabularInline):
    ct_field = "source_type"
    ct_fk_field = "source_id"

    model = RelatedContent


admin.site.register(RelatedType)