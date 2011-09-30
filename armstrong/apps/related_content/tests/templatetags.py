import datetime
import os
from django.template import Context, NodeList, RequestContext, Template,\
                            TemplateDoesNotExist, Variable
from django.core.files import File
from ._utils import TestCase
from .related_content_support.models import Article, Image
from ..models import RelatedType, RelatedContent


class lead_artTestCase(TestCase):
    def setUp(self):
        self.obj = Article.objects.create(title='foo')
        lead_art, created = RelatedType.objects.get_or_create(title='lead_art')
        path = os.path.split(__file__)[0]
        img = Image.objects.create(title='image')
        RelatedContent.objects.create(destination_object=img,
                                      source_object=self.obj,
                                      related_type=lead_art)

    def render(self, string):
        template = Template(string)
        ctx = {'obj': self.obj}
        return template.render(Context(ctx))

    def testLargeSize(self):
        large_string = "{% load related_content %}{% lead_art obj 'large' %}"
        small_string = "{% load related_content %}{% lead_art obj 'small' %}"
        large_rendered = self.render(large_string)
        small_rendered = self.render(small_string)
        self.assertEqual(large_rendered, 'Render: large')
        self.assertEqual(small_rendered, 'Render: small')
