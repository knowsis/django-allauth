from allauth.account.adapter import get_adapter
from allauth.account.forms import ResetPasswordForm
from allauth.utils import get_user_model
from django import forms
from django.utils.translation import ugettext_lazy as _


class ResetPasswordForm(ResetPasswordForm):

    def clean_email(self):
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        self.users = get_user_model().objects.filter(email__iexact=email)

        if not self.users.exists():
            raise forms.ValidationError(_("The e-mail address is not assigned"
                                          " to any user account"))
        return self.cleaned_data["email"]
