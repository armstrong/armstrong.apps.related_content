from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from django.db import models
from ._utils import *

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


class ReverseRelatedObjectsFieldTestCase(TestCase):
    def test_contains_all_related_objects_for_given_source(self):
        one, two, c = generate_model()
        related_content = two.reverse_related.all()
        self.assertEqual(1, related_content.count())
        self.assertEqual(related_content[0], one)
