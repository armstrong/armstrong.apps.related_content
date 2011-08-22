from ._utils import *

from ..models import RelatedContent
from ..models import RelatedType


class RelatedContentManagerTestCase(TestCase):
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
