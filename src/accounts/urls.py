from django.conf.urls import *
from django.contrib.auth import views as auth_views
from django.conf import settings

## This file was adapted from userena.urls

from userena import views as userena_views
from userena import settings as userena_settings

# use captcha-enabled signup form?
from userena.forms import SignupForm
SignupFormCls = SignupForm
if 'captcha' in settings.INSTALLED_APPS:
    from accounts.forms import CaptchaSignupForm
    SignupFormCls = CaptchaSignupForm


urlpatterns = patterns('',
    # Signup, signin and signout
    url(r'^signup/$',
       userena_views.signup,
       name='userena_signup',
       kwargs=dict(template_name='accounts/signup_form.html',
                   signup_form=SignupFormCls,
                   extra_context={'in_accounts_signup': True})),
    url(r'^signin/$',
       userena_views.signin,
       name='userena_signin',
       kwargs=dict(template_name='accounts/signin_form.html',
                   extra_context={'in_accounts_signin': True})),
    url(r'^signout/$',
       userena_views.signout,
       name='userena_signout',
       kwargs=dict(template_name='accounts/signout.html')),

    # Reset password
    url(r'^password/reset/$',
       auth_views.password_reset,
       {'template_name': 'accounts/password_reset_form.html',
        'email_template_name': 'accounts/emails/password_reset_message.txt'},
       name='userena_password_reset'),
    url(r'^password/reset/done/$',
       auth_views.password_reset_done,
       {'template_name': 'accounts/password_reset_done.html'},
       name='userena_password_reset_done'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
       auth_views.password_reset_confirm,
       {'template_name': 'accounts/password_reset_confirm_form.html'},
       name='userena_password_reset_confirm'),
    url(r'^password/reset/confirm/complete/$',
       auth_views.password_reset_complete,
       {'template_name': 'accounts/password_reset_complete.html'}),

    # Signup
    url(r'^(?P<username>[\.\w-]+)/signup/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'accounts/signup_complete.html',
        'extra_context': {'userena_activation_required': userena_settings.USERENA_ACTIVATION_REQUIRED,
                          'userena_activation_days': userena_settings.USERENA_ACTIVATION_DAYS}},
       name='userena_signup_complete'),

    # Activate
    url(r'^activate/(?P<activation_key>\w+)/$',
       userena_views.activate,
       name='userena_activate'),

    # Change email and confirm it
    url(r'^(?P<username>[\.\w-]+)/email/$',
       userena_views.email_change,
       {'template_name': 'accounts/email_form.html'},
       name='userena_email_change'),
    url(r'^(?P<username>[\.\w-]+)/email/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'accounts/email_change_complete.html'},
       name='userena_email_change_complete'),
    url(r'^(?P<username>[\.\w-]+)/confirm-email/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'accounts/email_confirm_complete.html'},
       name='userena_email_confirm_complete'),
    url(r'^confirm-email/(?P<confirmation_key>\w+)/$',
       userena_views.email_confirm,
       {'template_name': 'accounts/email_confirm_fail.html'},
       name='userena_email_confirm'),

    # Disabled account
    url(r'^(?P<username>[\.\w-]+)/disabled/$',
       userena_views.direct_to_user_template,
       {'template_name': 'accounts/disabled.html'},
       name='userena_disabled'),

    # Change password
    url(r'^(?P<username>[\.\w-]+)/password/$',
       userena_views.password_change,
       {'template_name': 'accounts/password_form.html'},
       name='userena_password_change'),
    url(r'^(?P<username>[\.\w-]+)/password/complete/$',
       userena_views.direct_to_user_template,
       {'template_name': 'accounts/password_complete.html'},
       name='userena_password_change_complete'),

    # Edit profile
    url(r'^(?P<username>[\.\w-]+)/edit/$',
       userena_views.profile_edit,
       name='userena_profile_edit',
       kwargs=dict(template_name='accounts/profile_form.html')),

    # View profiles
    url(r'^(?P<username>(?!signout|signup|signin)[\.\w-]+)/$',
       userena_views.profile_detail,
       name='userena_profile_detail',
       kwargs=dict(template_name='accounts/profile_detail.html')),
)

if not settings.USERENA_DISABLE_PROFILE_LIST:
    urlpatterns += patterns('',
        url(r'^page/(?P<page>[0-9]+)/$',
            userena_views.ProfileListView.as_view(),
            name='userena_profile_list_paginated'),
        url(r'^$',
            userena_views.ProfileListView.as_view(),
            name='userena_profile_list'),
    )
