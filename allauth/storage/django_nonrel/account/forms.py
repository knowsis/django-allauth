from allauth.account.forms import ResetPasswordForm


class ResetPasswordForm(ResetPasswordForm):

    def clean_email(self):
        email = self.cleaned_data["email"]
        email = get_adapter().clean_email(email)
        self.users = User.objects.filter(email__iexact=email)

        if not self.users.exists():
            raise forms.ValidationError(_("The e-mail address is not assigned"
                                          " to any user account"))
        return self.cleaned_data["email"]
