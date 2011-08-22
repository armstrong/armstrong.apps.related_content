import random

from armstrong.dev.tests.utils import ArmstrongTestCase

from .related_content_support.models import Article


def generate_fake_articles(n):
    ret = []
    for i in range(n):
        article = Article.objects.create(
            title="Some Random Article %d" % random.randint(1000, 2000)
        )
        ret.append(article)
    return ret


class TestCase(ArmstrongTestCase):
    pass
