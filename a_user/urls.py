from django.urls import path

from a_user.views import profile_delete_view, profile_edit_view, profile_emailchange, profile_settings_view, profile_view

urlpatterns = [
    path('', profile_view, name='profile'),
    path('edit', profile_edit_view, name='profile-edit'),
    path('onboarding', profile_edit_view, name='profile-onboarding'),
    path('settings', profile_settings_view, name='profile-settings'),
    path('emailchange', profile_emailchange, name='profile-emailchange'),
    path('delete/', profile_delete_view, name='profile-delete')
]
