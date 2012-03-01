from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from django.db import models
from ._utils import *
from django import template

from ..models import RelatedContent
from ..models import RelatedType

from .models import generate_model

class RelatedContentFieldTestCase(TestCase):
    def test_related_contains_all_related_models(self):
        one, two, c = generate_model()
        related_content = one.related_content.all()
        self.assertEqual(1, related_content.count())
        self.assertEqual(related_content[0].destination_object, two)


class RelatedObjectsFieldTestCase(TestCase):
    def test_contains_all_related_objects_for_given_source(self):
        one, two, c = generate_model()
        related_content = one.related.all()
        self.assertEqual(1, related_content.count())
        self.assertEqual(related_content[0], two)

    def test_filtering_by_type(self):
        one, two, c = generate_model()
        related_content = one.related.by_type(c.related_type.title)
        self.assertEqual(1, related_content.count())
        self.assertEqual(related_content[0], two)

    def test_filtering_by_getitem(self):
        one, two, c = generate_model()
        related_content = one.related[c.related_type.title]
        self.assertEqual(1, related_content.count())
        self.assertEqual(related_content[0], two)

    def test_filtering_by_type_with_no_results(self):
        one, two, c = generate_model()
        related_content = one.related.by_type("invalid_type")
        self.assertEqual(0, related_content.count())

    def test_template_filtering(self):
        one, two, c = generate_model()
        c.related_type.title = "type_title"
        c.related_type.save()
        t = template.Template("{{ one.related.type_title.0.title }}")
        result = t.render(template.Context(locals()))
        self.assertEqual(result, two.title)


class ReverseRelatedObjectsFieldTestCase(TestCase):
    def test_contains_all_related_objects_for_given_source(self):
        one, two, c = generate_model()
        related_content = two.reverse_related.all()
        self.assertEqual(1, related_content.count())
        self.assertEqual(related_content[0], one)
