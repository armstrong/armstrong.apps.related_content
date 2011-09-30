from armstrong.dev.tasks import *
import tempfile

settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.contenttypes',
        'armstrong.apps.related_content',
        'armstrong.apps.related_content.tests.related_content_support',
        'south',
    ),
    'ROOT_URLCONF': 'armstrong.apps.related_content.tests_related_content_support',
    'SITE_ID': 1,
    'STATIC_URL': '/static/',
}

main_app = "related_content"
full_name = "armstrong.apps.related_content"
tested_apps = (main_app,)
pip_install_first = True
