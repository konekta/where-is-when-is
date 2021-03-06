from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from apiv1.api import Api
from apiv1.resources import AreaResource, LocationResource
import autocomplete_light
from cms.views import details

from core.views import ProfileView, robots


autocomplete_light.autodiscover()
admin.autodiscover()

v1_api = Api()
v1_api.register(AreaResource())
v1_api.register(LocationResource())

urlpatterns = patterns(
    '',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^autocomplete/', include('autocomplete_light.urls')),

    url(r'^$', details, {'slug': ''}, name='pages-root'),
    url(r'^feedback/$', 'core.views.feedback', name='feedback'),
    url(r'^mobile/', include('mobile.urls')),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='account_profile'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^robots\.txt$', robots, name='robots.txt'),
    url(r'', include('world.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
