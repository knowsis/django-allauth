def split_mod(mod):
    mod_item = mod.split('.')[-1]
    mod_module = mod.replace('.' + mod_item, '')
    return mod_module, mod_item


def patch(old, new):
    old_module, old_item = split_mod(old)
    new_module, new_item = split_mod(new)

    setattr(__import__(old_module), old_item,
            getattr(__import__(new_module), new_item))

patches = [
    ('allauth.socialaccount.models.SocialApp',
     'allauth_alt.django_nonrel.socialaccount.models.SocialApp'),
    ('allauth.account.forms.ResetPasswordForm',
     'allauth_alt.django_nonrel.account.forms.ResetPasswordForm'),
    ('allauth.account.account.PasswordResetView',
     'allauth_alt.django_nonrel.account.views.PasswordResetView'),
]

for p in patches:
    patch(*p)
