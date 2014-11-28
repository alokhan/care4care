from django.conf.urls import patterns, url

from django.views.generic.base import TemplateView

from branch.views import NeedHelpView, OfferHelpView
from branch.forms import NeedHelpForm

urlpatterns = patterns('',
                       url(r'^needhelp/(?P<user_id>\d+)/$',
                           NeedHelpView.as_view(),
                           name='need_help'),
                       url(r'^offerhelp/(?P<user_id>\d+)/$',
                            NeedHelpView.as_view(),
                           name='offer_help'),
                       )
