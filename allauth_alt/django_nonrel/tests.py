from allauth_alt.django_nonrel.apps import NonRelConfig
from django.test import TestCase
from djangotoolbox.fields import ListField


class TestPatching(TestCase):
    def test_that_importing_nonrel_app_patches_allauth(self):
        from allauth_alt import django_nonrel
        NonRelConfig('allauth_alt.django_nonrel', django_nonrel).ready()

        from allauth.socialaccount.models import SocialApp
        from allauth_alt.django_nonrel.socialaccount.models import SocialApp as NonRelSocialApp

        self.assertTrue(isinstance(SocialApp, NonRelSocialApp))
