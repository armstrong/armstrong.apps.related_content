import datetime
import os
from django.template import Context, NodeList, RequestContext, Template,\
                            TemplateDoesNotExist, Variable
from django.core.files import File
from ._utils import TestCase
from armstrong.apps.images.models import Image
from .related_content_support.models import Article
from ..models import RelatedType, RelatedContent

class LeadArtNodeTestCase(TestCase):
    def testSomething(self):
        pass


class lead_artTestCase(TestCase):
    def setUp(self):
        self.obj = Article.objects.create(title='foo')
        lead_art, created = RelatedType.objects.get_or_create(title='lead_art')
        path = os.path.split(__file__)[0]
        img = Image.objects.create(title='image',
                                   slug='image',
                                   summary='colored boxes',
                                   pub_status='P',
                                   pub_date=datetime.datetime.now(),
                                   image=File(open(path + '/image.png')))
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
        self.assertTrue(large_rendered.startswith('<img src="cache'))
        self.assertTrue(small_rendered.startswith('<img src="cache'))
        self.assertNotEqual(large_rendered, small_rendered)
        self.assertEqual(large_rendered, self.render(large_string))
