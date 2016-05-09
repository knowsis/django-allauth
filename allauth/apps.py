from importlib import import_module
from logging import getLogger

from django.apps import AppConfig


logger = getLogger(__name__)


class AllauthConfig(AppConfig):
    name = 'allauth'

    def __init__(self, app_name, app_module):
        super(AllauthConfig, self).__init__(app_name, app_module)

    def ready(self):
        from django.conf import settings
        db_engine = settings.DATABASES['default']['ENGINE']

        if db_engine == 'django_mongodb_engine':
            patch_for_nonrel()


def patch_for_nonrel():
    for p in patches:
        patch(*p)


def split_mod(mod):
    mod_item = mod.split('.')[-1]
    mod_module = mod.replace('.' + mod_item, '')
    return mod_module, mod_item


def patch(old, new):
    old_module, old_item = split_mod(old)
    new_module, new_item = split_mod(new)

    logger.info('patching {0} with {1}'.format(old, new))

    old_module = import_module(old_module)
    new_module = import_module(new_module)
    setattr(old_module, old_item, getattr(new_module, new_item))

patches = [
    ('allauth.socialaccount.models.SocialApp',
     'allauth.alt_storage.django_nonrel.socialaccount.models.SocialApp'),
    ('allauth.account.forms.ResetPasswordForm',
     'allauth.alt_storage.django_nonrel.account.forms.ResetPasswordForm'),
    ('allauth.account.views.PasswordResetView',
     'allauth.alt_storage.django_nonrel.account.views.PasswordResetView'),
    ('allauth.account.auth_backends.AuthenticationBackend',
     'allauth.alt_storage.django_nonrel.account.auth_backends.AuthenticationBackend'),
]

