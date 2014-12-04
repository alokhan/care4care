from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',
    url(r'^$', 'main.views.home', name='home'),
    url(r'^social/', include('allauth.urls')),
    url(r'^accounts/logout/$', 'main.views.logout', name='logout'),
    url(r'^accounts/login/$', 'main.views.login', name='login'),
    url(r'^help/$', 'main.views.help', name='help'),

    url(r'^accounts/', include('main.urls_register')),
    url(r'^accounts/', include('main.urls_profile')),
    url(r'^accounts/', include('main.urls_verified')),
    url(r'^accounts/', include('main.urls_credits')),

    url(r'^statistics/', include('main.urls_statistics')),
    url(r'^messages/', include('main.urls_postman')),
    url(r'^seek_jobs/', include('main.urls_seek_jobs')),
    url(r'^search/', include('main.urls_search')),
)
