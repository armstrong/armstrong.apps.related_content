from django.db.models import ForeignKey
import fudge
import random
from ._utils import TestCase

from .. import admin
from ..models import RelatedContent
from ..admin import formfield_for_foreignkey_helper


def generate_fake_settings():
    settings = fudge.Fake()
    settings.has_attr(**{
        "ARMSTRONG_RELATED_TYPE_INITIAL_FILTER": {
            "title": "articles",
        }
    })
    return settings


def generate_fake_qs():
    qs = fudge.Fake()
    qs.provides("get")
    return qs


def generate_fake_type(qs=None):
    if not qs:
        qs = generate_fake_qs()
    type = fudge.Fake()
    type.has_attr(objects=qs)
    return type


def generate_fakes():
    fake_settings = generate_fake_settings()
    fake_qs = generate_fake_qs()
    fake_type = generate_fake_type(fake_qs)

    return {
        "settings": fake_settings,
        "qs": fake_qs,
        "type": fake_type,
    }


def random_args():
    return [str(random.randint(1000, 2000))
            for i in range(random.randint(1, 5))]


def random_kwargs():
    return dict(zip(random_args(), random_args()))


def random_args_and_kwargs():
    return random_args(), random_kwargs()


class RelatedContentInlineTestCase(TestCase):
    def setUp(self):
        self.model = RelatedContent()
        self.db_field = self.get_db_field_by_name("related_type")

    def get_db_field_by_name(self, name):
        return self.model._meta.get_field_by_name(name)[0]

    def test_returns_args_untouched_if_not_related_type(self):
        args, kwargs = random_args_and_kwargs()
        content_type_field = self.get_db_field_by_name("source_type")
        ret = formfield_for_foreignkey_helper({}, content_type_field,
                *args, **kwargs)
        returned_args = list(ret[0])
        db_field = returned_args.pop(0)
        # Test db_field separately to avoid false failure in Django
        self.assertIsA(db_field, ForeignKey)
        self.assertEqual(args, returned_args)

    def test_returns_kwargs_untouched_if_not_related_type(self):
        args, kwargs = random_args_and_kwargs()
        content_type_field = self.get_db_field_by_name("source_type")
        ret = formfield_for_foreignkey_helper({}, content_type_field,
                *args, **kwargs)
        returned_kwargs = ret[1]
        self.assertEqual(kwargs, returned_kwargs)

    def test_adds_initial_if_it_is_not_present(self):
        random_return = random.randint(10000, 20000)
        fake = fudge.Fake()
        fake.has_attr(pk=random_return)
        args, kwargs = random_args_and_kwargs()
        fake_settings = generate_fake_settings()
        fake_qs = fudge.Fake()
        fake_qs.expects("get").with_args(title="articles").returns(fake)
        fake_type = generate_fake_type(fake_qs)
        with fudge.patched_context(admin, "RelatedType", fake_type):
            with fudge.patched_context(admin, "settings", fake_settings):
                ret = formfield_for_foreignkey_helper({}, self.db_field,
                        *args, **kwargs)
                returned_kwargs = ret[1]
        self.assertTrue("initial" in returned_kwargs)
        self.assertEqual(returned_kwargs["initial"], random_return)

    def test_ignores_initial_if_provided(self):
        expected_return = random.randint(30000, 40000)
        random_return = random.randint(10000, 20000)
        fake = fudge.Fake().has_attr(pk=random_return)
        args, kwargs = random_args_and_kwargs()
        kwargs["initial"] = expected_return
        fake_settings = generate_fake_settings()
        fake_qs = fudge.Fake()
        fake_qs.expects("get").with_args(title="articles").returns(fake)
        fake_type = generate_fake_type(fake_qs)
        with fudge.patched_context(admin, "RelatedType", fake_type):
            with fudge.patched_context(admin, "settings", fake_settings):
                ret = formfield_for_foreignkey_helper({}, self.db_field,
                        *args, **kwargs)
                returned_kwargs = ret[1]
        self.assertTrue("initial" in returned_kwargs)
        self.assertEqual(returned_kwargs["initial"], expected_return)
