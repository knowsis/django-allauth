from allauth.account import app_settings
from allauth.account.views import AjaxCapableProcessFormViewMixin
from allauth.storage.django_nonrel.account.forms import ResetPasswordForm
from allauth.utils import get_form_class
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import FormView


class PasswordResetView(AjaxCapableProcessFormViewMixin, FormView):
    template_name = "account/password_reset.html"
    form_class = ResetPasswordForm
    success_url = reverse_lazy("account_reset_password_done")

    def get_form_class(self):
        return get_form_class(app_settings.FORMS,
                              'reset_password',
                              self.form_class)

    def form_valid(self, form):
        form.save(self.request)
        return super(PasswordResetView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(PasswordResetView, self).get_context_data(**kwargs)
        # NOTE: For backwards compatibility
        ret['password_reset_form'] = ret.get('form')
        # (end NOTE)
        return ret

password_reset = PasswordResetView.as_view()
