from django.conf.urls import patterns, url

from django.views.generic.base import TemplateView

from main.views import user_profile, manage_profile, EditProfileView, member_favorite

urlpatterns = patterns('',
                       url(r'^profile/$',
                           manage_profile,
                           name='profile_management'),
                       url(r'^profile/edit/$',
                           EditProfileView.as_view(),
                           name='edit_profile'),
                       url(r'^profile/(?P<user_id>\w{1,50})/$',
                           user_profile,
                           name='user_profile'),
                       url(r'^profile/network/$',
                           TemplateView.as_view(template_name='profile/personal_network.html'),
                           name='personal_network'),
                       url(r'^api/member_favorite/(?P<user_id>\w{1,50})/$',
                           member_favorite,
                           name='member_favorite'),
                       url(r'^api/member_personal_network/(?P<user_id>\w{1,50})/$',
                          member_personal_network,
                          name='member_personal_network'),
                       )
