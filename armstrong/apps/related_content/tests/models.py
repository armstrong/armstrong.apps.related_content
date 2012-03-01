from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericForeignKey
from django.db import models
from ._utils import *

from ..models import RelatedContent
from ..models import RelatedType


def generate_model():
    one, two = generate_fake_articles(2)
    t = RelatedType.objects.create(title="Some Random Type")
    c = RelatedContent.objects.create(
        related_type=t,
        source_object=one,
        destination_object=two
    )
    return one, two, c


class RelatedTypeTestCase(TestCase):
    def test_has_title(self):
        m = RelatedType()
        self.assertModelHasField(m, "title")


class RelatedContentTestCase(TestCase):
    def generate_model(self):
        one, two, c = generate_model()
        return c

    def test_has_related_Content(self):
        m = self.generate_model()
        self.assertRelatedTo(m, "related_type", RelatedType)

    def test_has_order(self):
        m = self.generate_model()
        self.assertModelHasField(m, "order", models.IntegerField)

    def test_has_source_type(self):
        m = self.generate_model()
        self.assertRelatedTo(m, "source_type", ContentType)

    def test_has_source_id(self):
        m = self.generate_model()
        self.assertModelHasField(m, "source_id", models.PositiveIntegerField)

    def test_has_source_object(self):
        m = self.generate_model()
        self.assertTrue(hasattr(m, "source_object"))

    def test_has_destination_type(self):
        m = self.generate_model()
        self.assertRelatedTo(m, "destination_type", ContentType)

    def test_has_destination_id(self):
        m = self.generate_model()
        self.assertModelHasField(m, "destination_id",
                models.PositiveIntegerField)

    def test_has_destination_object(self):
        m = self.generate_model()
        self.assertTrue(hasattr(m, "destination_object"))

