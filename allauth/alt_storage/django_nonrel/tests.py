from allauth.apps import patch_nonrel, AllauthConfig
from django.test.testcases import SimpleTestCase


class TestPatching(SimpleTestCase):
    def test_that_importing_nonrel_app_patches_allauth(self):
        from allauth.alt_storage import django_nonrel
        AllauthConfig('name', django_nonrel)

        # patch_nonrel()

        from allauth.socialaccount.models import SocialApp
        from allauth.alt_storage.django_nonrel.socialaccount.models import SocialApp as NonRelSocialApp

        self.assertTrue(isinstance(SocialApp, NonRelSocialApp))
