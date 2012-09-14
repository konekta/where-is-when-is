# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from views import zone_detail, location_detail


urlpatterns = patterns(
    '',

    url(r'^zone/(?P<slug>[-\w]+)/$', zone_detail, name='world_zone_detail'),
    url(r'^location/(?P<slug>[-\w]+)/$', location_detail, name='world_location_detail'),
)
