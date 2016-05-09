from allauth.apps import patch_for_nonrel, AllauthConfig
from django.test.testcases import SimpleTestCase


class TestPatching(SimpleTestCase):
    def test_that_importing_nonrel_app_patches_allauth(self):
        from allauth.alt_storage import django_nonrel
        AllauthConfig('name', django_nonrel).ready()

        from allauth.socialaccount.models import SocialApp
        from allauth.alt_storage.django_nonrel.socialaccount.models import SocialApp as NonRelSocialApp

        self.assertTrue(issubclass(SocialApp, NonRelSocialApp), 'expected a model to be patched')

        from allauth.account.forms import ResetPasswordForm
        from allauth.alt_storage.django_nonrel.account.forms import ResetPasswordForm as NonRelResetPasswordForm

        self.assertTrue(issubclass(ResetPasswordForm, NonRelResetPasswordForm), 'expected other classes to be patched')
