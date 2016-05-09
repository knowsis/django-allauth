from allauth.alt_storage.django_nonrel.nonrel import ListFieldWithForm
from allauth.socialaccount import providers
from allauth.socialaccount.models import SocialAppManager
from django.contrib.sites.models import Site
from django.db import models
from django.db.models import ForeignKey
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class SocialApp(models.Model):
    objects = SocialAppManager()

    provider = models.CharField(verbose_name=_('provider'),
                                max_length=30,
                                choices=providers.registry.as_choices())
    name = models.CharField(verbose_name=_('name'),
                            max_length=40)
    client_id = models.CharField(verbose_name=_('client id'),
                                 max_length=100,
                                 help_text=_('App ID, or consumer key'))
    secret = models.CharField(verbose_name=_('secret key'),
                              max_length=100,
                              help_text=_('API secret, client secret, or'
                                          ' consumer secret'))
    key = models.CharField(verbose_name=_('key'),
                           max_length=100,
                           blank=True,
                           help_text=_('Key'))
    # Most apps can be used across multiple domains, therefore we use
    # a ManyToManyField. Note that Facebook requires an app per domain
    # (unless the domains share a common base name).
    # blank=True allows for disabling apps without removing them
    # Use a ListField of ForeignKeys as MongoDbEngine doesn't support ManyToMany relationships
    sites = ListFieldWithForm(ForeignKey(Site))

    class Meta:
        verbose_name = _('social application')
        verbose_name_plural = _('social applications')

    def __str__(self):
        return self.name
