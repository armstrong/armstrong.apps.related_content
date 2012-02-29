from ._utils import *

from ..models import RelatedContent
from ..models import RelatedType


def relate(type, source, destination):
    return RelatedContent.objects.create(
        related_type=type,
        source_object=source,
        destination_object=destination)


def create_one_source_to_two_destinations():
    one, two, three = generate_fake_articles(3)
    t = RelatedType.objects.create(title="articles")
    relate(t, one, two)
    relate(t, one, three)
    return one, two, three


def create_two_sources_to_one_destination():
    one, two, three = generate_fake_articles(3)
    t = RelatedType.objects.create(title="articles")
    relate(t, one, two)
    relate(t, three, two)
    return one, two, three


class RelatedContentManagerTestCase(TestCase):
    def test_can_find_by_destination_object(self):
        one, two, three = create_one_source_to_two_destinations()
        related_content = RelatedContent.objects.filter(destination_object=two)
        self.assertEqual(1, related_content.count())

    def test_can_find_by_source_object(self):
        one, two, three = create_two_sources_to_one_destination()
        related_content = RelatedContent.objects.filter(source_object=one)
        self.assertEqual(1, related_content.count())

    def test_by_type_returns_an_empty_queryset_if_no_match_is_found(self):
        one, two = generate_fake_articles(2)

        self.assertEqual([], list(one.related_content.by_type("unknown")))

    def test_by_type_returns_matching_related_values_by_type_title(self):
        one, two = generate_fake_articles(2)

        t = RelatedType.objects.create(title="articles")
        relate(t, one, two)

        destination_objects = [a.destination_object for a in
                one.related_content.by_type("articles")]
        self.assertTrue(two in destination_objects)

    def test_by_type_can_be_used_after_filtering(self):
        one, two = generate_fake_articles(2)

        t = RelatedType.objects.create(title="articles")
        relate(t, one, two)

        destination_objects = [a.destination_object for a in
                one.related_content.all().by_type("articles")]
        self.assertTrue(two in destination_objects)

    def test_uses_queryset_with_custom_filter(self):
        one, two, three = create_one_source_to_two_destinations()
        related_content = (RelatedContent.objects.all()
                .filter(destination_object=two))
        self.assertEqual(1, related_content.count())

    def test_provides_method_for_finding_by_destination(self):
        one, two, three = create_one_source_to_two_destinations()
        related_content = RelatedContent.objects.by_destination(two)
        self.assertEqual(1, related_content.count())
        self.assertEqual(two, related_content[0].destination_object)

    def test_can_call_by_destination_after_filtering(self):
        one, two, three = create_one_source_to_two_destinations()
        related_content = RelatedContent.objects.all().by_destination(two)
        self.assertEqual(1, related_content.count())
        self.assertEqual(two, related_content[0].destination_object)

    def test_provides_method_for_finding_by_source(self):
        one, two, three = create_two_sources_to_one_destination()
        related_content = RelatedContent.objects.by_source(one)
        self.assertEqual(1, related_content.count())
        self.assertEqual(one, related_content[0].source_object)

    def test_can_call_by_source_after_filtering(self):
        one, two, three = create_two_sources_to_one_destination()
        related_content = RelatedContent.objects.all().by_source(one)
        self.assertEqual(1, related_content.count())
        self.assertEqual(one, related_content[0].source_object)
