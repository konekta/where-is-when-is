# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from olwidget.widgets import InfoLayer, Map

from models import Zone, Location


def zone_detail(request, slug):
    zone = get_object_or_404(Zone, slug=slug)

    worldborders = zone.worldborder_set.all()
    locations = zone.location_set.all()

    worldborders_layer = InfoLayer([(wb.poly_simplify, wb.name_1) for wb in worldborders])
    locations_layer = InfoLayer([(l.point, l.map_html) for l in locations])

    this_map = Map([worldborders_layer, locations_layer],
                   {'layers': ['google.streets', 'google.satellite', 'google.hybrid']})

    return render(request, 'world/zone_detail.html', {
        'zone': zone,
        'map': this_map,
    })

def location_detail(request, slug):
    location = get_object_or_404(Location, slug=slug)

    return render(request, 'world/location_detail.html', {
            'location': location,
            })
