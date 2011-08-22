from django import forms
from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

from armstrong.hatband import widgets

from .models import RelatedContent
from .models import RelatedType


class RelatedContentInlineForm(forms.ModelForm):
    class Meta:
        widgets = {
            "destination_type": forms.HiddenInput(),
            "destination_id": widgets.GenericKeyWidget(
                object_id_name="destination_id",
                content_type_name="destination_type",
            ),
            "order": forms.HiddenInput(),
        }


class RelatedContentInline(GenericTabularInline):
    ct_field = "source_type"
    ct_fk_field = "source_id"

    model = RelatedContent
    template = "admin/edit_inline/generickey.html"

    form = RelatedContentInlineForm


admin.site.register(RelatedType)
