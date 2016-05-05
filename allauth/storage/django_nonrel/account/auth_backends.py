from allauth.account.auth_backends import AuthenticationBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class NonRelAuthenticationBackend(AuthenticationBackend):

    def _authenticate_by_email(self, **credentials):
        # Even though allauth will pass along `email`, other apps may
        # not respect this setting. For example, when using
        # django-tastypie basic authentication, the login is always
        # passed as `username`.  So let's place nice with other apps
        # and use username as fallback
        email = credentials.get('email', credentials.get('username'))
        if email:
            users = User.objects.filter(email__iexact=email)
            for user in users:
                if user.check_password(credentials["password"]):
                    return user
        return None
