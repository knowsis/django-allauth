from importlib import import_module

from django.apps import AppConfig


class NonRelConfig(AppConfig):
    name = 'allauth_alt.django_nonrel'
    label = 'allauth_alt.django_nonrel'

    def __init__(self, app_name, app_module):
        super(NonRelConfig, self).__init__(app_name, app_module)

    def ready(self):
        for p in patches:
            patch(*p)


def split_mod(mod):
    mod_item = mod.split('.')[-1]
    mod_module = mod.replace('.' + mod_item, '')
    return mod_module, mod_item


def patch(old, new):
    old_module, old_item = split_mod(old)
    new_module, new_item = split_mod(new)

    print('patching {0} with {1}'.format(old, new))

    old_module = import_module(old_module)
    new_module = import_module(new_module)
    setattr(old_module, old_item, getattr(new_module, new_item))

patches = [
    ('allauth.socialaccount.models.SocialApp',
     'allauth_alt.django_nonrel.socialaccount.models.SocialApp'),
    ('allauth.account.forms.ResetPasswordForm',
     'allauth_alt.django_nonrel.account.forms.ResetPasswordForm'),
    ('allauth.account.views.PasswordResetView',
     'allauth_alt.django_nonrel.account.views.PasswordResetView'),
]

