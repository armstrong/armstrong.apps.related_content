from contextlib import contextmanager
import copy
from django import template
from django.contrib.contenttypes.models import ContentType
from django.template import RequestContext
from django.template.base import TemplateSyntaxError, VariableDoesNotExist
from ..models import RelatedContent

register = template.Library()


class LeadArtNode(template.Node):
    def __init__(self, from_object, preset):
        self.from_object = template.Variable(from_object)
        self.preset = template.Variable(preset)

    def render(self, context):
        obj = self.from_object.resolve(context)
        obj_type = ContentType.objects.get_for_model(obj)
        related_art = RelatedContent.objects.by_type('lead_art')\
                                            .filter(source_type=obj_type)\
                                            .filter(source_id=obj.id)
        try:
            art = related_art[0].destination_object
        except IndexError:
            return ''
        return art.render_visual(self.preset.resolve(context))


@register.tag
def lead_art(parser, token):
    tokens = token.split_contents()
    if len(tokens) is 3:
        _, from_object, preset = tokens
        return LeadArtNode(from_object, preset)

    message = "Too %s parameters" % ("many" if len(tokens) > 3 else "few")
    raise TemplateSyntaxError(message)
