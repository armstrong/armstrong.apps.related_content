from ._utils import *

from ..models import RelatedContent
from ..models import RelatedType


def relate(type, source, destination):
    return RelatedContent.objects.create(
        related_type=type,
        source_object=source,
        destination_object=destination)


class RelatedContentManagerTestCase(TestCase):
    def test_can_find_by_destination_object(self):
        one, two, three = generate_fake_articles(3)
        t = RelatedType.objects.create(title="articles")
        relate(t, one, two)
        relate(t, one, three)

        related_content = RelatedContent.objects.filter(destination_object=two)
        self.assertEqual(1, related_content.count())

    def test_can_find_by_source_object(self):
        one, two, three = generate_fake_articles(3)
        t = RelatedType.objects.create(title="articles")
        relate(t, one, two)
        relate(t, three, two)

        related_content = RelatedContent.objects.filter(source_object=one)
        self.assertEqual(1, related_content.count())

    def test_by_type_returns_an_empty_queryset_if_no_match_is_found(self):
        one, two = generate_fake_articles(2)

        self.assertEqual([], list(one.related.by_type("unknown")))

    def test_by_type_returns_matching_related_values_by_type_title(self):
        one, two = generate_fake_articles(2)

        t = RelatedType.objects.create(title="articles")
        c = RelatedContent.objects.create(
            related_type=t,
            source_object=one,
            destination_object=two
        )

        destination_objects = [a.destination_object for a in
                one.related.by_type("articles")]
        self.assertTrue(two in destination_objects)
