from armstrong.dev.tasks import *

settings = {
    'DEBUG': True,
    'INSTALLED_APPS': (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'armstrong.core.arm_content',
        'armstrong.apps.content',
        'armstrong.apps.images',
        'armstrong.apps.related_content',
        'armstrong.apps.related_content.tests.related_content_support',
        'sorl.thumbnail',
    ),
    'ROOT_URLCONF': 'armstrong.apps.related_content.tests_related_content_support',
    'SITE_ID': 1,
    'ARMSTRONG_PRESETS': {
        'small': {'width': 175},
        'large': {'width': 270},
    },
    'STATIC_URL': '/static/',
}

main_app = "related_content"
full_name = "armstrong.apps.related_content"
tested_apps = (main_app,)
pip_install_first = True
