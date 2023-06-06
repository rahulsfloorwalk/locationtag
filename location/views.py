from django.shortcuts import render
# from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import json
import locationtagger
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def location(request):
    place_entity = locationtagger.find_locations(text =request.POST['text'])
    countries = place_entity.countries
    regions = place_entity.regions
    cities = place_entity.cities
    data={}
    data['countries']=[]
    data['regions']=[]
    data['cities']=[]
    for i in countries:
        data['countries'].append(i)
    for i in regions:
        data['regions'].append(i)
    for i in cities:
        data['cities'].append(i)
    return HttpResponse(json.dumps(data), content_type='application/json')
    